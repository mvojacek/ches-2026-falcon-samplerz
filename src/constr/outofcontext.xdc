if {[llength [get_ports -quiet clk]] != 0} {
    create_clock -period 4.5 -name clk [get_ports clk]
}
if {[llength [get_ports -quiet aclk]] != 0} {
    create_clock -period 4.5 -name aclk [get_ports aclk]
}
