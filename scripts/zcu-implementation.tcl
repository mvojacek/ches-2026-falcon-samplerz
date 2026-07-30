source open.tcl

set top samplerz
set sim_top samplerz_axi_tb

set_property top $top [get_fileset sources_1]
update_compile_order -fileset sources_1
set_property top $sim_top [get_fileset sim_1]
update_compile_order -fileset sim_1

set ips [larg {
    xilinx_fp_mul2
    xilinx_fp_sub2
    xilinx_axi_lite_vip
}]
prepare_standalone_ips $ips
run_main synth_1
run_main impl_1
