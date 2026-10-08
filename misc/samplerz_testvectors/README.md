# SamplerZ test vectors

This directory contains Falcon SamplerZ known-answer data and scripts that convert it into datasets consumed by the SystemVerilog testbenches.

`parse_test_vector.py` parses the source vectors, `float_fractional_testcases.py` generates floating-point decomposition cases, and `sigma_mus_dataset.py` generates representative sigma/mu combinations.

Run the scripts from this directory using Python with NumPy installed. Input and output paths are relative to the current working directory; the generated `.sv` files are written here, not directly into `src/`.

```bash
python3 parse_test_vector.py
python3 float_fractional_testcases.py
python3 sigma_mus_dataset.py
```

The simulations use copies in `src/sim/data/`. After regeneration, deploy the generated files from this directory:

```bash
cp float_fractional_samplerzkat_testcases.sv ../../src/sim/data/
cp samplerz1024_sigma_mus_dataset.sv ../../src/sim/data/
```
