source open.tcl

prepare_standalone_ips [larg {
    xilinx_fp_mul2
    xilinx_fp_sub2
    xilinx_axi_lite_vip
}]

set sim_top samplerz_axi_tb
set_property top $sim_top [get_fileset sim_1]
set_property xsim.simulate.runtime all [get_fileset sim_1]
update_compile_order -fileset sim_1
launch_simulation
