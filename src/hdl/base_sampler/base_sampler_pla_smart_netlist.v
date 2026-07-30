// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
// Date        : Wed Apr 16 01:14:41 2025
// Host        : xps running 64-bit Pop!_OS 24.04 LTS
// Command     : write_verilog /home/xxx/Falcon/repo/src/hdl/base_sampler/base_sampler_pla_smart.netlist.v
// Design      : base_sampler_pla_smart_reg
// Purpose     : This is a Verilog netlist of the current design or from a specific cell of the design. The output is an
//               IEEE 1364-2001 compliant Verilog HDL file that contains netlist information obtained from the input
//               design files.
// Device      : xck26-sfvc784-2LV-c
// --------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

`ifdef BASE_SAMPLER_NETLIST
module base_sampler_pla_smart // @suppress "Design unit name"

   (uniform,
    sample,
    used);
  input [71:0]uniform;
  output [4:0]sample;
  output [6:0]used;

  wire [4:0]sample;
  wire \sample[0]_INST_0_i_10_n_0 ;
  wire \sample[0]_INST_0_i_11_n_0 ;
  wire \sample[0]_INST_0_i_12_n_0 ;
  wire \sample[0]_INST_0_i_13_n_0 ;
  wire \sample[0]_INST_0_i_14_n_0 ;
  wire \sample[0]_INST_0_i_15_n_0 ;
  wire \sample[0]_INST_0_i_16_n_0 ;
  wire \sample[0]_INST_0_i_17_n_0 ;
  wire \sample[0]_INST_0_i_18_n_0 ;
  wire \sample[0]_INST_0_i_19_n_0 ;
  wire \sample[0]_INST_0_i_1_n_0 ;
  wire \sample[0]_INST_0_i_20_n_0 ;
  wire \sample[0]_INST_0_i_21_n_0 ;
  wire \sample[0]_INST_0_i_22_n_0 ;
  wire \sample[0]_INST_0_i_23_n_0 ;
  wire \sample[0]_INST_0_i_24_n_0 ;
  wire \sample[0]_INST_0_i_25_n_0 ;
  wire \sample[0]_INST_0_i_26_n_0 ;
  wire \sample[0]_INST_0_i_27_n_0 ;
  wire \sample[0]_INST_0_i_28_n_0 ;
  wire \sample[0]_INST_0_i_29_n_0 ;
  wire \sample[0]_INST_0_i_2_n_0 ;
  wire \sample[0]_INST_0_i_30_n_0 ;
  wire \sample[0]_INST_0_i_31_n_0 ;
  wire \sample[0]_INST_0_i_32_n_0 ;
  wire \sample[0]_INST_0_i_33_n_0 ;
  wire \sample[0]_INST_0_i_34_n_0 ;
  wire \sample[0]_INST_0_i_35_n_0 ;
  wire \sample[0]_INST_0_i_36_n_0 ;
  wire \sample[0]_INST_0_i_37_n_0 ;
  wire \sample[0]_INST_0_i_38_n_0 ;
  wire \sample[0]_INST_0_i_39_n_0 ;
  wire \sample[0]_INST_0_i_3_n_0 ;
  wire \sample[0]_INST_0_i_40_n_0 ;
  wire \sample[0]_INST_0_i_41_n_0 ;
  wire \sample[0]_INST_0_i_42_n_0 ;
  wire \sample[0]_INST_0_i_43_n_0 ;
  wire \sample[0]_INST_0_i_44_n_0 ;
  wire \sample[0]_INST_0_i_45_n_0 ;
  wire \sample[0]_INST_0_i_46_n_0 ;
  wire \sample[0]_INST_0_i_47_n_0 ;
  wire \sample[0]_INST_0_i_48_n_0 ;
  wire \sample[0]_INST_0_i_49_n_0 ;
  wire \sample[0]_INST_0_i_4_n_0 ;
  wire \sample[0]_INST_0_i_50_n_0 ;
  wire \sample[0]_INST_0_i_51_n_0 ;
  wire \sample[0]_INST_0_i_52_n_0 ;
  wire \sample[0]_INST_0_i_53_n_0 ;
  wire \sample[0]_INST_0_i_54_n_0 ;
  wire \sample[0]_INST_0_i_55_n_0 ;
  wire \sample[0]_INST_0_i_56_n_0 ;
  wire \sample[0]_INST_0_i_57_n_0 ;
  wire \sample[0]_INST_0_i_58_n_0 ;
  wire \sample[0]_INST_0_i_59_n_0 ;
  wire \sample[0]_INST_0_i_5_n_0 ;
  wire \sample[0]_INST_0_i_60_n_0 ;
  wire \sample[0]_INST_0_i_61_n_0 ;
  wire \sample[0]_INST_0_i_62_n_0 ;
  wire \sample[0]_INST_0_i_63_n_0 ;
  wire \sample[0]_INST_0_i_64_n_0 ;
  wire \sample[0]_INST_0_i_65_n_0 ;
  wire \sample[0]_INST_0_i_66_n_0 ;
  wire \sample[0]_INST_0_i_67_n_0 ;
  wire \sample[0]_INST_0_i_68_n_0 ;
  wire \sample[0]_INST_0_i_69_n_0 ;
  wire \sample[0]_INST_0_i_6_n_0 ;
  wire \sample[0]_INST_0_i_70_n_0 ;
  wire \sample[0]_INST_0_i_71_n_0 ;
  wire \sample[0]_INST_0_i_72_n_0 ;
  wire \sample[0]_INST_0_i_73_n_0 ;
  wire \sample[0]_INST_0_i_74_n_0 ;
  wire \sample[0]_INST_0_i_75_n_0 ;
  wire \sample[0]_INST_0_i_76_n_0 ;
  wire \sample[0]_INST_0_i_7_n_0 ;
  wire \sample[0]_INST_0_i_8_n_0 ;
  wire \sample[0]_INST_0_i_9_n_0 ;
  wire \sample[1]_INST_0_i_10_n_0 ;
  wire \sample[1]_INST_0_i_11_n_0 ;
  wire \sample[1]_INST_0_i_12_n_0 ;
  wire \sample[1]_INST_0_i_13_n_0 ;
  wire \sample[1]_INST_0_i_14_n_0 ;
  wire \sample[1]_INST_0_i_15_n_0 ;
  wire \sample[1]_INST_0_i_16_n_0 ;
  wire \sample[1]_INST_0_i_17_n_0 ;
  wire \sample[1]_INST_0_i_18_n_0 ;
  wire \sample[1]_INST_0_i_19_n_0 ;
  wire \sample[1]_INST_0_i_1_n_0 ;
  wire \sample[1]_INST_0_i_20_n_0 ;
  wire \sample[1]_INST_0_i_21_n_0 ;
  wire \sample[1]_INST_0_i_22_n_0 ;
  wire \sample[1]_INST_0_i_23_n_0 ;
  wire \sample[1]_INST_0_i_24_n_0 ;
  wire \sample[1]_INST_0_i_25_n_0 ;
  wire \sample[1]_INST_0_i_26_n_0 ;
  wire \sample[1]_INST_0_i_27_n_0 ;
  wire \sample[1]_INST_0_i_28_n_0 ;
  wire \sample[1]_INST_0_i_29_n_0 ;
  wire \sample[1]_INST_0_i_2_n_0 ;
  wire \sample[1]_INST_0_i_30_n_0 ;
  wire \sample[1]_INST_0_i_31_n_0 ;
  wire \sample[1]_INST_0_i_32_n_0 ;
  wire \sample[1]_INST_0_i_33_n_0 ;
  wire \sample[1]_INST_0_i_34_n_0 ;
  wire \sample[1]_INST_0_i_35_n_0 ;
  wire \sample[1]_INST_0_i_36_n_0 ;
  wire \sample[1]_INST_0_i_37_n_0 ;
  wire \sample[1]_INST_0_i_38_n_0 ;
  wire \sample[1]_INST_0_i_39_n_0 ;
  wire \sample[1]_INST_0_i_3_n_0 ;
  wire \sample[1]_INST_0_i_40_n_0 ;
  wire \sample[1]_INST_0_i_41_n_0 ;
  wire \sample[1]_INST_0_i_42_n_0 ;
  wire \sample[1]_INST_0_i_43_n_0 ;
  wire \sample[1]_INST_0_i_44_n_0 ;
  wire \sample[1]_INST_0_i_45_n_0 ;
  wire \sample[1]_INST_0_i_46_n_0 ;
  wire \sample[1]_INST_0_i_47_n_0 ;
  wire \sample[1]_INST_0_i_48_n_0 ;
  wire \sample[1]_INST_0_i_49_n_0 ;
  wire \sample[1]_INST_0_i_4_n_0 ;
  wire \sample[1]_INST_0_i_50_n_0 ;
  wire \sample[1]_INST_0_i_51_n_0 ;
  wire \sample[1]_INST_0_i_52_n_0 ;
  wire \sample[1]_INST_0_i_53_n_0 ;
  wire \sample[1]_INST_0_i_54_n_0 ;
  wire \sample[1]_INST_0_i_55_n_0 ;
  wire \sample[1]_INST_0_i_56_n_0 ;
  wire \sample[1]_INST_0_i_57_n_0 ;
  wire \sample[1]_INST_0_i_58_n_0 ;
  wire \sample[1]_INST_0_i_59_n_0 ;
  wire \sample[1]_INST_0_i_5_n_0 ;
  wire \sample[1]_INST_0_i_60_n_0 ;
  wire \sample[1]_INST_0_i_61_n_0 ;
  wire \sample[1]_INST_0_i_62_n_0 ;
  wire \sample[1]_INST_0_i_63_n_0 ;
  wire \sample[1]_INST_0_i_64_n_0 ;
  wire \sample[1]_INST_0_i_65_n_0 ;
  wire \sample[1]_INST_0_i_66_n_0 ;
  wire \sample[1]_INST_0_i_67_n_0 ;
  wire \sample[1]_INST_0_i_68_n_0 ;
  wire \sample[1]_INST_0_i_69_n_0 ;
  wire \sample[1]_INST_0_i_6_n_0 ;
  wire \sample[1]_INST_0_i_70_n_0 ;
  wire \sample[1]_INST_0_i_71_n_0 ;
  wire \sample[1]_INST_0_i_72_n_0 ;
  wire \sample[1]_INST_0_i_73_n_0 ;
  wire \sample[1]_INST_0_i_74_n_0 ;
  wire \sample[1]_INST_0_i_75_n_0 ;
  wire \sample[1]_INST_0_i_76_n_0 ;
  wire \sample[1]_INST_0_i_7_n_0 ;
  wire \sample[1]_INST_0_i_8_n_0 ;
  wire \sample[1]_INST_0_i_9_n_0 ;
  wire \sample[2]_INST_0_i_10_n_0 ;
  wire \sample[2]_INST_0_i_11_n_0 ;
  wire \sample[2]_INST_0_i_12_n_0 ;
  wire \sample[2]_INST_0_i_13_n_0 ;
  wire \sample[2]_INST_0_i_14_n_0 ;
  wire \sample[2]_INST_0_i_15_n_0 ;
  wire \sample[2]_INST_0_i_16_n_0 ;
  wire \sample[2]_INST_0_i_17_n_0 ;
  wire \sample[2]_INST_0_i_18_n_0 ;
  wire \sample[2]_INST_0_i_19_n_0 ;
  wire \sample[2]_INST_0_i_1_n_0 ;
  wire \sample[2]_INST_0_i_20_n_0 ;
  wire \sample[2]_INST_0_i_21_n_0 ;
  wire \sample[2]_INST_0_i_22_n_0 ;
  wire \sample[2]_INST_0_i_23_n_0 ;
  wire \sample[2]_INST_0_i_24_n_0 ;
  wire \sample[2]_INST_0_i_25_n_0 ;
  wire \sample[2]_INST_0_i_26_n_0 ;
  wire \sample[2]_INST_0_i_27_n_0 ;
  wire \sample[2]_INST_0_i_28_n_0 ;
  wire \sample[2]_INST_0_i_29_n_0 ;
  wire \sample[2]_INST_0_i_2_n_0 ;
  wire \sample[2]_INST_0_i_30_n_0 ;
  wire \sample[2]_INST_0_i_31_n_0 ;
  wire \sample[2]_INST_0_i_32_n_0 ;
  wire \sample[2]_INST_0_i_33_n_0 ;
  wire \sample[2]_INST_0_i_34_n_0 ;
  wire \sample[2]_INST_0_i_35_n_0 ;
  wire \sample[2]_INST_0_i_36_n_0 ;
  wire \sample[2]_INST_0_i_37_n_0 ;
  wire \sample[2]_INST_0_i_38_n_0 ;
  wire \sample[2]_INST_0_i_39_n_0 ;
  wire \sample[2]_INST_0_i_3_n_0 ;
  wire \sample[2]_INST_0_i_40_n_0 ;
  wire \sample[2]_INST_0_i_41_n_0 ;
  wire \sample[2]_INST_0_i_42_n_0 ;
  wire \sample[2]_INST_0_i_43_n_0 ;
  wire \sample[2]_INST_0_i_44_n_0 ;
  wire \sample[2]_INST_0_i_45_n_0 ;
  wire \sample[2]_INST_0_i_46_n_0 ;
  wire \sample[2]_INST_0_i_47_n_0 ;
  wire \sample[2]_INST_0_i_48_n_0 ;
  wire \sample[2]_INST_0_i_49_n_0 ;
  wire \sample[2]_INST_0_i_4_n_0 ;
  wire \sample[2]_INST_0_i_50_n_0 ;
  wire \sample[2]_INST_0_i_51_n_0 ;
  wire \sample[2]_INST_0_i_52_n_0 ;
  wire \sample[2]_INST_0_i_53_n_0 ;
  wire \sample[2]_INST_0_i_54_n_0 ;
  wire \sample[2]_INST_0_i_55_n_0 ;
  wire \sample[2]_INST_0_i_56_n_0 ;
  wire \sample[2]_INST_0_i_57_n_0 ;
  wire \sample[2]_INST_0_i_58_n_0 ;
  wire \sample[2]_INST_0_i_59_n_0 ;
  wire \sample[2]_INST_0_i_5_n_0 ;
  wire \sample[2]_INST_0_i_60_n_0 ;
  wire \sample[2]_INST_0_i_61_n_0 ;
  wire \sample[2]_INST_0_i_62_n_0 ;
  wire \sample[2]_INST_0_i_63_n_0 ;
  wire \sample[2]_INST_0_i_64_n_0 ;
  wire \sample[2]_INST_0_i_65_n_0 ;
  wire \sample[2]_INST_0_i_66_n_0 ;
  wire \sample[2]_INST_0_i_67_n_0 ;
  wire \sample[2]_INST_0_i_68_n_0 ;
  wire \sample[2]_INST_0_i_6_n_0 ;
  wire \sample[2]_INST_0_i_7_n_0 ;
  wire \sample[2]_INST_0_i_8_n_0 ;
  wire \sample[2]_INST_0_i_9_n_0 ;
  wire \sample[3]_INST_0_i_10_n_0 ;
  wire \sample[3]_INST_0_i_11_n_0 ;
  wire \sample[3]_INST_0_i_12_n_0 ;
  wire \sample[3]_INST_0_i_13_n_0 ;
  wire \sample[3]_INST_0_i_14_n_0 ;
  wire \sample[3]_INST_0_i_15_n_0 ;
  wire \sample[3]_INST_0_i_16_n_0 ;
  wire \sample[3]_INST_0_i_17_n_0 ;
  wire \sample[3]_INST_0_i_18_n_0 ;
  wire \sample[3]_INST_0_i_19_n_0 ;
  wire \sample[3]_INST_0_i_1_n_0 ;
  wire \sample[3]_INST_0_i_20_n_0 ;
  wire \sample[3]_INST_0_i_21_n_0 ;
  wire \sample[3]_INST_0_i_22_n_0 ;
  wire \sample[3]_INST_0_i_23_n_0 ;
  wire \sample[3]_INST_0_i_24_n_0 ;
  wire \sample[3]_INST_0_i_25_n_0 ;
  wire \sample[3]_INST_0_i_26_n_0 ;
  wire \sample[3]_INST_0_i_27_n_0 ;
  wire \sample[3]_INST_0_i_28_n_0 ;
  wire \sample[3]_INST_0_i_29_n_0 ;
  wire \sample[3]_INST_0_i_2_n_0 ;
  wire \sample[3]_INST_0_i_30_n_0 ;
  wire \sample[3]_INST_0_i_31_n_0 ;
  wire \sample[3]_INST_0_i_32_n_0 ;
  wire \sample[3]_INST_0_i_33_n_0 ;
  wire \sample[3]_INST_0_i_34_n_0 ;
  wire \sample[3]_INST_0_i_35_n_0 ;
  wire \sample[3]_INST_0_i_36_n_0 ;
  wire \sample[3]_INST_0_i_37_n_0 ;
  wire \sample[3]_INST_0_i_38_n_0 ;
  wire \sample[3]_INST_0_i_39_n_0 ;
  wire \sample[3]_INST_0_i_3_n_0 ;
  wire \sample[3]_INST_0_i_40_n_0 ;
  wire \sample[3]_INST_0_i_41_n_0 ;
  wire \sample[3]_INST_0_i_42_n_0 ;
  wire \sample[3]_INST_0_i_43_n_0 ;
  wire \sample[3]_INST_0_i_44_n_0 ;
  wire \sample[3]_INST_0_i_45_n_0 ;
  wire \sample[3]_INST_0_i_46_n_0 ;
  wire \sample[3]_INST_0_i_47_n_0 ;
  wire \sample[3]_INST_0_i_48_n_0 ;
  wire \sample[3]_INST_0_i_49_n_0 ;
  wire \sample[3]_INST_0_i_4_n_0 ;
  wire \sample[3]_INST_0_i_50_n_0 ;
  wire \sample[3]_INST_0_i_51_n_0 ;
  wire \sample[3]_INST_0_i_52_n_0 ;
  wire \sample[3]_INST_0_i_53_n_0 ;
  wire \sample[3]_INST_0_i_54_n_0 ;
  wire \sample[3]_INST_0_i_55_n_0 ;
  wire \sample[3]_INST_0_i_56_n_0 ;
  wire \sample[3]_INST_0_i_57_n_0 ;
  wire \sample[3]_INST_0_i_58_n_0 ;
  wire \sample[3]_INST_0_i_5_n_0 ;
  wire \sample[3]_INST_0_i_6_n_0 ;
  wire \sample[3]_INST_0_i_7_n_0 ;
  wire \sample[3]_INST_0_i_8_n_0 ;
  wire \sample[3]_INST_0_i_9_n_0 ;
  wire \sample[4]_INST_0_i_10_n_0 ;
  wire \sample[4]_INST_0_i_11_n_0 ;
  wire \sample[4]_INST_0_i_12_n_0 ;
  wire \sample[4]_INST_0_i_13_n_0 ;
  wire \sample[4]_INST_0_i_14_n_0 ;
  wire \sample[4]_INST_0_i_15_n_0 ;
  wire \sample[4]_INST_0_i_16_n_0 ;
  wire \sample[4]_INST_0_i_17_n_0 ;
  wire \sample[4]_INST_0_i_18_n_0 ;
  wire \sample[4]_INST_0_i_19_n_0 ;
  wire \sample[4]_INST_0_i_1_n_0 ;
  wire \sample[4]_INST_0_i_20_n_0 ;
  wire \sample[4]_INST_0_i_21_n_0 ;
  wire \sample[4]_INST_0_i_22_n_0 ;
  wire \sample[4]_INST_0_i_23_n_0 ;
  wire \sample[4]_INST_0_i_24_n_0 ;
  wire \sample[4]_INST_0_i_25_n_0 ;
  wire \sample[4]_INST_0_i_26_n_0 ;
  wire \sample[4]_INST_0_i_2_n_0 ;
  wire \sample[4]_INST_0_i_3_n_0 ;
  wire \sample[4]_INST_0_i_4_n_0 ;
  wire \sample[4]_INST_0_i_5_n_0 ;
  wire \sample[4]_INST_0_i_6_n_0 ;
  wire \sample[4]_INST_0_i_7_n_0 ;
  wire \sample[4]_INST_0_i_8_n_0 ;
  wire \sample[4]_INST_0_i_9_n_0 ;
  wire [71:0]uniform;
  wire [6:0]used;
  wire \used[0]_INST_0_i_10_n_0 ;
  wire \used[0]_INST_0_i_11_n_0 ;
  wire \used[0]_INST_0_i_12_n_0 ;
  wire \used[0]_INST_0_i_13_n_0 ;
  wire \used[0]_INST_0_i_14_n_0 ;
  wire \used[0]_INST_0_i_15_n_0 ;
  wire \used[0]_INST_0_i_16_n_0 ;
  wire \used[0]_INST_0_i_17_n_0 ;
  wire \used[0]_INST_0_i_18_n_0 ;
  wire \used[0]_INST_0_i_19_n_0 ;
  wire \used[0]_INST_0_i_1_n_0 ;
  wire \used[0]_INST_0_i_20_n_0 ;
  wire \used[0]_INST_0_i_21_n_0 ;
  wire \used[0]_INST_0_i_22_n_0 ;
  wire \used[0]_INST_0_i_23_n_0 ;
  wire \used[0]_INST_0_i_24_n_0 ;
  wire \used[0]_INST_0_i_25_n_0 ;
  wire \used[0]_INST_0_i_26_n_0 ;
  wire \used[0]_INST_0_i_27_n_0 ;
  wire \used[0]_INST_0_i_28_n_0 ;
  wire \used[0]_INST_0_i_29_n_0 ;
  wire \used[0]_INST_0_i_2_n_0 ;
  wire \used[0]_INST_0_i_30_n_0 ;
  wire \used[0]_INST_0_i_31_n_0 ;
  wire \used[0]_INST_0_i_32_n_0 ;
  wire \used[0]_INST_0_i_33_n_0 ;
  wire \used[0]_INST_0_i_34_n_0 ;
  wire \used[0]_INST_0_i_35_n_0 ;
  wire \used[0]_INST_0_i_36_n_0 ;
  wire \used[0]_INST_0_i_37_n_0 ;
  wire \used[0]_INST_0_i_38_n_0 ;
  wire \used[0]_INST_0_i_39_n_0 ;
  wire \used[0]_INST_0_i_3_n_0 ;
  wire \used[0]_INST_0_i_40_n_0 ;
  wire \used[0]_INST_0_i_41_n_0 ;
  wire \used[0]_INST_0_i_42_n_0 ;
  wire \used[0]_INST_0_i_43_n_0 ;
  wire \used[0]_INST_0_i_44_n_0 ;
  wire \used[0]_INST_0_i_45_n_0 ;
  wire \used[0]_INST_0_i_46_n_0 ;
  wire \used[0]_INST_0_i_47_n_0 ;
  wire \used[0]_INST_0_i_48_n_0 ;
  wire \used[0]_INST_0_i_49_n_0 ;
  wire \used[0]_INST_0_i_4_n_0 ;
  wire \used[0]_INST_0_i_50_n_0 ;
  wire \used[0]_INST_0_i_51_n_0 ;
  wire \used[0]_INST_0_i_52_n_0 ;
  wire \used[0]_INST_0_i_53_n_0 ;
  wire \used[0]_INST_0_i_54_n_0 ;
  wire \used[0]_INST_0_i_55_n_0 ;
  wire \used[0]_INST_0_i_5_n_0 ;
  wire \used[0]_INST_0_i_6_n_0 ;
  wire \used[0]_INST_0_i_7_n_0 ;
  wire \used[0]_INST_0_i_8_n_0 ;
  wire \used[0]_INST_0_i_9_n_0 ;
  wire \used[1]_INST_0_i_10_n_0 ;
  wire \used[1]_INST_0_i_11_n_0 ;
  wire \used[1]_INST_0_i_12_n_0 ;
  wire \used[1]_INST_0_i_13_n_0 ;
  wire \used[1]_INST_0_i_14_n_0 ;
  wire \used[1]_INST_0_i_15_n_0 ;
  wire \used[1]_INST_0_i_16_n_0 ;
  wire \used[1]_INST_0_i_17_n_0 ;
  wire \used[1]_INST_0_i_18_n_0 ;
  wire \used[1]_INST_0_i_19_n_0 ;
  wire \used[1]_INST_0_i_1_n_0 ;
  wire \used[1]_INST_0_i_20_n_0 ;
  wire \used[1]_INST_0_i_21_n_0 ;
  wire \used[1]_INST_0_i_22_n_0 ;
  wire \used[1]_INST_0_i_23_n_0 ;
  wire \used[1]_INST_0_i_24_n_0 ;
  wire \used[1]_INST_0_i_25_n_0 ;
  wire \used[1]_INST_0_i_26_n_0 ;
  wire \used[1]_INST_0_i_27_n_0 ;
  wire \used[1]_INST_0_i_28_n_0 ;
  wire \used[1]_INST_0_i_29_n_0 ;
  wire \used[1]_INST_0_i_2_n_0 ;
  wire \used[1]_INST_0_i_30_n_0 ;
  wire \used[1]_INST_0_i_31_n_0 ;
  wire \used[1]_INST_0_i_32_n_0 ;
  wire \used[1]_INST_0_i_33_n_0 ;
  wire \used[1]_INST_0_i_34_n_0 ;
  wire \used[1]_INST_0_i_35_n_0 ;
  wire \used[1]_INST_0_i_36_n_0 ;
  wire \used[1]_INST_0_i_37_n_0 ;
  wire \used[1]_INST_0_i_38_n_0 ;
  wire \used[1]_INST_0_i_3_n_0 ;
  wire \used[1]_INST_0_i_4_n_0 ;
  wire \used[1]_INST_0_i_5_n_0 ;
  wire \used[1]_INST_0_i_6_n_0 ;
  wire \used[1]_INST_0_i_7_n_0 ;
  wire \used[1]_INST_0_i_8_n_0 ;
  wire \used[1]_INST_0_i_9_n_0 ;
  wire \used[2]_INST_0_i_10_n_0 ;
  wire \used[2]_INST_0_i_11_n_0 ;
  wire \used[2]_INST_0_i_12_n_0 ;
  wire \used[2]_INST_0_i_13_n_0 ;
  wire \used[2]_INST_0_i_14_n_0 ;
  wire \used[2]_INST_0_i_15_n_0 ;
  wire \used[2]_INST_0_i_16_n_0 ;
  wire \used[2]_INST_0_i_17_n_0 ;
  wire \used[2]_INST_0_i_18_n_0 ;
  wire \used[2]_INST_0_i_19_n_0 ;
  wire \used[2]_INST_0_i_1_n_0 ;
  wire \used[2]_INST_0_i_20_n_0 ;
  wire \used[2]_INST_0_i_21_n_0 ;
  wire \used[2]_INST_0_i_22_n_0 ;
  wire \used[2]_INST_0_i_23_n_0 ;
  wire \used[2]_INST_0_i_24_n_0 ;
  wire \used[2]_INST_0_i_25_n_0 ;
  wire \used[2]_INST_0_i_26_n_0 ;
  wire \used[2]_INST_0_i_27_n_0 ;
  wire \used[2]_INST_0_i_28_n_0 ;
  wire \used[2]_INST_0_i_29_n_0 ;
  wire \used[2]_INST_0_i_2_n_0 ;
  wire \used[2]_INST_0_i_30_n_0 ;
  wire \used[2]_INST_0_i_31_n_0 ;
  wire \used[2]_INST_0_i_32_n_0 ;
  wire \used[2]_INST_0_i_33_n_0 ;
  wire \used[2]_INST_0_i_34_n_0 ;
  wire \used[2]_INST_0_i_35_n_0 ;
  wire \used[2]_INST_0_i_3_n_0 ;
  wire \used[2]_INST_0_i_4_n_0 ;
  wire \used[2]_INST_0_i_5_n_0 ;
  wire \used[2]_INST_0_i_6_n_0 ;
  wire \used[2]_INST_0_i_7_n_0 ;
  wire \used[2]_INST_0_i_8_n_0 ;
  wire \used[2]_INST_0_i_9_n_0 ;
  wire \used[3]_INST_0_i_10_n_0 ;
  wire \used[3]_INST_0_i_11_n_0 ;
  wire \used[3]_INST_0_i_12_n_0 ;
  wire \used[3]_INST_0_i_13_n_0 ;
  wire \used[3]_INST_0_i_14_n_0 ;
  wire \used[3]_INST_0_i_1_n_0 ;
  wire \used[3]_INST_0_i_2_n_0 ;
  wire \used[3]_INST_0_i_3_n_0 ;
  wire \used[3]_INST_0_i_4_n_0 ;
  wire \used[3]_INST_0_i_5_n_0 ;
  wire \used[3]_INST_0_i_6_n_0 ;
  wire \used[3]_INST_0_i_7_n_0 ;
  wire \used[3]_INST_0_i_8_n_0 ;
  wire \used[3]_INST_0_i_9_n_0 ;
  wire \used[4]_INST_0_i_1_n_0 ;
  wire \used[4]_INST_0_i_2_n_0 ;
  wire \used[4]_INST_0_i_3_n_0 ;
  wire \used[5]_INST_0_i_10_n_0 ;
  wire \used[5]_INST_0_i_11_n_0 ;
  wire \used[5]_INST_0_i_12_n_0 ;
  wire \used[5]_INST_0_i_13_n_0 ;
  wire \used[5]_INST_0_i_14_n_0 ;
  wire \used[5]_INST_0_i_15_n_0 ;
  wire \used[5]_INST_0_i_1_n_0 ;
  wire \used[5]_INST_0_i_2_n_0 ;
  wire \used[5]_INST_0_i_3_n_0 ;
  wire \used[5]_INST_0_i_4_n_0 ;
  wire \used[5]_INST_0_i_5_n_0 ;
  wire \used[5]_INST_0_i_6_n_0 ;
  wire \used[5]_INST_0_i_7_n_0 ;
  wire \used[5]_INST_0_i_8_n_0 ;
  wire \used[5]_INST_0_i_9_n_0 ;
  wire \used[6]_INST_0_i_10_n_0 ;
  wire \used[6]_INST_0_i_11_n_0 ;
  wire \used[6]_INST_0_i_12_n_0 ;
  wire \used[6]_INST_0_i_13_n_0 ;
  wire \used[6]_INST_0_i_14_n_0 ;
  wire \used[6]_INST_0_i_15_n_0 ;
  wire \used[6]_INST_0_i_16_n_0 ;
  wire \used[6]_INST_0_i_17_n_0 ;
  wire \used[6]_INST_0_i_18_n_0 ;
  wire \used[6]_INST_0_i_19_n_0 ;
  wire \used[6]_INST_0_i_1_n_0 ;
  wire \used[6]_INST_0_i_2_n_0 ;
  wire \used[6]_INST_0_i_3_n_0 ;
  wire \used[6]_INST_0_i_4_n_0 ;
  wire \used[6]_INST_0_i_5_n_0 ;
  wire \used[6]_INST_0_i_6_n_0 ;
  wire \used[6]_INST_0_i_7_n_0 ;
  wire \used[6]_INST_0_i_8_n_0 ;
  wire \used[6]_INST_0_i_9_n_0 ;

  LUT6 #(
    .INIT(64'hBBBBBBBBABABABAA)) 
    \sample[0]_INST_0 
       (.I0(\sample[0]_INST_0_i_1_n_0 ),
        .I1(\sample[0]_INST_0_i_2_n_0 ),
        .I2(\sample[0]_INST_0_i_3_n_0 ),
        .I3(\sample[0]_INST_0_i_4_n_0 ),
        .I4(\sample[0]_INST_0_i_5_n_0 ),
        .I5(\sample[0]_INST_0_i_6_n_0 ),
        .O(sample[0]));
  (* SOFT_HLUTNM = "soft_lutpair33" *) 
  LUT4 #(
    .INIT(16'h005D)) 
    \sample[0]_INST_0_i_1 
       (.I0(uniform[0]),
        .I1(uniform[2]),
        .I2(uniform[3]),
        .I3(uniform[1]),
        .O(\sample[0]_INST_0_i_1_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair83" *) 
  LUT3 #(
    .INIT(8'h7F)) 
    \sample[0]_INST_0_i_10 
       (.I0(uniform[18]),
        .I1(uniform[20]),
        .I2(uniform[22]),
        .O(\sample[0]_INST_0_i_10_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair27" *) 
  LUT5 #(
    .INIT(32'h1FFFFFFF)) 
    \sample[0]_INST_0_i_11 
       (.I0(\sample[0]_INST_0_i_22_n_0 ),
        .I1(uniform[16]),
        .I2(uniform[13]),
        .I3(uniform[10]),
        .I4(uniform[12]),
        .O(\sample[0]_INST_0_i_11_n_0 ));
  LUT6 #(
    .INIT(64'h3B3B7F7F3FFF3333)) 
    \sample[0]_INST_0_i_12 
       (.I0(uniform[13]),
        .I1(uniform[7]),
        .I2(uniform[11]),
        .I3(uniform[14]),
        .I4(uniform[10]),
        .I5(uniform[12]),
        .O(\sample[0]_INST_0_i_12_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair38" *) 
  LUT4 #(
    .INIT(16'h08C0)) 
    \sample[0]_INST_0_i_13 
       (.I0(uniform[5]),
        .I1(uniform[2]),
        .I2(uniform[4]),
        .I3(uniform[3]),
        .O(\sample[0]_INST_0_i_13_n_0 ));
  LUT6 #(
    .INIT(64'h7840333333333333)) 
    \sample[0]_INST_0_i_14 
       (.I0(uniform[24]),
        .I1(uniform[20]),
        .I2(uniform[22]),
        .I3(uniform[23]),
        .I4(uniform[18]),
        .I5(uniform[19]),
        .O(\sample[0]_INST_0_i_14_n_0 ));
  LUT6 #(
    .INIT(64'h2FFFFF0F2F2FFF0F)) 
    \sample[0]_INST_0_i_15 
       (.I0(uniform[18]),
        .I1(uniform[16]),
        .I2(uniform[14]),
        .I3(uniform[17]),
        .I4(uniform[15]),
        .I5(uniform[19]),
        .O(\sample[0]_INST_0_i_15_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair81" *) 
  LUT3 #(
    .INIT(8'h04)) 
    \sample[0]_INST_0_i_16 
       (.I0(uniform[24]),
        .I1(uniform[20]),
        .I2(uniform[22]),
        .O(\sample[0]_INST_0_i_16_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair21" *) 
  LUT5 #(
    .INIT(32'h77777FFF)) 
    \sample[0]_INST_0_i_17 
       (.I0(uniform[24]),
        .I1(uniform[25]),
        .I2(uniform[28]),
        .I3(uniform[27]),
        .I4(\sample[0]_INST_0_i_23_n_0 ),
        .O(\sample[0]_INST_0_i_17_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF45454544)) 
    \sample[0]_INST_0_i_18 
       (.I0(\sample[0]_INST_0_i_24_n_0 ),
        .I1(\sample[0]_INST_0_i_25_n_0 ),
        .I2(\sample[0]_INST_0_i_26_n_0 ),
        .I3(\sample[0]_INST_0_i_27_n_0 ),
        .I4(\sample[0]_INST_0_i_28_n_0 ),
        .I5(\sample[0]_INST_0_i_29_n_0 ),
        .O(\sample[0]_INST_0_i_18_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF00004000)) 
    \sample[0]_INST_0_i_19 
       (.I0(\sample[0]_INST_0_i_30_n_0 ),
        .I1(uniform[29]),
        .I2(uniform[26]),
        .I3(uniform[30]),
        .I4(uniform[33]),
        .I5(\sample[0]_INST_0_i_31_n_0 ),
        .O(\sample[0]_INST_0_i_19_n_0 ));
  LUT6 #(
    .INIT(64'h77777FFF77FFFFFF)) 
    \sample[0]_INST_0_i_2 
       (.I0(uniform[0]),
        .I1(uniform[1]),
        .I2(uniform[5]),
        .I3(uniform[2]),
        .I4(uniform[4]),
        .I5(uniform[3]),
        .O(\sample[0]_INST_0_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFFABABABAF)) 
    \sample[0]_INST_0_i_20 
       (.I0(\sample[0]_INST_0_i_32_n_0 ),
        .I1(uniform[27]),
        .I2(uniform[24]),
        .I3(uniform[25]),
        .I4(uniform[26]),
        .I5(\sample[0]_INST_0_i_33_n_0 ),
        .O(\sample[0]_INST_0_i_20_n_0 ));
  LUT6 #(
    .INIT(64'h00404040FFFFFFFF)) 
    \sample[0]_INST_0_i_21 
       (.I0(uniform[25]),
        .I1(uniform[24]),
        .I2(uniform[26]),
        .I3(uniform[23]),
        .I4(uniform[28]),
        .I5(uniform[19]),
        .O(\sample[0]_INST_0_i_21_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair28" *) 
  LUT5 #(
    .INIT(32'h3000AA00)) 
    \sample[0]_INST_0_i_22 
       (.I0(uniform[17]),
        .I1(uniform[16]),
        .I2(uniform[18]),
        .I3(uniform[14]),
        .I4(uniform[15]),
        .O(\sample[0]_INST_0_i_22_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair22" *) 
  LUT5 #(
    .INIT(32'h010000FF)) 
    \sample[0]_INST_0_i_23 
       (.I0(uniform[30]),
        .I1(uniform[29]),
        .I2(uniform[31]),
        .I3(uniform[26]),
        .I4(uniform[28]),
        .O(\sample[0]_INST_0_i_23_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF2800FFFF)) 
    \sample[0]_INST_0_i_24 
       (.I0(uniform[35]),
        .I1(uniform[36]),
        .I2(uniform[37]),
        .I3(\sample[0]_INST_0_i_34_n_0 ),
        .I4(uniform[32]),
        .I5(\sample[0]_INST_0_i_35_n_0 ),
        .O(\sample[0]_INST_0_i_24_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair18" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[0]_INST_0_i_25 
       (.I0(uniform[36]),
        .I1(uniform[34]),
        .O(\sample[0]_INST_0_i_25_n_0 ));
  LUT6 #(
    .INIT(64'h16020404FFFFCCCC)) 
    \sample[0]_INST_0_i_26 
       (.I0(uniform[40]),
        .I1(uniform[38]),
        .I2(uniform[39]),
        .I3(uniform[41]),
        .I4(uniform[37]),
        .I5(uniform[35]),
        .O(\sample[0]_INST_0_i_26_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair46" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[0]_INST_0_i_27 
       (.I0(uniform[39]),
        .I1(uniform[38]),
        .O(\sample[0]_INST_0_i_27_n_0 ));
  LUT6 #(
    .INIT(64'h00000000FFFF005D)) 
    \sample[0]_INST_0_i_28 
       (.I0(\sample[4]_INST_0_i_14_n_0 ),
        .I1(\sample[0]_INST_0_i_36_n_0 ),
        .I2(\sample[0]_INST_0_i_37_n_0 ),
        .I3(\sample[0]_INST_0_i_38_n_0 ),
        .I4(\sample[0]_INST_0_i_39_n_0 ),
        .I5(\sample[0]_INST_0_i_40_n_0 ),
        .O(\sample[0]_INST_0_i_28_n_0 ));
  LUT5 #(
    .INIT(32'h7FFFFFFF)) 
    \sample[0]_INST_0_i_29 
       (.I0(uniform[31]),
        .I1(uniform[33]),
        .I2(uniform[29]),
        .I3(uniform[26]),
        .I4(uniform[30]),
        .O(\sample[0]_INST_0_i_29_n_0 ));
  LUT6 #(
    .INIT(64'h666E6E66FFFFFFFF)) 
    \sample[0]_INST_0_i_3 
       (.I0(uniform[7]),
        .I1(uniform[8]),
        .I2(uniform[9]),
        .I3(uniform[10]),
        .I4(uniform[11]),
        .I5(uniform[6]),
        .O(\sample[0]_INST_0_i_3_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair18" *) 
  LUT5 #(
    .INIT(32'h25D5AA00)) 
    \sample[0]_INST_0_i_30 
       (.I0(uniform[32]),
        .I1(uniform[36]),
        .I2(uniform[35]),
        .I3(uniform[34]),
        .I4(uniform[31]),
        .O(\sample[0]_INST_0_i_30_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF78703030)) 
    \sample[0]_INST_0_i_31 
       (.I0(uniform[30]),
        .I1(uniform[26]),
        .I2(uniform[29]),
        .I3(uniform[32]),
        .I4(uniform[31]),
        .I5(\sample[0]_INST_0_i_41_n_0 ),
        .O(\sample[0]_INST_0_i_31_n_0 ));
  LUT6 #(
    .INIT(64'h0006060600000F0F)) 
    \sample[0]_INST_0_i_32 
       (.I0(uniform[28]),
        .I1(uniform[29]),
        .I2(uniform[27]),
        .I3(uniform[30]),
        .I4(uniform[26]),
        .I5(uniform[25]),
        .O(\sample[0]_INST_0_i_32_n_0 ));
  LUT6 #(
    .INIT(64'h0000E00000000000)) 
    \sample[0]_INST_0_i_33 
       (.I0(uniform[29]),
        .I1(uniform[27]),
        .I2(uniform[26]),
        .I3(uniform[24]),
        .I4(uniform[28]),
        .I5(uniform[30]),
        .O(\sample[0]_INST_0_i_33_n_0 ));
  LUT6 #(
    .INIT(64'h00232323FFFFFFFF)) 
    \sample[0]_INST_0_i_34 
       (.I0(uniform[39]),
        .I1(uniform[38]),
        .I2(uniform[37]),
        .I3(uniform[40]),
        .I4(uniform[36]),
        .I5(uniform[34]),
        .O(\sample[0]_INST_0_i_34_n_0 ));
  LUT6 #(
    .INIT(64'h0070007000000050)) 
    \sample[0]_INST_0_i_35 
       (.I0(uniform[35]),
        .I1(uniform[39]),
        .I2(uniform[34]),
        .I3(uniform[36]),
        .I4(uniform[37]),
        .I5(uniform[38]),
        .O(\sample[0]_INST_0_i_35_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF4544FFFF)) 
    \sample[0]_INST_0_i_36 
       (.I0(\sample[0]_INST_0_i_42_n_0 ),
        .I1(\sample[3]_INST_0_i_40_n_0 ),
        .I2(\sample[0]_INST_0_i_43_n_0 ),
        .I3(\sample[0]_INST_0_i_44_n_0 ),
        .I4(\sample[0]_INST_0_i_45_n_0 ),
        .I5(\sample[0]_INST_0_i_46_n_0 ),
        .O(\sample[0]_INST_0_i_36_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF0000077C)) 
    \sample[0]_INST_0_i_37 
       (.I0(uniform[49]),
        .I1(uniform[45]),
        .I2(uniform[47]),
        .I3(uniform[48]),
        .I4(uniform[46]),
        .I5(\sample[0]_INST_0_i_47_n_0 ),
        .O(\sample[0]_INST_0_i_37_n_0 ));
  LUT6 #(
    .INIT(64'h55005500550AD50A)) 
    \sample[0]_INST_0_i_38 
       (.I0(uniform[41]),
        .I1(uniform[46]),
        .I2(uniform[45]),
        .I3(uniform[42]),
        .I4(uniform[47]),
        .I5(uniform[43]),
        .O(\sample[0]_INST_0_i_38_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair24" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[0]_INST_0_i_39 
       (.I0(uniform[44]),
        .I1(uniform[40]),
        .O(\sample[0]_INST_0_i_39_n_0 ));
  LUT6 #(
    .INIT(64'h00000000EAEAEAEE)) 
    \sample[0]_INST_0_i_4 
       (.I0(\sample[0]_INST_0_i_7_n_0 ),
        .I1(\used[5]_INST_0_i_5_n_0 ),
        .I2(\sample[0]_INST_0_i_8_n_0 ),
        .I3(\sample[0]_INST_0_i_9_n_0 ),
        .I4(\sample[0]_INST_0_i_10_n_0 ),
        .I5(\sample[0]_INST_0_i_11_n_0 ),
        .O(\sample[0]_INST_0_i_4_n_0 ));
  LUT6 #(
    .INIT(64'hAAFFAAFFABAABFAA)) 
    \sample[0]_INST_0_i_40 
       (.I0(\sample[0]_INST_0_i_48_n_0 ),
        .I1(uniform[42]),
        .I2(uniform[41]),
        .I3(uniform[37]),
        .I4(uniform[43]),
        .I5(uniform[40]),
        .O(\sample[0]_INST_0_i_40_n_0 ));
  LUT6 #(
    .INIT(64'h0300555500225555)) 
    \sample[0]_INST_0_i_41 
       (.I0(uniform[28]),
        .I1(uniform[31]),
        .I2(\sample[0]_INST_0_i_49_n_0 ),
        .I3(uniform[30]),
        .I4(uniform[26]),
        .I5(uniform[29]),
        .O(\sample[0]_INST_0_i_41_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair78" *) 
  LUT3 #(
    .INIT(8'hF1)) 
    \sample[0]_INST_0_i_42 
       (.I0(\sample[0]_INST_0_i_50_n_0 ),
        .I1(uniform[52]),
        .I2(\sample[0]_INST_0_i_51_n_0 ),
        .O(\sample[0]_INST_0_i_42_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair4" *) 
  LUT5 #(
    .INIT(32'hFFFF9000)) 
    \sample[0]_INST_0_i_43 
       (.I0(uniform[54]),
        .I1(uniform[55]),
        .I2(uniform[57]),
        .I3(\sample[0]_INST_0_i_52_n_0 ),
        .I4(\sample[0]_INST_0_i_53_n_0 ),
        .O(\sample[0]_INST_0_i_43_n_0 ));
  LUT6 #(
    .INIT(64'hBFFFBFBFAEEEAEAE)) 
    \sample[0]_INST_0_i_44 
       (.I0(\sample[0]_INST_0_i_54_n_0 ),
        .I1(uniform[58]),
        .I2(uniform[55]),
        .I3(\sample[0]_INST_0_i_55_n_0 ),
        .I4(\sample[0]_INST_0_i_56_n_0 ),
        .I5(\sample[0]_INST_0_i_57_n_0 ),
        .O(\sample[0]_INST_0_i_44_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair92" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \sample[0]_INST_0_i_45 
       (.I0(uniform[47]),
        .I1(uniform[48]),
        .O(\sample[0]_INST_0_i_45_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair95" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[0]_INST_0_i_46 
       (.I0(uniform[46]),
        .I1(uniform[45]),
        .O(\sample[0]_INST_0_i_46_n_0 ));
  LUT6 #(
    .INIT(64'h55757575FFFFFFFF)) 
    \sample[0]_INST_0_i_47 
       (.I0(\sample[0]_INST_0_i_58_n_0 ),
        .I1(uniform[45]),
        .I2(uniform[46]),
        .I3(uniform[48]),
        .I4(uniform[47]),
        .I5(\sample[0]_INST_0_i_59_n_0 ),
        .O(\sample[0]_INST_0_i_47_n_0 ));
  LUT6 #(
    .INIT(64'h0221333330333300)) 
    \sample[0]_INST_0_i_48 
       (.I0(uniform[47]),
        .I1(\sample[0]_INST_0_i_60_n_0 ),
        .I2(uniform[46]),
        .I3(uniform[45]),
        .I4(uniform[42]),
        .I5(uniform[43]),
        .O(\sample[0]_INST_0_i_48_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair15" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[0]_INST_0_i_49 
       (.I0(uniform[33]),
        .I1(uniform[32]),
        .O(\sample[0]_INST_0_i_49_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair71" *) 
  LUT4 #(
    .INIT(16'hFF09)) 
    \sample[0]_INST_0_i_5 
       (.I0(uniform[10]),
        .I1(uniform[11]),
        .I2(uniform[9]),
        .I3(\sample[0]_INST_0_i_12_n_0 ),
        .O(\sample[0]_INST_0_i_5_n_0 ));
  LUT6 #(
    .INIT(64'hF7FF2AAAFFFFEEEE)) 
    \sample[0]_INST_0_i_50 
       (.I0(uniform[50]),
        .I1(uniform[51]),
        .I2(uniform[54]),
        .I3(uniform[55]),
        .I4(uniform[53]),
        .I5(uniform[49]),
        .O(\sample[0]_INST_0_i_50_n_0 ));
  LUT6 #(
    .INIT(64'h0000CFF0AAAAAAFA)) 
    \sample[0]_INST_0_i_51 
       (.I0(uniform[52]),
        .I1(uniform[54]),
        .I2(uniform[53]),
        .I3(uniform[50]),
        .I4(uniform[51]),
        .I5(uniform[49]),
        .O(\sample[0]_INST_0_i_51_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair7" *) 
  LUT5 #(
    .INIT(32'h46666444)) 
    \sample[0]_INST_0_i_52 
       (.I0(uniform[54]),
        .I1(uniform[56]),
        .I2(uniform[60]),
        .I3(uniform[58]),
        .I4(uniform[59]),
        .O(\sample[0]_INST_0_i_52_n_0 ));
  LUT6 #(
    .INIT(64'h000300030F437373)) 
    \sample[0]_INST_0_i_53 
       (.I0(\sample[0]_INST_0_i_61_n_0 ),
        .I1(uniform[54]),
        .I2(uniform[53]),
        .I3(uniform[55]),
        .I4(uniform[57]),
        .I5(uniform[56]),
        .O(\sample[0]_INST_0_i_53_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair91" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[0]_INST_0_i_54 
       (.I0(uniform[56]),
        .I1(uniform[53]),
        .O(\sample[0]_INST_0_i_54_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF7500FFFF)) 
    \sample[0]_INST_0_i_55 
       (.I0(uniform[57]),
        .I1(\sample[0]_INST_0_i_62_n_0 ),
        .I2(uniform[60]),
        .I3(\used[0]_INST_0_i_39_n_0 ),
        .I4(uniform[54]),
        .I5(\sample[0]_INST_0_i_63_n_0 ),
        .O(\sample[0]_INST_0_i_55_n_0 ));
  LUT6 #(
    .INIT(64'hBFFFBFBFAAAAAAAA)) 
    \sample[0]_INST_0_i_56 
       (.I0(\sample[0]_INST_0_i_64_n_0 ),
        .I1(uniform[63]),
        .I2(uniform[59]),
        .I3(\sample[0]_INST_0_i_65_n_0 ),
        .I4(\sample[0]_INST_0_i_66_n_0 ),
        .I5(\sample[0]_INST_0_i_67_n_0 ),
        .O(\sample[0]_INST_0_i_56_n_0 ));
  LUT6 #(
    .INIT(64'hA0A08AA0AAAA8AAA)) 
    \sample[0]_INST_0_i_57 
       (.I0(\sample[0]_INST_0_i_68_n_0 ),
        .I1(\sample[0]_INST_0_i_69_n_0 ),
        .I2(uniform[55]),
        .I3(uniform[57]),
        .I4(uniform[59]),
        .I5(uniform[54]),
        .O(\sample[0]_INST_0_i_57_n_0 ));
  LUT6 #(
    .INIT(64'hDDDFFFDDFDFFFFFD)) 
    \sample[0]_INST_0_i_58 
       (.I0(uniform[46]),
        .I1(uniform[48]),
        .I2(uniform[47]),
        .I3(uniform[50]),
        .I4(uniform[49]),
        .I5(uniform[51]),
        .O(\sample[0]_INST_0_i_58_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF4FFFFFFF)) 
    \sample[0]_INST_0_i_59 
       (.I0(uniform[51]),
        .I1(uniform[50]),
        .I2(uniform[46]),
        .I3(uniform[49]),
        .I4(uniform[48]),
        .I5(uniform[47]),
        .O(\sample[0]_INST_0_i_59_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF6E66FFFF)) 
    \sample[0]_INST_0_i_6 
       (.I0(uniform[5]),
        .I1(uniform[6]),
        .I2(uniform[8]),
        .I3(uniform[9]),
        .I4(uniform[2]),
        .I5(\sample[0]_INST_0_i_13_n_0 ),
        .O(\sample[0]_INST_0_i_6_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair8" *) 
  LUT3 #(
    .INIT(8'hBF)) 
    \sample[0]_INST_0_i_60 
       (.I0(uniform[44]),
        .I1(uniform[40]),
        .I2(uniform[41]),
        .O(\sample[0]_INST_0_i_60_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair77" *) 
  LUT3 #(
    .INIT(8'h65)) 
    \sample[0]_INST_0_i_61 
       (.I0(uniform[58]),
        .I1(uniform[59]),
        .I2(uniform[55]),
        .O(\sample[0]_INST_0_i_61_n_0 ));
  LUT6 #(
    .INIT(64'hFFE83FEAFFE8FFEA)) 
    \sample[0]_INST_0_i_62 
       (.I0(uniform[62]),
        .I1(uniform[65]),
        .I2(uniform[64]),
        .I3(uniform[63]),
        .I4(uniform[66]),
        .I5(\sample[0]_INST_0_i_70_n_0 ),
        .O(\sample[0]_INST_0_i_62_n_0 ));
  LUT6 #(
    .INIT(64'h2022002220222022)) 
    \sample[0]_INST_0_i_63 
       (.I0(\sample[0]_INST_0_i_71_n_0 ),
        .I1(\sample[0]_INST_0_i_72_n_0 ),
        .I2(\sample[3]_INST_0_i_50_n_0 ),
        .I3(uniform[59]),
        .I4(uniform[63]),
        .I5(\sample[0]_INST_0_i_73_n_0 ),
        .O(\sample[0]_INST_0_i_63_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair2" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[0]_INST_0_i_64 
       (.I0(uniform[62]),
        .I1(uniform[61]),
        .O(\sample[0]_INST_0_i_64_n_0 ));
  LUT6 #(
    .INIT(64'h33B7000300A50000)) 
    \sample[0]_INST_0_i_65 
       (.I0(uniform[68]),
        .I1(uniform[67]),
        .I2(uniform[66]),
        .I3(uniform[65]),
        .I4(uniform[64]),
        .I5(\sample[0]_INST_0_i_74_n_0 ),
        .O(\sample[0]_INST_0_i_65_n_0 ));
  LUT6 #(
    .INIT(64'hBBBBBBBBFBBFBFBB)) 
    \sample[0]_INST_0_i_66 
       (.I0(\sample[0]_INST_0_i_75_n_0 ),
        .I1(uniform[67]),
        .I2(uniform[71]),
        .I3(uniform[68]),
        .I4(uniform[69]),
        .I5(\sample[0]_INST_0_i_76_n_0 ),
        .O(\sample[0]_INST_0_i_66_n_0 ));
  LUT6 #(
    .INIT(64'hFF7F00FF00F0FFFF)) 
    \sample[0]_INST_0_i_67 
       (.I0(uniform[66]),
        .I1(uniform[65]),
        .I2(uniform[64]),
        .I3(uniform[63]),
        .I4(uniform[59]),
        .I5(uniform[60]),
        .O(\sample[0]_INST_0_i_67_n_0 ));
  LUT6 #(
    .INIT(64'hDF7F0000FFF0FFFF)) 
    \sample[0]_INST_0_i_68 
       (.I0(uniform[61]),
        .I1(uniform[62]),
        .I2(uniform[59]),
        .I3(uniform[60]),
        .I4(uniform[54]),
        .I5(uniform[57]),
        .O(\sample[0]_INST_0_i_68_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair89" *) 
  LUT2 #(
    .INIT(4'h1)) 
    \sample[0]_INST_0_i_69 
       (.I0(uniform[60]),
        .I1(uniform[61]),
        .O(\sample[0]_INST_0_i_69_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair57" *) 
  LUT4 #(
    .INIT(16'hFF40)) 
    \sample[0]_INST_0_i_7 
       (.I0(uniform[21]),
        .I1(uniform[17]),
        .I2(\sample[0]_INST_0_i_14_n_0 ),
        .I3(\sample[0]_INST_0_i_15_n_0 ),
        .O(\sample[0]_INST_0_i_7_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair42" *) 
  LUT4 #(
    .INIT(16'h70FF)) 
    \sample[0]_INST_0_i_70 
       (.I0(uniform[67]),
        .I1(uniform[68]),
        .I2(uniform[69]),
        .I3(uniform[62]),
        .O(\sample[0]_INST_0_i_70_n_0 ));
  LUT6 #(
    .INIT(64'h19DDFFFFFFFFFFFF)) 
    \sample[0]_INST_0_i_71 
       (.I0(uniform[62]),
        .I1(uniform[64]),
        .I2(uniform[65]),
        .I3(uniform[63]),
        .I4(uniform[59]),
        .I5(uniform[60]),
        .O(\sample[0]_INST_0_i_71_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair2" *) 
  LUT5 #(
    .INIT(32'hA0E00FCF)) 
    \sample[0]_INST_0_i_72 
       (.I0(uniform[61]),
        .I1(uniform[62]),
        .I2(uniform[57]),
        .I3(uniform[59]),
        .I4(uniform[60]),
        .O(\sample[0]_INST_0_i_72_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair60" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[0]_INST_0_i_73 
       (.I0(uniform[60]),
        .I1(uniform[64]),
        .O(\sample[0]_INST_0_i_73_n_0 ));
  LUT6 #(
    .INIT(64'h00880800FFFFFFFF)) 
    \sample[0]_INST_0_i_74 
       (.I0(uniform[65]),
        .I1(uniform[66]),
        .I2(uniform[69]),
        .I3(uniform[70]),
        .I4(uniform[68]),
        .I5(uniform[64]),
        .O(\sample[0]_INST_0_i_74_n_0 ));
  LUT6 #(
    .INIT(64'h26FF0F0F0F0000FF)) 
    \sample[0]_INST_0_i_75 
       (.I0(uniform[69]),
        .I1(uniform[70]),
        .I2(uniform[68]),
        .I3(uniform[66]),
        .I4(uniform[65]),
        .I5(uniform[64]),
        .O(\sample[0]_INST_0_i_75_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair20" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[0]_INST_0_i_76 
       (.I0(uniform[64]),
        .I1(uniform[65]),
        .O(\sample[0]_INST_0_i_76_n_0 ));
  LUT6 #(
    .INIT(64'hF755005544550055)) 
    \sample[0]_INST_0_i_8 
       (.I0(uniform[20]),
        .I1(uniform[23]),
        .I2(uniform[25]),
        .I3(uniform[18]),
        .I4(uniform[19]),
        .I5(\sample[0]_INST_0_i_16_n_0 ),
        .O(\sample[0]_INST_0_i_8_n_0 ));
  LUT6 #(
    .INIT(64'h000000005555DDFD)) 
    \sample[0]_INST_0_i_9 
       (.I0(uniform[23]),
        .I1(\sample[0]_INST_0_i_17_n_0 ),
        .I2(\sample[0]_INST_0_i_18_n_0 ),
        .I3(\sample[0]_INST_0_i_19_n_0 ),
        .I4(\sample[0]_INST_0_i_20_n_0 ),
        .I5(\sample[0]_INST_0_i_21_n_0 ),
        .O(\sample[0]_INST_0_i_9_n_0 ));
  LUT6 #(
    .INIT(64'h80808088AAAAAAAA)) 
    \sample[1]_INST_0 
       (.I0(uniform[0]),
        .I1(uniform[2]),
        .I2(\sample[1]_INST_0_i_1_n_0 ),
        .I3(\sample[1]_INST_0_i_2_n_0 ),
        .I4(\sample[1]_INST_0_i_3_n_0 ),
        .I5(uniform[1]),
        .O(sample[1]));
  (* SOFT_HLUTNM = "soft_lutpair36" *) 
  LUT5 #(
    .INIT(32'h00704070)) 
    \sample[1]_INST_0_i_1 
       (.I0(uniform[6]),
        .I1(uniform[3]),
        .I2(uniform[4]),
        .I3(uniform[5]),
        .I4(uniform[7]),
        .O(\sample[1]_INST_0_i_1_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair53" *) 
  LUT4 #(
    .INIT(16'hBAAA)) 
    \sample[1]_INST_0_i_10 
       (.I0(\sample[1]_INST_0_i_17_n_0 ),
        .I1(uniform[23]),
        .I2(uniform[21]),
        .I3(\sample[1]_INST_0_i_18_n_0 ),
        .O(\sample[1]_INST_0_i_10_n_0 ));
  LUT6 #(
    .INIT(64'h00000000AAAAFFAE)) 
    \sample[1]_INST_0_i_11 
       (.I0(\sample[1]_INST_0_i_19_n_0 ),
        .I1(\sample[1]_INST_0_i_20_n_0 ),
        .I2(\sample[1]_INST_0_i_21_n_0 ),
        .I3(\sample[1]_INST_0_i_22_n_0 ),
        .I4(\sample[1]_INST_0_i_23_n_0 ),
        .I5(\sample[1]_INST_0_i_24_n_0 ),
        .O(\sample[1]_INST_0_i_11_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair80" *) 
  LUT3 #(
    .INIT(8'h7F)) 
    \sample[1]_INST_0_i_12 
       (.I0(uniform[25]),
        .I1(uniform[24]),
        .I2(uniform[22]),
        .O(\sample[1]_INST_0_i_12_n_0 ));
  LUT6 #(
    .INIT(64'h4FF444444F444444)) 
    \sample[1]_INST_0_i_13 
       (.I0(\sample[1]_INST_0_i_25_n_0 ),
        .I1(uniform[26]),
        .I2(uniform[24]),
        .I3(uniform[25]),
        .I4(\sample[1]_INST_0_i_26_n_0 ),
        .I5(uniform[23]),
        .O(\sample[1]_INST_0_i_13_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair70" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \sample[1]_INST_0_i_14 
       (.I0(uniform[17]),
        .I1(uniform[18]),
        .O(\sample[1]_INST_0_i_14_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair97" *) 
  LUT2 #(
    .INIT(4'h6)) 
    \sample[1]_INST_0_i_15 
       (.I0(uniform[21]),
        .I1(uniform[20]),
        .O(\sample[1]_INST_0_i_15_n_0 ));
  LUT6 #(
    .INIT(64'h000808880808C088)) 
    \sample[1]_INST_0_i_16 
       (.I0(uniform[10]),
        .I1(uniform[8]),
        .I2(uniform[12]),
        .I3(uniform[9]),
        .I4(uniform[11]),
        .I5(uniform[13]),
        .O(\sample[1]_INST_0_i_16_n_0 ));
  LUT6 #(
    .INIT(64'h0000000A40E040E0)) 
    \sample[1]_INST_0_i_17 
       (.I0(uniform[20]),
        .I1(uniform[19]),
        .I2(uniform[22]),
        .I3(uniform[21]),
        .I4(uniform[24]),
        .I5(uniform[23]),
        .O(\sample[1]_INST_0_i_17_n_0 ));
  LUT6 #(
    .INIT(64'h830B0000FFFFFFFF)) 
    \sample[1]_INST_0_i_18 
       (.I0(uniform[22]),
        .I1(uniform[24]),
        .I2(uniform[25]),
        .I3(uniform[26]),
        .I4(uniform[19]),
        .I5(uniform[20]),
        .O(\sample[1]_INST_0_i_18_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair54" *) 
  LUT4 #(
    .INIT(16'h7FFF)) 
    \sample[1]_INST_0_i_19 
       (.I0(uniform[28]),
        .I1(uniform[23]),
        .I2(uniform[29]),
        .I3(uniform[27]),
        .O(\sample[1]_INST_0_i_19_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair84" *) 
  LUT3 #(
    .INIT(8'h7F)) 
    \sample[1]_INST_0_i_2 
       (.I0(uniform[6]),
        .I1(uniform[3]),
        .I2(uniform[5]),
        .O(\sample[1]_INST_0_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF11110100)) 
    \sample[1]_INST_0_i_20 
       (.I0(\sample[1]_INST_0_i_27_n_0 ),
        .I1(\sample[1]_INST_0_i_28_n_0 ),
        .I2(\sample[1]_INST_0_i_29_n_0 ),
        .I3(\sample[1]_INST_0_i_30_n_0 ),
        .I4(\sample[1]_INST_0_i_31_n_0 ),
        .I5(\sample[1]_INST_0_i_32_n_0 ),
        .O(\sample[1]_INST_0_i_20_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair15" *) 
  LUT5 #(
    .INIT(32'h00088888)) 
    \sample[1]_INST_0_i_21 
       (.I0(uniform[30]),
        .I1(uniform[33]),
        .I2(uniform[36]),
        .I3(\sample[3]_INST_0_i_34_n_0 ),
        .I4(uniform[32]),
        .O(\sample[1]_INST_0_i_21_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair94" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[1]_INST_0_i_22 
       (.I0(uniform[31]),
        .I1(uniform[35]),
        .O(\sample[1]_INST_0_i_22_n_0 ));
  LUT6 #(
    .INIT(64'hEEEEEFEEFFFFFFFF)) 
    \sample[1]_INST_0_i_23 
       (.I0(\sample[1]_INST_0_i_33_n_0 ),
        .I1(\sample[1]_INST_0_i_34_n_0 ),
        .I2(\used[2]_INST_0_i_27_n_0 ),
        .I3(uniform[32]),
        .I4(uniform[31]),
        .I5(uniform[26]),
        .O(\sample[1]_INST_0_i_23_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF00008000)) 
    \sample[1]_INST_0_i_24 
       (.I0(uniform[32]),
        .I1(uniform[33]),
        .I2(uniform[28]),
        .I3(uniform[26]),
        .I4(uniform[30]),
        .I5(\sample[1]_INST_0_i_35_n_0 ),
        .O(\sample[1]_INST_0_i_24_n_0 ));
  LUT6 #(
    .INIT(64'h0000FB70FB7FFB7F)) 
    \sample[1]_INST_0_i_25 
       (.I0(uniform[27]),
        .I1(\sample[4]_INST_0_i_20_n_0 ),
        .I2(uniform[24]),
        .I3(uniform[25]),
        .I4(\sample[1]_INST_0_i_36_n_0 ),
        .I5(uniform[22]),
        .O(\sample[1]_INST_0_i_25_n_0 ));
  LUT2 #(
    .INIT(4'h2)) 
    \sample[1]_INST_0_i_26 
       (.I0(uniform[19]),
        .I1(uniform[22]),
        .O(\sample[1]_INST_0_i_26_n_0 ));
  LUT6 #(
    .INIT(64'h0B00030000000F00)) 
    \sample[1]_INST_0_i_27 
       (.I0(\sample[4]_INST_0_i_14_n_0 ),
        .I1(uniform[38]),
        .I2(uniform[40]),
        .I3(uniform[37]),
        .I4(uniform[39]),
        .I5(uniform[41]),
        .O(\sample[1]_INST_0_i_27_n_0 ));
  LUT6 #(
    .INIT(64'h04FFC0FF00FFFFFF)) 
    \sample[1]_INST_0_i_28 
       (.I0(uniform[41]),
        .I1(uniform[40]),
        .I2(uniform[38]),
        .I3(uniform[32]),
        .I4(uniform[37]),
        .I5(uniform[39]),
        .O(\sample[1]_INST_0_i_28_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair46" *) 
  LUT4 #(
    .INIT(16'hFEFF)) 
    \sample[1]_INST_0_i_29 
       (.I0(\sample[1]_INST_0_i_37_n_0 ),
        .I1(\sample[1]_INST_0_i_38_n_0 ),
        .I2(\sample[1]_INST_0_i_39_n_0 ),
        .I3(uniform[39]),
        .O(\sample[1]_INST_0_i_29_n_0 ));
  LUT6 #(
    .INIT(64'h00000000FFFF00AE)) 
    \sample[1]_INST_0_i_3 
       (.I0(\sample[1]_INST_0_i_4_n_0 ),
        .I1(\sample[1]_INST_0_i_5_n_0 ),
        .I2(\sample[1]_INST_0_i_6_n_0 ),
        .I3(\sample[1]_INST_0_i_7_n_0 ),
        .I4(\sample[1]_INST_0_i_8_n_0 ),
        .I5(\sample[1]_INST_0_i_9_n_0 ),
        .O(\sample[1]_INST_0_i_3_n_0 ));
  LUT6 #(
    .INIT(64'h11105555FFFFFFFF)) 
    \sample[1]_INST_0_i_30 
       (.I0(\sample[1]_INST_0_i_40_n_0 ),
        .I1(\sample[1]_INST_0_i_41_n_0 ),
        .I2(\sample[1]_INST_0_i_42_n_0 ),
        .I3(\sample[1]_INST_0_i_43_n_0 ),
        .I4(uniform[45]),
        .I5(uniform[43]),
        .O(\sample[1]_INST_0_i_30_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair79" *) 
  LUT3 #(
    .INIT(8'hF7)) 
    \sample[1]_INST_0_i_31 
       (.I0(uniform[38]),
        .I1(uniform[40]),
        .I2(\sample[1]_INST_0_i_44_n_0 ),
        .O(\sample[1]_INST_0_i_31_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair50" *) 
  LUT4 #(
    .INIT(16'h7F77)) 
    \sample[1]_INST_0_i_32 
       (.I0(uniform[30]),
        .I1(uniform[34]),
        .I2(uniform[36]),
        .I3(uniform[32]),
        .O(\sample[1]_INST_0_i_32_n_0 ));
  LUT6 #(
    .INIT(64'h0000A60000000000)) 
    \sample[1]_INST_0_i_33 
       (.I0(uniform[38]),
        .I1(uniform[37]),
        .I2(uniform[36]),
        .I3(\used[2]_INST_0_i_27_n_0 ),
        .I4(uniform[35]),
        .I5(\sample[4]_INST_0_i_16_n_0 ),
        .O(\sample[1]_INST_0_i_33_n_0 ));
  LUT6 #(
    .INIT(64'h220E000000000000)) 
    \sample[1]_INST_0_i_34 
       (.I0(uniform[35]),
        .I1(uniform[33]),
        .I2(uniform[34]),
        .I3(uniform[36]),
        .I4(uniform[32]),
        .I5(uniform[30]),
        .O(\sample[1]_INST_0_i_34_n_0 ));
  LUT6 #(
    .INIT(64'h0000000001FF09FF)) 
    \sample[1]_INST_0_i_35 
       (.I0(uniform[27]),
        .I1(uniform[26]),
        .I2(uniform[28]),
        .I3(uniform[29]),
        .I4(uniform[31]),
        .I5(\sample[1]_INST_0_i_45_n_0 ),
        .O(\sample[1]_INST_0_i_35_n_0 ));
  LUT6 #(
    .INIT(64'h000000001B000000)) 
    \sample[1]_INST_0_i_36 
       (.I0(uniform[28]),
        .I1(uniform[29]),
        .I2(uniform[30]),
        .I3(uniform[23]),
        .I4(uniform[25]),
        .I5(uniform[27]),
        .O(\sample[1]_INST_0_i_36_n_0 ));
  LUT6 #(
    .INIT(64'h00000000C7220000)) 
    \sample[1]_INST_0_i_37 
       (.I0(uniform[43]),
        .I1(uniform[44]),
        .I2(uniform[45]),
        .I3(uniform[41]),
        .I4(uniform[39]),
        .I5(uniform[42]),
        .O(\sample[1]_INST_0_i_37_n_0 ));
  LUT6 #(
    .INIT(64'h000011114C440000)) 
    \sample[1]_INST_0_i_38 
       (.I0(uniform[43]),
        .I1(uniform[44]),
        .I2(uniform[47]),
        .I3(uniform[48]),
        .I4(uniform[46]),
        .I5(uniform[45]),
        .O(\sample[1]_INST_0_i_38_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair9" *) 
  LUT5 #(
    .INIT(32'h00001000)) 
    \sample[1]_INST_0_i_39 
       (.I0(uniform[44]),
        .I1(uniform[41]),
        .I2(uniform[42]),
        .I3(uniform[39]),
        .I4(uniform[43]),
        .O(\sample[1]_INST_0_i_39_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair28" *) 
  LUT5 #(
    .INIT(32'h7777FFF7)) 
    \sample[1]_INST_0_i_4 
       (.I0(uniform[15]),
        .I1(uniform[14]),
        .I2(uniform[17]),
        .I3(uniform[18]),
        .I4(uniform[16]),
        .O(\sample[1]_INST_0_i_4_n_0 ));
  LUT6 #(
    .INIT(64'h0701070547010705)) 
    \sample[1]_INST_0_i_40 
       (.I0(uniform[46]),
        .I1(uniform[44]),
        .I2(uniform[45]),
        .I3(uniform[47]),
        .I4(uniform[48]),
        .I5(uniform[49]),
        .O(\sample[1]_INST_0_i_40_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair5" *) 
  LUT5 #(
    .INIT(32'hFFFF4000)) 
    \sample[1]_INST_0_i_41 
       (.I0(uniform[48]),
        .I1(uniform[46]),
        .I2(uniform[44]),
        .I3(\sample[1]_INST_0_i_46_n_0 ),
        .I4(\sample[1]_INST_0_i_47_n_0 ),
        .O(\sample[1]_INST_0_i_41_n_0 ));
  LUT6 #(
    .INIT(64'h000000005555DDFD)) 
    \sample[1]_INST_0_i_42 
       (.I0(\sample[4]_INST_0_i_17_n_0 ),
        .I1(\sample[1]_INST_0_i_48_n_0 ),
        .I2(\sample[1]_INST_0_i_49_n_0 ),
        .I3(\sample[1]_INST_0_i_50_n_0 ),
        .I4(\sample[1]_INST_0_i_51_n_0 ),
        .I5(\sample[1]_INST_0_i_52_n_0 ),
        .O(\sample[1]_INST_0_i_42_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF3700FFFF)) 
    \sample[1]_INST_0_i_43 
       (.I0(uniform[47]),
        .I1(uniform[49]),
        .I2(\sample[1]_INST_0_i_53_n_0 ),
        .I3(\sample[1]_INST_0_i_54_n_0 ),
        .I4(uniform[48]),
        .I5(\used[1]_INST_0_i_18_n_0 ),
        .O(\sample[1]_INST_0_i_43_n_0 ));
  LUT6 #(
    .INIT(64'h1F5F5B1B1F1F5717)) 
    \sample[1]_INST_0_i_44 
       (.I0(uniform[42]),
        .I1(uniform[39]),
        .I2(uniform[41]),
        .I3(uniform[45]),
        .I4(uniform[44]),
        .I5(uniform[43]),
        .O(\sample[1]_INST_0_i_44_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair11" *) 
  LUT5 #(
    .INIT(32'h4450FFFF)) 
    \sample[1]_INST_0_i_45 
       (.I0(uniform[29]),
        .I1(uniform[30]),
        .I2(uniform[28]),
        .I3(uniform[26]),
        .I4(uniform[23]),
        .O(\sample[1]_INST_0_i_45_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair40" *) 
  LUT4 #(
    .INIT(16'h6955)) 
    \sample[1]_INST_0_i_46 
       (.I0(uniform[50]),
        .I1(uniform[51]),
        .I2(uniform[49]),
        .I3(uniform[47]),
        .O(\sample[1]_INST_0_i_46_n_0 ));
  LUT6 #(
    .INIT(64'h1131111131333133)) 
    \sample[1]_INST_0_i_47 
       (.I0(uniform[44]),
        .I1(uniform[47]),
        .I2(uniform[48]),
        .I3(uniform[49]),
        .I4(uniform[50]),
        .I5(uniform[46]),
        .O(\sample[1]_INST_0_i_47_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair77" *) 
  LUT3 #(
    .INIT(8'h7F)) 
    \sample[1]_INST_0_i_48 
       (.I0(uniform[58]),
        .I1(uniform[53]),
        .I2(uniform[52]),
        .O(\sample[1]_INST_0_i_48_n_0 ));
  LUT6 #(
    .INIT(64'hBBABAAAABBBBBBBB)) 
    \sample[1]_INST_0_i_49 
       (.I0(\sample[1]_INST_0_i_55_n_0 ),
        .I1(\sample[1]_INST_0_i_56_n_0 ),
        .I2(\sample[1]_INST_0_i_57_n_0 ),
        .I3(\sample[1]_INST_0_i_58_n_0 ),
        .I4(\sample[1]_INST_0_i_59_n_0 ),
        .I5(uniform[59]),
        .O(\sample[1]_INST_0_i_49_n_0 ));
  LUT6 #(
    .INIT(64'h11115551FFFFFFFF)) 
    \sample[1]_INST_0_i_5 
       (.I0(\sample[1]_INST_0_i_10_n_0 ),
        .I1(\sample[4]_INST_0_i_21_n_0 ),
        .I2(\sample[1]_INST_0_i_11_n_0 ),
        .I3(\sample[1]_INST_0_i_12_n_0 ),
        .I4(\sample[1]_INST_0_i_13_n_0 ),
        .I5(\sample[1]_INST_0_i_14_n_0 ),
        .O(\sample[1]_INST_0_i_5_n_0 ));
  LUT6 #(
    .INIT(64'h5C7C3330507C3330)) 
    \sample[1]_INST_0_i_50 
       (.I0(\sample[1]_INST_0_i_60_n_0 ),
        .I1(uniform[57]),
        .I2(uniform[55]),
        .I3(uniform[56]),
        .I4(uniform[54]),
        .I5(uniform[59]),
        .O(\sample[1]_INST_0_i_50_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFABAAAAAAAAAA)) 
    \sample[1]_INST_0_i_51 
       (.I0(\sample[1]_INST_0_i_61_n_0 ),
        .I1(\sample[1]_INST_0_i_62_n_0 ),
        .I2(uniform[58]),
        .I3(uniform[54]),
        .I4(\sample[1]_INST_0_i_63_n_0 ),
        .I5(\sample[2]_INST_0_i_45_n_0 ),
        .O(\sample[1]_INST_0_i_51_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair39" *) 
  LUT4 #(
    .INIT(16'hFFF1)) 
    \sample[1]_INST_0_i_52 
       (.I0(\sample[1]_INST_0_i_54_n_0 ),
        .I1(uniform[49]),
        .I2(\sample[1]_INST_0_i_64_n_0 ),
        .I3(\sample[1]_INST_0_i_65_n_0 ),
        .O(\sample[1]_INST_0_i_52_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair90" *) 
  LUT2 #(
    .INIT(4'h2)) 
    \sample[1]_INST_0_i_53 
       (.I0(uniform[50]),
        .I1(uniform[51]),
        .O(\sample[1]_INST_0_i_53_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair43" *) 
  LUT4 #(
    .INIT(16'hFD7D)) 
    \sample[1]_INST_0_i_54 
       (.I0(uniform[47]),
        .I1(uniform[51]),
        .I2(uniform[52]),
        .I3(uniform[50]),
        .O(\sample[1]_INST_0_i_54_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair75" *) 
  LUT3 #(
    .INIT(8'h7F)) 
    \sample[1]_INST_0_i_55 
       (.I0(uniform[56]),
        .I1(uniform[57]),
        .I2(uniform[55]),
        .O(\sample[1]_INST_0_i_55_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFFFF01FFFF)) 
    \sample[1]_INST_0_i_56 
       (.I0(\sample[1]_INST_0_i_66_n_0 ),
        .I1(uniform[62]),
        .I2(uniform[63]),
        .I3(\sample[1]_INST_0_i_67_n_0 ),
        .I4(uniform[54]),
        .I5(\sample[1]_INST_0_i_68_n_0 ),
        .O(\sample[1]_INST_0_i_56_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair87" *) 
  LUT2 #(
    .INIT(4'h2)) 
    \sample[1]_INST_0_i_57 
       (.I0(uniform[62]),
        .I1(uniform[64]),
        .O(\sample[1]_INST_0_i_57_n_0 ));
  LUT6 #(
    .INIT(64'hF0F06F0F00F06F0F)) 
    \sample[1]_INST_0_i_58 
       (.I0(uniform[65]),
        .I1(uniform[66]),
        .I2(uniform[60]),
        .I3(uniform[61]),
        .I4(uniform[63]),
        .I5(\sample[1]_INST_0_i_69_n_0 ),
        .O(\sample[1]_INST_0_i_58_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF02020200)) 
    \sample[1]_INST_0_i_59 
       (.I0(uniform[62]),
        .I1(\sample[1]_INST_0_i_70_n_0 ),
        .I2(\sample[1]_INST_0_i_71_n_0 ),
        .I3(\sample[1]_INST_0_i_72_n_0 ),
        .I4(\sample[1]_INST_0_i_73_n_0 ),
        .I5(\sample[1]_INST_0_i_74_n_0 ),
        .O(\sample[1]_INST_0_i_59_n_0 ));
  LUT6 #(
    .INIT(64'h00000F0FEFEFF0FF)) 
    \sample[1]_INST_0_i_6 
       (.I0(\used[5]_INST_0_i_4_n_0 ),
        .I1(\sample[1]_INST_0_i_15_n_0 ),
        .I2(uniform[17]),
        .I3(uniform[16]),
        .I4(uniform[18]),
        .I5(uniform[19]),
        .O(\sample[1]_INST_0_i_6_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFF2FFFF55FF00)) 
    \sample[1]_INST_0_i_60 
       (.I0(uniform[61]),
        .I1(uniform[63]),
        .I2(uniform[62]),
        .I3(uniform[57]),
        .I4(uniform[59]),
        .I5(uniform[60]),
        .O(\sample[1]_INST_0_i_60_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair76" *) 
  LUT3 #(
    .INIT(8'h40)) 
    \sample[1]_INST_0_i_61 
       (.I0(uniform[52]),
        .I1(uniform[54]),
        .I2(uniform[55]),
        .O(\sample[1]_INST_0_i_61_n_0 ));
  LUT6 #(
    .INIT(64'hBAF0F0FFF0FFFFFF)) 
    \sample[1]_INST_0_i_62 
       (.I0(\sample[1]_INST_0_i_75_n_0 ),
        .I1(uniform[62]),
        .I2(uniform[59]),
        .I3(uniform[55]),
        .I4(uniform[57]),
        .I5(uniform[56]),
        .O(\sample[1]_INST_0_i_62_n_0 ));
  LUT6 #(
    .INIT(64'h0040000000000FF0)) 
    \sample[1]_INST_0_i_63 
       (.I0(uniform[59]),
        .I1(uniform[60]),
        .I2(uniform[55]),
        .I3(uniform[56]),
        .I4(uniform[57]),
        .I5(uniform[54]),
        .O(\sample[1]_INST_0_i_63_n_0 ));
  LUT6 #(
    .INIT(64'hABABBABEBABEABAF)) 
    \sample[1]_INST_0_i_64 
       (.I0(\sample[1]_INST_0_i_76_n_0 ),
        .I1(uniform[50]),
        .I2(uniform[51]),
        .I3(uniform[54]),
        .I4(uniform[53]),
        .I5(uniform[52]),
        .O(\sample[1]_INST_0_i_64_n_0 ));
  LUT6 #(
    .INIT(64'h2020002000400040)) 
    \sample[1]_INST_0_i_65 
       (.I0(uniform[52]),
        .I1(uniform[53]),
        .I2(uniform[51]),
        .I3(uniform[54]),
        .I4(uniform[57]),
        .I5(uniform[55]),
        .O(\sample[1]_INST_0_i_65_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair0" *) 
  LUT5 #(
    .INIT(32'hB3B30FFF)) 
    \sample[1]_INST_0_i_66 
       (.I0(uniform[65]),
        .I1(uniform[59]),
        .I2(uniform[60]),
        .I3(uniform[64]),
        .I4(uniform[61]),
        .O(\sample[1]_INST_0_i_66_n_0 ));
  LUT6 #(
    .INIT(64'h4000000000004000)) 
    \sample[1]_INST_0_i_67 
       (.I0(uniform[62]),
        .I1(uniform[63]),
        .I2(uniform[60]),
        .I3(uniform[61]),
        .I4(uniform[65]),
        .I5(uniform[64]),
        .O(\sample[1]_INST_0_i_67_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair1" *) 
  LUT4 #(
    .INIT(16'h1011)) 
    \sample[1]_INST_0_i_68 
       (.I0(uniform[61]),
        .I1(uniform[60]),
        .I2(uniform[63]),
        .I3(uniform[59]),
        .O(\sample[1]_INST_0_i_68_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair41" *) 
  LUT4 #(
    .INIT(16'hB3CF)) 
    \sample[1]_INST_0_i_69 
       (.I0(uniform[68]),
        .I1(uniform[67]),
        .I2(uniform[66]),
        .I3(uniform[65]),
        .O(\sample[1]_INST_0_i_69_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair31" *) 
  LUT5 #(
    .INIT(32'h26666222)) 
    \sample[1]_INST_0_i_7 
       (.I0(uniform[15]),
        .I1(uniform[13]),
        .I2(uniform[14]),
        .I3(uniform[17]),
        .I4(uniform[16]),
        .O(\sample[1]_INST_0_i_7_n_0 ));
  LUT6 #(
    .INIT(64'h4000444444004444)) 
    \sample[1]_INST_0_i_70 
       (.I0(uniform[65]),
        .I1(uniform[63]),
        .I2(uniform[69]),
        .I3(uniform[68]),
        .I4(uniform[67]),
        .I5(uniform[66]),
        .O(\sample[1]_INST_0_i_70_n_0 ));
  LUT6 #(
    .INIT(64'h4044400040044004)) 
    \sample[1]_INST_0_i_71 
       (.I0(uniform[67]),
        .I1(uniform[63]),
        .I2(uniform[69]),
        .I3(uniform[68]),
        .I4(uniform[70]),
        .I5(uniform[66]),
        .O(\sample[1]_INST_0_i_71_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair85" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[1]_INST_0_i_72 
       (.I0(uniform[67]),
        .I1(uniform[65]),
        .O(\sample[1]_INST_0_i_72_n_0 ));
  LUT6 #(
    .INIT(64'h08C0CCC08C80CCC0)) 
    \sample[1]_INST_0_i_73 
       (.I0(uniform[71]),
        .I1(uniform[63]),
        .I2(uniform[68]),
        .I3(uniform[69]),
        .I4(uniform[66]),
        .I5(uniform[70]),
        .O(\sample[1]_INST_0_i_73_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair3" *) 
  LUT5 #(
    .INIT(32'h7F77FFFF)) 
    \sample[1]_INST_0_i_74 
       (.I0(uniform[61]),
        .I1(uniform[60]),
        .I2(uniform[62]),
        .I3(uniform[63]),
        .I4(uniform[64]),
        .O(\sample[1]_INST_0_i_74_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair0" *) 
  LUT3 #(
    .INIT(8'hCB)) 
    \sample[1]_INST_0_i_75 
       (.I0(uniform[59]),
        .I1(uniform[61]),
        .I2(uniform[60]),
        .O(\sample[1]_INST_0_i_75_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair40" *) 
  LUT4 #(
    .INIT(16'h0008)) 
    \sample[1]_INST_0_i_76 
       (.I0(uniform[49]),
        .I1(uniform[50]),
        .I2(uniform[51]),
        .I3(uniform[47]),
        .O(\sample[1]_INST_0_i_76_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair72" *) 
  LUT4 #(
    .INIT(16'h7FFF)) 
    \sample[1]_INST_0_i_8 
       (.I0(uniform[9]),
        .I1(uniform[8]),
        .I2(uniform[12]),
        .I3(uniform[11]),
        .O(\sample[1]_INST_0_i_8_n_0 ));
  LUT6 #(
    .INIT(64'hBABBFFFFFFFFFFFF)) 
    \sample[1]_INST_0_i_9 
       (.I0(\sample[1]_INST_0_i_16_n_0 ),
        .I1(uniform[10]),
        .I2(\used[0]_INST_0_i_7_n_0 ),
        .I3(uniform[8]),
        .I4(uniform[7]),
        .I5(uniform[4]),
        .O(\sample[1]_INST_0_i_9_n_0 ));
  LUT6 #(
    .INIT(64'h00000000AAAAFFAE)) 
    \sample[2]_INST_0 
       (.I0(\sample[2]_INST_0_i_1_n_0 ),
        .I1(\sample[2]_INST_0_i_2_n_0 ),
        .I2(\sample[2]_INST_0_i_3_n_0 ),
        .I3(\sample[2]_INST_0_i_4_n_0 ),
        .I4(\sample[2]_INST_0_i_5_n_0 ),
        .I5(\sample[2]_INST_0_i_6_n_0 ),
        .O(sample[2]));
  LUT6 #(
    .INIT(64'h3505353535353535)) 
    \sample[2]_INST_0_i_1 
       (.I0(\sample[2]_INST_0_i_7_n_0 ),
        .I1(uniform[9]),
        .I2(uniform[4]),
        .I3(uniform[11]),
        .I4(uniform[10]),
        .I5(\sample[2]_INST_0_i_8_n_0 ),
        .O(\sample[2]_INST_0_i_1_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF11111555)) 
    \sample[2]_INST_0_i_10 
       (.I0(\sample[2]_INST_0_i_19_n_0 ),
        .I1(\sample[2]_INST_0_i_20_n_0 ),
        .I2(\sample[4]_INST_0_i_16_n_0 ),
        .I3(\sample[2]_INST_0_i_21_n_0 ),
        .I4(\sample[2]_INST_0_i_22_n_0 ),
        .I5(\sample[2]_INST_0_i_23_n_0 ),
        .O(\sample[2]_INST_0_i_10_n_0 ));
  LUT6 #(
    .INIT(64'h4000909060009090)) 
    \sample[2]_INST_0_i_11 
       (.I0(uniform[25]),
        .I1(uniform[26]),
        .I2(uniform[23]),
        .I3(uniform[27]),
        .I4(uniform[24]),
        .I5(\sample[2]_INST_0_i_20_n_0 ),
        .O(\sample[2]_INST_0_i_11_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair68" *) 
  LUT4 #(
    .INIT(16'h7FFF)) 
    \sample[2]_INST_0_i_12 
       (.I0(uniform[20]),
        .I1(uniform[22]),
        .I2(uniform[21]),
        .I3(uniform[17]),
        .O(\sample[2]_INST_0_i_12_n_0 ));
  LUT6 #(
    .INIT(64'hAEAAFEAAAAAAAAAA)) 
    \sample[2]_INST_0_i_13 
       (.I0(\sample[2]_INST_0_i_24_n_0 ),
        .I1(\sample[2]_INST_0_i_25_n_0 ),
        .I2(uniform[22]),
        .I3(uniform[17]),
        .I4(uniform[19]),
        .I5(uniform[21]),
        .O(\sample[2]_INST_0_i_13_n_0 ));
  LUT6 #(
    .INIT(64'h3515353535353535)) 
    \sample[2]_INST_0_i_14 
       (.I0(uniform[14]),
        .I1(uniform[16]),
        .I2(uniform[13]),
        .I3(uniform[19]),
        .I4(uniform[18]),
        .I5(uniform[17]),
        .O(\sample[2]_INST_0_i_14_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair31" *) 
  LUT5 #(
    .INIT(32'h01505500)) 
    \sample[2]_INST_0_i_15 
       (.I0(uniform[15]),
        .I1(uniform[17]),
        .I2(uniform[16]),
        .I3(uniform[14]),
        .I4(uniform[13]),
        .O(\sample[2]_INST_0_i_15_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair29" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[2]_INST_0_i_16 
       (.I0(uniform[7]),
        .I1(uniform[4]),
        .O(\sample[2]_INST_0_i_16_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair71" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[2]_INST_0_i_17 
       (.I0(uniform[8]),
        .I1(uniform[9]),
        .O(\sample[2]_INST_0_i_17_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair33" *) 
  LUT5 #(
    .INIT(32'h7F7FFF7F)) 
    \sample[2]_INST_0_i_18 
       (.I0(uniform[0]),
        .I1(uniform[1]),
        .I2(uniform[3]),
        .I3(uniform[2]),
        .I4(uniform[5]),
        .O(\sample[2]_INST_0_i_18_n_0 ));
  LUT6 #(
    .INIT(64'hBBBBBBBBFBBBBBBB)) 
    \sample[2]_INST_0_i_19 
       (.I0(\sample[2]_INST_0_i_26_n_0 ),
        .I1(uniform[23]),
        .I2(uniform[29]),
        .I3(uniform[27]),
        .I4(uniform[30]),
        .I5(uniform[28]),
        .O(\sample[2]_INST_0_i_19_n_0 ));
  LUT2 #(
    .INIT(4'h8)) 
    \sample[2]_INST_0_i_2 
       (.I0(uniform[15]),
        .I1(uniform[12]),
        .O(\sample[2]_INST_0_i_2_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair11" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \sample[2]_INST_0_i_20 
       (.I0(uniform[28]),
        .I1(uniform[29]),
        .O(\sample[2]_INST_0_i_20_n_0 ));
  LUT6 #(
    .INIT(64'hEEEEEEEEAEAEAAAE)) 
    \sample[2]_INST_0_i_21 
       (.I0(\sample[2]_INST_0_i_27_n_0 ),
        .I1(\used[2]_INST_0_i_27_n_0 ),
        .I2(\sample[2]_INST_0_i_28_n_0 ),
        .I3(\sample[2]_INST_0_i_29_n_0 ),
        .I4(\sample[2]_INST_0_i_30_n_0 ),
        .I5(\sample[2]_INST_0_i_31_n_0 ),
        .O(\sample[2]_INST_0_i_21_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair12" *) 
  LUT5 #(
    .INIT(32'h4F4F4FFF)) 
    \sample[2]_INST_0_i_22 
       (.I0(\sample[2]_INST_0_i_32_n_0 ),
        .I1(uniform[30]),
        .I2(uniform[27]),
        .I3(uniform[32]),
        .I4(uniform[31]),
        .O(\sample[2]_INST_0_i_22_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair80" *) 
  LUT3 #(
    .INIT(8'h7F)) 
    \sample[2]_INST_0_i_23 
       (.I0(uniform[24]),
        .I1(uniform[26]),
        .I2(uniform[25]),
        .O(\sample[2]_INST_0_i_23_n_0 ));
  LUT6 #(
    .INIT(64'h0F03AF0300030003)) 
    \sample[2]_INST_0_i_24 
       (.I0(uniform[22]),
        .I1(uniform[18]),
        .I2(uniform[17]),
        .I3(uniform[19]),
        .I4(uniform[21]),
        .I5(uniform[20]),
        .O(\sample[2]_INST_0_i_24_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair26" *) 
  LUT5 #(
    .INIT(32'hE000FFFF)) 
    \sample[2]_INST_0_i_25 
       (.I0(uniform[25]),
        .I1(uniform[24]),
        .I2(uniform[23]),
        .I3(uniform[19]),
        .I4(uniform[20]),
        .O(\sample[2]_INST_0_i_25_n_0 ));
  LUT6 #(
    .INIT(64'h0000000040000000)) 
    \sample[2]_INST_0_i_26 
       (.I0(uniform[29]),
        .I1(uniform[31]),
        .I2(uniform[30]),
        .I3(uniform[28]),
        .I4(uniform[27]),
        .I5(uniform[32]),
        .O(\sample[2]_INST_0_i_26_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair17" *) 
  LUT5 #(
    .INIT(32'h14AA00AA)) 
    \sample[2]_INST_0_i_27 
       (.I0(uniform[33]),
        .I1(uniform[35]),
        .I2(uniform[36]),
        .I3(uniform[30]),
        .I4(uniform[34]),
        .O(\sample[2]_INST_0_i_27_n_0 ));
  LUT6 #(
    .INIT(64'hCFCCDFDFCFCFDFDF)) 
    \sample[2]_INST_0_i_28 
       (.I0(\sample[2]_INST_0_i_33_n_0 ),
        .I1(\sample[2]_INST_0_i_34_n_0 ),
        .I2(uniform[39]),
        .I3(uniform[42]),
        .I4(uniform[41]),
        .I5(uniform[40]),
        .O(\sample[2]_INST_0_i_28_n_0 ));
  LUT6 #(
    .INIT(64'h55555555FFFF7775)) 
    \sample[2]_INST_0_i_29 
       (.I0(uniform[40]),
        .I1(\sample[2]_INST_0_i_35_n_0 ),
        .I2(\sample[2]_INST_0_i_36_n_0 ),
        .I3(\sample[2]_INST_0_i_37_n_0 ),
        .I4(\sample[2]_INST_0_i_38_n_0 ),
        .I5(\sample[2]_INST_0_i_39_n_0 ),
        .O(\sample[2]_INST_0_i_29_n_0 ));
  LUT6 #(
    .INIT(64'h00000000AAAAFFAE)) 
    \sample[2]_INST_0_i_3 
       (.I0(\sample[2]_INST_0_i_9_n_0 ),
        .I1(\sample[2]_INST_0_i_10_n_0 ),
        .I2(\sample[2]_INST_0_i_11_n_0 ),
        .I3(\sample[2]_INST_0_i_12_n_0 ),
        .I4(\sample[2]_INST_0_i_13_n_0 ),
        .I5(\sample[2]_INST_0_i_14_n_0 ),
        .O(\sample[2]_INST_0_i_3_n_0 ));
  LUT6 #(
    .INIT(64'hAAAAAAAABFAAAAAA)) 
    \sample[2]_INST_0_i_30 
       (.I0(\sample[2]_INST_0_i_40_n_0 ),
        .I1(uniform[44]),
        .I2(uniform[39]),
        .I3(uniform[40]),
        .I4(uniform[41]),
        .I5(uniform[42]),
        .O(\sample[2]_INST_0_i_30_n_0 ));
  LUT6 #(
    .INIT(64'h228830CC22880033)) 
    \sample[2]_INST_0_i_31 
       (.I0(\sample[2]_INST_0_i_41_n_0 ),
        .I1(uniform[38]),
        .I2(uniform[39]),
        .I3(uniform[37]),
        .I4(uniform[36]),
        .I5(uniform[35]),
        .O(\sample[2]_INST_0_i_31_n_0 ));
  LUT6 #(
    .INIT(64'hFF40F0CCFFFFF0FF)) 
    \sample[2]_INST_0_i_32 
       (.I0(\sample[2]_INST_0_i_42_n_0 ),
        .I1(uniform[31]),
        .I2(uniform[32]),
        .I3(uniform[34]),
        .I4(uniform[35]),
        .I5(uniform[33]),
        .O(\sample[2]_INST_0_i_32_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair8" *) 
  LUT5 #(
    .INIT(32'hFFFF0040)) 
    \sample[2]_INST_0_i_33 
       (.I0(uniform[44]),
        .I1(uniform[40]),
        .I2(uniform[41]),
        .I3(uniform[42]),
        .I4(\sample[2]_INST_0_i_40_n_0 ),
        .O(\sample[2]_INST_0_i_33_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair47" *) 
  LUT4 #(
    .INIT(16'h7FFF)) 
    \sample[2]_INST_0_i_34 
       (.I0(uniform[36]),
        .I1(uniform[37]),
        .I2(uniform[35]),
        .I3(uniform[38]),
        .O(\sample[2]_INST_0_i_34_n_0 ));
  LUT6 #(
    .INIT(64'hAAEAAAEAAFEFAAEA)) 
    \sample[2]_INST_0_i_35 
       (.I0(\sample[2]_INST_0_i_43_n_0 ),
        .I1(uniform[43]),
        .I2(\sample[2]_INST_0_i_44_n_0 ),
        .I3(uniform[46]),
        .I4(\used[5]_INST_0_i_15_n_0 ),
        .I5(uniform[49]),
        .O(\sample[2]_INST_0_i_35_n_0 ));
  LUT6 #(
    .INIT(64'h000000006F6FFF6F)) 
    \sample[2]_INST_0_i_36 
       (.I0(uniform[54]),
        .I1(uniform[51]),
        .I2(\sample[2]_INST_0_i_45_n_0 ),
        .I3(\sample[2]_INST_0_i_46_n_0 ),
        .I4(\sample[2]_INST_0_i_47_n_0 ),
        .I5(\sample[2]_INST_0_i_48_n_0 ),
        .O(\sample[2]_INST_0_i_36_n_0 ));
  LUT6 #(
    .INIT(64'h4540FFFFFFFFFFFF)) 
    \sample[2]_INST_0_i_37 
       (.I0(uniform[50]),
        .I1(uniform[52]),
        .I2(uniform[53]),
        .I3(uniform[51]),
        .I4(\used[6]_INST_0_i_13_n_0 ),
        .I5(uniform[47]),
        .O(\sample[2]_INST_0_i_37_n_0 ));
  LUT6 #(
    .INIT(64'h009FFFFFFFFFFFFF)) 
    \sample[2]_INST_0_i_38 
       (.I0(uniform[48]),
        .I1(uniform[47]),
        .I2(uniform[43]),
        .I3(uniform[46]),
        .I4(\sample[2]_INST_0_i_49_n_0 ),
        .I5(uniform[42]),
        .O(\sample[2]_INST_0_i_38_n_0 ));
  LUT6 #(
    .INIT(64'h03380F0003780F00)) 
    \sample[2]_INST_0_i_39 
       (.I0(uniform[47]),
        .I1(uniform[46]),
        .I2(uniform[44]),
        .I3(uniform[45]),
        .I4(uniform[43]),
        .I5(uniform[48]),
        .O(\sample[2]_INST_0_i_39_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair67" *) 
  LUT4 #(
    .INIT(16'hBBCF)) 
    \sample[2]_INST_0_i_4 
       (.I0(\sample[2]_INST_0_i_15_n_0 ),
        .I1(uniform[10]),
        .I2(uniform[11]),
        .I3(uniform[12]),
        .O(\sample[2]_INST_0_i_4_n_0 ));
  LUT6 #(
    .INIT(64'h00000CCC40C00000)) 
    \sample[2]_INST_0_i_40 
       (.I0(uniform[45]),
        .I1(uniform[39]),
        .I2(uniform[43]),
        .I3(uniform[41]),
        .I4(uniform[40]),
        .I5(uniform[42]),
        .O(\sample[2]_INST_0_i_40_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair10" *) 
  LUT5 #(
    .INIT(32'hA7D5FFFF)) 
    \sample[2]_INST_0_i_41 
       (.I0(uniform[37]),
        .I1(uniform[41]),
        .I2(uniform[39]),
        .I3(uniform[40]),
        .I4(uniform[35]),
        .O(\sample[2]_INST_0_i_41_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair96" *) 
  LUT2 #(
    .INIT(4'h2)) 
    \sample[2]_INST_0_i_42 
       (.I0(uniform[37]),
        .I1(uniform[36]),
        .O(\sample[2]_INST_0_i_42_n_0 ));
  LUT6 #(
    .INIT(64'h40426040FFFFFFFF)) 
    \sample[2]_INST_0_i_43 
       (.I0(uniform[47]),
        .I1(uniform[48]),
        .I2(uniform[50]),
        .I3(uniform[51]),
        .I4(uniform[49]),
        .I5(uniform[43]),
        .O(\sample[2]_INST_0_i_43_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair92" *) 
  LUT2 #(
    .INIT(4'h6)) 
    \sample[2]_INST_0_i_44 
       (.I0(uniform[47]),
        .I1(uniform[48]),
        .O(\sample[2]_INST_0_i_44_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair76" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \sample[2]_INST_0_i_45 
       (.I0(uniform[52]),
        .I1(uniform[53]),
        .O(\sample[2]_INST_0_i_45_n_0 ));
  LUT6 #(
    .INIT(64'h15155515FFFFFFFF)) 
    \sample[2]_INST_0_i_46 
       (.I0(\sample[2]_INST_0_i_50_n_0 ),
        .I1(uniform[59]),
        .I2(uniform[58]),
        .I3(\sample[2]_INST_0_i_51_n_0 ),
        .I4(\sample[2]_INST_0_i_52_n_0 ),
        .I5(uniform[55]),
        .O(\sample[2]_INST_0_i_46_n_0 ));
  LUT6 #(
    .INIT(64'hABABABABABABFFAB)) 
    \sample[2]_INST_0_i_47 
       (.I0(\sample[2]_INST_0_i_53_n_0 ),
        .I1(uniform[51]),
        .I2(uniform[54]),
        .I3(\sample[2]_INST_0_i_54_n_0 ),
        .I4(uniform[59]),
        .I5(uniform[57]),
        .O(\sample[2]_INST_0_i_47_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFFFBAAAAAA)) 
    \sample[2]_INST_0_i_48 
       (.I0(\sample[2]_INST_0_i_55_n_0 ),
        .I1(uniform[55]),
        .I2(\sample[2]_INST_0_i_56_n_0 ),
        .I3(\sample[2]_INST_0_i_45_n_0 ),
        .I4(\sample[2]_INST_0_i_57_n_0 ),
        .I5(\sample[2]_INST_0_i_58_n_0 ),
        .O(\sample[2]_INST_0_i_48_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair95" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \sample[2]_INST_0_i_49 
       (.I0(uniform[44]),
        .I1(uniform[45]),
        .O(\sample[2]_INST_0_i_49_n_0 ));
  LUT6 #(
    .INIT(64'hEFEFEFEEEFEEEFEE)) 
    \sample[2]_INST_0_i_5 
       (.I0(\sample[2]_INST_0_i_16_n_0 ),
        .I1(\sample[2]_INST_0_i_17_n_0 ),
        .I2(uniform[11]),
        .I3(uniform[12]),
        .I4(uniform[13]),
        .I5(uniform[10]),
        .O(\sample[2]_INST_0_i_5_n_0 ));
  LUT6 #(
    .INIT(64'h443044304400C400)) 
    \sample[2]_INST_0_i_50 
       (.I0(\sample[2]_INST_0_i_59_n_0 ),
        .I1(uniform[59]),
        .I2(uniform[60]),
        .I3(uniform[56]),
        .I4(uniform[57]),
        .I5(uniform[58]),
        .O(\sample[2]_INST_0_i_50_n_0 ));
  LUT6 #(
    .INIT(64'h7F7F7F7F7F7FFF7F)) 
    \sample[2]_INST_0_i_51 
       (.I0(uniform[60]),
        .I1(uniform[61]),
        .I2(uniform[57]),
        .I3(\sample[2]_INST_0_i_60_n_0 ),
        .I4(\sample[2]_INST_0_i_61_n_0 ),
        .I5(\sample[2]_INST_0_i_62_n_0 ),
        .O(\sample[2]_INST_0_i_51_n_0 ));
  LUT6 #(
    .INIT(64'h5500550055AA7D00)) 
    \sample[2]_INST_0_i_52 
       (.I0(uniform[56]),
        .I1(uniform[62]),
        .I2(uniform[63]),
        .I3(uniform[57]),
        .I4(uniform[61]),
        .I5(uniform[60]),
        .O(\sample[2]_INST_0_i_52_n_0 ));
  LUT6 #(
    .INIT(64'h23AF000F00000F00)) 
    \sample[2]_INST_0_i_53 
       (.I0(\sample[2]_INST_0_i_63_n_0 ),
        .I1(uniform[59]),
        .I2(uniform[55]),
        .I3(uniform[58]),
        .I4(uniform[56]),
        .I5(uniform[57]),
        .O(\sample[2]_INST_0_i_53_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair91" *) 
  LUT2 #(
    .INIT(4'h2)) 
    \sample[2]_INST_0_i_54 
       (.I0(uniform[58]),
        .I1(uniform[56]),
        .O(\sample[2]_INST_0_i_54_n_0 ));
  LUT6 #(
    .INIT(64'h00840F0F00F40FFF)) 
    \sample[2]_INST_0_i_55 
       (.I0(uniform[55]),
        .I1(uniform[54]),
        .I2(uniform[53]),
        .I3(uniform[52]),
        .I4(uniform[51]),
        .I5(uniform[50]),
        .O(\sample[2]_INST_0_i_55_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair86" *) 
  LUT2 #(
    .INIT(4'h6)) 
    \sample[2]_INST_0_i_56 
       (.I0(uniform[58]),
        .I1(uniform[57]),
        .O(\sample[2]_INST_0_i_56_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair7" *) 
  LUT2 #(
    .INIT(4'h2)) 
    \sample[2]_INST_0_i_57 
       (.I0(uniform[56]),
        .I1(uniform[54]),
        .O(\sample[2]_INST_0_i_57_n_0 ));
  LUT6 #(
    .INIT(64'h0040400000400040)) 
    \sample[2]_INST_0_i_58 
       (.I0(uniform[53]),
        .I1(uniform[52]),
        .I2(uniform[55]),
        .I3(uniform[56]),
        .I4(uniform[57]),
        .I5(uniform[54]),
        .O(\sample[2]_INST_0_i_58_n_0 ));
  LUT6 #(
    .INIT(64'hFFCCFECC3FFFFFFF)) 
    \sample[2]_INST_0_i_59 
       (.I0(uniform[64]),
        .I1(uniform[61]),
        .I2(uniform[62]),
        .I3(uniform[57]),
        .I4(uniform[63]),
        .I5(uniform[60]),
        .O(\sample[2]_INST_0_i_59_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF2A2A2AEA)) 
    \sample[2]_INST_0_i_6 
       (.I0(uniform[4]),
        .I1(uniform[2]),
        .I2(uniform[6]),
        .I3(uniform[8]),
        .I4(uniform[7]),
        .I5(\sample[2]_INST_0_i_18_n_0 ),
        .O(\sample[2]_INST_0_i_6_n_0 ));
  LUT6 #(
    .INIT(64'hEE2E2222FFFFFFFF)) 
    \sample[2]_INST_0_i_60 
       (.I0(\sample[2]_INST_0_i_64_n_0 ),
        .I1(uniform[65]),
        .I2(\sample[2]_INST_0_i_65_n_0 ),
        .I3(\sample[2]_INST_0_i_66_n_0 ),
        .I4(uniform[62]),
        .I5(uniform[63]),
        .O(\sample[2]_INST_0_i_60_n_0 ));
  LUT6 #(
    .INIT(64'h0000000000EEF300)) 
    \sample[2]_INST_0_i_61 
       (.I0(uniform[65]),
        .I1(uniform[63]),
        .I2(\sample[2]_INST_0_i_67_n_0 ),
        .I3(uniform[64]),
        .I4(uniform[66]),
        .I5(\sample[2]_INST_0_i_68_n_0 ),
        .O(\sample[2]_INST_0_i_61_n_0 ));
  LUT6 #(
    .INIT(64'h004300400000FFFF)) 
    \sample[2]_INST_0_i_62 
       (.I0(uniform[67]),
        .I1(uniform[66]),
        .I2(uniform[65]),
        .I3(uniform[63]),
        .I4(uniform[64]),
        .I5(uniform[62]),
        .O(\sample[2]_INST_0_i_62_n_0 ));
  LUT6 #(
    .INIT(64'h2F002F8F0AF00A0A)) 
    \sample[2]_INST_0_i_63 
       (.I0(uniform[58]),
        .I1(uniform[63]),
        .I2(uniform[60]),
        .I3(uniform[62]),
        .I4(uniform[59]),
        .I5(uniform[61]),
        .O(\sample[2]_INST_0_i_63_n_0 ));
  LUT6 #(
    .INIT(64'h278FAF8FFFFFFFFF)) 
    \sample[2]_INST_0_i_64 
       (.I0(uniform[64]),
        .I1(uniform[67]),
        .I2(uniform[66]),
        .I3(uniform[68]),
        .I4(uniform[69]),
        .I5(uniform[62]),
        .O(\sample[2]_INST_0_i_64_n_0 ));
  LUT6 #(
    .INIT(64'hD7FDDFFDD7F5D7F5)) 
    \sample[2]_INST_0_i_65 
       (.I0(uniform[66]),
        .I1(uniform[68]),
        .I2(uniform[69]),
        .I3(uniform[70]),
        .I4(uniform[71]),
        .I5(uniform[67]),
        .O(\sample[2]_INST_0_i_65_n_0 ));
  LUT6 #(
    .INIT(64'h8FCFFFFF0FC00F00)) 
    \sample[2]_INST_0_i_66 
       (.I0(uniform[70]),
        .I1(uniform[69]),
        .I2(uniform[64]),
        .I3(uniform[66]),
        .I4(uniform[68]),
        .I5(uniform[67]),
        .O(\sample[2]_INST_0_i_66_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair42" *) 
  LUT2 #(
    .INIT(4'h2)) 
    \sample[2]_INST_0_i_67 
       (.I0(uniform[68]),
        .I1(uniform[69]),
        .O(\sample[2]_INST_0_i_67_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair85" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[2]_INST_0_i_68 
       (.I0(uniform[62]),
        .I1(uniform[67]),
        .O(\sample[2]_INST_0_i_68_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair74" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \sample[2]_INST_0_i_7 
       (.I0(uniform[6]),
        .I1(uniform[2]),
        .O(\sample[2]_INST_0_i_7_n_0 ));
  LUT2 #(
    .INIT(4'h8)) 
    \sample[2]_INST_0_i_8 
       (.I0(uniform[7]),
        .I1(uniform[8]),
        .O(\sample[2]_INST_0_i_8_n_0 ));
  LUT6 #(
    .INIT(64'h7FFF7FFF7FFF7F7F)) 
    \sample[2]_INST_0_i_9 
       (.I0(uniform[13]),
        .I1(uniform[14]),
        .I2(uniform[16]),
        .I3(uniform[18]),
        .I4(uniform[17]),
        .I5(uniform[19]),
        .O(\sample[2]_INST_0_i_9_n_0 ));
  LUT6 #(
    .INIT(64'h00000000FFFF888A)) 
    \sample[3]_INST_0 
       (.I0(uniform[14]),
        .I1(\sample[3]_INST_0_i_1_n_0 ),
        .I2(\sample[3]_INST_0_i_2_n_0 ),
        .I3(\sample[3]_INST_0_i_3_n_0 ),
        .I4(\sample[3]_INST_0_i_4_n_0 ),
        .I5(\sample[3]_INST_0_i_5_n_0 ),
        .O(sample[3]));
  (* SOFT_HLUTNM = "soft_lutpair58" *) 
  LUT4 #(
    .INIT(16'h0430)) 
    \sample[3]_INST_0_i_1 
       (.I0(uniform[20]),
        .I1(uniform[16]),
        .I2(uniform[17]),
        .I3(uniform[19]),
        .O(\sample[3]_INST_0_i_1_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFFABAAFFFF)) 
    \sample[3]_INST_0_i_10 
       (.I0(\sample[3]_INST_0_i_26_n_0 ),
        .I1(uniform[33]),
        .I2(uniform[30]),
        .I3(\sample[4]_INST_0_i_16_n_0 ),
        .I4(uniform[29]),
        .I5(\sample[3]_INST_0_i_27_n_0 ),
        .O(\sample[3]_INST_0_i_10_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF0033008C)) 
    \sample[3]_INST_0_i_11 
       (.I0(uniform[28]),
        .I1(uniform[25]),
        .I2(uniform[23]),
        .I3(uniform[27]),
        .I4(uniform[26]),
        .I5(\sample[3]_INST_0_i_28_n_0 ),
        .O(\sample[3]_INST_0_i_11_n_0 ));
  LUT6 #(
    .INIT(64'h70FFFFFFFFFFFFFF)) 
    \sample[3]_INST_0_i_12 
       (.I0(uniform[13]),
        .I1(uniform[18]),
        .I2(uniform[14]),
        .I3(uniform[7]),
        .I4(uniform[4]),
        .I5(uniform[0]),
        .O(\sample[3]_INST_0_i_12_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair67" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \sample[3]_INST_0_i_13 
       (.I0(uniform[11]),
        .I1(uniform[12]),
        .O(\sample[3]_INST_0_i_13_n_0 ));
  LUT6 #(
    .INIT(64'h7FFFFFFFFFFFFFFF)) 
    \sample[3]_INST_0_i_14 
       (.I0(uniform[1]),
        .I1(uniform[2]),
        .I2(uniform[10]),
        .I3(uniform[6]),
        .I4(uniform[5]),
        .I5(uniform[3]),
        .O(\sample[3]_INST_0_i_14_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair73" *) 
  LUT4 #(
    .INIT(16'h5540)) 
    \sample[3]_INST_0_i_15 
       (.I0(uniform[15]),
        .I1(uniform[13]),
        .I2(uniform[16]),
        .I3(uniform[14]),
        .O(\sample[3]_INST_0_i_15_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair25" *) 
  LUT5 #(
    .INIT(32'hFCFC1F3C)) 
    \sample[3]_INST_0_i_16 
       (.I0(uniform[23]),
        .I1(uniform[21]),
        .I2(uniform[20]),
        .I3(uniform[19]),
        .I4(uniform[22]),
        .O(\sample[3]_INST_0_i_16_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair69" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \sample[3]_INST_0_i_17 
       (.I0(uniform[19]),
        .I1(uniform[21]),
        .O(\sample[3]_INST_0_i_17_n_0 ));
  LUT2 #(
    .INIT(4'h8)) 
    \sample[3]_INST_0_i_18 
       (.I0(uniform[25]),
        .I1(uniform[26]),
        .O(\sample[3]_INST_0_i_18_n_0 ));
  LUT2 #(
    .INIT(4'h7)) 
    \sample[3]_INST_0_i_19 
       (.I0(uniform[23]),
        .I1(uniform[28]),
        .O(\sample[3]_INST_0_i_19_n_0 ));
  LUT2 #(
    .INIT(4'h7)) 
    \sample[3]_INST_0_i_2 
       (.I0(uniform[17]),
        .I1(uniform[16]),
        .O(\sample[3]_INST_0_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hFAF2DDDDBE3E5D5D)) 
    \sample[3]_INST_0_i_20 
       (.I0(uniform[40]),
        .I1(uniform[38]),
        .I2(uniform[41]),
        .I3(uniform[43]),
        .I4(uniform[39]),
        .I5(uniform[42]),
        .O(\sample[3]_INST_0_i_20_n_0 ));
  LUT6 #(
    .INIT(64'hFF63FF63F0600060)) 
    \sample[3]_INST_0_i_21 
       (.I0(uniform[46]),
        .I1(uniform[45]),
        .I2(uniform[44]),
        .I3(uniform[43]),
        .I4(uniform[42]),
        .I5(uniform[41]),
        .O(\sample[3]_INST_0_i_21_n_0 ));
  LUT6 #(
    .INIT(64'hEAEE000000000000)) 
    \sample[3]_INST_0_i_22 
       (.I0(\sample[3]_INST_0_i_29_n_0 ),
        .I1(\sample[3]_INST_0_i_30_n_0 ),
        .I2(\sample[3]_INST_0_i_31_n_0 ),
        .I3(\sample[3]_INST_0_i_32_n_0 ),
        .I4(\sample[4]_INST_0_i_14_n_0 ),
        .I5(uniform[41]),
        .O(\sample[3]_INST_0_i_22_n_0 ));
  LUT6 #(
    .INIT(64'hBFFFFFFFFFFFFFFF)) 
    \sample[3]_INST_0_i_23 
       (.I0(\sample[3]_INST_0_i_33_n_0 ),
        .I1(uniform[37]),
        .I2(uniform[36]),
        .I3(uniform[35]),
        .I4(uniform[31]),
        .I5(uniform[33]),
        .O(\sample[3]_INST_0_i_23_n_0 ));
  LUT6 #(
    .INIT(64'hE2F300000033FFFF)) 
    \sample[3]_INST_0_i_24 
       (.I0(\sample[3]_INST_0_i_34_n_0 ),
        .I1(uniform[36]),
        .I2(\sample[3]_INST_0_i_35_n_0 ),
        .I3(uniform[35]),
        .I4(uniform[31]),
        .I5(uniform[33]),
        .O(\sample[3]_INST_0_i_24_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair50" *) 
  LUT3 #(
    .INIT(8'h7F)) 
    \sample[3]_INST_0_i_25 
       (.I0(uniform[30]),
        .I1(uniform[32]),
        .I2(uniform[34]),
        .O(\sample[3]_INST_0_i_25_n_0 ));
  LUT6 #(
    .INIT(64'h1104000000000000)) 
    \sample[3]_INST_0_i_26 
       (.I0(uniform[32]),
        .I1(uniform[33]),
        .I2(uniform[35]),
        .I3(uniform[34]),
        .I4(uniform[30]),
        .I5(uniform[31]),
        .O(\sample[3]_INST_0_i_26_n_0 ));
  LUT6 #(
    .INIT(64'h000000000000B033)) 
    \sample[3]_INST_0_i_27 
       (.I0(\sample[3]_INST_0_i_36_n_0 ),
        .I1(uniform[33]),
        .I2(uniform[35]),
        .I3(uniform[31]),
        .I4(uniform[34]),
        .I5(\sample[3]_INST_0_i_37_n_0 ),
        .O(\sample[3]_INST_0_i_27_n_0 ));
  LUT6 #(
    .INIT(64'h101F0F0F10FFFF0F)) 
    \sample[3]_INST_0_i_28 
       (.I0(\sample[3]_INST_0_i_38_n_0 ),
        .I1(uniform[28]),
        .I2(uniform[23]),
        .I3(uniform[26]),
        .I4(uniform[25]),
        .I5(uniform[24]),
        .O(\sample[3]_INST_0_i_28_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair19" *) 
  LUT4 #(
    .INIT(16'h0113)) 
    \sample[3]_INST_0_i_29 
       (.I0(uniform[44]),
        .I1(uniform[45]),
        .I2(uniform[47]),
        .I3(uniform[46]),
        .O(\sample[3]_INST_0_i_29_n_0 ));
  LUT6 #(
    .INIT(64'h88888888A8A8A8AA)) 
    \sample[3]_INST_0_i_3 
       (.I0(\sample[3]_INST_0_i_6_n_0 ),
        .I1(\sample[3]_INST_0_i_7_n_0 ),
        .I2(\sample[3]_INST_0_i_8_n_0 ),
        .I3(\sample[3]_INST_0_i_9_n_0 ),
        .I4(\sample[3]_INST_0_i_10_n_0 ),
        .I5(\sample[3]_INST_0_i_11_n_0 ),
        .O(\sample[3]_INST_0_i_3_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair19" *) 
  LUT5 #(
    .INIT(32'h88880008)) 
    \sample[3]_INST_0_i_30 
       (.I0(uniform[45]),
        .I1(uniform[44]),
        .I2(uniform[47]),
        .I3(uniform[48]),
        .I4(uniform[46]),
        .O(\sample[3]_INST_0_i_30_n_0 ));
  LUT6 #(
    .INIT(64'h030303C303337FFF)) 
    \sample[3]_INST_0_i_31 
       (.I0(uniform[52]),
        .I1(uniform[48]),
        .I2(uniform[47]),
        .I3(uniform[51]),
        .I4(uniform[50]),
        .I5(uniform[49]),
        .O(\sample[3]_INST_0_i_31_n_0 ));
  LUT6 #(
    .INIT(64'h51555151FFFFFFFF)) 
    \sample[3]_INST_0_i_32 
       (.I0(\sample[3]_INST_0_i_39_n_0 ),
        .I1(uniform[55]),
        .I2(\sample[3]_INST_0_i_40_n_0 ),
        .I3(\sample[3]_INST_0_i_41_n_0 ),
        .I4(\sample[3]_INST_0_i_42_n_0 ),
        .I5(\used[6]_INST_0_i_13_n_0 ),
        .O(\sample[3]_INST_0_i_32_n_0 ));
  LUT6 #(
    .INIT(64'h01FFBB0099CCFFFF)) 
    \sample[3]_INST_0_i_33 
       (.I0(uniform[42]),
        .I1(uniform[41]),
        .I2(uniform[43]),
        .I3(uniform[38]),
        .I4(uniform[39]),
        .I5(uniform[40]),
        .O(\sample[3]_INST_0_i_33_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair16" *) 
  LUT3 #(
    .INIT(8'h46)) 
    \sample[3]_INST_0_i_34 
       (.I0(uniform[37]),
        .I1(uniform[38]),
        .I2(uniform[39]),
        .O(\sample[3]_INST_0_i_34_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair23" *) 
  LUT2 #(
    .INIT(4'h1)) 
    \sample[3]_INST_0_i_35 
       (.I0(uniform[37]),
        .I1(uniform[38]),
        .O(\sample[3]_INST_0_i_35_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair96" *) 
  LUT2 #(
    .INIT(4'h1)) 
    \sample[3]_INST_0_i_36 
       (.I0(uniform[37]),
        .I1(uniform[36]),
        .O(\sample[3]_INST_0_i_36_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair12" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[3]_INST_0_i_37 
       (.I0(uniform[32]),
        .I1(uniform[30]),
        .O(\sample[3]_INST_0_i_37_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair55" *) 
  LUT4 #(
    .INIT(16'hF7FF)) 
    \sample[3]_INST_0_i_38 
       (.I0(uniform[29]),
        .I1(uniform[27]),
        .I2(uniform[30]),
        .I3(uniform[26]),
        .O(\sample[3]_INST_0_i_38_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFFFF150000)) 
    \sample[3]_INST_0_i_39 
       (.I0(\sample[3]_INST_0_i_43_n_0 ),
        .I1(uniform[55]),
        .I2(uniform[54]),
        .I3(\sample[3]_INST_0_i_44_n_0 ),
        .I4(\sample[4]_INST_0_i_17_n_0 ),
        .I5(\sample[3]_INST_0_i_45_n_0 ),
        .O(\sample[3]_INST_0_i_39_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair73" *) 
  LUT4 #(
    .INIT(16'h0007)) 
    \sample[3]_INST_0_i_4 
       (.I0(uniform[13]),
        .I1(uniform[16]),
        .I2(uniform[14]),
        .I3(uniform[15]),
        .O(\sample[3]_INST_0_i_4_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair78" *) 
  LUT3 #(
    .INIT(8'h7F)) 
    \sample[3]_INST_0_i_40 
       (.I0(uniform[52]),
        .I1(uniform[51]),
        .I2(uniform[50]),
        .O(\sample[3]_INST_0_i_40_n_0 ));
  LUT6 #(
    .INIT(64'h00430000FF40FFFF)) 
    \sample[3]_INST_0_i_41 
       (.I0(\sample[3]_INST_0_i_46_n_0 ),
        .I1(uniform[58]),
        .I2(uniform[57]),
        .I3(uniform[56]),
        .I4(uniform[54]),
        .I5(uniform[53]),
        .O(\sample[3]_INST_0_i_41_n_0 ));
  LUT6 #(
    .INIT(64'h11110111FFFFFFFF)) 
    \sample[3]_INST_0_i_42 
       (.I0(\sample[3]_INST_0_i_47_n_0 ),
        .I1(\sample[3]_INST_0_i_48_n_0 ),
        .I2(\used[0]_INST_0_i_25_n_0 ),
        .I3(uniform[61]),
        .I4(\sample[3]_INST_0_i_49_n_0 ),
        .I5(uniform[56]),
        .O(\sample[3]_INST_0_i_42_n_0 ));
  LUT6 #(
    .INIT(64'h777F0000FFFFFFFF)) 
    \sample[3]_INST_0_i_43 
       (.I0(uniform[55]),
        .I1(uniform[56]),
        .I2(uniform[58]),
        .I3(uniform[57]),
        .I4(uniform[52]),
        .I5(uniform[53]),
        .O(\sample[3]_INST_0_i_43_n_0 ));
  LUT6 #(
    .INIT(64'h00440000885700AA)) 
    \sample[3]_INST_0_i_44 
       (.I0(uniform[53]),
        .I1(uniform[57]),
        .I2(uniform[58]),
        .I3(uniform[56]),
        .I4(uniform[54]),
        .I5(uniform[55]),
        .O(\sample[3]_INST_0_i_44_n_0 ));
  LUT6 #(
    .INIT(64'h07030707FFFF0000)) 
    \sample[3]_INST_0_i_45 
       (.I0(uniform[53]),
        .I1(uniform[51]),
        .I2(uniform[52]),
        .I3(uniform[54]),
        .I4(uniform[50]),
        .I5(uniform[47]),
        .O(\sample[3]_INST_0_i_45_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair88" *) 
  LUT2 #(
    .INIT(4'h1)) 
    \sample[3]_INST_0_i_46 
       (.I0(uniform[60]),
        .I1(uniform[59]),
        .O(\sample[3]_INST_0_i_46_n_0 ));
  LUT6 #(
    .INIT(64'h5000100F00000000)) 
    \sample[3]_INST_0_i_47 
       (.I0(uniform[62]),
        .I1(uniform[63]),
        .I2(uniform[58]),
        .I3(uniform[59]),
        .I4(uniform[60]),
        .I5(\sample[3]_INST_0_i_50_n_0 ),
        .O(\sample[3]_INST_0_i_47_n_0 ));
  LUT6 #(
    .INIT(64'hEEEEEEEEEEEEEFEE)) 
    \sample[3]_INST_0_i_48 
       (.I0(\sample[3]_INST_0_i_51_n_0 ),
        .I1(\sample[3]_INST_0_i_52_n_0 ),
        .I2(\sample[3]_INST_0_i_53_n_0 ),
        .I3(uniform[54]),
        .I4(uniform[57]),
        .I5(uniform[58]),
        .O(\sample[3]_INST_0_i_48_n_0 ));
  LUT6 #(
    .INIT(64'hAA2A222A0AAAAAAA)) 
    \sample[3]_INST_0_i_49 
       (.I0(\sample[3]_INST_0_i_54_n_0 ),
        .I1(\sample[3]_INST_0_i_55_n_0 ),
        .I2(uniform[62]),
        .I3(uniform[63]),
        .I4(uniform[59]),
        .I5(uniform[60]),
        .O(\sample[3]_INST_0_i_49_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFFBFFF)) 
    \sample[3]_INST_0_i_5 
       (.I0(\sample[3]_INST_0_i_12_n_0 ),
        .I1(uniform[9]),
        .I2(uniform[8]),
        .I3(\sample[3]_INST_0_i_13_n_0 ),
        .I4(\sample[3]_INST_0_i_14_n_0 ),
        .I5(\sample[3]_INST_0_i_15_n_0 ),
        .O(\sample[3]_INST_0_i_5_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair86" *) 
  LUT2 #(
    .INIT(4'h2)) 
    \sample[3]_INST_0_i_50 
       (.I0(uniform[57]),
        .I1(uniform[61]),
        .O(\sample[3]_INST_0_i_50_n_0 ));
  LUT6 #(
    .INIT(64'h4444888840008080)) 
    \sample[3]_INST_0_i_51 
       (.I0(uniform[58]),
        .I1(uniform[59]),
        .I2(uniform[61]),
        .I3(uniform[62]),
        .I4(uniform[57]),
        .I5(uniform[60]),
        .O(\sample[3]_INST_0_i_51_n_0 ));
  LUT6 #(
    .INIT(64'h08000C0000000C00)) 
    \sample[3]_INST_0_i_52 
       (.I0(uniform[65]),
        .I1(uniform[57]),
        .I2(uniform[62]),
        .I3(\sample[3]_INST_0_i_53_n_0 ),
        .I4(uniform[63]),
        .I5(uniform[64]),
        .O(\sample[3]_INST_0_i_52_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair88" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \sample[3]_INST_0_i_53 
       (.I0(uniform[60]),
        .I1(uniform[59]),
        .O(\sample[3]_INST_0_i_53_n_0 ));
  LUT6 #(
    .INIT(64'h5515FFFFFFFFFFFF)) 
    \sample[3]_INST_0_i_54 
       (.I0(\sample[3]_INST_0_i_56_n_0 ),
        .I1(uniform[65]),
        .I2(uniform[66]),
        .I3(\sample[3]_INST_0_i_57_n_0 ),
        .I4(uniform[60]),
        .I5(uniform[62]),
        .O(\sample[3]_INST_0_i_54_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair45" *) 
  LUT4 #(
    .INIT(16'h91FF)) 
    \sample[3]_INST_0_i_55 
       (.I0(uniform[64]),
        .I1(uniform[65]),
        .I2(uniform[67]),
        .I3(uniform[59]),
        .O(\sample[3]_INST_0_i_55_n_0 ));
  LUT6 #(
    .INIT(64'h0300830000333333)) 
    \sample[3]_INST_0_i_56 
       (.I0(uniform[69]),
        .I1(uniform[66]),
        .I2(\sample[3]_INST_0_i_58_n_0 ),
        .I3(uniform[63]),
        .I4(uniform[65]),
        .I5(uniform[64]),
        .O(\sample[3]_INST_0_i_56_n_0 ));
  LUT6 #(
    .INIT(64'hCC0C3333F3373333)) 
    \sample[3]_INST_0_i_57 
       (.I0(uniform[70]),
        .I1(uniform[64]),
        .I2(uniform[68]),
        .I3(uniform[69]),
        .I4(uniform[63]),
        .I5(uniform[67]),
        .O(\sample[3]_INST_0_i_57_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair41" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \sample[3]_INST_0_i_58 
       (.I0(uniform[67]),
        .I1(uniform[68]),
        .O(\sample[3]_INST_0_i_58_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFFFB000000)) 
    \sample[3]_INST_0_i_6 
       (.I0(uniform[24]),
        .I1(uniform[23]),
        .I2(uniform[25]),
        .I3(uniform[19]),
        .I4(uniform[21]),
        .I5(\sample[3]_INST_0_i_16_n_0 ),
        .O(\sample[3]_INST_0_i_6_n_0 ));
  LUT6 #(
    .INIT(64'h5115FFFFFFFFFFFF)) 
    \sample[3]_INST_0_i_7 
       (.I0(uniform[24]),
        .I1(uniform[23]),
        .I2(uniform[26]),
        .I3(uniform[25]),
        .I4(\used[5]_INST_0_i_4_n_0 ),
        .I5(\sample[3]_INST_0_i_17_n_0 ),
        .O(\sample[3]_INST_0_i_7_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF07F0FFFF)) 
    \sample[3]_INST_0_i_8 
       (.I0(uniform[30]),
        .I1(uniform[31]),
        .I2(uniform[29]),
        .I3(uniform[27]),
        .I4(\sample[3]_INST_0_i_18_n_0 ),
        .I5(\sample[3]_INST_0_i_19_n_0 ),
        .O(\sample[3]_INST_0_i_8_n_0 ));
  LUT6 #(
    .INIT(64'h00000000FFFF00F7)) 
    \sample[3]_INST_0_i_9 
       (.I0(\sample[3]_INST_0_i_20_n_0 ),
        .I1(\sample[3]_INST_0_i_21_n_0 ),
        .I2(\sample[3]_INST_0_i_22_n_0 ),
        .I3(\sample[3]_INST_0_i_23_n_0 ),
        .I4(\sample[3]_INST_0_i_24_n_0 ),
        .I5(\sample[3]_INST_0_i_25_n_0 ),
        .O(\sample[3]_INST_0_i_9_n_0 ));
  LUT6 #(
    .INIT(64'h00000000EAAAAAAA)) 
    \sample[4]_INST_0 
       (.I0(\sample[4]_INST_0_i_1_n_0 ),
        .I1(\sample[4]_INST_0_i_2_n_0 ),
        .I2(uniform[53]),
        .I3(uniform[54]),
        .I4(uniform[58]),
        .I5(\sample[4]_INST_0_i_3_n_0 ),
        .O(sample[4]));
  LUT6 #(
    .INIT(64'h00F0020200000202)) 
    \sample[4]_INST_0_i_1 
       (.I0(uniform[54]),
        .I1(uniform[57]),
        .I2(uniform[56]),
        .I3(uniform[58]),
        .I4(uniform[53]),
        .I5(\sample[4]_INST_0_i_4_n_0 ),
        .O(\sample[4]_INST_0_i_1_n_0 ));
  LUT6 #(
    .INIT(64'h7FFFFFFFFFFFFFFF)) 
    \sample[4]_INST_0_i_10 
       (.I0(uniform[49]),
        .I1(uniform[45]),
        .I2(uniform[41]),
        .I3(uniform[37]),
        .I4(\sample[4]_INST_0_i_20_n_0 ),
        .I5(\sample[4]_INST_0_i_21_n_0 ),
        .O(\sample[4]_INST_0_i_10_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFFBFFFFFFF)) 
    \sample[4]_INST_0_i_11 
       (.I0(\sample[4]_INST_0_i_22_n_0 ),
        .I1(uniform[30]),
        .I2(uniform[22]),
        .I3(uniform[17]),
        .I4(uniform[3]),
        .I5(\sample[4]_INST_0_i_23_n_0 ),
        .O(\sample[4]_INST_0_i_11_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair89" *) 
  LUT2 #(
    .INIT(4'h2)) 
    \sample[4]_INST_0_i_12 
       (.I0(uniform[61]),
        .I1(uniform[63]),
        .O(\sample[4]_INST_0_i_12_n_0 ));
  LUT6 #(
    .INIT(64'hC0AA00AAC000C000)) 
    \sample[4]_INST_0_i_13 
       (.I0(\sample[4]_INST_0_i_24_n_0 ),
        .I1(uniform[64]),
        .I2(uniform[60]),
        .I3(uniform[63]),
        .I4(\sample[4]_INST_0_i_25_n_0 ),
        .I5(uniform[61]),
        .O(\sample[4]_INST_0_i_13_n_0 ));
  LUT2 #(
    .INIT(4'h8)) 
    \sample[4]_INST_0_i_14 
       (.I0(uniform[43]),
        .I1(uniform[42]),
        .O(\sample[4]_INST_0_i_14_n_0 ));
  LUT2 #(
    .INIT(4'h8)) 
    \sample[4]_INST_0_i_15 
       (.I0(uniform[47]),
        .I1(uniform[46]),
        .O(\sample[4]_INST_0_i_15_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair94" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \sample[4]_INST_0_i_16 
       (.I0(uniform[32]),
        .I1(uniform[31]),
        .O(\sample[4]_INST_0_i_16_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair90" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \sample[4]_INST_0_i_17 
       (.I0(uniform[50]),
        .I1(uniform[51]),
        .O(\sample[4]_INST_0_i_17_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair93" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \sample[4]_INST_0_i_18 
       (.I0(uniform[35]),
        .I1(uniform[34]),
        .O(\sample[4]_INST_0_i_18_n_0 ));
  LUT2 #(
    .INIT(4'h7)) 
    \sample[4]_INST_0_i_19 
       (.I0(uniform[1]),
        .I1(uniform[0]),
        .O(\sample[4]_INST_0_i_19_n_0 ));
  LUT6 #(
    .INIT(64'h0010FFFF03000300)) 
    \sample[4]_INST_0_i_2 
       (.I0(uniform[61]),
        .I1(uniform[60]),
        .I2(uniform[59]),
        .I3(uniform[57]),
        .I4(\sample[4]_INST_0_i_5_n_0 ),
        .I5(uniform[56]),
        .O(\sample[4]_INST_0_i_2_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair53" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \sample[4]_INST_0_i_20 
       (.I0(uniform[23]),
        .I1(uniform[19]),
        .O(\sample[4]_INST_0_i_20_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair97" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \sample[4]_INST_0_i_21 
       (.I0(uniform[21]),
        .I1(uniform[20]),
        .O(\sample[4]_INST_0_i_21_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair62" *) 
  LUT4 #(
    .INIT(16'h7FFF)) 
    \sample[4]_INST_0_i_22 
       (.I0(uniform[28]),
        .I1(uniform[26]),
        .I2(uniform[29]),
        .I3(uniform[2]),
        .O(\sample[4]_INST_0_i_22_n_0 ));
  LUT5 #(
    .INIT(32'hFFFF7FFF)) 
    \sample[4]_INST_0_i_23 
       (.I0(uniform[11]),
        .I1(uniform[33]),
        .I2(uniform[7]),
        .I3(uniform[6]),
        .I4(\sample[4]_INST_0_i_26_n_0 ),
        .O(\sample[4]_INST_0_i_23_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair20" *) 
  LUT5 #(
    .INIT(32'h0008FFFF)) 
    \sample[4]_INST_0_i_24 
       (.I0(uniform[64]),
        .I1(uniform[65]),
        .I2(uniform[67]),
        .I3(uniform[66]),
        .I4(uniform[60]),
        .O(\sample[4]_INST_0_i_24_n_0 ));
  LUT6 #(
    .INIT(64'h0820000000200008)) 
    \sample[4]_INST_0_i_25 
       (.I0(uniform[66]),
        .I1(uniform[65]),
        .I2(uniform[68]),
        .I3(uniform[69]),
        .I4(uniform[67]),
        .I5(uniform[70]),
        .O(\sample[4]_INST_0_i_25_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair61" *) 
  LUT4 #(
    .INIT(16'h7FFF)) 
    \sample[4]_INST_0_i_26 
       (.I0(uniform[5]),
        .I1(uniform[10]),
        .I2(uniform[4]),
        .I3(uniform[25]),
        .O(\sample[4]_INST_0_i_26_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFFFFFE)) 
    \sample[4]_INST_0_i_3 
       (.I0(\sample[4]_INST_0_i_6_n_0 ),
        .I1(\sample[4]_INST_0_i_7_n_0 ),
        .I2(\sample[4]_INST_0_i_8_n_0 ),
        .I3(\sample[4]_INST_0_i_9_n_0 ),
        .I4(\sample[4]_INST_0_i_10_n_0 ),
        .I5(\sample[4]_INST_0_i_11_n_0 ),
        .O(\sample[4]_INST_0_i_3_n_0 ));
  LUT6 #(
    .INIT(64'h1119111111111111)) 
    \sample[4]_INST_0_i_4 
       (.I0(uniform[54]),
        .I1(uniform[57]),
        .I2(uniform[60]),
        .I3(uniform[62]),
        .I4(uniform[61]),
        .I5(uniform[59]),
        .O(\sample[4]_INST_0_i_4_n_0 ));
  LUT6 #(
    .INIT(64'h0FF7FFFFFFF7FFFF)) 
    \sample[4]_INST_0_i_5 
       (.I0(\sample[4]_INST_0_i_12_n_0 ),
        .I1(uniform[60]),
        .I2(uniform[62]),
        .I3(uniform[59]),
        .I4(uniform[57]),
        .I5(\sample[4]_INST_0_i_13_n_0 ),
        .O(\sample[4]_INST_0_i_5_n_0 ));
  LUT6 #(
    .INIT(64'h7FFFFFFFFFFFFFFF)) 
    \sample[4]_INST_0_i_6 
       (.I0(uniform[27]),
        .I1(uniform[24]),
        .I2(\sample[4]_INST_0_i_14_n_0 ),
        .I3(\sample[4]_INST_0_i_15_n_0 ),
        .I4(uniform[15]),
        .I5(uniform[12]),
        .O(\sample[4]_INST_0_i_6_n_0 ));
  LUT6 #(
    .INIT(64'h7FFFFFFFFFFFFFFF)) 
    \sample[4]_INST_0_i_7 
       (.I0(\sample[4]_INST_0_i_16_n_0 ),
        .I1(uniform[40]),
        .I2(uniform[36]),
        .I3(\sample[4]_INST_0_i_17_n_0 ),
        .I4(uniform[16]),
        .I5(uniform[18]),
        .O(\sample[4]_INST_0_i_7_n_0 ));
  LUT6 #(
    .INIT(64'h7FFFFFFFFFFFFFFF)) 
    \sample[4]_INST_0_i_8 
       (.I0(uniform[48]),
        .I1(uniform[44]),
        .I2(uniform[14]),
        .I3(uniform[13]),
        .I4(uniform[39]),
        .I5(uniform[38]),
        .O(\sample[4]_INST_0_i_8_n_0 ));
  LUT6 #(
    .INIT(64'hFF7FFFFFFFFFFFFF)) 
    \sample[4]_INST_0_i_9 
       (.I0(uniform[55]),
        .I1(uniform[52]),
        .I2(\sample[4]_INST_0_i_18_n_0 ),
        .I3(\sample[4]_INST_0_i_19_n_0 ),
        .I4(uniform[8]),
        .I5(uniform[9]),
        .O(\sample[4]_INST_0_i_9_n_0 ));
  LUT6 #(
    .INIT(64'h00000000AAAAEEFE)) 
    \used[0]_INST_0 
       (.I0(\used[0]_INST_0_i_1_n_0 ),
        .I1(\used[0]_INST_0_i_2_n_0 ),
        .I2(\used[0]_INST_0_i_3_n_0 ),
        .I3(\used[0]_INST_0_i_4_n_0 ),
        .I4(\used[0]_INST_0_i_5_n_0 ),
        .I5(\used[0]_INST_0_i_6_n_0 ),
        .O(used[0]));
  (* SOFT_HLUTNM = "soft_lutpair34" *) 
  LUT5 #(
    .INIT(32'h44CFBBCF)) 
    \used[0]_INST_0_i_1 
       (.I0(uniform[5]),
        .I1(uniform[3]),
        .I2(uniform[1]),
        .I3(uniform[2]),
        .I4(uniform[4]),
        .O(\used[0]_INST_0_i_1_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair68" *) 
  LUT4 #(
    .INIT(16'h0008)) 
    \used[0]_INST_0_i_10 
       (.I0(uniform[20]),
        .I1(uniform[21]),
        .I2(uniform[22]),
        .I3(uniform[23]),
        .O(\used[0]_INST_0_i_10_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair32" *) 
  LUT5 #(
    .INIT(32'h5F8F5FFF)) 
    \used[0]_INST_0_i_11 
       (.I0(uniform[18]),
        .I1(uniform[19]),
        .I2(uniform[14]),
        .I3(uniform[17]),
        .I4(uniform[16]),
        .O(\used[0]_INST_0_i_11_n_0 ));
  LUT6 #(
    .INIT(64'hFEFFFEFEFEFFFEFF)) 
    \used[0]_INST_0_i_12 
       (.I0(\used[0]_INST_0_i_21_n_0 ),
        .I1(\used[0]_INST_0_i_22_n_0 ),
        .I2(\used[0]_INST_0_i_23_n_0 ),
        .I3(uniform[68]),
        .I4(\used[2]_INST_0_i_20_n_0 ),
        .I5(uniform[65]),
        .O(\used[0]_INST_0_i_12_n_0 ));
  LUT6 #(
    .INIT(64'h0000000000008000)) 
    \used[0]_INST_0_i_13 
       (.I0(\used[0]_INST_0_i_24_n_0 ),
        .I1(\used[0]_INST_0_i_25_n_0 ),
        .I2(\used[0]_INST_0_i_26_n_0 ),
        .I3(\used[6]_INST_0_i_15_n_0 ),
        .I4(\used[0]_INST_0_i_27_n_0 ),
        .I5(\used[0]_INST_0_i_28_n_0 ),
        .O(\used[0]_INST_0_i_13_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair32" *) 
  LUT3 #(
    .INIT(8'h38)) 
    \used[0]_INST_0_i_14 
       (.I0(uniform[19]),
        .I1(uniform[18]),
        .I2(uniform[17]),
        .O(\used[0]_INST_0_i_14_n_0 ));
  LUT6 #(
    .INIT(64'h0004FFFFFFFF0000)) 
    \used[0]_INST_0_i_15 
       (.I0(uniform[24]),
        .I1(uniform[23]),
        .I2(uniform[26]),
        .I3(uniform[25]),
        .I4(uniform[19]),
        .I5(uniform[21]),
        .O(\used[0]_INST_0_i_15_n_0 ));
  LUT2 #(
    .INIT(4'h7)) 
    \used[0]_INST_0_i_16 
       (.I0(uniform[24]),
        .I1(uniform[21]),
        .O(\used[0]_INST_0_i_16_n_0 ));
  LUT6 #(
    .INIT(64'h4F4F4F4F4F6FCF6F)) 
    \used[0]_INST_0_i_17 
       (.I0(uniform[25]),
        .I1(uniform[26]),
        .I2(uniform[23]),
        .I3(uniform[27]),
        .I4(uniform[29]),
        .I5(uniform[28]),
        .O(\used[0]_INST_0_i_17_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair62" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \used[0]_INST_0_i_18 
       (.I0(uniform[26]),
        .I1(uniform[28]),
        .O(\used[0]_INST_0_i_18_n_0 ));
  LUT6 #(
    .INIT(64'h00000000BBBBFFFB)) 
    \used[0]_INST_0_i_19 
       (.I0(\sample[3]_INST_0_i_37_n_0 ),
        .I1(uniform[29]),
        .I2(\used[0]_INST_0_i_29_n_0 ),
        .I3(\sample[0]_INST_0_i_25_n_0 ),
        .I4(\used[0]_INST_0_i_30_n_0 ),
        .I5(\used[0]_INST_0_i_31_n_0 ),
        .O(\used[0]_INST_0_i_19_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair35" *) 
  LUT5 #(
    .INIT(32'h0070FFFF)) 
    \used[0]_INST_0_i_2 
       (.I0(uniform[11]),
        .I1(uniform[12]),
        .I2(uniform[9]),
        .I3(uniform[10]),
        .I4(uniform[8]),
        .O(\used[0]_INST_0_i_2_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair25" *) 
  LUT5 #(
    .INIT(32'h0F0FDC5F)) 
    \used[0]_INST_0_i_20 
       (.I0(uniform[23]),
        .I1(uniform[21]),
        .I2(uniform[20]),
        .I3(uniform[19]),
        .I4(uniform[22]),
        .O(\used[0]_INST_0_i_20_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFBFFFFFFFFF)) 
    \used[0]_INST_0_i_21 
       (.I0(\used[0]_INST_0_i_32_n_0 ),
        .I1(uniform[11]),
        .I2(uniform[14]),
        .I3(\used[2]_INST_0_i_15_n_0 ),
        .I4(\sample[2]_INST_0_i_17_n_0 ),
        .I5(\sample[1]_INST_0_i_14_n_0 ),
        .O(\used[0]_INST_0_i_21_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair60" *) 
  LUT4 #(
    .INIT(16'h7FFF)) 
    \used[0]_INST_0_i_22 
       (.I0(uniform[64]),
        .I1(uniform[60]),
        .I2(uniform[63]),
        .I3(uniform[59]),
        .O(\used[0]_INST_0_i_22_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFFBFFFFFFF)) 
    \used[0]_INST_0_i_23 
       (.I0(\used[0]_INST_0_i_33_n_0 ),
        .I1(\used[6]_INST_0_i_16_n_0 ),
        .I2(uniform[23]),
        .I3(uniform[22]),
        .I4(\used[6]_INST_0_i_12_n_0 ),
        .I5(\used[0]_INST_0_i_34_n_0 ),
        .O(\used[0]_INST_0_i_23_n_0 ));
  LUT6 #(
    .INIT(64'h0000000000000040)) 
    \used[0]_INST_0_i_24 
       (.I0(\used[2]_INST_0_i_3_n_0 ),
        .I1(uniform[14]),
        .I2(uniform[18]),
        .I3(uniform[64]),
        .I4(\used[0]_INST_0_i_35_n_0 ),
        .I5(\used[0]_INST_0_i_36_n_0 ),
        .O(\used[0]_INST_0_i_24_n_0 ));
  LUT2 #(
    .INIT(4'h8)) 
    \used[0]_INST_0_i_25 
       (.I0(uniform[58]),
        .I1(uniform[57]),
        .O(\used[0]_INST_0_i_25_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair10" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \used[0]_INST_0_i_26 
       (.I0(uniform[41]),
        .I1(uniform[40]),
        .O(\used[0]_INST_0_i_26_n_0 ));
  LUT6 #(
    .INIT(64'h7FFFFFFFFFFFFFFF)) 
    \used[0]_INST_0_i_27 
       (.I0(\used[5]_INST_0_i_5_n_0 ),
        .I1(uniform[3]),
        .I2(uniform[8]),
        .I3(uniform[44]),
        .I4(uniform[45]),
        .I5(\sample[4]_INST_0_i_14_n_0 ),
        .O(\used[0]_INST_0_i_27_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFFFF7FFFFF)) 
    \used[0]_INST_0_i_28 
       (.I0(\used[0]_INST_0_i_37_n_0 ),
        .I1(\used[0]_INST_0_i_38_n_0 ),
        .I2(\used[0]_INST_0_i_39_n_0 ),
        .I3(uniform[67]),
        .I4(uniform[63]),
        .I5(\used[0]_INST_0_i_40_n_0 ),
        .O(\used[0]_INST_0_i_28_n_0 ));
  LUT6 #(
    .INIT(64'h00000000AAEAEEEE)) 
    \used[0]_INST_0_i_29 
       (.I0(\used[0]_INST_0_i_41_n_0 ),
        .I1(\used[0]_INST_0_i_42_n_0 ),
        .I2(\used[0]_INST_0_i_43_n_0 ),
        .I3(\used[0]_INST_0_i_44_n_0 ),
        .I4(uniform[46]),
        .I5(\used[0]_INST_0_i_45_n_0 ),
        .O(\used[0]_INST_0_i_29_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair61" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \used[0]_INST_0_i_3 
       (.I0(uniform[10]),
        .I1(uniform[11]),
        .O(\used[0]_INST_0_i_3_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair23" *) 
  LUT5 #(
    .INIT(32'h777F6666)) 
    \used[0]_INST_0_i_30 
       (.I0(uniform[33]),
        .I1(uniform[35]),
        .I2(uniform[38]),
        .I3(uniform[37]),
        .I4(uniform[34]),
        .O(\used[0]_INST_0_i_30_n_0 ));
  LUT6 #(
    .INIT(64'h777775FFF555F555)) 
    \used[0]_INST_0_i_31 
       (.I0(uniform[27]),
        .I1(\used[1]_INST_0_i_24_n_0 ),
        .I2(uniform[31]),
        .I3(uniform[30]),
        .I4(uniform[32]),
        .I5(uniform[29]),
        .O(\used[0]_INST_0_i_31_n_0 ));
  LUT6 #(
    .INIT(64'hDFFFFFFFFFFFFFFF)) 
    \used[0]_INST_0_i_32 
       (.I0(\used[0]_INST_0_i_38_n_0 ),
        .I1(\used[6]_INST_0_i_17_n_0 ),
        .I2(uniform[67]),
        .I3(uniform[66]),
        .I4(uniform[24]),
        .I5(uniform[21]),
        .O(\used[0]_INST_0_i_32_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF7FFFFFFF)) 
    \used[0]_INST_0_i_33 
       (.I0(uniform[51]),
        .I1(uniform[54]),
        .I2(uniform[55]),
        .I3(uniform[61]),
        .I4(\used[0]_INST_0_i_25_n_0 ),
        .I5(\used[0]_INST_0_i_36_n_0 ),
        .O(\used[0]_INST_0_i_33_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF7FFFFFFF)) 
    \used[0]_INST_0_i_34 
       (.I0(\used[0]_INST_0_i_46_n_0 ),
        .I1(uniform[37]),
        .I2(uniform[39]),
        .I3(uniform[56]),
        .I4(uniform[62]),
        .I5(\used[0]_INST_0_i_47_n_0 ),
        .O(\used[0]_INST_0_i_34_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair56" *) 
  LUT4 #(
    .INIT(16'h7FFF)) 
    \used[0]_INST_0_i_35 
       (.I0(uniform[22]),
        .I1(uniform[23]),
        .I2(uniform[4]),
        .I3(uniform[5]),
        .O(\used[0]_INST_0_i_35_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair51" *) 
  LUT4 #(
    .INIT(16'h7FFF)) 
    \used[0]_INST_0_i_36 
       (.I0(uniform[20]),
        .I1(uniform[19]),
        .I2(uniform[29]),
        .I3(uniform[28]),
        .O(\used[0]_INST_0_i_36_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair6" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \used[0]_INST_0_i_37 
       (.I0(uniform[51]),
        .I1(uniform[53]),
        .O(\used[0]_INST_0_i_37_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair59" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \used[0]_INST_0_i_38 
       (.I0(uniform[47]),
        .I1(uniform[49]),
        .O(\used[0]_INST_0_i_38_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair63" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \used[0]_INST_0_i_39 
       (.I0(uniform[61]),
        .I1(uniform[59]),
        .O(\used[0]_INST_0_i_39_n_0 ));
  LUT6 #(
    .INIT(64'h8888888888A8AAAA)) 
    \used[0]_INST_0_i_4 
       (.I0(\used[0]_INST_0_i_7_n_0 ),
        .I1(\used[0]_INST_0_i_8_n_0 ),
        .I2(\used[0]_INST_0_i_9_n_0 ),
        .I3(\used[0]_INST_0_i_10_n_0 ),
        .I4(uniform[17]),
        .I5(\used[0]_INST_0_i_11_n_0 ),
        .O(\used[0]_INST_0_i_4_n_0 ));
  LUT6 #(
    .INIT(64'hFF7FFF7FFFFFFF7F)) 
    \used[0]_INST_0_i_40 
       (.I0(\used[0]_INST_0_i_48_n_0 ),
        .I1(uniform[37]),
        .I2(uniform[39]),
        .I3(\used[2]_INST_0_i_15_n_0 ),
        .I4(uniform[3]),
        .I5(uniform[2]),
        .O(\used[0]_INST_0_i_40_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF62003300)) 
    \used[0]_INST_0_i_41 
       (.I0(uniform[43]),
        .I1(uniform[44]),
        .I2(uniform[46]),
        .I3(uniform[41]),
        .I4(uniform[45]),
        .I5(\used[0]_INST_0_i_49_n_0 ),
        .O(\used[0]_INST_0_i_41_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair13" *) 
  LUT5 #(
    .INIT(32'hE0A000F0)) 
    \used[0]_INST_0_i_42 
       (.I0(uniform[43]),
        .I1(uniform[46]),
        .I2(uniform[41]),
        .I3(uniform[44]),
        .I4(uniform[45]),
        .O(\used[0]_INST_0_i_42_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair44" *) 
  LUT4 #(
    .INIT(16'hDD80)) 
    \used[0]_INST_0_i_43 
       (.I0(uniform[48]),
        .I1(uniform[49]),
        .I2(uniform[50]),
        .I3(uniform[47]),
        .O(\used[0]_INST_0_i_43_n_0 ));
  LUT6 #(
    .INIT(64'hAAEA000000000000)) 
    \used[0]_INST_0_i_44 
       (.I0(\used[0]_INST_0_i_50_n_0 ),
        .I1(uniform[54]),
        .I2(\sample[2]_INST_0_i_45_n_0 ),
        .I3(\used[0]_INST_0_i_51_n_0 ),
        .I4(\sample[0]_INST_0_i_45_n_0 ),
        .I5(uniform[50]),
        .O(\used[0]_INST_0_i_44_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair16" *) 
  LUT5 #(
    .INIT(32'h2101FFFF)) 
    \used[0]_INST_0_i_45 
       (.I0(uniform[38]),
        .I1(uniform[39]),
        .I2(uniform[40]),
        .I3(uniform[41]),
        .I4(uniform[37]),
        .O(\used[0]_INST_0_i_45_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair9" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \used[0]_INST_0_i_46 
       (.I0(uniform[41]),
        .I1(uniform[42]),
        .O(\used[0]_INST_0_i_46_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair27" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \used[0]_INST_0_i_47 
       (.I0(uniform[10]),
        .I1(uniform[12]),
        .O(\used[0]_INST_0_i_47_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair87" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \used[0]_INST_0_i_48 
       (.I0(uniform[62]),
        .I1(uniform[60]),
        .O(\used[0]_INST_0_i_48_n_0 ));
  LUT6 #(
    .INIT(64'h7FFF7FFF77F77FF7)) 
    \used[0]_INST_0_i_49 
       (.I0(uniform[38]),
        .I1(uniform[39]),
        .I2(uniform[42]),
        .I3(uniform[40]),
        .I4(uniform[43]),
        .I5(uniform[41]),
        .O(\used[0]_INST_0_i_49_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair37" *) 
  LUT5 #(
    .INIT(32'h7FFF7F7F)) 
    \used[0]_INST_0_i_5 
       (.I0(uniform[5]),
        .I1(uniform[3]),
        .I2(uniform[6]),
        .I3(uniform[7]),
        .I4(uniform[8]),
        .O(\used[0]_INST_0_i_5_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair6" *) 
  LUT5 #(
    .INIT(32'hFFFF5557)) 
    \used[0]_INST_0_i_50 
       (.I0(uniform[51]),
        .I1(uniform[54]),
        .I2(uniform[53]),
        .I3(uniform[52]),
        .I4(\used[0]_INST_0_i_52_n_0 ),
        .O(\used[0]_INST_0_i_50_n_0 ));
  LUT6 #(
    .INIT(64'hEC00ECEC3F3F3F3F)) 
    \used[0]_INST_0_i_51 
       (.I0(uniform[59]),
        .I1(uniform[57]),
        .I2(uniform[58]),
        .I3(\used[0]_INST_0_i_53_n_0 ),
        .I4(uniform[55]),
        .I5(uniform[56]),
        .O(\used[0]_INST_0_i_51_n_0 ));
  LUT6 #(
    .INIT(64'h0000A0FF70F00000)) 
    \used[0]_INST_0_i_52 
       (.I0(uniform[56]),
        .I1(uniform[57]),
        .I2(uniform[52]),
        .I3(uniform[53]),
        .I4(uniform[54]),
        .I5(uniform[55]),
        .O(\used[0]_INST_0_i_52_n_0 ));
  LUT6 #(
    .INIT(64'hF100F1F18F8F8F8F)) 
    \used[0]_INST_0_i_53 
       (.I0(uniform[60]),
        .I1(uniform[61]),
        .I2(uniform[58]),
        .I3(\used[0]_INST_0_i_54_n_0 ),
        .I4(uniform[57]),
        .I5(uniform[59]),
        .O(\used[0]_INST_0_i_53_n_0 ));
  LUT6 #(
    .INIT(64'hFFC70000FF00FF00)) 
    \used[0]_INST_0_i_54 
       (.I0(uniform[66]),
        .I1(uniform[65]),
        .I2(uniform[64]),
        .I3(\sample[0]_INST_0_i_64_n_0 ),
        .I4(\used[0]_INST_0_i_55_n_0 ),
        .I5(uniform[60]),
        .O(\used[0]_INST_0_i_54_n_0 ));
  LUT6 #(
    .INIT(64'h2ECCAECCCC44CC44)) 
    \used[0]_INST_0_i_55 
       (.I0(uniform[62]),
        .I1(uniform[61]),
        .I2(uniform[65]),
        .I3(uniform[64]),
        .I4(uniform[66]),
        .I5(uniform[63]),
        .O(\used[0]_INST_0_i_55_n_0 ));
  LUT6 #(
    .INIT(64'hFFFF5DFF5D5D5D5D)) 
    \used[0]_INST_0_i_6 
       (.I0(uniform[0]),
        .I1(uniform[2]),
        .I2(uniform[1]),
        .I3(\used[0]_INST_0_i_12_n_0 ),
        .I4(\used[0]_INST_0_i_13_n_0 ),
        .I5(\used[5]_INST_0_i_8_n_0 ),
        .O(\used[0]_INST_0_i_6_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair72" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \used[0]_INST_0_i_7 
       (.I0(uniform[12]),
        .I1(uniform[9]),
        .O(\used[0]_INST_0_i_7_n_0 ));
  LUT6 #(
    .INIT(64'h04FF00FFFFFF00FF)) 
    \used[0]_INST_0_i_8 
       (.I0(\used[0]_INST_0_i_14_n_0 ),
        .I1(uniform[17]),
        .I2(uniform[16]),
        .I3(uniform[13]),
        .I4(uniform[14]),
        .I5(uniform[15]),
        .O(\used[0]_INST_0_i_8_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF45454544)) 
    \used[0]_INST_0_i_9 
       (.I0(\used[0]_INST_0_i_15_n_0 ),
        .I1(\used[0]_INST_0_i_16_n_0 ),
        .I2(\used[0]_INST_0_i_17_n_0 ),
        .I3(\used[0]_INST_0_i_18_n_0 ),
        .I4(\used[0]_INST_0_i_19_n_0 ),
        .I5(\used[0]_INST_0_i_20_n_0 ),
        .O(\used[0]_INST_0_i_9_n_0 ));
  LUT6 #(
    .INIT(64'h000000009F1F9F9F)) 
    \used[1]_INST_0 
       (.I0(uniform[1]),
        .I1(uniform[2]),
        .I2(uniform[0]),
        .I3(\used[1]_INST_0_i_1_n_0 ),
        .I4(\used[1]_INST_0_i_2_n_0 ),
        .I5(\used[1]_INST_0_i_3_n_0 ),
        .O(used[1]));
  (* SOFT_HLUTNM = "soft_lutpair36" *) 
  LUT3 #(
    .INIT(8'h7C)) 
    \used[1]_INST_0_i_1 
       (.I0(uniform[5]),
        .I1(uniform[4]),
        .I2(uniform[3]),
        .O(\used[1]_INST_0_i_1_n_0 ));
  LUT6 #(
    .INIT(64'h7FFFFFFFFFFFFFFF)) 
    \used[1]_INST_0_i_10 
       (.I0(uniform[67]),
        .I1(uniform[62]),
        .I2(uniform[53]),
        .I3(uniform[57]),
        .I4(uniform[39]),
        .I5(uniform[38]),
        .O(\used[1]_INST_0_i_10_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFFDFFF)) 
    \used[1]_INST_0_i_11 
       (.I0(\used[6]_INST_0_i_11_n_0 ),
        .I1(\used[1]_INST_0_i_18_n_0 ),
        .I2(uniform[40]),
        .I3(uniform[42]),
        .I4(\used[2]_INST_0_i_22_n_0 ),
        .I5(\used[1]_INST_0_i_19_n_0 ),
        .O(\used[1]_INST_0_i_11_n_0 ));
  LUT6 #(
    .INIT(64'hEFFFFFFFFFFFFFFF)) 
    \used[1]_INST_0_i_12 
       (.I0(\used[1]_INST_0_i_20_n_0 ),
        .I1(\used[1]_INST_0_i_21_n_0 ),
        .I2(uniform[15]),
        .I3(uniform[2]),
        .I4(uniform[50]),
        .I5(uniform[0]),
        .O(\used[1]_INST_0_i_12_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair21" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \used[1]_INST_0_i_13 
       (.I0(uniform[25]),
        .I1(uniform[24]),
        .O(\used[1]_INST_0_i_13_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair54" *) 
  LUT4 #(
    .INIT(16'hE005)) 
    \used[1]_INST_0_i_14 
       (.I0(uniform[28]),
        .I1(uniform[29]),
        .I2(uniform[26]),
        .I3(uniform[27]),
        .O(\used[1]_INST_0_i_14_n_0 ));
  LUT6 #(
    .INIT(64'h8088AAAA80888088)) 
    \used[1]_INST_0_i_15 
       (.I0(\sample[2]_INST_0_i_20_n_0 ),
        .I1(\sample[4]_INST_0_i_16_n_0 ),
        .I2(\used[1]_INST_0_i_22_n_0 ),
        .I3(\used[1]_INST_0_i_23_n_0 ),
        .I4(\used[1]_INST_0_i_24_n_0 ),
        .I5(uniform[30]),
        .O(\used[1]_INST_0_i_15_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair66" *) 
  LUT3 #(
    .INIT(8'h01)) 
    \used[1]_INST_0_i_16 
       (.I0(uniform[26]),
        .I1(uniform[25]),
        .I2(uniform[24]),
        .O(\used[1]_INST_0_i_16_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair64" *) 
  LUT4 #(
    .INIT(16'h6F3F)) 
    \used[1]_INST_0_i_17 
       (.I0(uniform[23]),
        .I1(uniform[22]),
        .I2(uniform[19]),
        .I3(uniform[20]),
        .O(\used[1]_INST_0_i_17_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair5" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \used[1]_INST_0_i_18 
       (.I0(uniform[44]),
        .I1(uniform[46]),
        .O(\used[1]_INST_0_i_18_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair82" *) 
  LUT3 #(
    .INIT(8'hBF)) 
    \used[1]_INST_0_i_19 
       (.I0(uniform[68]),
        .I1(uniform[69]),
        .I2(uniform[70]),
        .O(\used[1]_INST_0_i_19_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF55555100)) 
    \used[1]_INST_0_i_2 
       (.I0(\used[1]_INST_0_i_4_n_0 ),
        .I1(\used[1]_INST_0_i_5_n_0 ),
        .I2(\used[1]_INST_0_i_6_n_0 ),
        .I3(\used[1]_INST_0_i_7_n_0 ),
        .I4(\used[1]_INST_0_i_8_n_0 ),
        .I5(\used[1]_INST_0_i_9_n_0 ),
        .O(\used[1]_INST_0_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hF7FFFFFFFFFFFFFF)) 
    \used[1]_INST_0_i_20 
       (.I0(uniform[3]),
        .I1(uniform[8]),
        .I2(\used[1]_INST_0_i_25_n_0 ),
        .I3(\used[6]_INST_0_i_16_n_0 ),
        .I4(uniform[60]),
        .I5(uniform[64]),
        .O(\used[1]_INST_0_i_20_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair63" *) 
  LUT4 #(
    .INIT(16'h7FFF)) 
    \used[1]_INST_0_i_21 
       (.I0(uniform[59]),
        .I1(uniform[61]),
        .I2(uniform[58]),
        .I3(uniform[43]),
        .O(\used[1]_INST_0_i_21_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair17" *) 
  LUT4 #(
    .INIT(16'h75D5)) 
    \used[1]_INST_0_i_22 
       (.I0(uniform[30]),
        .I1(uniform[34]),
        .I2(uniform[33]),
        .I3(uniform[35]),
        .O(\used[1]_INST_0_i_22_n_0 ));
  LUT6 #(
    .INIT(64'h4F1FFFFFFFFFFF0F)) 
    \used[1]_INST_0_i_23 
       (.I0(\used[1]_INST_0_i_26_n_0 ),
        .I1(uniform[39]),
        .I2(\used[2]_INST_0_i_27_n_0 ),
        .I3(uniform[38]),
        .I4(uniform[36]),
        .I5(uniform[37]),
        .O(\used[1]_INST_0_i_23_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair52" *) 
  LUT4 #(
    .INIT(16'hAAA8)) 
    \used[1]_INST_0_i_24 
       (.I0(uniform[31]),
        .I1(uniform[33]),
        .I2(uniform[34]),
        .I3(uniform[32]),
        .O(\used[1]_INST_0_i_24_n_0 ));
  LUT2 #(
    .INIT(4'h7)) 
    \used[1]_INST_0_i_25 
       (.I0(uniform[66]),
        .I1(uniform[65]),
        .O(\used[1]_INST_0_i_25_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFD5DD00000022)) 
    \used[1]_INST_0_i_26 
       (.I0(uniform[39]),
        .I1(uniform[41]),
        .I2(\used[4]_INST_0_i_3_n_0 ),
        .I3(uniform[42]),
        .I4(\used[1]_INST_0_i_27_n_0 ),
        .I5(uniform[40]),
        .O(\used[1]_INST_0_i_26_n_0 ));
  LUT6 #(
    .INIT(64'h000000000F7F0F0F)) 
    \used[1]_INST_0_i_27 
       (.I0(\used[1]_INST_0_i_28_n_0 ),
        .I1(uniform[47]),
        .I2(uniform[46]),
        .I3(\used[1]_INST_0_i_29_n_0 ),
        .I4(uniform[43]),
        .I5(\used[1]_INST_0_i_30_n_0 ),
        .O(\used[1]_INST_0_i_27_n_0 ));
  LUT6 #(
    .INIT(64'hF1000000FFFFFFFF)) 
    \used[1]_INST_0_i_28 
       (.I0(\used[1]_INST_0_i_31_n_0 ),
        .I1(\used[1]_INST_0_i_32_n_0 ),
        .I2(\used[1]_INST_0_i_33_n_0 ),
        .I3(uniform[50]),
        .I4(uniform[51]),
        .I5(\used[6]_INST_0_i_13_n_0 ),
        .O(\used[1]_INST_0_i_28_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair44" *) 
  LUT4 #(
    .INIT(16'h0800)) 
    \used[1]_INST_0_i_29 
       (.I0(uniform[50]),
        .I1(uniform[48]),
        .I2(uniform[47]),
        .I3(uniform[49]),
        .O(\used[1]_INST_0_i_29_n_0 ));
  LUT6 #(
    .INIT(64'h0000000000000010)) 
    \used[1]_INST_0_i_3 
       (.I0(\used[2]_INST_0_i_13_n_0 ),
        .I1(\used[1]_INST_0_i_10_n_0 ),
        .I2(\used[6]_INST_0_i_7_n_0 ),
        .I3(\used[1]_INST_0_i_11_n_0 ),
        .I4(\used[1]_INST_0_i_12_n_0 ),
        .I5(\used[6]_INST_0_i_2_n_0 ),
        .O(\used[1]_INST_0_i_3_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair48" *) 
  LUT3 #(
    .INIT(8'h7F)) 
    \used[1]_INST_0_i_30 
       (.I0(uniform[44]),
        .I1(uniform[45]),
        .I2(uniform[41]),
        .O(\used[1]_INST_0_i_30_n_0 ));
  LUT6 #(
    .INIT(64'h55D500C055D5FFFF)) 
    \used[1]_INST_0_i_31 
       (.I0(\used[1]_INST_0_i_34_n_0 ),
        .I1(uniform[57]),
        .I2(uniform[56]),
        .I3(uniform[58]),
        .I4(uniform[53]),
        .I5(\used[1]_INST_0_i_35_n_0 ),
        .O(\used[1]_INST_0_i_31_n_0 ));
  LUT6 #(
    .INIT(64'h00000000BFCF0000)) 
    \used[1]_INST_0_i_32 
       (.I0(\used[1]_INST_0_i_36_n_0 ),
        .I1(uniform[61]),
        .I2(uniform[59]),
        .I3(uniform[62]),
        .I4(\used[1]_INST_0_i_37_n_0 ),
        .I5(\used[1]_INST_0_i_38_n_0 ),
        .O(\used[1]_INST_0_i_32_n_0 ));
  LUT6 #(
    .INIT(64'h0808FFFF00FFFF00)) 
    \used[1]_INST_0_i_33 
       (.I0(uniform[56]),
        .I1(uniform[57]),
        .I2(uniform[55]),
        .I3(uniform[53]),
        .I4(uniform[52]),
        .I5(uniform[54]),
        .O(\used[1]_INST_0_i_33_n_0 ));
  LUT6 #(
    .INIT(64'h8888888808888888)) 
    \used[1]_INST_0_i_34 
       (.I0(uniform[54]),
        .I1(uniform[55]),
        .I2(uniform[58]),
        .I3(uniform[59]),
        .I4(uniform[56]),
        .I5(uniform[57]),
        .O(\used[1]_INST_0_i_34_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair4" *) 
  LUT2 #(
    .INIT(4'h2)) 
    \used[1]_INST_0_i_35 
       (.I0(uniform[54]),
        .I1(uniform[55]),
        .O(\used[1]_INST_0_i_35_n_0 ));
  LUT6 #(
    .INIT(64'h6AAA00005555FFFF)) 
    \used[1]_INST_0_i_36 
       (.I0(uniform[65]),
        .I1(uniform[68]),
        .I2(uniform[67]),
        .I3(uniform[66]),
        .I4(uniform[64]),
        .I5(uniform[63]),
        .O(\used[1]_INST_0_i_36_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair75" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \used[1]_INST_0_i_37 
       (.I0(uniform[56]),
        .I1(uniform[57]),
        .O(\used[1]_INST_0_i_37_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair1" *) 
  LUT5 #(
    .INIT(32'h0F7FF000)) 
    \used[1]_INST_0_i_38 
       (.I0(uniform[63]),
        .I1(uniform[64]),
        .I2(uniform[60]),
        .I3(uniform[61]),
        .I4(uniform[59]),
        .O(\used[1]_INST_0_i_38_n_0 ));
  LUT6 #(
    .INIT(64'h7FFF7777F7777777)) 
    \used[1]_INST_0_i_4 
       (.I0(uniform[7]),
        .I1(uniform[8]),
        .I2(uniform[12]),
        .I3(uniform[11]),
        .I4(uniform[9]),
        .I5(uniform[10]),
        .O(\used[1]_INST_0_i_4_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFA20000)) 
    \used[1]_INST_0_i_5 
       (.I0(\used[1]_INST_0_i_13_n_0 ),
        .I1(\used[1]_INST_0_i_14_n_0 ),
        .I2(\used[1]_INST_0_i_15_n_0 ),
        .I3(\used[1]_INST_0_i_16_n_0 ),
        .I4(\used[5]_INST_0_i_4_n_0 ),
        .I5(\used[1]_INST_0_i_17_n_0 ),
        .O(\used[1]_INST_0_i_5_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair69" *) 
  LUT4 #(
    .INIT(16'h28FF)) 
    \used[1]_INST_0_i_6 
       (.I0(uniform[19]),
        .I1(uniform[21]),
        .I2(uniform[20]),
        .I3(uniform[16]),
        .O(\used[1]_INST_0_i_6_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair70" *) 
  LUT4 #(
    .INIT(16'hAA80)) 
    \used[1]_INST_0_i_7 
       (.I0(uniform[15]),
        .I1(uniform[17]),
        .I2(uniform[18]),
        .I3(uniform[16]),
        .O(\used[1]_INST_0_i_7_n_0 ));
  LUT6 #(
    .INIT(64'h40FFFFFFFFFFFFFF)) 
    \used[1]_INST_0_i_8 
       (.I0(\sample[1]_INST_0_i_14_n_0 ),
        .I1(uniform[15]),
        .I2(uniform[16]),
        .I3(\used[6]_INST_0_i_19_n_0 ),
        .I4(uniform[10]),
        .I5(uniform[9]),
        .O(\used[1]_INST_0_i_8_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair37" *) 
  LUT4 #(
    .INIT(16'h1FFF)) 
    \used[1]_INST_0_i_9 
       (.I0(uniform[8]),
        .I1(uniform[7]),
        .I2(uniform[3]),
        .I3(uniform[6]),
        .O(\used[1]_INST_0_i_9_n_0 ));
  LUT6 #(
    .INIT(64'h00000000FFFF00F2)) 
    \used[2]_INST_0 
       (.I0(\used[2]_INST_0_i_1_n_0 ),
        .I1(\used[2]_INST_0_i_2_n_0 ),
        .I2(\used[2]_INST_0_i_3_n_0 ),
        .I3(\used[2]_INST_0_i_4_n_0 ),
        .I4(\used[2]_INST_0_i_5_n_0 ),
        .I5(\used[2]_INST_0_i_6_n_0 ),
        .O(used[2]));
  LUT6 #(
    .INIT(64'hFFFFFFFF55551154)) 
    \used[2]_INST_0_i_1 
       (.I0(\used[2]_INST_0_i_7_n_0 ),
        .I1(uniform[26]),
        .I2(uniform[25]),
        .I3(uniform[24]),
        .I4(\used[2]_INST_0_i_8_n_0 ),
        .I5(\used[2]_INST_0_i_9_n_0 ),
        .O(\used[2]_INST_0_i_1_n_0 ));
  LUT6 #(
    .INIT(64'hF2FFFFFFFFFFFFFF)) 
    \used[2]_INST_0_i_10 
       (.I0(\used[2]_INST_0_i_20_n_0 ),
        .I1(uniform[68]),
        .I2(\used[2]_INST_0_i_21_n_0 ),
        .I3(\used[5]_INST_0_i_12_n_0 ),
        .I4(uniform[1]),
        .I5(\used[6]_INST_0_i_16_n_0 ),
        .O(\used[2]_INST_0_i_10_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFFEFFFFFFF)) 
    \used[2]_INST_0_i_11 
       (.I0(\used[2]_INST_0_i_22_n_0 ),
        .I1(\used[2]_INST_0_i_23_n_0 ),
        .I2(uniform[63]),
        .I3(uniform[61]),
        .I4(uniform[60]),
        .I5(\used[2]_INST_0_i_24_n_0 ),
        .O(\used[2]_INST_0_i_11_n_0 ));
  LUT6 #(
    .INIT(64'h8000000000000000)) 
    \used[2]_INST_0_i_12 
       (.I0(\used[2]_INST_0_i_25_n_0 ),
        .I1(uniform[18]),
        .I2(uniform[27]),
        .I3(uniform[66]),
        .I4(uniform[35]),
        .I5(\used[2]_INST_0_i_26_n_0 ),
        .O(\used[2]_INST_0_i_12_n_0 ));
  LUT5 #(
    .INIT(32'h7FFFFFFF)) 
    \used[2]_INST_0_i_13 
       (.I0(uniform[56]),
        .I1(uniform[54]),
        .I2(uniform[47]),
        .I3(uniform[51]),
        .I4(uniform[10]),
        .O(\used[2]_INST_0_i_13_n_0 ));
  LUT6 #(
    .INIT(64'h7FFFFFFFFFFFFFFF)) 
    \used[2]_INST_0_i_14 
       (.I0(uniform[43]),
        .I1(uniform[32]),
        .I2(\sample[2]_INST_0_i_20_n_0 ),
        .I3(\used[2]_INST_0_i_27_n_0 ),
        .I4(uniform[41]),
        .I5(uniform[38]),
        .O(\used[2]_INST_0_i_14_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair55" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \used[2]_INST_0_i_15 
       (.I0(uniform[25]),
        .I1(uniform[27]),
        .O(\used[2]_INST_0_i_15_n_0 ));
  LUT6 #(
    .INIT(64'h7FEEFFEE7FEE7FEE)) 
    \used[2]_INST_0_i_16 
       (.I0(uniform[32]),
        .I1(uniform[33]),
        .I2(uniform[35]),
        .I3(uniform[34]),
        .I4(uniform[36]),
        .I5(\sample[3]_INST_0_i_35_n_0 ),
        .O(\used[2]_INST_0_i_16_n_0 ));
  LUT6 #(
    .INIT(64'hBFFFFFFFFFFFFFFF)) 
    \used[2]_INST_0_i_17 
       (.I0(\used[2]_INST_0_i_28_n_0 ),
        .I1(uniform[37]),
        .I2(uniform[38]),
        .I3(uniform[39]),
        .I4(uniform[36]),
        .I5(uniform[34]),
        .O(\used[2]_INST_0_i_17_n_0 ));
  LUT6 #(
    .INIT(64'h11111111111F1111)) 
    \used[2]_INST_0_i_18 
       (.I0(uniform[26]),
        .I1(uniform[25]),
        .I2(\used[6]_INST_0_i_4_n_0 ),
        .I3(\used[2]_INST_0_i_14_n_0 ),
        .I4(\used[5]_INST_0_i_12_n_0 ),
        .I5(\used[2]_INST_0_i_29_n_0 ),
        .O(\used[2]_INST_0_i_18_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair83" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \used[2]_INST_0_i_19 
       (.I0(uniform[19]),
        .I1(uniform[18]),
        .O(\used[2]_INST_0_i_19_n_0 ));
  LUT6 #(
    .INIT(64'h777F7F7FFFFFFFFF)) 
    \used[2]_INST_0_i_2 
       (.I0(uniform[13]),
        .I1(uniform[14]),
        .I2(uniform[16]),
        .I3(uniform[18]),
        .I4(uniform[17]),
        .I5(uniform[15]),
        .O(\used[2]_INST_0_i_2_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair82" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \used[2]_INST_0_i_20 
       (.I0(uniform[70]),
        .I1(uniform[69]),
        .O(\used[2]_INST_0_i_20_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair59" *) 
  LUT4 #(
    .INIT(16'h7FFF)) 
    \used[2]_INST_0_i_21 
       (.I0(uniform[49]),
        .I1(uniform[48]),
        .I2(uniform[39]),
        .I3(uniform[50]),
        .O(\used[2]_INST_0_i_21_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair58" *) 
  LUT4 #(
    .INIT(16'h7FFF)) 
    \used[2]_INST_0_i_22 
       (.I0(uniform[16]),
        .I1(uniform[17]),
        .I2(uniform[19]),
        .I3(uniform[23]),
        .O(\used[2]_INST_0_i_22_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair30" *) 
  LUT3 #(
    .INIT(8'h7F)) 
    \used[2]_INST_0_i_23 
       (.I0(uniform[11]),
        .I1(uniform[9]),
        .I2(uniform[12]),
        .O(\used[2]_INST_0_i_23_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair65" *) 
  LUT4 #(
    .INIT(16'h7FFF)) 
    \used[2]_INST_0_i_24 
       (.I0(uniform[46]),
        .I1(uniform[44]),
        .I2(uniform[40]),
        .I3(uniform[42]),
        .O(\used[2]_INST_0_i_24_n_0 ));
  LUT6 #(
    .INIT(64'h8000000000000000)) 
    \used[2]_INST_0_i_25 
       (.I0(uniform[26]),
        .I1(uniform[25]),
        .I2(uniform[22]),
        .I3(uniform[24]),
        .I4(uniform[2]),
        .I5(uniform[3]),
        .O(\used[2]_INST_0_i_25_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair45" *) 
  LUT4 #(
    .INIT(16'h8000)) 
    \used[2]_INST_0_i_26 
       (.I0(uniform[65]),
        .I1(uniform[67]),
        .I2(uniform[64]),
        .I3(uniform[59]),
        .O(\used[2]_INST_0_i_26_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair93" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \used[2]_INST_0_i_27 
       (.I0(uniform[33]),
        .I1(uniform[34]),
        .O(\used[2]_INST_0_i_27_n_0 ));
  LUT6 #(
    .INIT(64'h4000404003030303)) 
    \used[2]_INST_0_i_28 
       (.I0(\used[4]_INST_0_i_3_n_0 ),
        .I1(uniform[42]),
        .I2(uniform[40]),
        .I3(\used[2]_INST_0_i_30_n_0 ),
        .I4(\used[6]_INST_0_i_12_n_0 ),
        .I5(uniform[41]),
        .O(\used[2]_INST_0_i_28_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFFFBFFFFFF)) 
    \used[2]_INST_0_i_29 
       (.I0(uniform[64]),
        .I1(uniform[35]),
        .I2(uniform[63]),
        .I3(uniform[56]),
        .I4(uniform[59]),
        .I5(\used[2]_INST_0_i_15_n_0 ),
        .O(\used[2]_INST_0_i_29_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair35" *) 
  LUT4 #(
    .INIT(16'h7FFF)) 
    \used[2]_INST_0_i_3 
       (.I0(uniform[9]),
        .I1(uniform[10]),
        .I2(uniform[12]),
        .I3(uniform[11]),
        .O(\used[2]_INST_0_i_3_n_0 ));
  LUT6 #(
    .INIT(64'h220F22FF22FF22FF)) 
    \used[2]_INST_0_i_30 
       (.I0(\used[2]_INST_0_i_31_n_0 ),
        .I1(\used[2]_INST_0_i_32_n_0 ),
        .I2(uniform[49]),
        .I3(uniform[47]),
        .I4(uniform[48]),
        .I5(uniform[50]),
        .O(\used[2]_INST_0_i_30_n_0 ));
  LUT6 #(
    .INIT(64'h8080808080808000)) 
    \used[2]_INST_0_i_31 
       (.I0(\used[6]_INST_0_i_13_n_0 ),
        .I1(uniform[50]),
        .I2(uniform[51]),
        .I3(uniform[52]),
        .I4(uniform[53]),
        .I5(uniform[54]),
        .O(\used[2]_INST_0_i_31_n_0 ));
  LUT6 #(
    .INIT(64'hA888000000000000)) 
    \used[2]_INST_0_i_32 
       (.I0(\used[2]_INST_0_i_33_n_0 ),
        .I1(uniform[55]),
        .I2(uniform[57]),
        .I3(uniform[56]),
        .I4(\sample[2]_INST_0_i_45_n_0 ),
        .I5(uniform[54]),
        .O(\used[2]_INST_0_i_32_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFFE0000000)) 
    \used[2]_INST_0_i_33 
       (.I0(uniform[65]),
        .I1(uniform[63]),
        .I2(\used[0]_INST_0_i_39_n_0 ),
        .I3(uniform[62]),
        .I4(uniform[60]),
        .I5(\used[2]_INST_0_i_34_n_0 ),
        .O(\used[2]_INST_0_i_33_n_0 ));
  LUT6 #(
    .INIT(64'h77F7FFFFFFFF33F3)) 
    \used[2]_INST_0_i_34 
       (.I0(uniform[58]),
        .I1(uniform[57]),
        .I2(\used[2]_INST_0_i_35_n_0 ),
        .I3(uniform[59]),
        .I4(uniform[55]),
        .I5(uniform[56]),
        .O(\used[2]_INST_0_i_34_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair3" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \used[2]_INST_0_i_35 
       (.I0(uniform[60]),
        .I1(uniform[61]),
        .O(\used[2]_INST_0_i_35_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair74" *) 
  LUT4 #(
    .INIT(16'h7FFF)) 
    \used[2]_INST_0_i_4 
       (.I0(uniform[2]),
        .I1(uniform[6]),
        .I2(uniform[8]),
        .I3(uniform[7]),
        .O(\used[2]_INST_0_i_4_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair34" *) 
  LUT5 #(
    .INIT(32'h7FFFFF00)) 
    \used[2]_INST_0_i_5 
       (.I0(uniform[4]),
        .I1(uniform[5]),
        .I2(uniform[3]),
        .I3(uniform[1]),
        .I4(uniform[2]),
        .O(\used[2]_INST_0_i_5_n_0 ));
  LUT6 #(
    .INIT(64'h00000010FFFFFFFF)) 
    \used[2]_INST_0_i_6 
       (.I0(\used[2]_INST_0_i_10_n_0 ),
        .I1(\used[2]_INST_0_i_11_n_0 ),
        .I2(\used[2]_INST_0_i_12_n_0 ),
        .I3(\used[2]_INST_0_i_13_n_0 ),
        .I4(\used[2]_INST_0_i_14_n_0 ),
        .I5(uniform[0]),
        .O(\used[2]_INST_0_i_6_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair64" *) 
  LUT4 #(
    .INIT(16'h7FFF)) 
    \used[2]_INST_0_i_7 
       (.I0(uniform[20]),
        .I1(uniform[21]),
        .I2(uniform[22]),
        .I3(uniform[23]),
        .O(\used[2]_INST_0_i_7_n_0 ));
  LUT6 #(
    .INIT(64'h00000000FEEEFEFE)) 
    \used[2]_INST_0_i_8 
       (.I0(\used[5]_INST_0_i_10_n_0 ),
        .I1(\used[2]_INST_0_i_15_n_0 ),
        .I2(\used[6]_INST_0_i_11_n_0 ),
        .I3(\used[2]_INST_0_i_16_n_0 ),
        .I4(\used[2]_INST_0_i_17_n_0 ),
        .I5(\used[2]_INST_0_i_18_n_0 ),
        .O(\used[2]_INST_0_i_8_n_0 ));
  LUT6 #(
    .INIT(64'h7F7F7F7F7F7F7FFF)) 
    \used[2]_INST_0_i_9 
       (.I0(\used[2]_INST_0_i_19_n_0 ),
        .I1(uniform[17]),
        .I2(uniform[16]),
        .I3(uniform[21]),
        .I4(uniform[20]),
        .I5(uniform[22]),
        .O(\used[2]_INST_0_i_9_n_0 ));
  LUT5 #(
    .INIT(32'h0000AE00)) 
    \used[3]_INST_0 
       (.I0(\used[3]_INST_0_i_1_n_0 ),
        .I1(\used[3]_INST_0_i_2_n_0 ),
        .I2(\used[3]_INST_0_i_3_n_0 ),
        .I3(uniform[0]),
        .I4(\used[3]_INST_0_i_4_n_0 ),
        .O(used[3]));
  LUT6 #(
    .INIT(64'hFFFFFFFF11111110)) 
    \used[3]_INST_0_i_1 
       (.I0(\used[3]_INST_0_i_5_n_0 ),
        .I1(\used[6]_INST_0_i_8_n_0 ),
        .I2(uniform[21]),
        .I3(uniform[20]),
        .I4(uniform[22]),
        .I5(\used[3]_INST_0_i_6_n_0 ),
        .O(\used[3]_INST_0_i_1_n_0 ));
  LUT6 #(
    .INIT(64'h5D0000005D5D005D)) 
    \used[3]_INST_0_i_10 
       (.I0(uniform[53]),
        .I1(\used[5]_INST_0_i_14_n_0 ),
        .I2(\used[3]_INST_0_i_14_n_0 ),
        .I3(uniform[52]),
        .I4(\used[5]_INST_0_i_12_n_0 ),
        .I5(uniform[54]),
        .O(\used[3]_INST_0_i_10_n_0 ));
  LUT6 #(
    .INIT(64'h8888888880000000)) 
    \used[3]_INST_0_i_11 
       (.I0(uniform[40]),
        .I1(uniform[42]),
        .I2(uniform[45]),
        .I3(uniform[46]),
        .I4(uniform[44]),
        .I5(uniform[43]),
        .O(\used[3]_INST_0_i_11_n_0 ));
  LUT6 #(
    .INIT(64'h8088000000000000)) 
    \used[3]_INST_0_i_12 
       (.I0(uniform[59]),
        .I1(uniform[58]),
        .I2(uniform[60]),
        .I3(uniform[70]),
        .I4(uniform[56]),
        .I5(uniform[54]),
        .O(\used[3]_INST_0_i_12_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF7FFFFFFF)) 
    \used[3]_INST_0_i_13 
       (.I0(\used[6]_INST_0_i_13_n_0 ),
        .I1(\sample[4]_INST_0_i_17_n_0 ),
        .I2(uniform[47]),
        .I3(uniform[43]),
        .I4(uniform[45]),
        .I5(\used[1]_INST_0_i_18_n_0 ),
        .O(\used[3]_INST_0_i_13_n_0 ));
  LUT6 #(
    .INIT(64'h8000000000000000)) 
    \used[3]_INST_0_i_14 
       (.I0(\used[2]_INST_0_i_26_n_0 ),
        .I1(uniform[63]),
        .I2(uniform[62]),
        .I3(uniform[66]),
        .I4(uniform[60]),
        .I5(uniform[61]),
        .O(\used[3]_INST_0_i_14_n_0 ));
  LUT6 #(
    .INIT(64'h5FFC5FFC5FFCFFFF)) 
    \used[3]_INST_0_i_2 
       (.I0(\used[3]_INST_0_i_7_n_0 ),
        .I1(uniform[38]),
        .I2(uniform[36]),
        .I3(uniform[37]),
        .I4(uniform[28]),
        .I5(uniform[29]),
        .O(\used[3]_INST_0_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF0EEEFFFF)) 
    \used[3]_INST_0_i_3 
       (.I0(uniform[28]),
        .I1(uniform[29]),
        .I2(\used[6]_INST_0_i_9_n_0 ),
        .I3(\used[6]_INST_0_i_11_n_0 ),
        .I4(uniform[22]),
        .I5(\used[6]_INST_0_i_8_n_0 ),
        .O(\used[3]_INST_0_i_3_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair38" *) 
  LUT5 #(
    .INIT(32'h7FFFFFFF)) 
    \used[3]_INST_0_i_4 
       (.I0(uniform[3]),
        .I1(uniform[2]),
        .I2(uniform[5]),
        .I3(uniform[4]),
        .I4(uniform[1]),
        .O(\used[3]_INST_0_i_4_n_0 ));
  LUT6 #(
    .INIT(64'h8000000000000000)) 
    \used[3]_INST_0_i_5 
       (.I0(uniform[27]),
        .I1(uniform[25]),
        .I2(uniform[26]),
        .I3(uniform[22]),
        .I4(\used[3]_INST_0_i_8_n_0 ),
        .I5(\sample[4]_INST_0_i_21_n_0 ),
        .O(\used[3]_INST_0_i_5_n_0 ));
  LUT6 #(
    .INIT(64'h7FFFFFFFFFFFFFFF)) 
    \used[3]_INST_0_i_6 
       (.I0(uniform[12]),
        .I1(uniform[9]),
        .I2(uniform[11]),
        .I3(\sample[2]_INST_0_i_8_n_0 ),
        .I4(uniform[10]),
        .I5(uniform[6]),
        .O(\used[3]_INST_0_i_6_n_0 ));
  LUT6 #(
    .INIT(64'hE000000000000000)) 
    \used[3]_INST_0_i_7 
       (.I0(\used[3]_INST_0_i_9_n_0 ),
        .I1(\used[3]_INST_0_i_10_n_0 ),
        .I2(uniform[39]),
        .I3(uniform[38]),
        .I4(uniform[41]),
        .I5(\used[3]_INST_0_i_11_n_0 ),
        .O(\used[3]_INST_0_i_7_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair26" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \used[3]_INST_0_i_8 
       (.I0(uniform[23]),
        .I1(uniform[24]),
        .O(\used[3]_INST_0_i_8_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF01110000)) 
    \used[3]_INST_0_i_9 
       (.I0(\used[6]_INST_0_i_10_n_0 ),
        .I1(uniform[68]),
        .I2(uniform[70]),
        .I3(uniform[69]),
        .I4(\used[3]_INST_0_i_12_n_0 ),
        .I5(\used[3]_INST_0_i_13_n_0 ),
        .O(\used[3]_INST_0_i_9_n_0 ));
  LUT3 #(
    .INIT(8'h8A)) 
    \used[4]_INST_0 
       (.I0(\used[5]_INST_0_i_6_n_0 ),
        .I1(\used[4]_INST_0_i_1_n_0 ),
        .I2(\used[6]_INST_0_i_1_n_0 ),
        .O(used[4]));
  LUT6 #(
    .INIT(64'h0000DF0055555555)) 
    \used[4]_INST_0_i_1 
       (.I0(uniform[29]),
        .I1(\used[5]_INST_0_i_7_n_0 ),
        .I2(uniform[45]),
        .I3(\used[4]_INST_0_i_2_n_0 ),
        .I4(\used[4]_INST_0_i_3_n_0 ),
        .I5(uniform[28]),
        .O(\used[4]_INST_0_i_1_n_0 ));
  LUT6 #(
    .INIT(64'h0000000080000000)) 
    \used[4]_INST_0_i_2 
       (.I0(\used[5]_INST_0_i_8_n_0 ),
        .I1(uniform[40]),
        .I2(uniform[41]),
        .I3(uniform[39]),
        .I4(uniform[42]),
        .I5(\used[5]_INST_0_i_9_n_0 ),
        .O(\used[4]_INST_0_i_2_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair13" *) 
  LUT4 #(
    .INIT(16'h1555)) 
    \used[4]_INST_0_i_3 
       (.I0(uniform[43]),
        .I1(uniform[44]),
        .I2(uniform[46]),
        .I3(uniform[45]),
        .O(\used[4]_INST_0_i_3_n_0 ));
  LUT6 #(
    .INIT(64'h0200000000000000)) 
    \used[5]_INST_0 
       (.I0(\used[5]_INST_0_i_1_n_0 ),
        .I1(\used[5]_INST_0_i_2_n_0 ),
        .I2(\used[5]_INST_0_i_3_n_0 ),
        .I3(\used[5]_INST_0_i_4_n_0 ),
        .I4(\used[5]_INST_0_i_5_n_0 ),
        .I5(\used[5]_INST_0_i_6_n_0 ),
        .O(used[5]));
  LUT6 #(
    .INIT(64'hFBFFFFFFFFFFFFFF)) 
    \used[5]_INST_0_i_1 
       (.I0(\used[5]_INST_0_i_7_n_0 ),
        .I1(\used[5]_INST_0_i_8_n_0 ),
        .I2(\used[5]_INST_0_i_9_n_0 ),
        .I3(uniform[41]),
        .I4(uniform[45]),
        .I5(uniform[28]),
        .O(\used[5]_INST_0_i_1_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair51" *) 
  LUT2 #(
    .INIT(4'h1)) 
    \used[5]_INST_0_i_10 
       (.I0(uniform[28]),
        .I1(uniform[29]),
        .O(\used[5]_INST_0_i_10_n_0 ));
  LUT6 #(
    .INIT(64'h8000000000000000)) 
    \used[5]_INST_0_i_11 
       (.I0(uniform[8]),
        .I1(uniform[3]),
        .I2(uniform[2]),
        .I3(uniform[1]),
        .I4(uniform[5]),
        .I5(uniform[6]),
        .O(\used[5]_INST_0_i_11_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair49" *) 
  LUT4 #(
    .INIT(16'h8000)) 
    \used[5]_INST_0_i_12 
       (.I0(uniform[58]),
        .I1(uniform[55]),
        .I2(uniform[57]),
        .I3(uniform[53]),
        .O(\used[5]_INST_0_i_12_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair24" *) 
  LUT5 #(
    .INIT(32'h7FFFFFFF)) 
    \used[5]_INST_0_i_13 
       (.I0(uniform[46]),
        .I1(uniform[44]),
        .I2(uniform[40]),
        .I3(uniform[49]),
        .I4(uniform[48]),
        .O(\used[5]_INST_0_i_13_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair14" *) 
  LUT5 #(
    .INIT(32'h88808080)) 
    \used[5]_INST_0_i_14 
       (.I0(uniform[54]),
        .I1(uniform[56]),
        .I2(uniform[59]),
        .I3(uniform[60]),
        .I4(uniform[61]),
        .O(\used[5]_INST_0_i_14_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair43" *) 
  LUT4 #(
    .INIT(16'h7FFF)) 
    \used[5]_INST_0_i_15 
       (.I0(uniform[50]),
        .I1(uniform[51]),
        .I2(uniform[52]),
        .I3(uniform[47]),
        .O(\used[5]_INST_0_i_15_n_0 ));
  LUT6 #(
    .INIT(64'h7FFFFFFFFFFFFFFF)) 
    \used[5]_INST_0_i_2 
       (.I0(uniform[18]),
        .I1(uniform[19]),
        .I2(uniform[14]),
        .I3(uniform[15]),
        .I4(uniform[13]),
        .I5(uniform[16]),
        .O(\used[5]_INST_0_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF7FFFFFFF)) 
    \used[5]_INST_0_i_3 
       (.I0(uniform[26]),
        .I1(uniform[25]),
        .I2(uniform[27]),
        .I3(uniform[23]),
        .I4(uniform[24]),
        .I5(\used[5]_INST_0_i_10_n_0 ),
        .O(\used[5]_INST_0_i_3_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair81" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \used[5]_INST_0_i_4 
       (.I0(uniform[22]),
        .I1(uniform[20]),
        .O(\used[5]_INST_0_i_4_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair57" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \used[5]_INST_0_i_5 
       (.I0(uniform[17]),
        .I1(uniform[21]),
        .O(\used[5]_INST_0_i_5_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair29" *) 
  LUT5 #(
    .INIT(32'h20000000)) 
    \used[5]_INST_0_i_6 
       (.I0(\used[5]_INST_0_i_11_n_0 ),
        .I1(\used[2]_INST_0_i_3_n_0 ),
        .I2(uniform[0]),
        .I3(uniform[4]),
        .I4(uniform[7]),
        .O(\used[5]_INST_0_i_6_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFFFF7FFFFF)) 
    \used[5]_INST_0_i_7 
       (.I0(uniform[39]),
        .I1(\sample[4]_INST_0_i_14_n_0 ),
        .I2(\used[5]_INST_0_i_12_n_0 ),
        .I3(\used[5]_INST_0_i_13_n_0 ),
        .I4(\used[5]_INST_0_i_14_n_0 ),
        .I5(\used[5]_INST_0_i_15_n_0 ),
        .O(\used[5]_INST_0_i_7_n_0 ));
  LUT6 #(
    .INIT(64'h8000000000000000)) 
    \used[5]_INST_0_i_8 
       (.I0(uniform[33]),
        .I1(uniform[31]),
        .I2(uniform[35]),
        .I3(uniform[34]),
        .I4(uniform[32]),
        .I5(uniform[30]),
        .O(\used[5]_INST_0_i_8_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair47" *) 
  LUT4 #(
    .INIT(16'h7FFF)) 
    \used[5]_INST_0_i_9 
       (.I0(uniform[36]),
        .I1(uniform[37]),
        .I2(uniform[29]),
        .I3(uniform[38]),
        .O(\used[5]_INST_0_i_9_n_0 ));
  LUT6 #(
    .INIT(64'h0000000000000002)) 
    \used[6]_INST_0 
       (.I0(\used[6]_INST_0_i_1_n_0 ),
        .I1(\used[6]_INST_0_i_2_n_0 ),
        .I2(\used[6]_INST_0_i_3_n_0 ),
        .I3(\used[6]_INST_0_i_4_n_0 ),
        .I4(\used[6]_INST_0_i_5_n_0 ),
        .I5(\used[6]_INST_0_i_6_n_0 ),
        .O(used[6]));
  LUT6 #(
    .INIT(64'h0000000080000000)) 
    \used[6]_INST_0_i_1 
       (.I0(uniform[20]),
        .I1(uniform[21]),
        .I2(uniform[24]),
        .I3(uniform[23]),
        .I4(\used[6]_INST_0_i_7_n_0 ),
        .I5(\used[6]_INST_0_i_8_n_0 ),
        .O(\used[6]_INST_0_i_1_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair49" *) 
  LUT4 #(
    .INIT(16'h7FFF)) 
    \used[6]_INST_0_i_10 
       (.I0(uniform[57]),
        .I1(uniform[53]),
        .I2(uniform[52]),
        .I3(uniform[55]),
        .O(\used[6]_INST_0_i_10_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair22" *) 
  LUT4 #(
    .INIT(16'h8000)) 
    \used[6]_INST_0_i_11 
       (.I0(uniform[30]),
        .I1(uniform[31]),
        .I2(uniform[29]),
        .I3(uniform[28]),
        .O(\used[6]_INST_0_i_11_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair48" *) 
  LUT4 #(
    .INIT(16'h8000)) 
    \used[6]_INST_0_i_12 
       (.I0(uniform[44]),
        .I1(uniform[43]),
        .I2(uniform[45]),
        .I3(uniform[46]),
        .O(\used[6]_INST_0_i_12_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair39" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \used[6]_INST_0_i_13 
       (.I0(uniform[48]),
        .I1(uniform[49]),
        .O(\used[6]_INST_0_i_13_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair65" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \used[6]_INST_0_i_14 
       (.I0(uniform[42]),
        .I1(uniform[40]),
        .O(\used[6]_INST_0_i_14_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair14" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \used[6]_INST_0_i_15 
       (.I0(uniform[56]),
        .I1(uniform[54]),
        .O(\used[6]_INST_0_i_15_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair56" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \used[6]_INST_0_i_16 
       (.I0(uniform[5]),
        .I1(uniform[4]),
        .O(\used[6]_INST_0_i_16_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair84" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \used[6]_INST_0_i_17 
       (.I0(uniform[2]),
        .I1(uniform[3]),
        .O(\used[6]_INST_0_i_17_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair79" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \used[6]_INST_0_i_18 
       (.I0(uniform[41]),
        .I1(uniform[38]),
        .O(\used[6]_INST_0_i_18_n_0 ));
  LUT2 #(
    .INIT(4'h8)) 
    \used[6]_INST_0_i_19 
       (.I0(uniform[14]),
        .I1(uniform[13]),
        .O(\used[6]_INST_0_i_19_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair30" *) 
  LUT5 #(
    .INIT(32'h7FFFFFFF)) 
    \used[6]_INST_0_i_2 
       (.I0(uniform[12]),
        .I1(uniform[9]),
        .I2(uniform[11]),
        .I3(\used[6]_INST_0_i_9_n_0 ),
        .I4(uniform[7]),
        .O(\used[6]_INST_0_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hAABFFFFFFFFFFFFF)) 
    \used[6]_INST_0_i_3 
       (.I0(\used[6]_INST_0_i_10_n_0 ),
        .I1(uniform[61]),
        .I2(uniform[60]),
        .I3(uniform[59]),
        .I4(\used[6]_INST_0_i_11_n_0 ),
        .I5(\used[6]_INST_0_i_12_n_0 ),
        .O(\used[6]_INST_0_i_3_n_0 ));
  LUT6 #(
    .INIT(64'h7FFFFFFFFFFFFFFF)) 
    \used[6]_INST_0_i_4 
       (.I0(uniform[50]),
        .I1(uniform[39]),
        .I2(\used[6]_INST_0_i_13_n_0 ),
        .I3(\used[6]_INST_0_i_14_n_0 ),
        .I4(uniform[47]),
        .I5(uniform[51]),
        .O(\used[6]_INST_0_i_4_n_0 ));
  LUT6 #(
    .INIT(64'h7FFFFFFFFFFFFFFF)) 
    \used[6]_INST_0_i_5 
       (.I0(uniform[8]),
        .I1(uniform[58]),
        .I2(\used[6]_INST_0_i_15_n_0 ),
        .I3(\used[6]_INST_0_i_16_n_0 ),
        .I4(uniform[10]),
        .I5(uniform[6]),
        .O(\used[6]_INST_0_i_5_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFF7FFF)) 
    \used[6]_INST_0_i_6 
       (.I0(uniform[37]),
        .I1(uniform[36]),
        .I2(uniform[1]),
        .I3(uniform[0]),
        .I4(\used[6]_INST_0_i_17_n_0 ),
        .I5(\used[6]_INST_0_i_18_n_0 ),
        .O(\used[6]_INST_0_i_6_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair66" *) 
  LUT4 #(
    .INIT(16'h8000)) 
    \used[6]_INST_0_i_7 
       (.I0(uniform[22]),
        .I1(uniform[26]),
        .I2(uniform[25]),
        .I3(uniform[27]),
        .O(\used[6]_INST_0_i_7_n_0 ));
  LUT6 #(
    .INIT(64'h7FFFFFFFFFFFFFFF)) 
    \used[6]_INST_0_i_8 
       (.I0(uniform[19]),
        .I1(uniform[18]),
        .I2(uniform[17]),
        .I3(uniform[16]),
        .I4(\used[6]_INST_0_i_19_n_0 ),
        .I5(uniform[15]),
        .O(\used[6]_INST_0_i_8_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair52" *) 
  LUT4 #(
    .INIT(16'h8000)) 
    \used[6]_INST_0_i_9 
       (.I0(uniform[34]),
        .I1(uniform[35]),
        .I2(uniform[32]),
        .I3(uniform[33]),
        .O(\used[6]_INST_0_i_9_n_0 ));
endmodule

(* STRUCTURAL_NETLIST = "yes" *)
module base_sampler_pla_smart_reg
   (clk,
    uniform,
    sample,
    used);
  input clk;
  input [71:0]uniform;
  output [4:0]sample;
  output [6:0]used;

  wire \<const0> ;
  wire \<const1> ;
  wire [4:0]_sample;
  wire [71:0]_uniform;
  wire [6:0]_used;
  wire clk;
  wire [4:0]sample;
  wire [71:0]uniform;
  wire [6:0]used;

  GND GND
       (.G(\<const0> ));
  VCC VCC
       (.P(\<const1> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[0] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[0]),
        .Q(_uniform[0]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[10] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[10]),
        .Q(_uniform[10]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[11] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[11]),
        .Q(_uniform[11]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[12] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[12]),
        .Q(_uniform[12]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[13] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[13]),
        .Q(_uniform[13]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[14] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[14]),
        .Q(_uniform[14]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[15] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[15]),
        .Q(_uniform[15]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[16] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[16]),
        .Q(_uniform[16]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[17] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[17]),
        .Q(_uniform[17]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[18] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[18]),
        .Q(_uniform[18]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[19] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[19]),
        .Q(_uniform[19]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[1] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[1]),
        .Q(_uniform[1]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[20] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[20]),
        .Q(_uniform[20]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[21] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[21]),
        .Q(_uniform[21]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[22] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[22]),
        .Q(_uniform[22]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[23] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[23]),
        .Q(_uniform[23]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[24] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[24]),
        .Q(_uniform[24]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[25] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[25]),
        .Q(_uniform[25]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[26] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[26]),
        .Q(_uniform[26]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[27] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[27]),
        .Q(_uniform[27]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[28] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[28]),
        .Q(_uniform[28]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[29] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[29]),
        .Q(_uniform[29]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[2] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[2]),
        .Q(_uniform[2]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[30] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[30]),
        .Q(_uniform[30]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[31] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[31]),
        .Q(_uniform[31]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[32] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[32]),
        .Q(_uniform[32]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[33] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[33]),
        .Q(_uniform[33]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[34] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[34]),
        .Q(_uniform[34]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[35] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[35]),
        .Q(_uniform[35]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[36] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[36]),
        .Q(_uniform[36]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[37] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[37]),
        .Q(_uniform[37]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[38] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[38]),
        .Q(_uniform[38]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[39] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[39]),
        .Q(_uniform[39]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[3] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[3]),
        .Q(_uniform[3]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[40] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[40]),
        .Q(_uniform[40]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[41] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[41]),
        .Q(_uniform[41]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[42] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[42]),
        .Q(_uniform[42]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[43] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[43]),
        .Q(_uniform[43]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[44] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[44]),
        .Q(_uniform[44]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[45] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[45]),
        .Q(_uniform[45]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[46] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[46]),
        .Q(_uniform[46]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[47] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[47]),
        .Q(_uniform[47]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[48] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[48]),
        .Q(_uniform[48]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[49] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[49]),
        .Q(_uniform[49]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[4] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[4]),
        .Q(_uniform[4]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[50] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[50]),
        .Q(_uniform[50]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[51] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[51]),
        .Q(_uniform[51]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[52] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[52]),
        .Q(_uniform[52]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[53] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[53]),
        .Q(_uniform[53]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[54] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[54]),
        .Q(_uniform[54]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[55] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[55]),
        .Q(_uniform[55]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[56] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[56]),
        .Q(_uniform[56]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[57] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[57]),
        .Q(_uniform[57]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[58] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[58]),
        .Q(_uniform[58]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[59] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[59]),
        .Q(_uniform[59]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[5] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[5]),
        .Q(_uniform[5]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[60] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[60]),
        .Q(_uniform[60]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[61] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[61]),
        .Q(_uniform[61]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[62] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[62]),
        .Q(_uniform[62]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[63] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[63]),
        .Q(_uniform[63]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[64] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[64]),
        .Q(_uniform[64]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[65] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[65]),
        .Q(_uniform[65]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[66] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[66]),
        .Q(_uniform[66]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[67] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[67]),
        .Q(_uniform[67]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[68] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[68]),
        .Q(_uniform[68]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[69] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[69]),
        .Q(_uniform[69]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[6] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[6]),
        .Q(_uniform[6]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[70] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[70]),
        .Q(_uniform[70]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[71] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[71]),
        .Q(_uniform[71]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[7] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[7]),
        .Q(_uniform[7]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[8] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[8]),
        .Q(_uniform[8]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \_uniform_reg[9] 
       (.C(clk),
        .CE(\<const1> ),
        .D(uniform[9]),
        .Q(_uniform[9]),
        .R(\<const0> ));
  (* KEEP_HIERARCHY = "yes" *) 
  base_sampler_pla_smart inst
       (.sample(_sample),
        .uniform(_uniform),
        .used(_used));
  FDRE #(
    .INIT(1'b0)) 
    \sample_reg[0] 
       (.C(clk),
        .CE(\<const1> ),
        .D(_sample[0]),
        .Q(sample[0]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \sample_reg[1] 
       (.C(clk),
        .CE(\<const1> ),
        .D(_sample[1]),
        .Q(sample[1]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \sample_reg[2] 
       (.C(clk),
        .CE(\<const1> ),
        .D(_sample[2]),
        .Q(sample[2]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \sample_reg[3] 
       (.C(clk),
        .CE(\<const1> ),
        .D(_sample[3]),
        .Q(sample[3]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \sample_reg[4] 
       (.C(clk),
        .CE(\<const1> ),
        .D(_sample[4]),
        .Q(sample[4]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \used_reg[0] 
       (.C(clk),
        .CE(\<const1> ),
        .D(_used[0]),
        .Q(used[0]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \used_reg[1] 
       (.C(clk),
        .CE(\<const1> ),
        .D(_used[1]),
        .Q(used[1]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \used_reg[2] 
       (.C(clk),
        .CE(\<const1> ),
        .D(_used[2]),
        .Q(used[2]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \used_reg[3] 
       (.C(clk),
        .CE(\<const1> ),
        .D(_used[3]),
        .Q(used[3]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \used_reg[4] 
       (.C(clk),
        .CE(\<const1> ),
        .D(_used[4]),
        .Q(used[4]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \used_reg[5] 
       (.C(clk),
        .CE(\<const1> ),
        .D(_used[5]),
        .Q(used[5]),
        .R(\<const0> ));
  FDRE #(
    .INIT(1'b0)) 
    \used_reg[6] 
       (.C(clk),
        .CE(\<const1> ),
        .D(_used[6]),
        .Q(used[6]),
        .R(\<const0> ));
endmodule
`endif