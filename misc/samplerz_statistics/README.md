# SamplerZ statistics

This directory contains scripts, sample archives, statistical results, plots, and a notebook used to evaluate SamplerZ output from simulation and hardware against Falcon reference samples.

`load_samples.py` loads the captured samples and histograms, while `saga.py` and the bundled Falcon reference code support the statistical tests. Use the `justfile` to unpack or repack the sample archive. Python dependencies are listed in `requirements.txt` if you need to re-run them.
