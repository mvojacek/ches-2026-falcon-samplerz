# Boolean base sampler

This directory contains tooling for generating and evaluating the Boolean decision-tree implementation of Falcon's base Gaussian sampler.

- `generator/` builds the sampler tree from Falcon's probability distribution and converts it to SystemVerilog.
- `testing/` contains scripts and captured data for checking the output distribution and randomness consumption against reference samplers.
