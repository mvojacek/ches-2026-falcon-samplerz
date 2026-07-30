# SamplerZ test vectors

This directory contains Falcon SamplerZ known-answer data and scripts that convert it into datasets consumed by the SystemVerilog testbenches.

`parse_test_vector.py` parses the source vectors, `float_fractional_testcases.py` generates floating-point decomposition cases, and `sigma_mus_dataset.py` generates representative sigma/mu combinations. The generated `.sv` files reside in src/ for direct use by the simulations.
