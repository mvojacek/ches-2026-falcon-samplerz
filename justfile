_list:
    @just -l

[private]
mkdirs:
    mkdir -p src/ip/*/gen vivado vitis
[private]
links: mkdirs
    cd vivado && ln -sf ../scripts/*.tcl ./
    cd vitis && ln -sf ../scripts/*.tcl ./

# Delete projects and IP outputs
[group('util')]
clean: && mkdirs
    rm -rf src/ip/*/gen vivado vitis

# Setup the project for the ZCU104
[group('zcu')]
zcu-project: mkdirs links
    cd vivado && vivado -mode batch -source ./zcu-project.tcl
# Run synthesis and implementation. Needs project.
[group('zcu')]
zcu-implementation:
    cd vivado && vivado -mode batch -source ./zcu-implementation.tcl
# Generate and export reports for a completed ZCU implementation.
[group('zcu')]
zcu-report:
    cd vivado && vivado -mode batch -source ./zcu-report.tcl
    python3 scripts/export-reports-zcu.py
# Clean, setup project, and build for ZCU, and open GUI
[group('zcu')]
zcu: clean zcu-project zcu-implementation gui

# Setup the project for the Kria KV260
[group('kria')]
kria-project: mkdirs links
    cd vivado && vivado -mode batch -source ./kria-project.tcl
# Run synthesis, implementation and generate bitstream. Needs project.
[group('kria')]
kria-implementation:
    cd vivado && vivado -mode batch -source ./kria-implementation.tcl
# Clean, setup project, and build for Kria, and open GUI
[group('kria')]
kria: clean kria-project kria-implementation gui

# Open the project in the Vivado GUI. Needs project.
[group('utils')]
gui:
    #!/bin/sh
    [ -t 1 ] && exec 1>/dev/null
    [ -t 2 ] && exec 2>/dev/null
    cd vivado && exec vivado falcon.xpr &

# Start the Vivado TCL console
[group('utils')]
cli:
    cd vivado && exec vivado -mode tcl

# Run simulation of samplerz AXI module. Needs project.
[group('simulation')]
sim-samplerz-axi:
    cd vivado && vivado -mode batch -source ./sim-samplerz-axi.tcl
    # To open the simulation waveform, run the following in a Vivado TCL console:
    # open_wave_database ./falcon.sim/sim_1/behav/xsim/samplerz_axi_tb_behav.wdb
    # open_wave_config ../src/sim/samplerz_axi_tb_behav.wcfg

# Run simulation of samplerz bare module. Needs project.
[group('simulation')]
sim-samplerz:
    cd vivado && vivado -mode batch -source ./sim-samplerz.tcl
    # To open the simulation waveform, run the following in a Vivado TCL console:
    # open_wave_database ./falcon.sim/sim_1/behav/xsim/samplerz_tb_behav.wdb
    # open_wave_config ../src/sim/samplerz_tb_behav.wcfg

# Clone the xilinx device tree repo needed to build DT overlays
[group('device-tree')]
clone-xilinx-devicetree:
    git clone https://github.com/Xilinx/device-tree-xlnx || true
    cd device-tree-xlnx && git checkout xlnx_rel_v2025.1 && git pull

# Generate device tree .dtsi from .xsa using Vitis, then generate .dtbo
[group('device-tree')]
devicetree-vitis: && devicetree
    cd vitis && xsct devicetree.tcl

# Generate .dtbo from .dtsi using dtc
[group('device-tree')]
devicetree:
    dtc -I dts -O dtb -o out/samplerz.dtbo out/samplerz.dtsi

# Setup and build Kria project including bitstream and device-tree
all: kria clone-xilinx-devicetree devicetree-vitis devicetree
