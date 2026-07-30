set target kv260
set top design_1_wrapper
set sim_top samplerz_axi_tb
set recreate 0
set outofcontext 0
source common.tcl
configure_project [list]
source open.tcl

if {$argc > 0} {
    set_property verilog_define $argv [get_filesets sim_1]
}

set_property top $sim_top [get_fileset sim_1]
update_compile_order -fileset sim_1
set_property generate_scripts_only 1 [current_fileset -simset]
launch_simulation
set_property generate_scripts_only 0 [current_fileset -simset]
