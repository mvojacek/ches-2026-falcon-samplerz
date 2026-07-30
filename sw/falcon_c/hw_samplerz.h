#ifndef HW_SAMPLERZ_H
#define HW_SAMPLERZ_H

#include "config.h"
#include "inner.h"
#include "../rdtsc.h"

void track_doublesample_cycles(uint64_t cycles);
void print_sample_statistics();

void init_hw();

int Zf(singleSampleSW)(void *ctx, fpr mu, fpr isigma);
int Zf(singleSampleSWtimed)(void *ctx, fpr mu, fpr isigma);
int Zf(singleSampleHWtimed)(void *ctx, fpr mu, fpr isigma);

void Zf(doubleSampleSW)(void *ctx, fpr mu1, fpr mu2, fpr isigma, fpr* t1, fpr* t2);
void Zf(doubleSampleSWtimed)(void *ctx, fpr mu1, fpr mu2, fpr isigma, fpr* t1, fpr* t2);
void Zf(doubleSampleHWtimed)(void *ctx, fpr mu1, fpr mu2, fpr isigma, fpr* t1, fpr* t2);

#ifdef FALCON_HW_SAMPLERZ
#define doubleSample (Zf(doubleSampleHWtimed))
#define singleSample (Zf(singleSampleHWtimed))
#else
#define doubleSample (Zf(doubleSampleSWtimed))
#define singleSample (Zf(singleSampleSWtimed))
#endif

#endif
