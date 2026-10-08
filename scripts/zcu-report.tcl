# Require completed runs before reporting the routed bare core.
if {[current_project -quiet] eq ""} { source open.tcl }
assert_run_complete synth_1
assert_run_complete impl_1
open_run impl_1

# Resource, timing, and power reports.
set report_dir ../out/reports/zcu104-samplerz
file mkdir $report_dir
report_utilization -file $report_dir/utilization.rpt
report_utilization -hierarchical -file $report_dir/utilization-hierarchical.rpt
report_timing_summary -delay_type min_max -report_unconstrained -max_paths 10 -file $report_dir/timing-summary.rpt
report_timing -delay_type max -max_paths 10 -file $report_dir/setup-paths.rpt
report_timing -delay_type min -max_paths 10 -file $report_dir/hold-paths.rpt
report_power -file $report_dir/power.rpt
puts "REPORTS_COMPLETE out/reports/zcu104-samplerz"
