if {![info exists target]} {
    error "Set project options before sourcing project.tcl"
}

source common.tcl
configure_project [list]

set cur [current_project -quiet]
if {$recreate || ![file isfile ${project_name}.xpr]} {
    if {$cur ne ""} {
        close_project
    }
    create_project $project_name $project_dir -part $part_name -force
} elseif {$cur ne $project_name} {
    if {$cur ne ""} {
        close_project
    }
    open_project "${project_name}.xpr"
}

set obj [current_project]
foreach {name value} $board_properties {
    set_property -name $name -value $value -objects $obj
}
set_property target_language Verilog $obj
set_property simulator_language Mixed $obj

if {[string equal [get_filesets -quiet sources_1] ""]} {
    create_fileset -srcset sources_1
}
if {[string equal [get_filesets -quiet constrs_ooc] ""]} {
    create_fileset -constrset constrs_ooc
}
if {[string equal [get_filesets -quiet sim_1] ""]} {
    create_fileset -simset sim_1
}

set_property INCLUDE_DIRS [larg {
    "../src/hdl/include"
}] [current_fileset]

set obj [get_fileset sources_1]
add_files -fileset $obj -norecurse [larg {
    "../src/hdl/base_sampler/base_sampler_pla_smart.sv"

    "../src/hdl/chacha/chacha_qr.v"
    "../src/hdl/chacha/chacha_core.v"

    "../src/hdl/math/float_2exp_floor.sv"
    "../src/hdl/math/fp_abs.sv"
    "../src/hdl/math/fp_div2n.sv"
    "../src/hdl/math/fp_exp.sv"
    "../src/hdl/math/fp_int_frac.sv"
    "../src/hdl/math/fp_mul.sv"
    "../src/hdl/math/fp_negate.sv"
    "../src/hdl/math/fp_sub.sv"
    "../src/hdl/math/i2f_small.sv"
    "../src/hdl/math/lz_counter.sv"

    "../src/hdl/pkg/fp_pkg.sv"
    "../src/hdl/pkg/samplerz_pkg.sv"

    "../src/hdl/rand/refills.sv"
    "../src/hdl/rand/lazy_uniform_cmp.sv"
    "../src/hdl/rand/parallel_to_serial.sv"
    "../src/hdl/rand/refill_uniform_buf.sv"
    "../src/hdl/rand/prng_refill.sv"

    "../src/hdl/samplerz/add_mu_z.sv"
    "../src/hdl/samplerz/adjust_z0_to_z.sv"
    "../src/hdl/samplerz/berexp.sv"
    "../src/hdl/samplerz/refillable_base_sampler.sv"
    "../src/hdl/samplerz/refillable_uniform_cmp.sv"
    "../src/hdl/samplerz/samplerz.sv"
    "../src/hdl/samplerz/samplerz_axi_top.sv"

    "../src/hdl/util/delay.sv"
    "../src/hdl/util/histogram.sv"

    "../src/flopoco/flopoco_ieee_exp.vhdl"

    "../src/registers/axi4lite_intf.sv"
    "../src/registers/hw/samplerz_axi.sv"
    "../src/registers/hw/samplerz_axi_pkg.sv"
    "../src/registers/hw/samplerz_axi_map_pkg.sv"
}]
add_files -fileset $obj -norecurse "../src/hdl/samplerz/samplerz_axi_top_wrapper.v"
update_compile_order -fileset sources_1

if {$recreate} {
    foreach design [larg {
        design_1
        design_axi_test
    }] {
        source ../src/bd/$design.tcl
        make_wrapper -files [get_files $project_name.srcs/sources_1/bd/$design/$design.bd] -top -import
        close_bd_design [get_bd_designs $design]
    }
}

set ips [larg {
    xilinx_fp_mul2
    xilinx_fp_sub2
    xilinx_axi_lite_vip
}]
set ip_files [lmap f $ips {set f "../src/ip/$f/$f.xci"}]
add_files -fileset $obj -norecurse $ip_files

set obj [get_fileset constrs_ooc]
add_files -fileset $obj -norecurse [larg {
    "../src/constr/outofcontext.xdc"
}]

set obj [get_fileset sim_1]
add_files -fileset $obj -norecurse [larg {
    "../src/sim/base_sampler_pla_smart_tb.sv"
    "../src/sim/float_fractional_tb.sv"
    "../src/sim/i2f_small_tb.sv"
    "../src/sim/lazy_uniform_cmp_tb.sv"
    "../src/sim/refill_uniform_buf_tb.sv"
    "../src/sim/refill_uniform_buf_tb_behav.wcfg"
    "../src/sim/samplerz_tb.sv"
    "../src/sim/samplerz_tb_behav.wcfg"
    "../src/sim/samplerz_axi_tb.sv"
    "../src/sim/samplerz_axi_tb_behav.wcfg"
    "../src/sim/histogram_tb.sv"
    "../src/sim/histogram_tb_behav.wcfg"
}]

add_files -fileset sources_1 -scan_for_includes
add_files -fileset sim_1 -scan_for_includes

if {$outofcontext} {
    set_property -name {STEPS.SYNTH_DESIGN.ARGS.MORE OPTIONS} -value {-mode out_of_context} -objects [get_runs synth_1]
    set_property constrset constrs_ooc [get_runs impl_1]
    set_property constrset constrs_ooc [get_runs synth_1]
} else {
    set_property -name {STEPS.SYNTH_DESIGN.ARGS.MORE OPTIONS} -value {} -objects [get_runs synth_1]
}

foreach fs [get_filesets] {
    set_property -quiet verilog_define $verilog_defines $fs
}

set_property top $top [get_fileset sources_1]
update_compile_order -fileset sources_1
set_property top $sim_top [get_fileset sim_1]
update_compile_order -fileset sim_1
