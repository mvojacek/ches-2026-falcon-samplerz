source common.tcl

set cur [current_project -quiet]
if {$cur ne $project_name} {
    if {$cur ne ""} {
        close_project
    }
    open_project "${project_name}.xpr"
}