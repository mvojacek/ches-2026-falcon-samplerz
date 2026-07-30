source common.tcl
source open.tcl

set modules [larg {
    samplerz_axi_top
    prng_refill
    chacha_core
    histogram
    samplerz
    fp_abs
    fp_int_frac
    refillable_base_sampler
    refill_uniform_buf_basesampler
    base_sampler_pla_smart
    base_sampler_pla
    base_sampler_rcdt
    i2f_small_z
    i2f_small_z0_sq
    fp_sub
    fp_mul
    fp_div2n
    berexp
    fp_exp
    float_2exp_floor
    refillable_uniform_cmp
    lazy_uniform_cmp
    refill_uniform_buf_cmp
    add_mu_z
}]

# for each of the modules, do as with samplerz_axi_top here:
# create_run synth_area_samplerz_axi_top -flow {Vivado Synthesis 2025}
# create_run impl_area_axi_top -parent_run synth_area_samplerz_axi_top -flow {Vivado Implementation 2025}
# set_property strategy Flow_AreaOptimized_high [get_runs synth_area_samplerz_axi_top]
# set_property -name {STEPS.SYNTH_DESIGN.ARGS.MORE OPTIONS} -value {-mode out_of_context} -objects [get_runs synth_area_samplerz_axi_top]
# set_property top samplerz_axi_top [current_fileset]
# update_compile_order -fileset [current_fileset]
# launch_runs impl_area_axi_top -jobs 12

puts "Phase 1: Reporting..."
foreach module $modules {
    open_run impl_area_${module}
    report_utilization -file "${module}.util.rpt" -name "Utilization Report"
}
