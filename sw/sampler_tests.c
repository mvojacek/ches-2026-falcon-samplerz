#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/mman.h>
#include <stdbool.h>
#include <string.h>

#include "../src/registers/sw/c/samplerz_axi_bitfield_little.h"
#include "rdtsc.h"

#define SAMPLERZ_AXI_BASE_ADDR 0x6000000000

volatile samplerz_axi_t *dev = 0;

void map_samplerz_axi()
{
    int fd = open("/dev/mem", O_RDWR | O_SYNC);
    if (fd < 0)
    {
        perror("Failed to open /dev/mem");
        exit(EXIT_FAILURE);
    }

    size_t map_size = sizeof(samplerz_axi_t);

    void *mapped_base = mmap(NULL, map_size, PROT_READ | PROT_WRITE, MAP_SHARED, fd, SAMPLERZ_AXI_BASE_ADDR);
    if (mapped_base == MAP_FAILED)
    {
        perror("Failed to mmap");
        close(fd);
        exit(EXIT_FAILURE);
    }

    close(fd);
    dev = (volatile samplerz_axi_t *)mapped_base;
}

void unmap_samplerz_axi()
{
    if (munmap((void *)dev, sizeof(samplerz_axi_t)) < 0)
    {
        perror("Failed to munmap");
        exit(EXIT_FAILURE);
    }
    dev = NULL;
}

void samplerz_reset()
{
    // Reset the samplerz module
    dev->control.f.reset = 1;
}

void samplerz_wait_full()
{
    while (dev->control.f.rand_full == 0)
    {
    }
}

void samplerz_init_prng()
{
    int fd = open("/dev/urandom", O_RDONLY);
    if (fd < 0)
    {
        perror("Failed to open /dev/urandom");
        exit(EXIT_FAILURE);
    }

    uint32_t temp_seed[sizeof(dev->prng.seed) / sizeof(uint32_t)];
    if (read(fd, temp_seed, sizeof(temp_seed)) != sizeof(temp_seed))
    {
        perror("Failed to read random data");
        close(fd);
        exit(EXIT_FAILURE);
    }

    close(fd);

    for (size_t i = 0; i < sizeof(temp_seed) / sizeof(uint32_t); i++)
    {
        dev->prng.seed[i].w = temp_seed[i];
    }
    dev->prng.counter.w = 0;
}

void samplerz_configure(double sigma_inv, double mu1, double mu2, bool falcon1024, bool continuous)
{
    dev->sginv.w = *(uint64_t *)&sigma_inv;
    dev->mu1.w = *(uint64_t *)&mu1;
    dev->mu2.w = *(uint64_t *)&mu2;

    dev->control.f.falcon1024 = falcon1024;
    dev->control.f.continuous = continuous;
}

uint64_t total_samples = 0;
uint64_t total_bits_used = 0;
uint64_t total_busy_cycles = 0;

void samplerz_readsamples(int *z1, int *z2)
{
    *z1 = *(volatile int32_t *)&dev->z1.w;
    *z2 = *(volatile int32_t *)&dev->z2.w;
    samplerz_wait_full();
    total_samples++;
    total_bits_used += dev->consumed_bits.w;
    total_busy_cycles += dev->busy_cycles.w;
}

void samplerz_status()
{
    printf("== SAMPLERZ_AXI Status ===\n");

    samplerz_axi__control_t control_reg = dev->control;
    printf("Control Register: 0x%08X\n", control_reg.w);
    printf("Falcon1024: %d\n", control_reg.f.falcon1024);
    printf("Done: %d\n", control_reg.f.done);
    printf("Start: %d\n", control_reg.f.start);
    printf("Continuous: %d\n", control_reg.f.continuous);
    printf("Reset: %d\n", control_reg.f.reset);
    printf("Busy: %d\n", control_reg.f.busy);
    printf("Full: %d\n", control_reg.f.rand_full);

    printf("Busy Cycles: %lu\n", dev->busy_cycles.w);
    printf("Consumed Bits: %lu\n", dev->consumed_bits.w);

    printf("PRNG Counter: 0x%016lX\n", dev->prng.counter.w);

    printf("===========================================\n");
}

uint64_t continuous_busy_cycles = 0;
uint64_t continuous_bits_used = 0;
uint64_t continuous_samples_z1 = 0;
uint64_t continuous_samples_z2 = 0;

void samplerz_histogram(int i, double sigma_inv, double mu)
{
    printf("== SAMPLERZ_AXI Histogram for z%d ===\n", i + 1);

    uint64_t histogram[40];
    int32_t pivot_value;
    uint32_t pivot_index;

    memcpy(histogram, dev->sample_histograms[i].histogram, sizeof(histogram));
    memcpy(&pivot_value, &dev->sample_histograms[i].pivot_value.w, sizeof(pivot_value));
    memcpy(&pivot_index, &dev->sample_histograms[i].pivot_index.w, sizeof(pivot_index));

    uint64_t sum = 0;
    for (int i = 0; i < 40; i++)
    {
        printf("  %4d: %10lu\n", pivot_value + i - pivot_index, histogram[i]);
        sum += histogram[i];
    }
    printf("Sum: %lu\n", sum);
    printf("================================\n");

    char filename[128];
    snprintf(filename, sizeof(filename), "../misc/samplerz_statistics/samples_hw_hist/%016lX_%016lX.txt", *(uint64_t *)&sigma_inv, *(uint64_t *)&mu);

    FILE *file = fopen(filename, "w");
    if (!file)
    {
        perror("Failed to open file for writing");
        return;
    }

    for (int i = 0; i < 40; i++)
    {
        fprintf(file, "%4d: %10lu\n", pivot_value + i - pivot_index, histogram[i]);
    }

    fclose(file);

    // statistics
    samplerz_wait_full();
    continuous_busy_cycles = dev->busy_cycles.w;
    continuous_bits_used = dev->consumed_bits.w;
    if (i == 0)
    {
        continuous_samples_z1 = sum;
    }
    else
    {
        continuous_samples_z2 = sum;
    }
}

bool samplerz_doublesample_timed(bool falcon1024, double sigma_inv, double mu1, double mu2, int *z1, int *z2)
{
    uint64_t pre_write = rdtsc_barrier();

    samplerz_configure(sigma_inv, mu1, mu2, falcon1024, false);
    dev->control.f.start = 1;

    uint64_t pre = rdtsc_barrier();

    while (dev->control.f.done == 0)
    {
        // Busy wait
    }

    uint64_t post = rdtsc_barrier();

    samplerz_readsamples(z1, z2);

    uint64_t post_read = rdtsc_barrier();

    uint32_t freq = rdtsc_freq();
    printf("Write time: %lu ns\n", (pre - pre_write) * 1000000000 / freq);
    printf("Compute time: %lu ns\n", (post - pre) * 1000000000 / freq);
    printf("Read time: %lu ns\n", (post_read - post) * 1000000000 / freq);
    printf("Total time: %lu ns\n", (post_read - pre_write) * 1000000000 / freq);

    return true;
}

void samplerz_doublesample_no_init(int *z1, int *z2)
{
    dev->control.f.start = 1;
    while (dev->control.f.done == 0)
    {
    }
    samplerz_readsamples(z1, z2);
}

bool run_continuous(double sigma_inv, double mu1, double mu2, int seconds)
{
    samplerz_configure(sigma_inv, mu1, mu2, true, true);

    dev->control.f.start = 1;

    if (seconds >= 0)
    {
        sleep(seconds);
    }
    else
    {
        printf("Press any key to stop...\n");
        getchar();
    }

    samplerz_status();

    dev->control.f.stop = 1;

    samplerz_status();

    return true;
}

void get_n_samples(int n, double sigma_inv, double mu1, double mu2, bool falcon1024)
{
    char filename1[128], filename2[128];
    snprintf(filename1, sizeof(filename1), "../misc/samplerz_statistics/samples_hw/%016lX_%016lX.txt", *(uint64_t *)&sigma_inv, *(uint64_t *)&mu1);
    snprintf(filename2, sizeof(filename2), "../misc/samplerz_statistics/samples_hw/%016lX_%016lX.txt", *(uint64_t *)&sigma_inv, *(uint64_t *)&mu2);
    FILE *file1 = fopen(filename1, "a");
    FILE *file2 = fopen(filename2, "a");
    if (!file1 || !file2)
    {
        perror("Failed to open file for writing");
        return;
    }

    samplerz_configure(sigma_inv, mu1, mu2, falcon1024, false);
    int z1, z2;
    for (int i = 0; i < n; i++)
    {
        samplerz_doublesample_no_init(&z1, &z2);
        fprintf(file1, "%d\n", z1);
        fprintf(file2, "%d\n", z2);
        if (n > 100000 && i % 100000 == 0)
        {
            printf("Sample %d: z1 = %d, z2 = %d\n", i, z1, z2);
        }
    }

    fclose(file1);
    fclose(file2);
}
void randomize_parameters(double *sigma_inv, double *mu1, double *mu2, bool falcon1024)
{
    double sigma_min = falcon1024 ? 1.298280334 : 1.277833697;
    double sigma_max = 1.8205;

    double sigma = sigma_min + (sigma_max - sigma_min) * ((double)rand() / RAND_MAX);
    *sigma_inv = 1.0 / sigma;
    *mu1 = ((double)rand() / RAND_MAX) * 10000.0 - 5000.0;
    *mu2 = ((double)rand() / RAND_MAX) * 10000.0 - 5000.0;
}

void single_sample_test(bool falcon1024)
{
    double sigma_inv, mu1, mu2;
    int z1, z2;

    randomize_parameters(&sigma_inv, &mu1, &mu2, falcon1024);

    printf("Getting samples with sigma_inv = %f, mu1 = %f, mu2 = %f\n", sigma_inv, mu1, mu2);
    if (samplerz_doublesample_timed(true, sigma_inv, mu1, mu2, &z1, &z2))
    {
        printf("Generated samples: z1 = %d, z2 = %d\n", z1, z2);
    }
    else
    {
        printf("Failed to get samples\n");
    }
    samplerz_wait_full();
    samplerz_status();
}

void continuous_test(bool falcon1024, int seconds)
{
    double sigma_inv, mu1, mu2;
    int z1, z2;

    randomize_parameters(&sigma_inv, &mu1, &mu2, falcon1024);

    printf("Getting samples with sigma_inv = %f, mu1 = %f, mu2 = %f\n", sigma_inv, mu1, mu2);
    if (run_continuous(sigma_inv, mu1, mu2, seconds))
    {
        samplerz_histogram(0, sigma_inv, mu1);
        samplerz_histogram(1, sigma_inv, mu2);
    }
    else
    {
        printf("Failed to get samples\n");
    }
    samplerz_wait_full();
    samplerz_status();
}

void get_sample_set(bool falcon1024, int count, int samples)
{
    printf("Getting %d sets of %d samples...\n", count, samples);
    for (int i = 0; i < count; i++)
    {
        double sigma_inv, mu1, mu2;
        randomize_parameters(&sigma_inv, &mu1, &mu2, falcon1024);
        if (count < 10) {
            printf("Getting samples with sigma_inv = %f, mu1 = %f, mu2 = %f\n", sigma_inv, mu1, mu2);
        }
        get_n_samples(samples, sigma_inv, mu1, mu2, falcon1024);
        printf(".");
        fflush(stdout);
    }
    printf("\n");
    samplerz_wait_full();
    samplerz_status();
}

int main()
{
    srand((unsigned int)time(NULL)); // Seed the random number generator with the current time

    map_samplerz_axi();

    printf("Marker: 0x%08X\n", dev->marker.w);

    samplerz_init_prng();
    samplerz_reset();
    samplerz_wait_full();
    samplerz_status();

    bool falcon1024 = true;
    single_sample_test(falcon1024);
    // continuous_test(falcon1024, 10);
    // get_sample_set(falcon1024, 1, 1000000); // large sample set
    get_sample_set(falcon1024, 970, 100000); // same dataset as in falcon reference C tests

    if (total_samples != 0)
    {
        printf(" ===== One-shot =====\n");
        printf("Total double samples: %lu\n", total_samples);
        printf("Total bits used: %lu\n", total_bits_used);
        printf("Total busy cycles: %lu\n", total_busy_cycles);
        printf("Average busy cycles per double sample: %f\n", (double)total_busy_cycles / total_samples);
        printf("Average bits used per double sample: %f\n", (double)total_bits_used / total_samples);
        printf("Average bits used per busy cycle: %f\n", (double)total_bits_used / total_busy_cycles);
    }

    uint64_t continuous_total_samples = continuous_samples_z1 + continuous_samples_z2;
    if (continuous_total_samples != 0)
    {
        printf(" ===== Continuous =====\n");
        printf("Continuous busy cycles: %lu\n", continuous_busy_cycles);
        printf("Continuous bits used: %lu\n", continuous_bits_used);
        printf("Continuous samples z1: %lu\n", continuous_samples_z1);
        printf("Continuous samples z2: %lu\n", continuous_samples_z2);
        printf("Continuous total samples: %lu\n", continuous_total_samples);
        printf("Average busy cycles per continuous sample: %f\n", (double)continuous_busy_cycles / continuous_total_samples);
        printf("Average bits used per continuous sample: %f\n", (double)continuous_bits_used / continuous_total_samples);
        printf("Average bits used per busy cycle: %f\n", (double)continuous_bits_used / continuous_busy_cycles);
    }

    unmap_samplerz_axi();

    return 0;
}
