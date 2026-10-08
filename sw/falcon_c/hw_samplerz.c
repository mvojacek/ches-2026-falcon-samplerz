
#include <stdio.h>
#include <inttypes.h>
#include "hw_samplerz.h"
#ifdef FALCON_HW_SAMPLERZ
#include <fcntl.h>
#include <sys/mman.h>
#include <stdbool.h>
#include <unistd.h>
#include "../../src/registers/sw/c/samplerz_axi_bitfield_little.h"
#endif

uint64_t total_doublesamples = 0;
uint64_t total_doublesample_cycles = 0;
uint64_t total_singlesamples = 0;
uint64_t total_singlesample_cycles = 0;

void track_doublesample_cycles(uint64_t cycles)
{
    total_doublesamples++;
    total_doublesample_cycles += cycles;
}

void track_singlesample_cycles(uint64_t cycles)
{
    total_singlesamples++;
    total_singlesample_cycles += cycles;
}

static void print_statistics(const char *kind, uint64_t count, uint64_t ticks,
    uint64_t frequency)
{
    printf("Total %ssamples: %" PRIu64 "\n", kind, count);
    printf("Total %ssample ticks: %" PRIu64 "\n", kind, ticks);
    if (count == 0 || frequency == 0) {
        printf("Average %ssample time: N/A\n", kind);
        printf("Average %ssample time (ticks): N/A\n", kind);
        return;
    }
    printf("Average %ssample time: %.2Lf ns\n", kind,
        rdtsc_nanoseconds(ticks, frequency) / (long double)count);
    printf("Average %ssample time (ticks): %.2Lf\n", kind,
        (long double)ticks / (long double)count);
}

void print_sample_statistics(void)
{
    uint64_t frequency = rdtsc_freq();
    printf("Timer: %s, %" PRIu64 " Hz\n", RDTSC_UNITS, frequency);
    print_statistics("single", total_singlesamples, total_singlesample_cycles, frequency);
    print_statistics("double", total_doublesamples, total_doublesample_cycles, frequency);
}

// int Zf(sampler)(void *ctx, fpr mu, fpr isigma);

int Zf(singleSampleSW)(void *ctx, fpr mu, fpr isigma) {
    return Zf(sampler)(ctx, mu, isigma);
}

int Zf(singleSampleSWtimed)(void *ctx, fpr mu, fpr isigma) {
    uint64_t pre = rdtsc_barrier();
    int sample = Zf(sampler)(ctx, mu, isigma);
    uint64_t post = rdtsc_barrier();
    track_singlesample_cycles(post - pre);
    return sample;
}

void Zf(doubleSampleSW)(void *ctx, fpr mu1, fpr mu2, fpr isigma, fpr* t1, fpr* t2)
{
	*t1 = fpr_of(Zf(sampler)(ctx, mu1, isigma));
	*t2 = fpr_of(Zf(sampler)(ctx, mu2, isigma));
}

void Zf(doubleSampleSWtimed)(void *ctx, fpr mu1, fpr mu2, fpr isigma, fpr* t1, fpr* t2)
{
    int z1, z2;
	uint64_t pre = rdtsc_barrier();
	z1 = Zf(sampler)(ctx, mu1, isigma);
	z2 = Zf(sampler)(ctx, mu2, isigma);
	uint64_t post = rdtsc_barrier();
	track_doublesample_cycles(post - pre);
    *t1 = fpr_of(z1);
    *t2 = fpr_of(z2);
}

#ifdef FALCON_HW_SAMPLERZ
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

void samplerz_configure(bool falcon1024, bool continuous)
{
    dev->control.f.falcon1024 = falcon1024;
    dev->control.f.continuous = continuous;
}

typedef union {
    fpr f;
    uint64_t w;
} fpr_union_hack;

static inline uint64_t fpr_to_uint(fpr f) {
    fpr_union_hack temp = { .f = f };
    return temp.w;
}

void configure_from_context(void* ctx) {
    sampler_context* spc = ctx;
    dev->control.f.falcon1024 = fpr_to_uint(spc->sigma_min) == fpr_to_uint(fpr_sigma_min[10]);
}

static inline void hw_doublesample(uint64_t mu1, uint64_t mu2, uint64_t sigma_inv, int* z1, int* z2)
{
    dev->sginv.w = sigma_inv;
    dev->mu1.w = mu1;
    dev->mu2.w = mu2;
    dev->control.f.start = 1;
    while (dev->control.f.done == 0)
    {
    }
    *z1 = *(volatile int32_t*) &dev->z1.w;
    *z2 = *(volatile int32_t*) &dev->z2.w;
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

void init_hw() {
    map_samplerz_axi();
    samplerz_init_prng();
    samplerz_configure(true, false);
    dev->control.f.reset = 1;
}

void Zf(doubleSampleHWtimed)(void *ctx, fpr mu1, fpr mu2, fpr isigma, fpr* t1, fpr* t2)
{
    configure_from_context(ctx);
    int z1, z2;
    uint64_t mu1i = fpr_to_uint(mu1);
    uint64_t mu2i = fpr_to_uint(mu2);
    uint64_t isigmai = fpr_to_uint(isigma);
    uint64_t pre = rdtsc_barrier();
    hw_doublesample(mu1i, mu2i, isigmai, &z1, &z2);
    uint64_t post = rdtsc_barrier();
    track_doublesample_cycles(post - pre);
    *t1 = fpr_of(z1);
    *t2 = fpr_of(z2);
}

int Zf(singleSampleHWtimed)(void *ctx, fpr mu, fpr isigma)
{
    configure_from_context(ctx);
    int sample;
    uint64_t mui = fpr_to_uint(mu);
    uint64_t isigmai = fpr_to_uint(isigma);
    uint64_t pre = rdtsc_barrier();
    hw_doublesample(mui, mui, isigmai, &sample, &sample);
    uint64_t post = rdtsc_barrier();
    track_singlesample_cycles(post - pre);
    return sample;
}
#endif

