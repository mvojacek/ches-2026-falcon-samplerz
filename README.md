# CHES 2026: Pipelining FALCON's SamplerZ: Artifacts

This repository contains the artifacts for the [included](./tches2026_4-samplerz.pdf) CHES 2026 paper.

Included are the HDL sources, IP definitions, project creation, implementation and deployment scripts, and some additional data and measurements.

## Quick setup TLDR

- Unless you have Vivado 2025.1 installed:
- Install [Vagrant](https://developer.hashicorp.com/vagrant/install), [Virtualbox](https://www.virtualbox.org/wiki/Downloads) (on any OS)
- Install rsync (on Windows e.g. using [Cygwin](https://www.cygwin.com/install.html))
- Download/clone this repository
- Inside the `vm/` directory:
  - Place AMD credentials in `.env` based on `.env.sample`
  - Run `vagrant up`
    - Follow the instructions on the command line:
    - Once the VM desktop auto-logins and firefox is started, login to AMD account (credentials will be autofilled)
    - Complete the download form. Firefox will close and installation will continue in the commandline. Wait for the command to finish.
  - Run `vagrant provision --provision-with project-zcu`. Wait for the command to finish.
- In the VM, Vivado will start and the project will be open. You may run synthesis, implementation, report usage, timing, etc.
- For more details and other configurations, continue reading.

## Repository layout

- `src/` - hardware sources and their build inputs.
  - `hdl/` - synthesizable RTL.
    - `base_sampler/` - PLA-based base sampler and generated netlists.
    - `chacha/` - ChaCha PRNG core from https://github.com/secworks/chacha.
    - `math/` - custom floating-point arithmetic, conversion, and utility blocks.
    - `measure/` - alternative/instrumented designs used for measurement. Included for completeness, not used in implementation.
    - `pkg/` - shared SystemVerilog packages with constants and type definitions.
    - `rand/` - randomness refill and buffering logic.
    - `samplerz/` - Gaussian-sampler datapath and AXI-Lite top level.
    - `util/` - generic RTL blocks.
  - `registers/` - register-map sources and generated RTL/software bindings for the optional AXI-Lite interface.
    - `samplerz_axi.rdl` - sampler AXI-Lite register specification.
    - `regblock_udps.rdl` and `plugins/` - PeakRDL extensions.
    - `hw/` and `sw/` - generated hardware register blocks and C headers.
    - `doc/` - generated register documentation.
    - `justfile` - register-code generation commands - uses PeakRDL, necessary only if modifying the `.rdl` definition files.
  - `bd/` - Exported Vivado Block Designs.
    - `design_1.tcl` - integrates the sampler as an AXI-Lite peripheral within the KV260 Zynq UltraScale+ processing system.
    - `design_axi_test.tcl` - Simulation harness for the AXI-equipped samplerz peripheral
  - `constr/` - board-specific and out-of-context timing constraints.
  - `flopoco/` - generated FloPoCo floating-point exponent implementation, including generator scripts.
  - `ip/` - Exported Vivado IPs (floating-point MUL, SUB, and AXI verification IP).
  - `sim/` - SystemVerilog test benches and waveform configurations.
    - `samplerz_tb.sv` + `samplerz_tb_behav.wcfg` - direct simulation of the sampler.
    - `samplerz_axi_tb.sv` + `samplerz_axi_tb_behav.wcfg` - simulation of the sampler including its AXI-Lite interface using the Vivado harness block design.
- `scripts/` - Vivado project, simulation, implementation, reporting, export, and XSCT device-tree scripts.
- `out/` - exported KV260 deployment artifacts: bitstream, binary bitstream, hardware handoff, XSA, and device-tree overlay.
  - `reports/zcu104-samplerz/` - ZCU104 bare-core utilization, timing, power Vivado reports, and summary.
- `sw/` - target-side software.
  - `sampler_tests.c` - direct AXI register test program.
  - `falcon_c/` - Falcon C implementation, including optional hardware-sampler integration (`hw_samplerz.c`).
  - `justfile` - build, permission, FPGA-load, and test commands.
  - `reports/` and `out/` - collected benchmark reports and built executables.
- `vm/` - Vagrant+VirtualBox environment for Vivado 2025.1.
- `misc/` - supporting material not used by the main Vivado build.
  - `base_sampler_boolean/` - scripts and data for a Boolean base-sampler implementation.
  - `flopoco_exp_precision/` - scripts, test vectors, and results for FloPoCo exponent-precision experiments.
  - `samplerz_statistics/` - Python analysis, samples, plots, and the bundled Falcon statistical-model code; see its [README](misc/samplerz_statistics/README.md).
  - `samplerz_testvectors/` - generators for some simulation testvectors.
  - `paper_calculations.py` - RIPST and time-area calculations from paper inputs and measured hardware counters. Run `python3 misc/paper_calculations.py` from the repository root.

## Requirements

**Note:** There is a Vagrant+Virtualbox script available, which automates most of the installation and project creation in an isolated environment, see the [VM section](#vivado-vm).

General dependencies:

- Git
- `just` - main recipe runner for the project
- Clang and Make on an aarch or x86 POSIX host for C software
  - The hardware accelerator is only supported on aarch64 (Zynq)
- Python 3.14 for the archived-statistics and register-regeneration environment recipes

For project creation, synthesis and simulation:

- Vivado 2025.1 with Zynq UltraScale+ MPSoC and Kria device support

To regenerate DT overlay for the AXI-Lite peripheral on Linux:

- Vitis/XSCT 2025.1
- `dtc`

Repository setup:

```sh
just clone-xilinx-devicetree # only needed for DT overlay generation
```

Vivado (and Vitis if needed) should be in `PATH`, e.g.:

```sh
source ${INSTALL_DIR}/2025.1/Vivado/settings64.sh
# -- OR --
source ${INSTALL_DIR}/2025.1/Vitis/settings64.sh
```

## Just

Just can be obtained from [github](https://github.com/casey/just) or installed with the convenience script:

```sh
curl https://just.systems/install.sh | bash -s -- --to ~/.local/bin
export PATH="$PATH:$HOME/.local/bin"
```

You can run `just` without arguments to list available commands and command groups, including descriptions. Inspect the `justfile` to see what is run, or use `just -n` to simulate a recipe without running anything.

You can chain multiple recipes in a single invocation:

```sh
just clean kria-project kria-implementation gui
```

## Reproduce the ZCU104 out-of-context synthesis and simulation

This project is used to compare to prior works using this platform. Synthesis, implementation and simulation is possible, deployment is not (a Block Design for the platform would have to be created).

From the repository root:

```sh
# There is a helper to automate most of this:
just zcu # runs: clean, zcu-project, zcu-implementation, gui

just clean # Deletes ./vivado folder and others
# optionally: tweak options in ./scripts/{common,zcu-project}.tcl

just zcu-project # Creates the project in ./vivado
just gui # Opens the vivado GUI for the created project

# either synthetize and implement in the GUI, or:
just zcu-implementation # runs syn+impl
# or in the *Vivado TCL console*:
source ./zcu-implementation.tcl # or any other tcl script from ./scripts
# inspect netlist, report usage, timings, etc.

# either simulate in the GUI, or run any of:
just sim-samplerz # simulate samplerz_tb
just sim-samplerz-axi # simulate samplerz_axi_tb
# The simulations have tweakable constants inline, take a look.
# After running, inspect simulation outputs, and perhaps waveform.
# Alternatively:
# - simply `Set as Top` the desired module under `Simulation sources`
# - `Run Simulation`
# - `Run All` (F3)
# - select appropriate .wcfg tab for this module
# This has the benefit of automatically opening the simulation waveform
# in a scope, instead of only writing it to a .wdb file.
```

Vivado reports for an out-of-context run at 222 MHz on the ZCU104 are provided in `out/reports/zcu104-samplerz/`, including an extracted summary of the most important run results. You may re-generate these reports from a completed implementation run by running:

```sh
just zcu-report
```

Available tops for implementation:

- `samplerz` - only the samplerz core itself
- `samplerz_axi_top` / `samplerz_axi_top_wrapper` - samplerz + PRNG + AXI + histograms
- ... any children of their children

Available tops for simulation:

- `samplerz_tb` - test `samplerz` module (use `samplerz_tb_behav.wcfg`)
- `samplerz_axi_tb` - test `samplerz_axi_top` module using Vivado AXI harness (use `samplerz_axi_tb_behav.wcfg`)
- `*_tb` - other testbenches for submodules

## Reproduce the KV260 hardware build

This project contains a Vivado Block Design for the full KV260 platform, to which the samplerz is connected as an AXI4-Lite peripheral, usable from Linux userspace via `/dev/mem`.

From the repository root:

```sh
# There is a helper to automate most of this:
just kria # runs: clean, kria-project, kria-implementation, gui

just clean
# optionally tweak settings in ./scripts/{common,kria-project}.tcl

just kria-project # creates project
just gui # opens project

# either run synthesis, implementation and bitstream generation manually, or:
just kria-implementation # runs syn+impl+bitstream on the design_1_wrapper top and exports results to ./out
# or in the *Vivado TCL console*:
source ./kria-implementation.tcl # or any other tcl script from ./scripts
```

The results are copied to `./out`:

- `out/samplerz.bit` - bitstream with header
- `out/samplerz.bit.bin` - raw bitstream (no header)
- `out/samplerz.hwh` - hardware handoff file with details about the `design_1` BD
- `out/samplerz.xsa` - hardware platform for use with Vitis

If you modify the memory map of the block design, you must re-generate the DT overlay using Vitis (XSCT):

```sh
just clone-xilinx-devicetree
just devicetree-vitis
```

This will recreate both `out/samplerz.dtsi` and `out/samplerz.dtbo` from the `out/samplerz.xsa` file. It is also possible to manually adjust the `.dtsi` and only recreate the `.dtbo` with `dtc`.

In this project, implementation for other tops and simulations can also be run, although this is not the primary use for this project.

## Deploy on a KV260 Linux target

To get running with the KV260 platform, a Linux system must be imaged onto its SD card, which has the appropriate drivers and user-space tools for the FPGA PL device. We recommend Canonical's 'Ubuntu on AMD' images for this purpose: https://ubuntu.com/download/amd#kria-k26. Specifically, we used, [Ubuntu Desktop 22.04 LTS](https://people.canonical.com/~platform/images/xilinx/kria-ubuntu-22.04/iot-limerick-kria-classic-desktop-2204-20240304-165.img.xz), but [Ubuntu Server 24.04 LTS](https://people.canonical.com/~platform/images/xilinx/kria-ubuntu-24.04/iot-limerick-kria-classic-server-2404-classic-24.04-x07-20250423.img.xz) could likely also be used.

After imaging, mount the root filesystem and ensure the following:

- an SSH key is added, or a password is set and password SSH is enabled
- network configuration is correct (e.g. DHCP)
- copy the whole repository/artifact to the device (this can be done later over SSH using e.g. rsync)

Then, boot the device, connect to it either over SSH or over the USB serial console and login, then:

- install `just` using the convenience script (alternatively, you may run the commands in the `justfile` recipes manually)
- inside of the `sw/` directory you copied:

```sh
just load # (re-)loads the samplerz.bit.bin to the FPGA PL and samplerz.dtbo into the kernel

just build # builds the userspace testing program

# if not running as root:
just perms # makes /dev/mem rw for the current user
just caps # gives the built binary cap_sys_rawio
# these are necessary to work with /dev/mem as a non-root user.

just run # run the samplerz tests
```

If the tests succeed, you may further exercise the module using the Falcon reference C implementation in `sw/falcon_c`, modified to use the accelerator via `/dev/mem`. By default, it uses the software sampler. Select the floating-point backend and enable `FALCON_HW_SAMPLERZ` in `sw/falcon_c/config.h` to use the accelerator. After changing the configuration, rebuild and run the tests and benchmark:

```sh
cd falcon_c
make clean
make
./test_falcon
./speed 0.01
```

Hardware execution requires root or `cap_sys_rawio` and access to `/dev/mem`, same as the samplerz tests.

## Register regeneration

Only needed when changing the register map. From `src/registers/`, install the dependencies from `requirements.txt` and generate RTL, SV constants, HTML, C headers, then Python bindings:

```sh
just env
just gen # runs gen-sv gen-sv-const gen-html gen-c gen-py in order
```

## Vivado VM

The `vm/` directory supplies a recipe for an Ubuntu 24.04 desktop VM with Vivado 2025.1 on a persistent virtual disk. It requires Vagrant, VirtualBox, rsync, AMD credentials, approximately 24 GB RAM, and 110 GB of host disk.

This is the recommended way to reproduce this work, unless you already have Vivado 2025.1 installed.

Requirements:

- [VirtualBox](https://www.virtualbox.org/wiki/Downloads) 7+
- [Vagrant](https://developer.hashicorp.com/vagrant/install) 2.4+
- rsync (on Windows using e.g. [Cygwin](https://www.cygwin.com/install.html))
- 24 GB RAM (configurable)
- at least 110 GB disk space (goes down to ~75 GB after installation)
- AMD account credentials (no licenses required)

Create `./vm/.env` based on `./vm/.env.sample`:

- `XILINX_USERNAME` - AMD account email
- `XILINX_PASSWORD` - AMD account password
- `VIVADO_VM_MEMORY` *(optional, default: `24576`)* - VM memory in MB
- `VIVADO_VM_CPUS` *(optional, default: host physical core count)* - VM CPU count
- `VIVADO_XILINX_DISK_GB` *(optional, default: `100`)* - persistent Vivado disk size in GB

The AMD/Xilinx credentials are used inside the VM during provisioning to download the Vivado installer, and during the installation itself.

VM disks are placed in the `./vm/` directory:

- `vm-root.vdi` - the root and project disk
- `vm-vivado.vdi` - mounted at `/opt/Xilinx`, stores Vivado installation. It is persistent.

Once the `vm-vivado.vdi` disk is created by a successful Vivado installation, it is not removed by `vagrant destroy`, and Vivado installation is not run again if it already exists. This allows for re-building the VM if needed, without re-downloading and re-installing Vivado each time.

To start the VM (and Vivado installation if not completed previously):

```sh
cd vm
vagrant up
# Other useful commands:
vagrant destroy -f
vagrant up --provision
```

The installation process is visible on the command-line. Do not interact with the VM until a logged-in desktop appears: in particular do not try to login before autologin is executed. The screen may turn black briefly while the gdm session is restarted, and this is fine.

If installing Vivado, the download link for the installer will be opened in Firefox inside the VM (but you will immediately be redirected to the AMD login form). The login form should be autofilled with the credentials you provided. Log in, confirm the US export regulation form, and start the download. Once the download is successful, the browser will automatically close and installation will start in the vagrant command line. Should there be any problems with this process, you may manually place the `AMD Unified Installer for FPGAs & Adaptive SoCs 2025.1: Linux Self Extracting Web Installer` .bin file inside `/home/vagrant/Downloads/vivado_installer`.

The installation is completed once the `vagrant up` command exits and can be verified by running e.g. `which vivado` inside a GUI terminal in the VM or inside a shell started by `vagrant ssh`.

The whole repository (except subfolders unnecessary for build) is copied into the VM automatically as `/home/vagrant/Desktop/samplerz`. If you wish to update the copy, you may run `vagrant rsync` at any time.

You may now manually proceed with setting up the project and running it inside the VM. The `just` tool is already installed.

Alternatively, you may run either of

```
vagrant provision --provision-with project-zcu
vagrant provision --provision-with project-kria
```

to start the project creation process from the host and open the GUI automatically.

## LICENSE summary

Externally licensed files:

- misc/samplerz_statistics/falcon/** - [MIT](./misc/samplerz_statistics/falcon/LICENSE) (c) Thomas Prest (2018)
- misc/samplerz_statistics/** (select files) - [PQShield SAGA license](./misc/samplerz_statistics/SAGA_LICENCE) (c) PQShield Ltd. (2019)
- misc/base_sampler_boolean/generator/sampler.c - https://github.com/Angshumank/const_gauss_split
- src/flopoco/flopoco_ieee_exp.vhdl - [LGPL-3.0-only](https://opensource.org/license/lgpl-3-0) (c) Florent de Dinechin, Bogdan Pasca (2007-2022)
- src/hdl/chacha/** - [BSD-2-Clause](./src/hdl/chacha/LICENSE) (c) Joachim Strömbergson (2013)
- src/registers/{sw,doc}/** - PeakRDL GPL-3.0/MIT (see file headers)
- src/hdl/base_sampler/*_netlist.v - subject to AMD EULA
- src/hdl/measure/falconsign_berexp_onlyexp.sv - [Apache-2.0](https://github.com/YiOuyang1/FalconSign/blob/main/LICENSE)
- src/hdl/measure/basesampler_bisamplerz.sv - [Apache-2.0](https://github.com/Shaibk/Bi-SamplerZ/blob/main/LICENSE)
- sw/falcon_c/** - [MIT](./sw/falcon_c/LICENSE) (c) Falcon Project (2017-2020)

This work's original files:

- src/** - [CERN-OHL-S-2.0](./src/LICENSE)
- tches2026_4-samplerz.pdf - [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- *everything else* - dual-licensed under [Apache-2.0 or MIT](./LICENSE), at your option
