source common.tcl
source open.tcl

set modules [larg {
    chacha_core_wrap
    # samplerz_axi_top
    # prng_refill
    # histogram
    # samplerz
    # fp_abs
    # fp_int_frac
    # refillable_base_sampler
    # refill_uniform_buf_basesampler
    # base_sampler_pla_smart
    # base_sampler_pla
    # base_sampler_rcdt
    # i2f_small_z
    # i2f_small_z0_sq
    # fp_sub
    # fp_mul
    # fp_div2n
    # berexp
    # fp_exp
    # float_2exp_floor
    # refillable_uniform_cmp
    # lazy_uniform_cmp
    # refill_uniform_buf_cmp
    # add_mu_z
}]

# for each of the modules, do as with samplerz_axi_top here:
# create_run synth_area_samplerz_axi_top -flow {Vivado Synthesis 2025}
# create_run impl_area_axi_top -parent_run synth_area_samplerz_axi_top -flow {Vivado Implementation 2025}
# set_property strategy Flow_AreaOptimized_high [get_runs synth_area_samplerz_axi_top]
# set_property -name {STEPS.SYNTH_DESIGN.ARGS.MORE OPTIONS} -value {-mode out_of_context} -objects [get_runs synth_area_samplerz_axi_top]
# set_property top samplerz_axi_top [current_fileset]
# update_compile_order -fileset [current_fileset]
# launch_runs impl_area_axi_top -jobs 12

puts "Phase 1: Creating runs..."
foreach module $modules {
    puts "  Processing ${module}..."
    if {[get_runs -quiet synth_area_${module}] == ""} {
        create_run synth_area_${module} -flow {Vivado Synthesis 2025}
    }
    if {[get_runs -quiet impl_area_${module}] == ""} {
        create_run impl_area_${module} -parent_run synth_area_${module} -flow {Vivado Implementation 2025}
    }
}

puts "Phase 2: Configuring runs..."
foreach module $modules {
    puts "  Configuring ${module}..."
    #set_property strategy Flow_AreaOptimized_high [get_runs synth_area_${module}]
    set_property strategy {Vivado Synthesis Defaults} [get_runs synth_area_${module}]
    set_property -name {STEPS.SYNTH_DESIGN.ARGS.MORE OPTIONS} -value {-mode out_of_context} -objects [get_runs synth_area_${module}]
}

puts "Phase 3: Launching runs..."
foreach module $modules {
    puts "  Launching ${module}..."
    reset_run synth_area_${module}
    
    set_property top ${module} [current_fileset]
    update_compile_order -fileset [current_fileset]
    # after 2000
    
    # while {[llength [get_runs -filter {STATUS == "Running"}]] >= 8} {
    #     after 10000
    # }
    
    # launch_runs impl_area_${module} -jobs 1
    launch_runs -scripts_only impl_area_${module} -to_step route_design
    # after 10000
}
