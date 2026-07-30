#!/usr/bin/env sage --python

from os import urandom

import numpy as np
from sage.rings.real_mpfr import RealField

RRR = RealField(200)

# RCDT from falcon_py
RCDT_PREC = 72
RCDT = [
    3024686241123004913666,
    1564742784480091954050,
    636254429462080897535,
    199560484645026482916,
    47667343854657281903,
    8595902006365044063,
    1163297957344668388,
    117656387352093658,
    8867391802663976,
    496969357462633,
    20680885154299,
    638331848991,
    14602316184,
    247426747,
    3104126,
    28824,
    198,
    1]


# RCDT basesampler from falcon_py
def basesampler(randombytes=urandom):
    u = int.from_bytes(randombytes(RCDT_PREC >> 3), "little")

    z0 = 0
    for elt in RCDT:
        z0 += int(u < elt)
    return z0

rcdt_sample_counts = [0] * 19
for i in range(1000000):
    sample = basesampler()
    rcdt_sample_counts[sample] += 1
rcdt_samples = sum(rcdt_sample_counts)
rcdt_samples_normalized = [x / rcdt_samples for x in rcdt_sample_counts]

from samples_postsyn import sample_counts, used_counts

samples = np.array(sample_counts)
indices = samples[0,:,0]
samples = samples[0,:,1]
samples = samples / samples.sum()

# used average
used_counts = np.array(used_counts)
used_indices = used_counts[0,:,0]
used_counts = used_counts[:,:,1]
used_counts = used_counts.sum(axis=0)
used_counts = used_counts / used_counts.sum()
used_avg = np.average(used_indices, weights=used_counts)

print(f"Used bits avg: {used_avg}")

# get a theoretical distribution in the graph
falcon_sigma_max = RRR(1.8205)
falcon_sigma_max_2sqi = RRR(1) / (2 * falcon_sigma_max * falcon_sigma_max)
exp_y = [(-RRR(x * x) * falcon_sigma_max_2sqi).exp() for x in indices]
# computed to high precision in Mathematica using the jacobi theta-3 function
norm_factor = RRR("2.78165838698286821622928290962579613100690729989801914044547309804236244786646278878491561464967268708244551492586772024")
exp_y_normalized = [x / norm_factor for x in exp_y]

# plot both under each other as a bar chart
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2)
axs[0].bar([x-0.3 for x in indices], samples, width=0.3, color='red', label='DUT')
axs[0].bar([x for x in indices], exp_y_normalized, width=0.3, color='b', label='Discrete half-gaussian')
axs[0].bar([x+0.3 for x in indices], rcdt_samples_normalized, width=0.3, color='green', label='RCDT')
used_bar = axs[1].bar(used_indices, used_counts, color='blue')
axs[1].bar_label(used_bar, fmt='%.3f', label_type='edge')
axs[0].set_title('Sample probability distribution (1M samples)')
axs[1].set_title('Used bits of randomness')
axs[0].set_xlabel('z')
axs[1].set_xlabel('bits')
axs[0].set_ylabel('Probability')
axs[1].set_ylabel('Probability')
axs[0].legend()
axs[0].set_xticks(indices)
axs[1].set_xticks(used_indices)
axs[1].set_yticks(np.arange(0, 0.5, 0.1))
# plot range
axs[0].set_xlim([0.5, 10.5])
axs[0].set_ylim([10e-7, 0.9])
axs[1].set_xlim([1.5, 12.5])
axs[1].set_ylim([0, 0.6])
axs[0].set_yscale('log')
# show the plot
plt.tight_layout()
plt.savefig("boolean-sampler-data.svg")
plt.show()
