# FloPoCo exponential precision

This directory contains the inputs, testbench, and analysis scripts used to measure the numerical error of the FloPoCo-generated floating-point exponential unit.

The compressed test vectors can be unpacked with `uncompress.sh`. Run `just flopoco5-exp-precision` to analyze the simulator output and regenerate the precision report and plot; this requires SageMath and Matplotlib.
