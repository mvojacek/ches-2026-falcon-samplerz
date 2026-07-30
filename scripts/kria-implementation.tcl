source open.tcl

set export_name samplerz
set bd design_1
set top design_1_wrapper
set target kv260
set part_name xck26-sfvc784-2LV-c
set con constr_$target
set syn synth_bit
set imp impl_bit

if {[llength [get_filesets $con -quiet]] == 0} {
    create_fileset -constrset $con
}
if {[llength [get_runs $syn -quiet]] == 0} {
    create_run $syn -flow {Vivado Synthesis 2024} -constrset $con -part $part_name
}
if {[llength [get_runs $imp -quiet]] == 0} {
    create_run $imp -flow {Vivado Implementation 2024} -constrset $con -part $part_name -parent_run $syn
}

current_run [get_runs $imp]
set_property top $top [get_fileset sources_1]
update_compile_order -fileset sources_1
set constraint_file "../src/constr/$target.xdc"
if {![file isfile $constraint_file]} {
    error "Missing board constraint file: $constraint_file"
}
add_files -fileset $con -norecurse $constraint_file

set_property {STEPS.SYNTH_DESIGN.ARGS.MORE OPTIONS} {} [get_runs $syn]
set_property STEPS.WRITE_BITSTREAM.ARGS.BIN_FILE true [get_runs $imp]

set ips [larg {
    xilinx_fp_mul2
    xilinx_fp_sub2
    xilinx_axi_lite_vip
}]
prepare_standalone_ips $ips

set obj [get_files ${project_name}.srcs/sources_1/bd/$bd/$bd.bd]
prepare_ip_runs $obj
run_incomplete_runs "${bd}_.*synth_.*"
run_main $syn

if {[get_property NEEDS_REFRESH [get_runs $imp]]} {
    reset_run $imp
}
set run [get_runs $imp -filter {PROGRESS < 100 || STATUS != "write_bitstream Complete!"}]
if {[llength $run] != 0} {
    launch_runs $run {*}$launch_runs_args -to_step write_bitstream
    wait_on_runs $run
}

open_run $imp
write_hw_platform -fixed -include_bit -force -file ../out/$export_name.xsa
file copy -force $project_name.runs/$imp/$top.bit ../out/$export_name.bit
file copy -force $project_name.runs/$imp/$top.bin ../out/$export_name.bit.bin
file copy -force $project_name.gen/sources_1/bd/$bd/hw_handoff/$bd.hwh ../out/$export_name.hwh
