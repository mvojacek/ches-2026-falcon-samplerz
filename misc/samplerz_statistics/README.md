# SamplerZ statistics

This directory contains scripts, sample archives, statistical results, plots, and a notebook used to evaluate SamplerZ output from simulation and hardware against Falcon reference samples.

`load_samples.py` contains functions to load the captured samples and histograms, while `saga.py` and the bundled Falcon reference code provide the statistical tests. Use the `justfile` to unpack or repack the sample archive.

From this directory, using Python 3.14:

```sh
just decompress # unpack sample archive
just env # create venv and install requirements.txt
just analyze # run the notebook
```

`just analyze` executes `notebook.ipynb` in place, updating its outputs, the p-value CSVs, and separate simulation and hardware histogram PDFs. Note that the notebook is distributed pre-run including its plot outputs:

- `samplerz_hw_histograms_3x2.pdf` - histograms of samples collected in hardware on the Zynq platform for 6 parameter-sets
- `samplerz_sim_histograms_5x4.pdf` - histograms of 20 parameter-sets obtained by behavioral simulation

Additionally, `samplerz_sim_large_histograms_3x2.pdf` and `samplerz_sim_large_histograms_5x5.pdf` show results from larger simulation datasets that are not distributed due to their size. Similar datasets can be generated at any time using the provided simulation scripts.
