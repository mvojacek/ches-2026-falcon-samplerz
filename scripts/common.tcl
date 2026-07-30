# https://wiki.tcl-lang.org/page/Convenient+list+arguments+%2D+larg
proc ::larg list {
    regsub -line -all {^\s*#.*$} $list {} list
    uplevel "list [string map {\n { }} $list]"
}

set project_name falcon
set project_dir "./"
set src_dir "../src"

set verilog_defines [larg {
    # BASE_SAMPLER_NETLIST=defined
    # SZ_KEEP_HIERARCHY=defined
}]

set launch_runs_args {-jobs 6}
# set launch_runs_args {-jobs 4 -host {192.168.3.119 6} -remote_cmd {ssh -q -o User=user -o ConnectTimeout=30 -o ConnectionAttempts=3 -o BatchMode=yes}}

proc configure_project {options} {
    foreach {name value} $options {
        set ::$name $value
    }

    if {$::target eq "kv260"} {
        set ::part_name xck26-sfvc784-2LV-c
        set ::board_properties [list \
            board_part "xilinx.com:kv260_som:part0:1.4" \
            board_connections "som240_1_connector xilinx.com:kv260_carrier:som240_1_connector:1.3" \
            platform.board_id "kv260_som_som240_1_connector_kv260_carrier_som240_1_connector"]
    } elseif {$::target eq "zcu104"} {
        set ::part_name xczu7ev-ffvc1156-2-e
        set ::board_properties [list board_part "xilinx.com:zcu104:part0:1.1"]
    } else {
        error "Unsupported target: $::target"
    }
}

proc prepare_standalone_ips {names} {
    set objects [get_ips -quiet $names]
    if {[llength $objects] != [llength $names]} {
        error "Could not find all standalone IPs: $names"
    }
    foreach ip $objects {
        if {[get_property IS_LOCKED $ip]} {
            upgrade_ip $ip
        }
    }
    generate_target all $objects
    export_ip_user_files -of_objects $objects
    return $objects
}

proc prepare_ip_runs {objects} {
    generate_target all $objects
    export_ip_user_files -of_objects $objects
    foreach ip $objects {
        create_ip_run $ip
    }
}

proc run_incomplete_runs {pattern} {
    set runs [get_runs -regex $pattern -filter {PROGRESS < 100}]
    if {[llength $runs] != 0} {
        launch_runs $runs {*}$::launch_runs_args
        wait_on_runs {*}$runs
    }
}

proc run_main {run {to_step ""}} {
    if {[get_property NEEDS_REFRESH [get_runs $run]]} {
        reset_run $run
    }
    set pending [get_runs $run -filter {PROGRESS < 100}]
    if {[llength $pending] != 0} {
        if {$to_step eq ""} {
            launch_runs $pending {*}$::launch_runs_args
        } else {
            launch_runs $pending {*}$::launch_runs_args -to_step $to_step
        }
        wait_on_runs $pending
    }
}
