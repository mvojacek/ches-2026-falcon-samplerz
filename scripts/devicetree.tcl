# Copy the hardware design to build directory
file copy -force ../out/samplerz.xsa samplerz.xsa

# Generate the device tree overlay using the hardware design
hsi open_hw_design samplerz.xsa
hsi set_repo_path ../device-tree-xlnx
hsi create_sw_design device-tree -os device_tree -proc psu_cortexa53_0
hsi set_property CONFIG.dt_overlay true [hsi get_os]
hsi set_property CONFIG.dt_zocl true [hsi get_os]
hsi generate_target -dir out
hsi close_hw_design [hsi current_hw_design]

# Export the device tree overlay to the out directory
file copy -force out/pl.dtsi ../out/samplerz.dtsi
