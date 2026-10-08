#ifndef RDTSC_H
#define RDTSC_H

#include <stdint.h>

#if defined(__ARM_ARCH_ISA_A64) || defined(__aarch64__)
#define RDTSC_UNITS "architectural counter ticks"

// https://stackoverflow.com/a/78053906, modified
// Adapted from: https://github.com/cloudius-systems/osv/blob/master/arch/aarch64/arm-clock.cc
static inline uint64_t rdtsc() {
    //Please note we read CNTVCT cpu system register which provides
    //the accross-system consistent value of the virtual system counter.
    uint64_t cntvct;
    asm volatile ("mrs %0, cntvct_el0; " : "=r"(cntvct) :: "memory");
    return cntvct;
}

static inline uint64_t rdtsc_barrier() {
    uint64_t cntvct;
    asm volatile ("isb; mrs %0, cntvct_el0; isb; " : "=r"(cntvct) :: "memory");
    return cntvct;
}

static inline uint32_t rdtsc_freq() {
    uint64_t freq_hz;
    asm volatile ("mrs %0, cntfrq_el0; isb; " : "=r"(freq_hz) :: "memory");
    return (uint32_t) freq_hz;
}
#elif defined(__x86_64__) || defined(__i386__)
#define RDTSC_UNITS "monotonic nanoseconds"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdatomic.h>

static inline uint64_t rdtsc() {
    struct timespec now;
    if (clock_gettime(CLOCK_MONOTONIC, &now) != 0) {
        perror("clock_gettime");
        exit(EXIT_FAILURE);
    }
    return (uint64_t)now.tv_sec * UINT64_C(1000000000) + (uint64_t)now.tv_nsec;
}

static inline uint64_t rdtsc_barrier() {
    atomic_signal_fence(memory_order_seq_cst);
    uint64_t value = rdtsc();
    atomic_signal_fence(memory_order_seq_cst);
    return value;
}

static inline uint32_t rdtsc_freq() {
    return UINT32_C(1000000000);
}
#else
#error Unsupported timer target: requires AArch64 or POSIX x86
#endif

static inline long double rdtsc_nanoseconds(uint64_t ticks, uint64_t frequency) {
    return (long double)ticks * 1000000000.0L / (long double)frequency;
}

#endif
