// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2024.2 (lin64) Build 5239630 Fri Nov 08 22:34:34 MST 2024
// Date        : Wed Apr 16 01:15:15 2025
// Host        : xps running 64-bit Pop!_OS 24.04 LTS
// Command     : write_verilog /home/xxx/Falcon/repo/src/hdl/base_sampler/base_sampler_pla.netlist.v
// Design      : base_sampler_pla_reg
// Purpose     : This is a Verilog netlist of the current design or from a specific cell of the design. The output is an
//               IEEE 1364-2001 compliant Verilog HDL file that contains netlist information obtained from the input
//               design files.
// Device      : xck26-sfvc784-2LV-c
// --------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

`ifdef BASE_SAMPLER_NETLIST
module base_sampler_pla // @suppress "Design unit name"
   (uniform,
    sample);
  input [96:0]uniform;
  output [4:0]sample;

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
  wire \sample[0]_INST_0_i_77_n_0 ;
  wire \sample[0]_INST_0_i_78_n_0 ;
  wire \sample[0]_INST_0_i_79_n_0 ;
  wire \sample[0]_INST_0_i_7_n_0 ;
  wire \sample[0]_INST_0_i_80_n_0 ;
  wire \sample[0]_INST_0_i_81_n_0 ;
  wire \sample[0]_INST_0_i_82_n_0 ;
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
  wire \sample[1]_INST_0_i_77_n_0 ;
  wire \sample[1]_INST_0_i_78_n_0 ;
  wire \sample[1]_INST_0_i_79_n_0 ;
  wire \sample[1]_INST_0_i_7_n_0 ;
  wire \sample[1]_INST_0_i_80_n_0 ;
  wire \sample[1]_INST_0_i_81_n_0 ;
  wire \sample[1]_INST_0_i_82_n_0 ;
  wire \sample[1]_INST_0_i_83_n_0 ;
  wire \sample[1]_INST_0_i_84_n_0 ;
  wire \sample[1]_INST_0_i_85_n_0 ;
  wire \sample[1]_INST_0_i_86_n_0 ;
  wire \sample[1]_INST_0_i_87_n_0 ;
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
  wire \sample[3]_INST_0_i_59_n_0 ;
  wire \sample[3]_INST_0_i_5_n_0 ;
  wire \sample[3]_INST_0_i_60_n_0 ;
  wire \sample[3]_INST_0_i_61_n_0 ;
  wire \sample[3]_INST_0_i_62_n_0 ;
  wire \sample[3]_INST_0_i_63_n_0 ;
  wire \sample[3]_INST_0_i_64_n_0 ;
  wire \sample[3]_INST_0_i_65_n_0 ;
  wire \sample[3]_INST_0_i_66_n_0 ;
  wire \sample[3]_INST_0_i_67_n_0 ;
  wire \sample[3]_INST_0_i_68_n_0 ;
  wire \sample[3]_INST_0_i_69_n_0 ;
  wire \sample[3]_INST_0_i_6_n_0 ;
  wire \sample[3]_INST_0_i_70_n_0 ;
  wire \sample[3]_INST_0_i_71_n_0 ;
  wire \sample[3]_INST_0_i_72_n_0 ;
  wire \sample[3]_INST_0_i_73_n_0 ;
  wire \sample[3]_INST_0_i_74_n_0 ;
  wire \sample[3]_INST_0_i_75_n_0 ;
  wire \sample[3]_INST_0_i_76_n_0 ;
  wire \sample[3]_INST_0_i_77_n_0 ;
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
  wire \sample[4]_INST_0_i_27_n_0 ;
  wire \sample[4]_INST_0_i_28_n_0 ;
  wire \sample[4]_INST_0_i_29_n_0 ;
  wire \sample[4]_INST_0_i_2_n_0 ;
  wire \sample[4]_INST_0_i_30_n_0 ;
  wire \sample[4]_INST_0_i_31_n_0 ;
  wire \sample[4]_INST_0_i_32_n_0 ;
  wire \sample[4]_INST_0_i_33_n_0 ;
  wire \sample[4]_INST_0_i_34_n_0 ;
  wire \sample[4]_INST_0_i_35_n_0 ;
  wire \sample[4]_INST_0_i_36_n_0 ;
  wire \sample[4]_INST_0_i_37_n_0 ;
  wire \sample[4]_INST_0_i_38_n_0 ;
  wire \sample[4]_INST_0_i_3_n_0 ;
  wire \sample[4]_INST_0_i_4_n_0 ;
  wire \sample[4]_INST_0_i_5_n_0 ;
  wire \sample[4]_INST_0_i_6_n_0 ;
  wire \sample[4]_INST_0_i_7_n_0 ;
  wire \sample[4]_INST_0_i_8_n_0 ;
  wire \sample[4]_INST_0_i_9_n_0 ;
  wire [96:0]uniform;

  LUT6 #(
    .INIT(64'h000088A8AAAAAAAA)) 
    \sample[0]_INST_0 
       (.I0(\sample[0]_INST_0_i_1_n_0 ),
        .I1(\sample[0]_INST_0_i_2_n_0 ),
        .I2(\sample[0]_INST_0_i_3_n_0 ),
        .I3(\sample[0]_INST_0_i_4_n_0 ),
        .I4(\sample[0]_INST_0_i_5_n_0 ),
        .I5(uniform[1]),
        .O(sample[0]));
  LUT5 #(
    .INIT(32'hAAAA08AA)) 
    \sample[0]_INST_0_i_1 
       (.I0(\sample[4]_INST_0_i_6_n_0 ),
        .I1(uniform[2]),
        .I2(uniform[3]),
        .I3(uniform[0]),
        .I4(uniform[1]),
        .O(\sample[0]_INST_0_i_1_n_0 ));
  LUT6 #(
    .INIT(64'hBBBBFBBBFBBBFBBB)) 
    \sample[0]_INST_0_i_10 
       (.I0(\sample[0]_INST_0_i_14_n_0 ),
        .I1(uniform[19]),
        .I2(\sample[0]_INST_0_i_21_n_0 ),
        .I3(uniform[24]),
        .I4(uniform[23]),
        .I5(uniform[28]),
        .O(\sample[0]_INST_0_i_10_n_0 ));
  LUT5 #(
    .INIT(32'hFFFFFF80)) 
    \sample[0]_INST_0_i_11 
       (.I0(uniform[15]),
        .I1(uniform[19]),
        .I2(\sample[0]_INST_0_i_22_n_0 ),
        .I3(\sample[0]_INST_0_i_23_n_0 ),
        .I4(\sample[0]_INST_0_i_13_n_0 ),
        .O(\sample[0]_INST_0_i_11_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair26" *) 
  LUT5 #(
    .INIT(32'hBFBBBBBF)) 
    \sample[0]_INST_0_i_12 
       (.I0(\sample[0]_INST_0_i_24_n_0 ),
        .I1(uniform[7]),
        .I2(uniform[9]),
        .I3(uniform[10]),
        .I4(uniform[11]),
        .O(\sample[0]_INST_0_i_12_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair24" *) 
  LUT5 #(
    .INIT(32'h2F002000)) 
    \sample[0]_INST_0_i_13 
       (.I0(uniform[18]),
        .I1(uniform[16]),
        .I2(uniform[15]),
        .I3(uniform[14]),
        .I4(uniform[17]),
        .O(\sample[0]_INST_0_i_13_n_0 ));
  LUT6 #(
    .INIT(64'h000000F000A0D000)) 
    \sample[0]_INST_0_i_14 
       (.I0(uniform[23]),
        .I1(uniform[25]),
        .I2(uniform[19]),
        .I3(uniform[21]),
        .I4(uniform[24]),
        .I5(uniform[22]),
        .O(\sample[0]_INST_0_i_14_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair25" *) 
  LUT5 #(
    .INIT(32'h10200020)) 
    \sample[0]_INST_0_i_15 
       (.I0(uniform[22]),
        .I1(uniform[21]),
        .I2(uniform[19]),
        .I3(uniform[24]),
        .I4(uniform[23]),
        .O(\sample[0]_INST_0_i_15_n_0 ));
  LUT6 #(
    .INIT(64'hEEEEEEEEEFEFEFFF)) 
    \sample[0]_INST_0_i_16 
       (.I0(\sample[0]_INST_0_i_25_n_0 ),
        .I1(\sample[0]_INST_0_i_26_n_0 ),
        .I2(uniform[27]),
        .I3(uniform[26]),
        .I4(uniform[25]),
        .I5(uniform[24]),
        .O(\sample[0]_INST_0_i_16_n_0 ));
  LUT6 #(
    .INIT(64'h03030343FFFFFFFF)) 
    \sample[0]_INST_0_i_17 
       (.I0(uniform[29]),
        .I1(uniform[28]),
        .I2(uniform[26]),
        .I3(uniform[31]),
        .I4(uniform[30]),
        .I5(\sample[0]_INST_0_i_27_n_0 ),
        .O(\sample[0]_INST_0_i_17_n_0 ));
  LUT6 #(
    .INIT(64'h00000000FFFF00AE)) 
    \sample[0]_INST_0_i_18 
       (.I0(\sample[0]_INST_0_i_28_n_0 ),
        .I1(\sample[0]_INST_0_i_29_n_0 ),
        .I2(\sample[0]_INST_0_i_30_n_0 ),
        .I3(\sample[0]_INST_0_i_31_n_0 ),
        .I4(\sample[0]_INST_0_i_32_n_0 ),
        .I5(\sample[0]_INST_0_i_33_n_0 ),
        .O(\sample[0]_INST_0_i_18_n_0 ));
  LUT5 #(
    .INIT(32'h7FFFFFFF)) 
    \sample[0]_INST_0_i_19 
       (.I0(uniform[33]),
        .I1(uniform[31]),
        .I2(uniform[29]),
        .I3(uniform[26]),
        .I4(uniform[30]),
        .O(\sample[0]_INST_0_i_19_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF4FFFFF0F)) 
    \sample[0]_INST_0_i_2 
       (.I0(uniform[8]),
        .I1(uniform[9]),
        .I2(uniform[2]),
        .I3(uniform[6]),
        .I4(uniform[5]),
        .I5(\sample[0]_INST_0_i_6_n_0 ),
        .O(\sample[0]_INST_0_i_2_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair18" *) 
  LUT5 #(
    .INIT(32'h77777FFF)) 
    \sample[0]_INST_0_i_20 
       (.I0(uniform[24]),
        .I1(uniform[25]),
        .I2(uniform[28]),
        .I3(uniform[27]),
        .I4(\sample[0]_INST_0_i_34_n_0 ),
        .O(\sample[0]_INST_0_i_20_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair61" *) 
  LUT2 #(
    .INIT(4'h2)) 
    \sample[0]_INST_0_i_21 
       (.I0(uniform[26]),
        .I1(uniform[25]),
        .O(\sample[0]_INST_0_i_21_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair28" *) 
  LUT5 #(
    .INIT(32'h4440FFFF)) 
    \sample[0]_INST_0_i_22 
       (.I0(uniform[20]),
        .I1(uniform[23]),
        .I2(uniform[21]),
        .I3(uniform[22]),
        .I4(uniform[17]),
        .O(\sample[0]_INST_0_i_22_n_0 ));
  LUT6 #(
    .INIT(64'h3333333377337F33)) 
    \sample[0]_INST_0_i_23 
       (.I0(uniform[18]),
        .I1(uniform[14]),
        .I2(uniform[19]),
        .I3(uniform[17]),
        .I4(uniform[21]),
        .I5(uniform[20]),
        .O(\sample[0]_INST_0_i_23_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair27" *) 
  LUT5 #(
    .INIT(32'h30773F00)) 
    \sample[0]_INST_0_i_24 
       (.I0(uniform[14]),
        .I1(uniform[11]),
        .I2(uniform[13]),
        .I3(uniform[12]),
        .I4(uniform[10]),
        .O(\sample[0]_INST_0_i_24_n_0 ));
  LUT6 #(
    .INIT(64'h0000060F0600060F)) 
    \sample[0]_INST_0_i_25 
       (.I0(uniform[28]),
        .I1(uniform[29]),
        .I2(uniform[27]),
        .I3(uniform[25]),
        .I4(uniform[26]),
        .I5(uniform[30]),
        .O(\sample[0]_INST_0_i_25_n_0 ));
  LUT6 #(
    .INIT(64'h0800080008000000)) 
    \sample[0]_INST_0_i_26 
       (.I0(uniform[26]),
        .I1(uniform[24]),
        .I2(uniform[28]),
        .I3(uniform[30]),
        .I4(uniform[27]),
        .I5(uniform[29]),
        .O(\sample[0]_INST_0_i_26_n_0 ));
  LUT6 #(
    .INIT(64'h433373F3733373F3)) 
    \sample[0]_INST_0_i_27 
       (.I0(\sample[0]_INST_0_i_35_n_0 ),
        .I1(uniform[29]),
        .I2(uniform[26]),
        .I3(uniform[30]),
        .I4(uniform[31]),
        .I5(uniform[32]),
        .O(\sample[0]_INST_0_i_27_n_0 ));
  LUT2 #(
    .INIT(4'h7)) 
    \sample[0]_INST_0_i_28 
       (.I0(uniform[39]),
        .I1(uniform[38]),
        .O(\sample[0]_INST_0_i_28_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF00001151)) 
    \sample[0]_INST_0_i_29 
       (.I0(\sample[0]_INST_0_i_36_n_0 ),
        .I1(\sample[1]_INST_0_i_35_n_0 ),
        .I2(\sample[0]_INST_0_i_37_n_0 ),
        .I3(\sample[0]_INST_0_i_38_n_0 ),
        .I4(\sample[0]_INST_0_i_39_n_0 ),
        .I5(\sample[0]_INST_0_i_40_n_0 ),
        .O(\sample[0]_INST_0_i_29_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF55551110)) 
    \sample[0]_INST_0_i_3 
       (.I0(\sample[0]_INST_0_i_7_n_0 ),
        .I1(\sample[0]_INST_0_i_8_n_0 ),
        .I2(\sample[0]_INST_0_i_9_n_0 ),
        .I3(\sample[0]_INST_0_i_10_n_0 ),
        .I4(\sample[0]_INST_0_i_11_n_0 ),
        .I5(\sample[0]_INST_0_i_12_n_0 ),
        .O(\sample[0]_INST_0_i_3_n_0 ));
  LUT6 #(
    .INIT(64'hAAAAFFFFABBFAAAA)) 
    \sample[0]_INST_0_i_30 
       (.I0(\sample[0]_INST_0_i_41_n_0 ),
        .I1(uniform[42]),
        .I2(uniform[43]),
        .I3(uniform[41]),
        .I4(uniform[37]),
        .I5(uniform[40]),
        .O(\sample[0]_INST_0_i_30_n_0 ));
  LUT6 #(
    .INIT(64'h555055F055D0DF50)) 
    \sample[0]_INST_0_i_31 
       (.I0(uniform[35]),
        .I1(uniform[41]),
        .I2(uniform[37]),
        .I3(uniform[38]),
        .I4(uniform[39]),
        .I5(uniform[40]),
        .O(\sample[0]_INST_0_i_31_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair42" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[0]_INST_0_i_32 
       (.I0(uniform[36]),
        .I1(uniform[34]),
        .O(\sample[0]_INST_0_i_32_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair43" *) 
  LUT4 #(
    .INIT(16'hFFEF)) 
    \sample[0]_INST_0_i_33 
       (.I0(\sample[0]_INST_0_i_42_n_0 ),
        .I1(\sample[0]_INST_0_i_43_n_0 ),
        .I2(uniform[32]),
        .I3(\sample[0]_INST_0_i_44_n_0 ),
        .O(\sample[0]_INST_0_i_33_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair19" *) 
  LUT5 #(
    .INIT(32'h000F100F)) 
    \sample[0]_INST_0_i_34 
       (.I0(uniform[30]),
        .I1(uniform[31]),
        .I2(uniform[26]),
        .I3(uniform[28]),
        .I4(uniform[29]),
        .O(\sample[0]_INST_0_i_34_n_0 ));
  LUT6 #(
    .INIT(64'h0F000F00B0CF7F0F)) 
    \sample[0]_INST_0_i_35 
       (.I0(uniform[36]),
        .I1(uniform[35]),
        .I2(uniform[31]),
        .I3(uniform[32]),
        .I4(uniform[34]),
        .I5(uniform[33]),
        .O(\sample[0]_INST_0_i_35_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair41" *) 
  LUT4 #(
    .INIT(16'h0F10)) 
    \sample[0]_INST_0_i_36 
       (.I0(uniform[45]),
        .I1(uniform[43]),
        .I2(uniform[41]),
        .I3(uniform[42]),
        .O(\sample[0]_INST_0_i_36_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF55551110)) 
    \sample[0]_INST_0_i_37 
       (.I0(\sample[0]_INST_0_i_45_n_0 ),
        .I1(\sample[0]_INST_0_i_46_n_0 ),
        .I2(\sample[0]_INST_0_i_47_n_0 ),
        .I3(\sample[0]_INST_0_i_48_n_0 ),
        .I4(\sample[0]_INST_0_i_49_n_0 ),
        .I5(\sample[0]_INST_0_i_50_n_0 ),
        .O(\sample[0]_INST_0_i_37_n_0 ));
  LUT6 #(
    .INIT(64'hAABFABBEAABFBFBE)) 
    \sample[0]_INST_0_i_38 
       (.I0(\sample[0]_INST_0_i_51_n_0 ),
        .I1(uniform[48]),
        .I2(uniform[47]),
        .I3(uniform[45]),
        .I4(uniform[46]),
        .I5(uniform[49]),
        .O(\sample[0]_INST_0_i_38_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair16" *) 
  LUT5 #(
    .INIT(32'h00400000)) 
    \sample[0]_INST_0_i_39 
       (.I0(uniform[47]),
        .I1(uniform[45]),
        .I2(uniform[42]),
        .I3(uniform[43]),
        .I4(uniform[46]),
        .O(\sample[0]_INST_0_i_39_n_0 ));
  LUT6 #(
    .INIT(64'h66666EE6FFFFFFFF)) 
    \sample[0]_INST_0_i_4 
       (.I0(uniform[8]),
        .I1(uniform[7]),
        .I2(uniform[11]),
        .I3(uniform[10]),
        .I4(uniform[9]),
        .I5(uniform[5]),
        .O(\sample[0]_INST_0_i_4_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair68" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[0]_INST_0_i_40 
       (.I0(uniform[40]),
        .I1(uniform[44]),
        .O(\sample[0]_INST_0_i_40_n_0 ));
  LUT6 #(
    .INIT(64'h0333233320331333)) 
    \sample[0]_INST_0_i_41 
       (.I0(uniform[47]),
        .I1(\sample[0]_INST_0_i_52_n_0 ),
        .I2(uniform[43]),
        .I3(uniform[42]),
        .I4(uniform[45]),
        .I5(uniform[46]),
        .O(\sample[0]_INST_0_i_41_n_0 ));
  LUT6 #(
    .INIT(64'h0400040004004400)) 
    \sample[0]_INST_0_i_42 
       (.I0(uniform[37]),
        .I1(uniform[36]),
        .I2(uniform[34]),
        .I3(uniform[35]),
        .I4(uniform[38]),
        .I5(uniform[40]),
        .O(\sample[0]_INST_0_i_42_n_0 ));
  LUT6 #(
    .INIT(64'h0000400040404040)) 
    \sample[0]_INST_0_i_43 
       (.I0(uniform[36]),
        .I1(uniform[35]),
        .I2(uniform[37]),
        .I3(uniform[39]),
        .I4(uniform[38]),
        .I5(uniform[34]),
        .O(\sample[0]_INST_0_i_43_n_0 ));
  LUT6 #(
    .INIT(64'h000C00040C0C0004)) 
    \sample[0]_INST_0_i_44 
       (.I0(uniform[37]),
        .I1(uniform[34]),
        .I2(uniform[36]),
        .I3(uniform[35]),
        .I4(uniform[38]),
        .I5(uniform[39]),
        .O(\sample[0]_INST_0_i_44_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair57" *) 
  LUT3 #(
    .INIT(8'hF1)) 
    \sample[0]_INST_0_i_45 
       (.I0(\sample[0]_INST_0_i_53_n_0 ),
        .I1(uniform[52]),
        .I2(\sample[0]_INST_0_i_54_n_0 ),
        .O(\sample[0]_INST_0_i_45_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFF4700)) 
    \sample[0]_INST_0_i_46 
       (.I0(\sample[0]_INST_0_i_55_n_0 ),
        .I1(uniform[59]),
        .I2(\sample[0]_INST_0_i_56_n_0 ),
        .I3(\sample[0]_INST_0_i_57_n_0 ),
        .I4(\sample[0]_INST_0_i_58_n_0 ),
        .I5(\sample[0]_INST_0_i_59_n_0 ),
        .O(\sample[0]_INST_0_i_46_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair65" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[0]_INST_0_i_47 
       (.I0(uniform[55]),
        .I1(uniform[56]),
        .O(\sample[0]_INST_0_i_47_n_0 ));
  LUT6 #(
    .INIT(64'h000000000000EAEE)) 
    \sample[0]_INST_0_i_48 
       (.I0(\sample[0]_INST_0_i_60_n_0 ),
        .I1(\sample[0]_INST_0_i_61_n_0 ),
        .I2(\sample[0]_INST_0_i_62_n_0 ),
        .I3(\sample[0]_INST_0_i_63_n_0 ),
        .I4(\sample[0]_INST_0_i_64_n_0 ),
        .I5(\sample[0]_INST_0_i_65_n_0 ),
        .O(\sample[0]_INST_0_i_48_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair4" *) 
  LUT5 #(
    .INIT(32'h1FFFFFFF)) 
    \sample[0]_INST_0_i_49 
       (.I0(\sample[0]_INST_0_i_59_n_0 ),
        .I1(uniform[53]),
        .I2(uniform[50]),
        .I3(uniform[51]),
        .I4(uniform[52]),
        .O(\sample[0]_INST_0_i_49_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair34" *) 
  LUT5 #(
    .INIT(32'h1577FFFF)) 
    \sample[0]_INST_0_i_5 
       (.I0(uniform[4]),
        .I1(uniform[3]),
        .I2(uniform[5]),
        .I3(uniform[2]),
        .I4(uniform[0]),
        .O(\sample[0]_INST_0_i_5_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair40" *) 
  LUT4 #(
    .INIT(16'h7FFF)) 
    \sample[0]_INST_0_i_50 
       (.I0(uniform[48]),
        .I1(uniform[47]),
        .I2(uniform[45]),
        .I3(uniform[46]),
        .O(\sample[0]_INST_0_i_50_n_0 ));
  LUT6 #(
    .INIT(64'h08000A008A00808A)) 
    \sample[0]_INST_0_i_51 
       (.I0(uniform[46]),
        .I1(uniform[51]),
        .I2(uniform[47]),
        .I3(uniform[49]),
        .I4(uniform[50]),
        .I5(uniform[48]),
        .O(\sample[0]_INST_0_i_51_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF01FFFFFF)) 
    \sample[0]_INST_0_i_52 
       (.I0(uniform[42]),
        .I1(uniform[43]),
        .I2(uniform[45]),
        .I3(uniform[40]),
        .I4(uniform[41]),
        .I5(uniform[44]),
        .O(\sample[0]_INST_0_i_52_n_0 ));
  LUT6 #(
    .INIT(64'hDFFFFFFF7F00FFF0)) 
    \sample[0]_INST_0_i_53 
       (.I0(uniform[55]),
        .I1(uniform[54]),
        .I2(uniform[51]),
        .I3(uniform[50]),
        .I4(uniform[49]),
        .I5(uniform[53]),
        .O(\sample[0]_INST_0_i_53_n_0 ));
  LUT6 #(
    .INIT(64'h3A3B0A3B3A0A3A0A)) 
    \sample[0]_INST_0_i_54 
       (.I0(uniform[52]),
        .I1(uniform[51]),
        .I2(uniform[49]),
        .I3(uniform[50]),
        .I4(uniform[54]),
        .I5(uniform[53]),
        .O(\sample[0]_INST_0_i_54_n_0 ));
  LUT6 #(
    .INIT(64'hAFBB00BBAFBB0000)) 
    \sample[0]_INST_0_i_55 
       (.I0(\sample[0]_INST_0_i_66_n_0 ),
        .I1(uniform[63]),
        .I2(uniform[62]),
        .I3(uniform[61]),
        .I4(uniform[57]),
        .I5(uniform[54]),
        .O(\sample[0]_INST_0_i_55_n_0 ));
  LUT6 #(
    .INIT(64'h6FF0FFF0EFF0FFF0)) 
    \sample[0]_INST_0_i_56 
       (.I0(uniform[61]),
        .I1(uniform[62]),
        .I2(uniform[54]),
        .I3(uniform[57]),
        .I4(uniform[60]),
        .I5(uniform[63]),
        .O(\sample[0]_INST_0_i_56_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair56" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \sample[0]_INST_0_i_57 
       (.I0(uniform[55]),
        .I1(uniform[58]),
        .O(\sample[0]_INST_0_i_57_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFFAAEA)) 
    \sample[0]_INST_0_i_58 
       (.I0(\sample[0]_INST_0_i_67_n_0 ),
        .I1(\sample[0]_INST_0_i_68_n_0 ),
        .I2(\sample[1]_INST_0_i_74_n_0 ),
        .I3(\sample[0]_INST_0_i_69_n_0 ),
        .I4(\sample[0]_INST_0_i_70_n_0 ),
        .I5(\sample[0]_INST_0_i_71_n_0 ),
        .O(\sample[0]_INST_0_i_58_n_0 ));
  LUT6 #(
    .INIT(64'h0700050300005557)) 
    \sample[0]_INST_0_i_59 
       (.I0(uniform[53]),
        .I1(\sample[0]_INST_0_i_72_n_0 ),
        .I2(uniform[56]),
        .I3(uniform[57]),
        .I4(uniform[54]),
        .I5(uniform[55]),
        .O(\sample[0]_INST_0_i_59_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair34" *) 
  LUT4 #(
    .INIT(16'h6200)) 
    \sample[0]_INST_0_i_6 
       (.I0(uniform[4]),
        .I1(uniform[3]),
        .I2(uniform[5]),
        .I3(uniform[2]),
        .O(\sample[0]_INST_0_i_6_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair6" *) 
  LUT3 #(
    .INIT(8'h7F)) 
    \sample[0]_INST_0_i_60 
       (.I0(uniform[58]),
        .I1(uniform[59]),
        .I2(uniform[57]),
        .O(\sample[0]_INST_0_i_60_n_0 ));
  LUT6 #(
    .INIT(64'h6EEEFFFF6EEE6EEE)) 
    \sample[0]_INST_0_i_61 
       (.I0(uniform[64]),
        .I1(\sample[1]_INST_0_i_72_n_0 ),
        .I2(\sample[0]_INST_0_i_73_n_0 ),
        .I3(uniform[60]),
        .I4(\sample[0]_INST_0_i_74_n_0 ),
        .I5(uniform[61]),
        .O(\sample[0]_INST_0_i_61_n_0 ));
  LUT6 #(
    .INIT(64'h00000000FFFF7077)) 
    \sample[0]_INST_0_i_62 
       (.I0(\sample[0]_INST_0_i_75_n_0 ),
        .I1(\sample[0]_INST_0_i_76_n_0 ),
        .I2(\sample[0]_INST_0_i_77_n_0 ),
        .I3(\sample[0]_INST_0_i_78_n_0 ),
        .I4(\sample[0]_INST_0_i_73_n_0 ),
        .I5(\sample[0]_INST_0_i_79_n_0 ),
        .O(\sample[0]_INST_0_i_62_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair63" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \sample[0]_INST_0_i_63 
       (.I0(uniform[62]),
        .I1(uniform[61]),
        .O(\sample[0]_INST_0_i_63_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF00000411)) 
    \sample[0]_INST_0_i_64 
       (.I0(\sample[0]_INST_0_i_80_n_0 ),
        .I1(uniform[63]),
        .I2(uniform[66]),
        .I3(\sample[0]_INST_0_i_81_n_0 ),
        .I4(uniform[62]),
        .I5(\sample[0]_INST_0_i_82_n_0 ),
        .O(\sample[0]_INST_0_i_64_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair9" *) 
  LUT5 #(
    .INIT(32'h00002208)) 
    \sample[0]_INST_0_i_65 
       (.I0(uniform[58]),
        .I1(uniform[57]),
        .I2(uniform[62]),
        .I3(uniform[60]),
        .I4(uniform[59]),
        .O(\sample[0]_INST_0_i_65_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair0" *) 
  LUT5 #(
    .INIT(32'hFFFF4FFF)) 
    \sample[0]_INST_0_i_66 
       (.I0(uniform[63]),
        .I1(uniform[64]),
        .I2(uniform[54]),
        .I3(uniform[57]),
        .I4(uniform[60]),
        .O(\sample[0]_INST_0_i_66_n_0 ));
  LUT6 #(
    .INIT(64'h000000B000F00000)) 
    \sample[0]_INST_0_i_67 
       (.I0(uniform[59]),
        .I1(uniform[57]),
        .I2(uniform[54]),
        .I3(uniform[55]),
        .I4(uniform[58]),
        .I5(uniform[56]),
        .O(\sample[0]_INST_0_i_67_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair9" *) 
  LUT3 #(
    .INIT(8'hA8)) 
    \sample[0]_INST_0_i_68 
       (.I0(uniform[57]),
        .I1(uniform[62]),
        .I2(uniform[60]),
        .O(\sample[0]_INST_0_i_68_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair37" *) 
  LUT4 #(
    .INIT(16'hFF7F)) 
    \sample[0]_INST_0_i_69 
       (.I0(uniform[59]),
        .I1(uniform[56]),
        .I2(uniform[61]),
        .I3(uniform[58]),
        .O(\sample[0]_INST_0_i_69_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair23" *) 
  LUT5 #(
    .INIT(32'h7F7F7FFF)) 
    \sample[0]_INST_0_i_7 
       (.I0(uniform[12]),
        .I1(uniform[10]),
        .I2(uniform[13]),
        .I3(uniform[16]),
        .I4(\sample[0]_INST_0_i_13_n_0 ),
        .O(\sample[0]_INST_0_i_7_n_0 ));
  LUT6 #(
    .INIT(64'h00010000FF000000)) 
    \sample[0]_INST_0_i_70 
       (.I0(uniform[58]),
        .I1(uniform[59]),
        .I2(uniform[60]),
        .I3(uniform[57]),
        .I4(uniform[56]),
        .I5(uniform[54]),
        .O(\sample[0]_INST_0_i_70_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair6" *) 
  LUT5 #(
    .INIT(32'h10011000)) 
    \sample[0]_INST_0_i_71 
       (.I0(uniform[56]),
        .I1(uniform[57]),
        .I2(uniform[58]),
        .I3(uniform[59]),
        .I4(uniform[55]),
        .O(\sample[0]_INST_0_i_71_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair8" *) 
  LUT4 #(
    .INIT(16'h802A)) 
    \sample[0]_INST_0_i_72 
       (.I0(uniform[57]),
        .I1(uniform[58]),
        .I2(uniform[60]),
        .I3(uniform[59]),
        .O(\sample[0]_INST_0_i_72_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair64" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[0]_INST_0_i_73 
       (.I0(uniform[63]),
        .I1(uniform[65]),
        .O(\sample[0]_INST_0_i_73_n_0 ));
  LUT6 #(
    .INIT(64'hFC00A0000C00F000)) 
    \sample[0]_INST_0_i_74 
       (.I0(uniform[67]),
        .I1(uniform[65]),
        .I2(uniform[63]),
        .I3(uniform[62]),
        .I4(uniform[66]),
        .I5(uniform[68]),
        .O(\sample[0]_INST_0_i_74_n_0 ));
  LUT5 #(
    .INIT(32'hD5000AA0)) 
    \sample[0]_INST_0_i_75 
       (.I0(uniform[66]),
        .I1(uniform[71]),
        .I2(uniform[70]),
        .I3(uniform[67]),
        .I4(uniform[69]),
        .O(\sample[0]_INST_0_i_75_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair3" *) 
  LUT2 #(
    .INIT(4'h2)) 
    \sample[0]_INST_0_i_76 
       (.I0(uniform[64]),
        .I1(uniform[68]),
        .O(\sample[0]_INST_0_i_76_n_0 ));
  LUT5 #(
    .INIT(32'h3F3FFF7F)) 
    \sample[0]_INST_0_i_77 
       (.I0(uniform[64]),
        .I1(uniform[66]),
        .I2(uniform[68]),
        .I3(uniform[70]),
        .I4(uniform[67]),
        .O(\sample[0]_INST_0_i_77_n_0 ));
  LUT5 #(
    .INIT(32'h64FFFFFF)) 
    \sample[0]_INST_0_i_78 
       (.I0(uniform[69]),
        .I1(uniform[71]),
        .I2(uniform[70]),
        .I3(uniform[67]),
        .I4(uniform[64]),
        .O(\sample[0]_INST_0_i_78_n_0 ));
  LUT6 #(
    .INIT(64'h003C2003000C000C)) 
    \sample[0]_INST_0_i_79 
       (.I0(uniform[69]),
        .I1(uniform[66]),
        .I2(uniform[65]),
        .I3(uniform[64]),
        .I4(uniform[67]),
        .I5(uniform[63]),
        .O(\sample[0]_INST_0_i_79_n_0 ));
  LUT6 #(
    .INIT(64'hF1FFF1FFF1FFFFFF)) 
    \sample[0]_INST_0_i_8 
       (.I0(\sample[0]_INST_0_i_14_n_0 ),
        .I1(uniform[22]),
        .I2(\sample[1]_INST_0_i_11_n_0 ),
        .I3(uniform[20]),
        .I4(uniform[21]),
        .I5(\sample[0]_INST_0_i_15_n_0 ),
        .O(\sample[0]_INST_0_i_8_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair35" *) 
  LUT4 #(
    .INIT(16'h7FFF)) 
    \sample[0]_INST_0_i_80 
       (.I0(uniform[61]),
        .I1(uniform[60]),
        .I2(uniform[59]),
        .I3(uniform[57]),
        .O(\sample[0]_INST_0_i_80_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair31" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \sample[0]_INST_0_i_81 
       (.I0(uniform[64]),
        .I1(uniform[65]),
        .O(\sample[0]_INST_0_i_81_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair8" *) 
  LUT5 #(
    .INIT(32'h02020200)) 
    \sample[0]_INST_0_i_82 
       (.I0(uniform[57]),
        .I1(uniform[59]),
        .I2(uniform[58]),
        .I3(uniform[61]),
        .I4(uniform[60]),
        .O(\sample[0]_INST_0_i_82_n_0 ));
  LUT6 #(
    .INIT(64'h88888888A8A8A8AA)) 
    \sample[0]_INST_0_i_9 
       (.I0(uniform[23]),
        .I1(\sample[0]_INST_0_i_16_n_0 ),
        .I2(\sample[0]_INST_0_i_17_n_0 ),
        .I3(\sample[0]_INST_0_i_18_n_0 ),
        .I4(\sample[0]_INST_0_i_19_n_0 ),
        .I5(\sample[0]_INST_0_i_20_n_0 ),
        .O(\sample[0]_INST_0_i_9_n_0 ));
  LUT6 #(
    .INIT(64'h55550111FFFFFFFF)) 
    \sample[1]_INST_0 
       (.I0(\sample[1]_INST_0_i_1_n_0 ),
        .I1(\sample[1]_INST_0_i_2_n_0 ),
        .I2(\sample[1]_INST_0_i_3_n_0 ),
        .I3(\sample[1]_INST_0_i_4_n_0 ),
        .I4(\sample[1]_INST_0_i_5_n_0 ),
        .I5(\sample[4]_INST_0_i_6_n_0 ),
        .O(sample[1]));
  LUT6 #(
    .INIT(64'h15FF0000FFFFFFFF)) 
    \sample[1]_INST_0_i_1 
       (.I0(uniform[5]),
        .I1(uniform[4]),
        .I2(\sample[1]_INST_0_i_6_n_0 ),
        .I3(uniform[2]),
        .I4(uniform[1]),
        .I5(uniform[0]),
        .O(\sample[1]_INST_0_i_1_n_0 ));
  LUT6 #(
    .INIT(64'h00000000AAAAEEFE)) 
    \sample[1]_INST_0_i_10 
       (.I0(\sample[1]_INST_0_i_16_n_0 ),
        .I1(\sample[1]_INST_0_i_17_n_0 ),
        .I2(\sample[1]_INST_0_i_18_n_0 ),
        .I3(\sample[1]_INST_0_i_19_n_0 ),
        .I4(\sample[1]_INST_0_i_20_n_0 ),
        .I5(\sample[1]_INST_0_i_21_n_0 ),
        .O(\sample[1]_INST_0_i_10_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair20" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[1]_INST_0_i_11 
       (.I0(uniform[17]),
        .I1(uniform[18]),
        .O(\sample[1]_INST_0_i_11_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair24" *) 
  LUT5 #(
    .INIT(32'h32FFFFFF)) 
    \sample[1]_INST_0_i_12 
       (.I0(uniform[18]),
        .I1(uniform[16]),
        .I2(uniform[17]),
        .I3(uniform[14]),
        .I4(uniform[15]),
        .O(\sample[1]_INST_0_i_12_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair53" *) 
  LUT4 #(
    .INIT(16'h7737)) 
    \sample[1]_INST_0_i_13 
       (.I0(uniform[6]),
        .I1(uniform[3]),
        .I2(uniform[4]),
        .I3(uniform[7]),
        .O(\sample[1]_INST_0_i_13_n_0 ));
  LUT6 #(
    .INIT(64'h00D5FFFFFFFFFFFF)) 
    \sample[1]_INST_0_i_14 
       (.I0(uniform[8]),
        .I1(uniform[12]),
        .I2(uniform[9]),
        .I3(uniform[10]),
        .I4(uniform[7]),
        .I5(uniform[4]),
        .O(\sample[1]_INST_0_i_14_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair21" *) 
  LUT5 #(
    .INIT(32'h080C0C00)) 
    \sample[1]_INST_0_i_15 
       (.I0(uniform[22]),
        .I1(uniform[17]),
        .I2(uniform[19]),
        .I3(uniform[20]),
        .I4(uniform[21]),
        .O(\sample[1]_INST_0_i_15_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair22" *) 
  LUT5 #(
    .INIT(32'h54FFFFFF)) 
    \sample[1]_INST_0_i_16 
       (.I0(uniform[21]),
        .I1(uniform[22]),
        .I2(uniform[24]),
        .I3(uniform[20]),
        .I4(uniform[23]),
        .O(\sample[1]_INST_0_i_16_n_0 ));
  LUT6 #(
    .INIT(64'h0F0B000FFFFFFFFF)) 
    \sample[1]_INST_0_i_17 
       (.I0(uniform[27]),
        .I1(uniform[26]),
        .I2(uniform[22]),
        .I3(uniform[24]),
        .I4(uniform[25]),
        .I5(uniform[19]),
        .O(\sample[1]_INST_0_i_17_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF55551110)) 
    \sample[1]_INST_0_i_18 
       (.I0(\sample[1]_INST_0_i_22_n_0 ),
        .I1(\sample[1]_INST_0_i_23_n_0 ),
        .I2(\sample[1]_INST_0_i_24_n_0 ),
        .I3(\sample[1]_INST_0_i_25_n_0 ),
        .I4(\sample[1]_INST_0_i_26_n_0 ),
        .I5(\sample[1]_INST_0_i_27_n_0 ),
        .O(\sample[1]_INST_0_i_18_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF10005555)) 
    \sample[1]_INST_0_i_19 
       (.I0(\sample[1]_INST_0_i_28_n_0 ),
        .I1(\sample[1]_INST_0_i_29_n_0 ),
        .I2(uniform[28]),
        .I3(uniform[32]),
        .I4(uniform[29]),
        .I5(\sample[1]_INST_0_i_30_n_0 ),
        .O(\sample[1]_INST_0_i_19_n_0 ));
  LUT5 #(
    .INIT(32'hFFFF0884)) 
    \sample[1]_INST_0_i_2 
       (.I0(uniform[13]),
        .I1(uniform[9]),
        .I2(uniform[11]),
        .I3(uniform[12]),
        .I4(\sample[1]_INST_0_i_7_n_0 ),
        .O(\sample[1]_INST_0_i_2_n_0 ));
  LUT5 #(
    .INIT(32'h000000D5)) 
    \sample[1]_INST_0_i_20 
       (.I0(uniform[21]),
        .I1(uniform[19]),
        .I2(uniform[25]),
        .I3(uniform[24]),
        .I4(uniform[22]),
        .O(\sample[1]_INST_0_i_20_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair49" *) 
  LUT4 #(
    .INIT(16'hFF04)) 
    \sample[1]_INST_0_i_21 
       (.I0(uniform[23]),
        .I1(uniform[21]),
        .I2(uniform[20]),
        .I3(\sample[1]_INST_0_i_31_n_0 ),
        .O(\sample[1]_INST_0_i_21_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair10" *) 
  LUT5 #(
    .INIT(32'hFFFF4000)) 
    \sample[1]_INST_0_i_22 
       (.I0(\sample[1]_INST_0_i_32_n_0 ),
        .I1(uniform[30]),
        .I2(uniform[33]),
        .I3(uniform[31]),
        .I4(\sample[1]_INST_0_i_33_n_0 ),
        .O(\sample[1]_INST_0_i_22_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair15" *) 
  LUT5 #(
    .INIT(32'hE2222222)) 
    \sample[1]_INST_0_i_23 
       (.I0(uniform[35]),
        .I1(uniform[32]),
        .I2(uniform[36]),
        .I3(uniform[33]),
        .I4(\sample[1]_INST_0_i_34_n_0 ),
        .O(\sample[1]_INST_0_i_23_n_0 ));
  LUT6 #(
    .INIT(64'h00000000FFFF005D)) 
    \sample[1]_INST_0_i_24 
       (.I0(\sample[1]_INST_0_i_35_n_0 ),
        .I1(\sample[1]_INST_0_i_36_n_0 ),
        .I2(\sample[1]_INST_0_i_37_n_0 ),
        .I3(\sample[1]_INST_0_i_38_n_0 ),
        .I4(\sample[1]_INST_0_i_39_n_0 ),
        .I5(\sample[1]_INST_0_i_40_n_0 ),
        .O(\sample[1]_INST_0_i_24_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair46" *) 
  LUT4 #(
    .INIT(16'h7FFF)) 
    \sample[1]_INST_0_i_25 
       (.I0(uniform[33]),
        .I1(uniform[36]),
        .I2(uniform[32]),
        .I3(uniform[38]),
        .O(\sample[1]_INST_0_i_25_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair60" *) 
  LUT3 #(
    .INIT(8'h7F)) 
    \sample[1]_INST_0_i_26 
       (.I0(uniform[34]),
        .I1(uniform[30]),
        .I2(uniform[31]),
        .O(\sample[1]_INST_0_i_26_n_0 ));
  LUT6 #(
    .INIT(64'h454FFFFFFFFFFFFF)) 
    \sample[1]_INST_0_i_27 
       (.I0(uniform[28]),
        .I1(uniform[31]),
        .I2(uniform[26]),
        .I3(uniform[25]),
        .I4(\sample[2]_INST_0_i_25_n_0 ),
        .I5(uniform[29]),
        .O(\sample[1]_INST_0_i_27_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFEFFF0FFFEFFF)) 
    \sample[1]_INST_0_i_28 
       (.I0(uniform[28]),
        .I1(uniform[29]),
        .I2(uniform[25]),
        .I3(uniform[24]),
        .I4(uniform[26]),
        .I5(uniform[30]),
        .O(\sample[1]_INST_0_i_28_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair10" *) 
  LUT2 #(
    .INIT(4'h1)) 
    \sample[1]_INST_0_i_29 
       (.I0(uniform[30]),
        .I1(uniform[33]),
        .O(\sample[1]_INST_0_i_29_n_0 ));
  LUT6 #(
    .INIT(64'h55551110FFFFFFFF)) 
    \sample[1]_INST_0_i_3 
       (.I0(\sample[1]_INST_0_i_8_n_0 ),
        .I1(\sample[1]_INST_0_i_9_n_0 ),
        .I2(\sample[1]_INST_0_i_10_n_0 ),
        .I3(\sample[1]_INST_0_i_11_n_0 ),
        .I4(\sample[1]_INST_0_i_12_n_0 ),
        .I5(uniform[9]),
        .O(\sample[1]_INST_0_i_3_n_0 ));
  LUT6 #(
    .INIT(64'hAAAFAAAAFFBFBABA)) 
    \sample[1]_INST_0_i_30 
       (.I0(\sample[1]_INST_0_i_41_n_0 ),
        .I1(uniform[22]),
        .I2(uniform[24]),
        .I3(uniform[27]),
        .I4(uniform[26]),
        .I5(uniform[25]),
        .O(\sample[1]_INST_0_i_30_n_0 ));
  LUT6 #(
    .INIT(64'h000000009F3F00F0)) 
    \sample[1]_INST_0_i_31 
       (.I0(uniform[26]),
        .I1(uniform[25]),
        .I2(uniform[21]),
        .I3(uniform[24]),
        .I4(uniform[22]),
        .I5(\sample[1]_INST_0_i_42_n_0 ),
        .O(\sample[1]_INST_0_i_31_n_0 ));
  LUT6 #(
    .INIT(64'hAEBE0000EBEBFFFF)) 
    \sample[1]_INST_0_i_32 
       (.I0(uniform[36]),
        .I1(uniform[38]),
        .I2(uniform[37]),
        .I3(uniform[39]),
        .I4(uniform[32]),
        .I5(uniform[35]),
        .O(\sample[1]_INST_0_i_32_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair11" *) 
  LUT5 #(
    .INIT(32'hFBAAAAAA)) 
    \sample[1]_INST_0_i_33 
       (.I0(\sample[1]_INST_0_i_43_n_0 ),
        .I1(uniform[26]),
        .I2(\sample[1]_INST_0_i_44_n_0 ),
        .I3(uniform[25]),
        .I4(uniform[28]),
        .O(\sample[1]_INST_0_i_33_n_0 ));
  LUT6 #(
    .INIT(64'h00404000307030F0)) 
    \sample[1]_INST_0_i_34 
       (.I0(uniform[38]),
        .I1(uniform[37]),
        .I2(uniform[35]),
        .I3(uniform[40]),
        .I4(uniform[41]),
        .I5(uniform[39]),
        .O(\sample[1]_INST_0_i_34_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair67" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \sample[1]_INST_0_i_35 
       (.I0(uniform[42]),
        .I1(uniform[43]),
        .O(\sample[1]_INST_0_i_35_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF55551110)) 
    \sample[1]_INST_0_i_36 
       (.I0(\sample[1]_INST_0_i_45_n_0 ),
        .I1(\sample[1]_INST_0_i_46_n_0 ),
        .I2(\sample[4]_INST_0_i_26_n_0 ),
        .I3(\sample[1]_INST_0_i_47_n_0 ),
        .I4(\sample[1]_INST_0_i_48_n_0 ),
        .I5(\sample[1]_INST_0_i_49_n_0 ),
        .O(\sample[1]_INST_0_i_36_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFFABAEABEF)) 
    \sample[1]_INST_0_i_37 
       (.I0(\sample[1]_INST_0_i_50_n_0 ),
        .I1(uniform[47]),
        .I2(uniform[44]),
        .I3(uniform[45]),
        .I4(uniform[46]),
        .I5(\sample[1]_INST_0_i_51_n_0 ),
        .O(\sample[1]_INST_0_i_37_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF55750000)) 
    \sample[1]_INST_0_i_38 
       (.I0(uniform[39]),
        .I1(\sample[1]_INST_0_i_52_n_0 ),
        .I2(uniform[48]),
        .I3(uniform[47]),
        .I4(uniform[42]),
        .I5(\sample[1]_INST_0_i_53_n_0 ),
        .O(\sample[1]_INST_0_i_38_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair48" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[1]_INST_0_i_39 
       (.I0(uniform[40]),
        .I1(uniform[41]),
        .O(\sample[1]_INST_0_i_39_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair27" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \sample[1]_INST_0_i_4 
       (.I0(uniform[11]),
        .I1(uniform[12]),
        .O(\sample[1]_INST_0_i_4_n_0 ));
  LUT5 #(
    .INIT(32'hFFFF40FF)) 
    \sample[1]_INST_0_i_40 
       (.I0(\sample[1]_INST_0_i_54_n_0 ),
        .I1(uniform[39]),
        .I2(uniform[40]),
        .I3(uniform[35]),
        .I4(\sample[1]_INST_0_i_55_n_0 ),
        .O(\sample[1]_INST_0_i_40_n_0 ));
  LUT6 #(
    .INIT(64'hAAABAAAAAAAAAAAA)) 
    \sample[1]_INST_0_i_41 
       (.I0(\sample[1]_INST_0_i_56_n_0 ),
        .I1(uniform[27]),
        .I2(uniform[26]),
        .I3(uniform[28]),
        .I4(uniform[25]),
        .I5(uniform[24]),
        .O(\sample[1]_INST_0_i_41_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair25" *) 
  LUT2 #(
    .INIT(4'hB)) 
    \sample[1]_INST_0_i_42 
       (.I0(uniform[23]),
        .I1(uniform[19]),
        .O(\sample[1]_INST_0_i_42_n_0 ));
  LUT6 #(
    .INIT(64'h0000000070FF7070)) 
    \sample[1]_INST_0_i_43 
       (.I0(uniform[33]),
        .I1(uniform[34]),
        .I2(uniform[32]),
        .I3(uniform[28]),
        .I4(uniform[26]),
        .I5(uniform[31]),
        .O(\sample[1]_INST_0_i_43_n_0 ));
  LUT6 #(
    .INIT(64'h1000D00010000000)) 
    \sample[1]_INST_0_i_44 
       (.I0(uniform[34]),
        .I1(uniform[36]),
        .I2(uniform[30]),
        .I3(uniform[32]),
        .I4(uniform[33]),
        .I5(uniform[35]),
        .O(\sample[1]_INST_0_i_44_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF00001441)) 
    \sample[1]_INST_0_i_45 
       (.I0(\sample[4]_INST_0_i_29_n_0 ),
        .I1(uniform[49]),
        .I2(uniform[50]),
        .I3(uniform[51]),
        .I4(uniform[48]),
        .I5(\sample[1]_INST_0_i_57_n_0 ),
        .O(\sample[1]_INST_0_i_45_n_0 ));
  LUT5 #(
    .INIT(32'h444F4F4F)) 
    \sample[1]_INST_0_i_46 
       (.I0(uniform[51]),
        .I1(\sample[1]_INST_0_i_58_n_0 ),
        .I2(\sample[1]_INST_0_i_59_n_0 ),
        .I3(\sample[1]_INST_0_i_60_n_0 ),
        .I4(\sample[1]_INST_0_i_61_n_0 ),
        .O(\sample[1]_INST_0_i_46_n_0 ));
  LUT6 #(
    .INIT(64'h00000000AAAAEEFE)) 
    \sample[1]_INST_0_i_47 
       (.I0(\sample[1]_INST_0_i_62_n_0 ),
        .I1(\sample[1]_INST_0_i_63_n_0 ),
        .I2(\sample[1]_INST_0_i_64_n_0 ),
        .I3(\sample[1]_INST_0_i_65_n_0 ),
        .I4(\sample[1]_INST_0_i_66_n_0 ),
        .I5(\sample[1]_INST_0_i_67_n_0 ),
        .O(\sample[1]_INST_0_i_47_n_0 ));
  LUT6 #(
    .INIT(64'hAAAAAAAAFFBEEABE)) 
    \sample[1]_INST_0_i_48 
       (.I0(\sample[4]_INST_0_i_29_n_0 ),
        .I1(uniform[52]),
        .I2(uniform[53]),
        .I3(uniform[50]),
        .I4(uniform[54]),
        .I5(uniform[51]),
        .O(\sample[1]_INST_0_i_48_n_0 ));
  LUT6 #(
    .INIT(64'h0111FFFFFFFFFFFF)) 
    \sample[1]_INST_0_i_49 
       (.I0(\sample[1]_INST_0_i_68_n_0 ),
        .I1(\sample[1]_INST_0_i_57_n_0 ),
        .I2(uniform[48]),
        .I3(uniform[49]),
        .I4(uniform[47]),
        .I5(uniform[44]),
        .O(\sample[1]_INST_0_i_49_n_0 ));
  LUT6 #(
    .INIT(64'h55D5FFFF55D555D5)) 
    \sample[1]_INST_0_i_5 
       (.I0(uniform[1]),
        .I1(\sample[1]_INST_0_i_6_n_0 ),
        .I2(uniform[4]),
        .I3(uniform[5]),
        .I4(\sample[1]_INST_0_i_13_n_0 ),
        .I5(\sample[1]_INST_0_i_14_n_0 ),
        .O(\sample[1]_INST_0_i_5_n_0 ));
  LUT6 #(
    .INIT(64'h4FCF000000000000)) 
    \sample[1]_INST_0_i_50 
       (.I0(uniform[49]),
        .I1(uniform[50]),
        .I2(uniform[46]),
        .I3(uniform[51]),
        .I4(\sample[1]_INST_0_i_69_n_0 ),
        .I5(uniform[48]),
        .O(\sample[1]_INST_0_i_50_n_0 ));
  LUT6 #(
    .INIT(64'h0000011111000111)) 
    \sample[1]_INST_0_i_51 
       (.I0(uniform[48]),
        .I1(uniform[47]),
        .I2(uniform[49]),
        .I3(uniform[45]),
        .I4(uniform[46]),
        .I5(uniform[50]),
        .O(\sample[1]_INST_0_i_51_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair59" *) 
  LUT3 #(
    .INIT(8'hDF)) 
    \sample[1]_INST_0_i_52 
       (.I0(uniform[44]),
        .I1(uniform[45]),
        .I2(uniform[46]),
        .O(\sample[1]_INST_0_i_52_n_0 ));
  LUT6 #(
    .INIT(64'h22220E02000C0202)) 
    \sample[1]_INST_0_i_53 
       (.I0(uniform[39]),
        .I1(uniform[42]),
        .I2(uniform[43]),
        .I3(uniform[46]),
        .I4(uniform[45]),
        .I5(uniform[44]),
        .O(\sample[1]_INST_0_i_53_n_0 ));
  LUT6 #(
    .INIT(64'hAAAAAA8AAA82AA82)) 
    \sample[1]_INST_0_i_54 
       (.I0(uniform[37]),
        .I1(uniform[42]),
        .I2(uniform[43]),
        .I3(uniform[44]),
        .I4(uniform[45]),
        .I5(uniform[41]),
        .O(\sample[1]_INST_0_i_54_n_0 ));
  LUT6 #(
    .INIT(64'h0800000000000000)) 
    \sample[1]_INST_0_i_55 
       (.I0(uniform[39]),
        .I1(uniform[42]),
        .I2(uniform[40]),
        .I3(uniform[41]),
        .I4(uniform[43]),
        .I5(uniform[37]),
        .O(\sample[1]_INST_0_i_55_n_0 ));
  LUT6 #(
    .INIT(64'h000000001D000000)) 
    \sample[1]_INST_0_i_56 
       (.I0(uniform[29]),
        .I1(uniform[28]),
        .I2(uniform[30]),
        .I3(uniform[25]),
        .I4(uniform[26]),
        .I5(uniform[27]),
        .O(\sample[1]_INST_0_i_56_n_0 ));
  LUT6 #(
    .INIT(64'h000000001F9F0000)) 
    \sample[1]_INST_0_i_57 
       (.I0(uniform[52]),
        .I1(uniform[51]),
        .I2(uniform[46]),
        .I3(uniform[50]),
        .I4(uniform[45]),
        .I5(\sample[1]_INST_0_i_70_n_0 ),
        .O(\sample[1]_INST_0_i_57_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair39" *) 
  LUT4 #(
    .INIT(16'h0979)) 
    \sample[1]_INST_0_i_58 
       (.I0(uniform[52]),
        .I1(uniform[53]),
        .I2(uniform[50]),
        .I3(uniform[54]),
        .O(\sample[1]_INST_0_i_58_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair39" *) 
  LUT4 #(
    .INIT(16'hCA75)) 
    \sample[1]_INST_0_i_59 
       (.I0(uniform[52]),
        .I1(uniform[55]),
        .I2(uniform[50]),
        .I3(uniform[53]),
        .O(\sample[1]_INST_0_i_59_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair53" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[1]_INST_0_i_6 
       (.I0(uniform[3]),
        .I1(uniform[6]),
        .O(\sample[1]_INST_0_i_6_n_0 ));
  LUT6 #(
    .INIT(64'h77777777FF7F7FFF)) 
    \sample[1]_INST_0_i_60 
       (.I0(uniform[57]),
        .I1(uniform[52]),
        .I2(uniform[54]),
        .I3(\sample[2]_INST_0_i_53_n_0 ),
        .I4(uniform[58]),
        .I5(uniform[55]),
        .O(\sample[1]_INST_0_i_60_n_0 ));
  LUT6 #(
    .INIT(64'hAAAA0000EFAA0000)) 
    \sample[1]_INST_0_i_61 
       (.I0(uniform[54]),
        .I1(uniform[57]),
        .I2(uniform[56]),
        .I3(uniform[52]),
        .I4(uniform[50]),
        .I5(uniform[55]),
        .O(\sample[1]_INST_0_i_61_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF0000CCC4)) 
    \sample[1]_INST_0_i_62 
       (.I0(\sample[1]_INST_0_i_71_n_0 ),
        .I1(uniform[57]),
        .I2(uniform[59]),
        .I3(\sample[1]_INST_0_i_72_n_0 ),
        .I4(uniform[56]),
        .I5(\sample[1]_INST_0_i_73_n_0 ),
        .O(\sample[1]_INST_0_i_62_n_0 ));
  LUT6 #(
    .INIT(64'h00A20000FFFFFFFF)) 
    \sample[1]_INST_0_i_63 
       (.I0(uniform[54]),
        .I1(\sample[1]_INST_0_i_74_n_0 ),
        .I2(uniform[61]),
        .I3(uniform[59]),
        .I4(\sample[1]_INST_0_i_75_n_0 ),
        .I5(uniform[57]),
        .O(\sample[1]_INST_0_i_63_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF55555510)) 
    \sample[1]_INST_0_i_64 
       (.I0(\sample[1]_INST_0_i_76_n_0 ),
        .I1(\sample[1]_INST_0_i_77_n_0 ),
        .I2(uniform[65]),
        .I3(\sample[1]_INST_0_i_78_n_0 ),
        .I4(\sample[1]_INST_0_i_79_n_0 ),
        .I5(\sample[1]_INST_0_i_80_n_0 ),
        .O(\sample[1]_INST_0_i_64_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFFDFDFFFDF)) 
    \sample[1]_INST_0_i_65 
       (.I0(\sample[1]_INST_0_i_81_n_0 ),
        .I1(\sample[1]_INST_0_i_82_n_0 ),
        .I2(\sample[1]_INST_0_i_75_n_0 ),
        .I3(\sample[1]_INST_0_i_83_n_0 ),
        .I4(\sample[1]_INST_0_i_84_n_0 ),
        .I5(\sample[1]_INST_0_i_85_n_0 ),
        .O(\sample[1]_INST_0_i_65_n_0 ));
  LUT6 #(
    .INIT(64'h131313D313131313)) 
    \sample[1]_INST_0_i_66 
       (.I0(uniform[56]),
        .I1(uniform[57]),
        .I2(\sample[1]_INST_0_i_71_n_0 ),
        .I3(uniform[59]),
        .I4(uniform[62]),
        .I5(uniform[63]),
        .O(\sample[1]_INST_0_i_66_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF00800000)) 
    \sample[1]_INST_0_i_67 
       (.I0(uniform[54]),
        .I1(uniform[53]),
        .I2(uniform[52]),
        .I3(uniform[58]),
        .I4(\sample[1]_INST_0_i_86_n_0 ),
        .I5(\sample[1]_INST_0_i_87_n_0 ),
        .O(\sample[1]_INST_0_i_67_n_0 ));
  LUT6 #(
    .INIT(64'h1441000000000000)) 
    \sample[1]_INST_0_i_68 
       (.I0(uniform[48]),
        .I1(uniform[51]),
        .I2(uniform[50]),
        .I3(uniform[49]),
        .I4(uniform[46]),
        .I5(uniform[45]),
        .O(\sample[1]_INST_0_i_68_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair16" *) 
  LUT2 #(
    .INIT(4'h2)) 
    \sample[1]_INST_0_i_69 
       (.I0(uniform[45]),
        .I1(uniform[47]),
        .O(\sample[1]_INST_0_i_69_n_0 ));
  LUT6 #(
    .INIT(64'h0FBFFFFFFFFFFFFF)) 
    \sample[1]_INST_0_i_7 
       (.I0(uniform[7]),
        .I1(uniform[4]),
        .I2(uniform[3]),
        .I3(uniform[6]),
        .I4(uniform[10]),
        .I5(uniform[8]),
        .O(\sample[1]_INST_0_i_7_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair12" *) 
  LUT2 #(
    .INIT(4'hB)) 
    \sample[1]_INST_0_i_70 
       (.I0(uniform[49]),
        .I1(uniform[48]),
        .O(\sample[1]_INST_0_i_70_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair2" *) 
  LUT4 #(
    .INIT(16'hC4C0)) 
    \sample[1]_INST_0_i_71 
       (.I0(uniform[61]),
        .I1(uniform[54]),
        .I2(uniform[60]),
        .I3(uniform[59]),
        .O(\sample[1]_INST_0_i_71_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair36" *) 
  LUT2 #(
    .INIT(4'hB)) 
    \sample[1]_INST_0_i_72 
       (.I0(uniform[62]),
        .I1(uniform[63]),
        .O(\sample[1]_INST_0_i_72_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair56" *) 
  LUT3 #(
    .INIT(8'h7F)) 
    \sample[1]_INST_0_i_73 
       (.I0(uniform[58]),
        .I1(uniform[52]),
        .I2(uniform[53]),
        .O(\sample[1]_INST_0_i_73_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair62" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[1]_INST_0_i_74 
       (.I0(uniform[60]),
        .I1(uniform[62]),
        .O(\sample[1]_INST_0_i_74_n_0 ));
  LUT6 #(
    .INIT(64'hDFF5FFF5FFF5DFF5)) 
    \sample[1]_INST_0_i_75 
       (.I0(uniform[63]),
        .I1(uniform[62]),
        .I2(uniform[61]),
        .I3(uniform[60]),
        .I4(uniform[64]),
        .I5(uniform[65]),
        .O(\sample[1]_INST_0_i_75_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair5" *) 
  LUT3 #(
    .INIT(8'h08)) 
    \sample[1]_INST_0_i_76 
       (.I0(uniform[67]),
        .I1(uniform[65]),
        .I2(uniform[63]),
        .O(\sample[1]_INST_0_i_76_n_0 ));
  LUT6 #(
    .INIT(64'hB300A0FFBB08A0FF)) 
    \sample[1]_INST_0_i_77 
       (.I0(uniform[66]),
        .I1(uniform[67]),
        .I2(uniform[70]),
        .I3(uniform[69]),
        .I4(uniform[68]),
        .I5(uniform[71]),
        .O(\sample[1]_INST_0_i_77_n_0 ));
  LUT6 #(
    .INIT(64'h0000D500FFFFFFFF)) 
    \sample[1]_INST_0_i_78 
       (.I0(uniform[65]),
        .I1(uniform[71]),
        .I2(uniform[69]),
        .I3(uniform[67]),
        .I4(uniform[68]),
        .I5(uniform[63]),
        .O(\sample[1]_INST_0_i_78_n_0 ));
  LUT6 #(
    .INIT(64'h0000002008080828)) 
    \sample[1]_INST_0_i_79 
       (.I0(uniform[66]),
        .I1(uniform[67]),
        .I2(uniform[65]),
        .I3(uniform[70]),
        .I4(uniform[68]),
        .I5(uniform[69]),
        .O(\sample[1]_INST_0_i_79_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair30" *) 
  LUT5 #(
    .INIT(32'h26666222)) 
    \sample[1]_INST_0_i_8 
       (.I0(uniform[15]),
        .I1(uniform[13]),
        .I2(uniform[14]),
        .I3(uniform[17]),
        .I4(uniform[16]),
        .O(\sample[1]_INST_0_i_8_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair1" *) 
  LUT4 #(
    .INIT(16'h7FFF)) 
    \sample[1]_INST_0_i_80 
       (.I0(uniform[64]),
        .I1(uniform[60]),
        .I2(uniform[61]),
        .I3(uniform[62]),
        .O(\sample[1]_INST_0_i_80_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair1" *) 
  LUT5 #(
    .INIT(32'hFFFCEFFF)) 
    \sample[1]_INST_0_i_81 
       (.I0(uniform[64]),
        .I1(uniform[63]),
        .I2(uniform[62]),
        .I3(uniform[60]),
        .I4(uniform[61]),
        .O(\sample[1]_INST_0_i_81_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair2" *) 
  LUT5 #(
    .INIT(32'h0111FFFF)) 
    \sample[1]_INST_0_i_82 
       (.I0(uniform[59]),
        .I1(uniform[61]),
        .I2(uniform[60]),
        .I3(uniform[62]),
        .I4(uniform[54]),
        .O(\sample[1]_INST_0_i_82_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair36" *) 
  LUT4 #(
    .INIT(16'h8043)) 
    \sample[1]_INST_0_i_83 
       (.I0(uniform[67]),
        .I1(uniform[62]),
        .I2(uniform[63]),
        .I3(uniform[65]),
        .O(\sample[1]_INST_0_i_83_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF9010FFFF)) 
    \sample[1]_INST_0_i_84 
       (.I0(uniform[66]),
        .I1(uniform[65]),
        .I2(uniform[63]),
        .I3(uniform[68]),
        .I4(uniform[61]),
        .I5(uniform[64]),
        .O(\sample[1]_INST_0_i_84_n_0 ));
  LUT6 #(
    .INIT(64'h0428042004200428)) 
    \sample[1]_INST_0_i_85 
       (.I0(uniform[62]),
        .I1(uniform[60]),
        .I2(uniform[63]),
        .I3(uniform[64]),
        .I4(uniform[66]),
        .I5(uniform[65]),
        .O(\sample[1]_INST_0_i_85_n_0 ));
  LUT6 #(
    .INIT(64'h203F00F000CF00F0)) 
    \sample[1]_INST_0_i_86 
       (.I0(uniform[62]),
        .I1(uniform[61]),
        .I2(uniform[56]),
        .I3(uniform[59]),
        .I4(uniform[57]),
        .I5(uniform[60]),
        .O(\sample[1]_INST_0_i_86_n_0 ));
  LUT6 #(
    .INIT(64'h0000F0F00383F0F0)) 
    \sample[1]_INST_0_i_87 
       (.I0(uniform[60]),
        .I1(uniform[57]),
        .I2(uniform[54]),
        .I3(uniform[59]),
        .I4(uniform[52]),
        .I5(uniform[56]),
        .O(\sample[1]_INST_0_i_87_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair20" *) 
  LUT5 #(
    .INIT(32'hAABBBBEF)) 
    \sample[1]_INST_0_i_9 
       (.I0(\sample[1]_INST_0_i_15_n_0 ),
        .I1(uniform[18]),
        .I2(uniform[16]),
        .I3(uniform[17]),
        .I4(uniform[19]),
        .O(\sample[1]_INST_0_i_9_n_0 ));
  LUT6 #(
    .INIT(64'h00000000AAAAEEFE)) 
    \sample[2]_INST_0 
       (.I0(\sample[2]_INST_0_i_1_n_0 ),
        .I1(\sample[2]_INST_0_i_2_n_0 ),
        .I2(uniform[13]),
        .I3(\sample[2]_INST_0_i_3_n_0 ),
        .I4(\sample[2]_INST_0_i_4_n_0 ),
        .I5(\sample[2]_INST_0_i_5_n_0 ),
        .O(sample[2]));
  LUT6 #(
    .INIT(64'hF2F7F2FFF2FFF2F2)) 
    \sample[2]_INST_0_i_1 
       (.I0(\sample[2]_INST_0_i_6_n_0 ),
        .I1(\sample[2]_INST_0_i_7_n_0 ),
        .I2(\sample[2]_INST_0_i_8_n_0 ),
        .I3(uniform[9]),
        .I4(uniform[8]),
        .I5(uniform[7]),
        .O(\sample[2]_INST_0_i_1_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair52" *) 
  LUT4 #(
    .INIT(16'h7FFF)) 
    \sample[2]_INST_0_i_10 
       (.I0(uniform[15]),
        .I1(uniform[14]),
        .I2(uniform[16]),
        .I3(uniform[18]),
        .O(\sample[2]_INST_0_i_10_n_0 ));
  LUT6 #(
    .INIT(64'h7F7F7F7F777F7F7F)) 
    \sample[2]_INST_0_i_11 
       (.I0(uniform[19]),
        .I1(uniform[20]),
        .I2(uniform[22]),
        .I3(uniform[21]),
        .I4(uniform[23]),
        .I5(\sample[3]_INST_0_i_11_n_0 ),
        .O(\sample[2]_INST_0_i_11_n_0 ));
  LUT6 #(
    .INIT(64'hBABBBABBBABBBABA)) 
    \sample[2]_INST_0_i_12 
       (.I0(\sample[2]_INST_0_i_18_n_0 ),
        .I1(\sample[2]_INST_0_i_19_n_0 ),
        .I2(\sample[2]_INST_0_i_20_n_0 ),
        .I3(\sample[2]_INST_0_i_21_n_0 ),
        .I4(\sample[2]_INST_0_i_22_n_0 ),
        .I5(\sample[2]_INST_0_i_23_n_0 ),
        .O(\sample[2]_INST_0_i_12_n_0 ));
  LUT6 #(
    .INIT(64'hAAAAEAEAEAAAAAAA)) 
    \sample[2]_INST_0_i_13 
       (.I0(\sample[2]_INST_0_i_24_n_0 ),
        .I1(\sample[2]_INST_0_i_25_n_0 ),
        .I2(uniform[23]),
        .I3(\sample[2]_INST_0_i_20_n_0 ),
        .I4(uniform[25]),
        .I5(uniform[26]),
        .O(\sample[2]_INST_0_i_13_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair21" *) 
  LUT5 #(
    .INIT(32'h40AA7000)) 
    \sample[2]_INST_0_i_14 
       (.I0(uniform[19]),
        .I1(uniform[22]),
        .I2(uniform[21]),
        .I3(uniform[17]),
        .I4(uniform[20]),
        .O(\sample[2]_INST_0_i_14_n_0 ));
  LUT6 #(
    .INIT(64'h303C101C303C703C)) 
    \sample[2]_INST_0_i_15 
       (.I0(uniform[18]),
        .I1(uniform[16]),
        .I2(uniform[15]),
        .I3(uniform[14]),
        .I4(uniform[19]),
        .I5(uniform[17]),
        .O(\sample[2]_INST_0_i_15_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFEFFFF)) 
    \sample[2]_INST_0_i_16 
       (.I0(\sample[4]_INST_0_i_15_n_0 ),
        .I1(uniform[94]),
        .I2(uniform[96]),
        .I3(uniform[95]),
        .I4(uniform[1]),
        .I5(\sample[4]_INST_0_i_24_n_0 ),
        .O(\sample[2]_INST_0_i_16_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFEFFFF)) 
    \sample[2]_INST_0_i_17 
       (.I0(uniform[77]),
        .I1(uniform[76]),
        .I2(uniform[74]),
        .I3(uniform[75]),
        .I4(uniform[3]),
        .I5(\sample[3]_INST_0_i_36_n_0 ),
        .O(\sample[2]_INST_0_i_17_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair61" *) 
  LUT3 #(
    .INIT(8'h7F)) 
    \sample[2]_INST_0_i_18 
       (.I0(uniform[24]),
        .I1(uniform[26]),
        .I2(uniform[25]),
        .O(\sample[2]_INST_0_i_18_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair49" *) 
  LUT2 #(
    .INIT(4'hB)) 
    \sample[2]_INST_0_i_19 
       (.I0(\sample[2]_INST_0_i_26_n_0 ),
        .I1(uniform[23]),
        .O(\sample[2]_INST_0_i_19_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF07073070)) 
    \sample[2]_INST_0_i_2 
       (.I0(uniform[16]),
        .I1(uniform[13]),
        .I2(uniform[14]),
        .I3(uniform[17]),
        .I4(uniform[15]),
        .I5(\sample[2]_INST_0_i_9_n_0 ),
        .O(\sample[2]_INST_0_i_2_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair47" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[2]_INST_0_i_20 
       (.I0(uniform[28]),
        .I1(uniform[29]),
        .O(\sample[2]_INST_0_i_20_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair45" *) 
  LUT4 #(
    .INIT(16'hBBBF)) 
    \sample[2]_INST_0_i_21 
       (.I0(\sample[2]_INST_0_i_27_n_0 ),
        .I1(uniform[27]),
        .I2(uniform[31]),
        .I3(uniform[32]),
        .O(\sample[2]_INST_0_i_21_n_0 ));
  LUT6 #(
    .INIT(64'h77777777FFFFF77F)) 
    \sample[2]_INST_0_i_22 
       (.I0(uniform[32]),
        .I1(uniform[31]),
        .I2(uniform[35]),
        .I3(uniform[36]),
        .I4(\sample[2]_INST_0_i_28_n_0 ),
        .I5(uniform[33]),
        .O(\sample[2]_INST_0_i_22_n_0 ));
  LUT6 #(
    .INIT(64'h000000000EFFFFFF)) 
    \sample[2]_INST_0_i_23 
       (.I0(\sample[2]_INST_0_i_29_n_0 ),
        .I1(\sample[2]_INST_0_i_30_n_0 ),
        .I2(\sample[2]_INST_0_i_31_n_0 ),
        .I3(uniform[36]),
        .I4(uniform[34]),
        .I5(\sample[2]_INST_0_i_32_n_0 ),
        .O(\sample[2]_INST_0_i_23_n_0 ));
  LUT6 #(
    .INIT(64'h3F333F33BF337733)) 
    \sample[2]_INST_0_i_24 
       (.I0(uniform[26]),
        .I1(uniform[21]),
        .I2(uniform[22]),
        .I3(uniform[23]),
        .I4(uniform[25]),
        .I5(uniform[24]),
        .O(\sample[2]_INST_0_i_24_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair45" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \sample[2]_INST_0_i_25 
       (.I0(uniform[24]),
        .I1(uniform[27]),
        .O(\sample[2]_INST_0_i_25_n_0 ));
  LUT6 #(
    .INIT(64'h0080088000800080)) 
    \sample[2]_INST_0_i_26 
       (.I0(uniform[30]),
        .I1(uniform[27]),
        .I2(uniform[29]),
        .I3(uniform[28]),
        .I4(uniform[32]),
        .I5(uniform[31]),
        .O(\sample[2]_INST_0_i_26_n_0 ));
  LUT6 #(
    .INIT(64'h00202020002088A8)) 
    \sample[2]_INST_0_i_27 
       (.I0(uniform[30]),
        .I1(uniform[34]),
        .I2(uniform[33]),
        .I3(uniform[31]),
        .I4(uniform[32]),
        .I5(uniform[35]),
        .O(\sample[2]_INST_0_i_27_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair60" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[2]_INST_0_i_28 
       (.I0(uniform[30]),
        .I1(uniform[34]),
        .O(\sample[2]_INST_0_i_28_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair48" *) 
  LUT4 #(
    .INIT(16'h7FFF)) 
    \sample[2]_INST_0_i_29 
       (.I0(uniform[37]),
        .I1(uniform[40]),
        .I2(uniform[35]),
        .I3(uniform[39]),
        .O(\sample[2]_INST_0_i_29_n_0 ));
  LUT6 #(
    .INIT(64'h00000000AAAAEEFE)) 
    \sample[2]_INST_0_i_3 
       (.I0(\sample[2]_INST_0_i_10_n_0 ),
        .I1(\sample[2]_INST_0_i_11_n_0 ),
        .I2(\sample[2]_INST_0_i_12_n_0 ),
        .I3(\sample[2]_INST_0_i_13_n_0 ),
        .I4(\sample[2]_INST_0_i_14_n_0 ),
        .I5(\sample[2]_INST_0_i_15_n_0 ),
        .O(\sample[2]_INST_0_i_3_n_0 ));
  LUT6 #(
    .INIT(64'h00000000AAAAEEFE)) 
    \sample[2]_INST_0_i_30 
       (.I0(\sample[2]_INST_0_i_33_n_0 ),
        .I1(\sample[2]_INST_0_i_34_n_0 ),
        .I2(\sample[2]_INST_0_i_35_n_0 ),
        .I3(\sample[2]_INST_0_i_36_n_0 ),
        .I4(\sample[2]_INST_0_i_37_n_0 ),
        .I5(\sample[2]_INST_0_i_38_n_0 ),
        .O(\sample[2]_INST_0_i_30_n_0 ));
  LUT3 #(
    .INIT(8'hF4)) 
    \sample[2]_INST_0_i_31 
       (.I0(\sample[2]_INST_0_i_39_n_0 ),
        .I1(uniform[35]),
        .I2(\sample[2]_INST_0_i_40_n_0 ),
        .O(\sample[2]_INST_0_i_31_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF00004100)) 
    \sample[2]_INST_0_i_32 
       (.I0(uniform[37]),
        .I1(uniform[38]),
        .I2(uniform[35]),
        .I3(uniform[34]),
        .I4(uniform[36]),
        .I5(\sample[2]_INST_0_i_41_n_0 ),
        .O(\sample[2]_INST_0_i_32_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF07FFFFFF)) 
    \sample[2]_INST_0_i_33 
       (.I0(\sample[2]_INST_0_i_42_n_0 ),
        .I1(uniform[43]),
        .I2(uniform[46]),
        .I3(uniform[44]),
        .I4(uniform[45]),
        .I5(\sample[2]_INST_0_i_43_n_0 ),
        .O(\sample[2]_INST_0_i_33_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair44" *) 
  LUT4 #(
    .INIT(16'h7FFF)) 
    \sample[2]_INST_0_i_34 
       (.I0(uniform[49]),
        .I1(uniform[48]),
        .I2(uniform[52]),
        .I3(uniform[50]),
        .O(\sample[2]_INST_0_i_34_n_0 ));
  LUT6 #(
    .INIT(64'hF4FFF4FFFFFFF0FF)) 
    \sample[2]_INST_0_i_35 
       (.I0(\sample[2]_INST_0_i_44_n_0 ),
        .I1(\sample[2]_INST_0_i_45_n_0 ),
        .I2(\sample[2]_INST_0_i_46_n_0 ),
        .I3(uniform[51]),
        .I4(\sample[2]_INST_0_i_47_n_0 ),
        .I5(uniform[57]),
        .O(\sample[2]_INST_0_i_35_n_0 ));
  LUT6 #(
    .INIT(64'h0343490940404040)) 
    \sample[2]_INST_0_i_36 
       (.I0(uniform[54]),
        .I1(uniform[56]),
        .I2(uniform[53]),
        .I3(uniform[58]),
        .I4(uniform[57]),
        .I5(uniform[55]),
        .O(\sample[2]_INST_0_i_36_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFFBBFB)) 
    \sample[2]_INST_0_i_37 
       (.I0(\sample[2]_INST_0_i_48_n_0 ),
        .I1(uniform[43]),
        .I2(\sample[2]_INST_0_i_42_n_0 ),
        .I3(uniform[46]),
        .I4(\sample[2]_INST_0_i_49_n_0 ),
        .I5(\sample[2]_INST_0_i_50_n_0 ),
        .O(\sample[2]_INST_0_i_37_n_0 ));
  LUT6 #(
    .INIT(64'h5530753077307730)) 
    \sample[2]_INST_0_i_38 
       (.I0(\sample[2]_INST_0_i_51_n_0 ),
        .I1(uniform[42]),
        .I2(uniform[43]),
        .I3(uniform[41]),
        .I4(uniform[45]),
        .I5(uniform[44]),
        .O(\sample[2]_INST_0_i_38_n_0 ));
  LUT6 #(
    .INIT(64'hFF8FFFFFFFFF3FFF)) 
    \sample[2]_INST_0_i_39 
       (.I0(uniform[43]),
        .I1(uniform[41]),
        .I2(uniform[38]),
        .I3(uniform[40]),
        .I4(uniform[42]),
        .I5(uniform[39]),
        .O(\sample[2]_INST_0_i_39_n_0 ));
  LUT6 #(
    .INIT(64'h545FFFFFFFFFFFFF)) 
    \sample[2]_INST_0_i_4 
       (.I0(uniform[11]),
        .I1(uniform[9]),
        .I2(uniform[10]),
        .I3(uniform[12]),
        .I4(uniform[8]),
        .I5(uniform[7]),
        .O(\sample[2]_INST_0_i_4_n_0 ));
  LUT6 #(
    .INIT(64'h0000DF8F3FFF0000)) 
    \sample[2]_INST_0_i_40 
       (.I0(uniform[41]),
        .I1(uniform[39]),
        .I2(uniform[35]),
        .I3(uniform[40]),
        .I4(uniform[38]),
        .I5(uniform[37]),
        .O(\sample[2]_INST_0_i_40_n_0 ));
  LUT6 #(
    .INIT(64'h5DDD5D5DFFFFFFFF)) 
    \sample[2]_INST_0_i_41 
       (.I0(uniform[30]),
        .I1(\sample[2]_INST_0_i_52_n_0 ),
        .I2(uniform[34]),
        .I3(uniform[38]),
        .I4(uniform[39]),
        .I5(uniform[33]),
        .O(\sample[2]_INST_0_i_41_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair13" *) 
  LUT2 #(
    .INIT(4'h6)) 
    \sample[2]_INST_0_i_42 
       (.I0(uniform[47]),
        .I1(uniform[48]),
        .O(\sample[2]_INST_0_i_42_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair67" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[2]_INST_0_i_43 
       (.I0(uniform[41]),
        .I1(uniform[42]),
        .O(\sample[2]_INST_0_i_43_n_0 ));
  LUT6 #(
    .INIT(64'h750075007500FFFF)) 
    \sample[2]_INST_0_i_44 
       (.I0(uniform[55]),
        .I1(uniform[60]),
        .I2(uniform[61]),
        .I3(\sample[2]_INST_0_i_53_n_0 ),
        .I4(\sample[2]_INST_0_i_54_n_0 ),
        .I5(uniform[58]),
        .O(\sample[2]_INST_0_i_44_n_0 ));
  LUT6 #(
    .INIT(64'h00A8FFFFFFFFFFFF)) 
    \sample[2]_INST_0_i_45 
       (.I0(\sample[2]_INST_0_i_55_n_0 ),
        .I1(\sample[2]_INST_0_i_56_n_0 ),
        .I2(\sample[2]_INST_0_i_57_n_0 ),
        .I3(\sample[2]_INST_0_i_58_n_0 ),
        .I4(uniform[58]),
        .I5(uniform[55]),
        .O(\sample[2]_INST_0_i_45_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair54" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[2]_INST_0_i_46 
       (.I0(uniform[53]),
        .I1(uniform[54]),
        .O(\sample[2]_INST_0_i_46_n_0 ));
  LUT6 #(
    .INIT(64'h9FFFF0003FFFFFFF)) 
    \sample[2]_INST_0_i_47 
       (.I0(uniform[61]),
        .I1(uniform[60]),
        .I2(uniform[55]),
        .I3(uniform[59]),
        .I4(uniform[56]),
        .I5(uniform[58]),
        .O(\sample[2]_INST_0_i_47_n_0 ));
  LUT6 #(
    .INIT(64'h0202020202A20202)) 
    \sample[2]_INST_0_i_48 
       (.I0(uniform[48]),
        .I1(\sample[2]_INST_0_i_59_n_0 ),
        .I2(\sample[2]_INST_0_i_60_n_0 ),
        .I3(uniform[52]),
        .I4(uniform[51]),
        .I5(\sample[2]_INST_0_i_61_n_0 ),
        .O(\sample[2]_INST_0_i_48_n_0 ));
  LUT6 #(
    .INIT(64'h0008008800F80088)) 
    \sample[2]_INST_0_i_49 
       (.I0(uniform[48]),
        .I1(uniform[47]),
        .I2(uniform[51]),
        .I3(uniform[49]),
        .I4(uniform[50]),
        .I5(uniform[52]),
        .O(\sample[2]_INST_0_i_49_n_0 ));
  LUT6 #(
    .INIT(64'hEFFEFEFEFFFEFFFE)) 
    \sample[2]_INST_0_i_5 
       (.I0(\sample[2]_INST_0_i_16_n_0 ),
        .I1(\sample[2]_INST_0_i_17_n_0 ),
        .I2(uniform[4]),
        .I3(uniform[2]),
        .I4(uniform[6]),
        .I5(uniform[5]),
        .O(\sample[2]_INST_0_i_5_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair13" *) 
  LUT5 #(
    .INIT(32'h10041111)) 
    \sample[2]_INST_0_i_50 
       (.I0(uniform[48]),
        .I1(uniform[49]),
        .I2(uniform[50]),
        .I3(uniform[51]),
        .I4(uniform[47]),
        .O(\sample[2]_INST_0_i_50_n_0 ));
  LUT6 #(
    .INIT(64'hFEF5FF0FF00FFF0F)) 
    \sample[2]_INST_0_i_51 
       (.I0(uniform[47]),
        .I1(uniform[48]),
        .I2(uniform[45]),
        .I3(uniform[44]),
        .I4(uniform[43]),
        .I5(uniform[46]),
        .O(\sample[2]_INST_0_i_51_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair17" *) 
  LUT3 #(
    .INIT(8'h08)) 
    \sample[2]_INST_0_i_52 
       (.I0(uniform[37]),
        .I1(uniform[35]),
        .I2(uniform[36]),
        .O(\sample[2]_INST_0_i_52_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair29" *) 
  LUT2 #(
    .INIT(4'h2)) 
    \sample[2]_INST_0_i_53 
       (.I0(uniform[56]),
        .I1(uniform[59]),
        .O(\sample[2]_INST_0_i_53_n_0 ));
  LUT6 #(
    .INIT(64'hAAAA2AAAAA2AAAAA)) 
    \sample[2]_INST_0_i_54 
       (.I0(uniform[55]),
        .I1(uniform[59]),
        .I2(uniform[56]),
        .I3(uniform[62]),
        .I4(uniform[60]),
        .I5(uniform[61]),
        .O(\sample[2]_INST_0_i_54_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF45454500)) 
    \sample[2]_INST_0_i_55 
       (.I0(\sample[2]_INST_0_i_62_n_0 ),
        .I1(\sample[2]_INST_0_i_63_n_0 ),
        .I2(\sample[2]_INST_0_i_64_n_0 ),
        .I3(uniform[67]),
        .I4(\sample[2]_INST_0_i_65_n_0 ),
        .I5(\sample[2]_INST_0_i_66_n_0 ),
        .O(\sample[2]_INST_0_i_55_n_0 ));
  LUT6 #(
    .INIT(64'hF0FFF0F09FAF5FFF)) 
    \sample[2]_INST_0_i_56 
       (.I0(uniform[66]),
        .I1(uniform[67]),
        .I2(uniform[62]),
        .I3(uniform[65]),
        .I4(uniform[64]),
        .I5(uniform[63]),
        .O(\sample[2]_INST_0_i_56_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair66" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[2]_INST_0_i_57 
       (.I0(uniform[60]),
        .I1(uniform[61]),
        .O(\sample[2]_INST_0_i_57_n_0 ));
  LUT6 #(
    .INIT(64'hAAAAAABEBEAAAAAA)) 
    \sample[2]_INST_0_i_58 
       (.I0(\sample[2]_INST_0_i_67_n_0 ),
        .I1(uniform[63]),
        .I2(uniform[62]),
        .I3(uniform[60]),
        .I4(uniform[61]),
        .I5(uniform[59]),
        .O(\sample[2]_INST_0_i_58_n_0 ));
  LUT6 #(
    .INIT(64'hFBFF00FF000000FF)) 
    \sample[2]_INST_0_i_59 
       (.I0(uniform[52]),
        .I1(uniform[54]),
        .I2(uniform[55]),
        .I3(uniform[50]),
        .I4(uniform[47]),
        .I5(uniform[51]),
        .O(\sample[2]_INST_0_i_59_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair26" *) 
  LUT3 #(
    .INIT(8'h0E)) 
    \sample[2]_INST_0_i_6 
       (.I0(uniform[10]),
        .I1(uniform[9]),
        .I2(uniform[11]),
        .O(\sample[2]_INST_0_i_6_n_0 ));
  LUT6 #(
    .INIT(64'hFFBC000000000000)) 
    \sample[2]_INST_0_i_60 
       (.I0(uniform[54]),
        .I1(uniform[50]),
        .I2(uniform[52]),
        .I3(uniform[51]),
        .I4(uniform[53]),
        .I5(uniform[47]),
        .O(\sample[2]_INST_0_i_60_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair58" *) 
  LUT3 #(
    .INIT(8'h2A)) 
    \sample[2]_INST_0_i_61 
       (.I0(uniform[50]),
        .I1(uniform[54]),
        .I2(uniform[55]),
        .O(\sample[2]_INST_0_i_61_n_0 ));
  LUT6 #(
    .INIT(64'h0F2F0F0F0F0FFF0F)) 
    \sample[2]_INST_0_i_62 
       (.I0(uniform[68]),
        .I1(uniform[69]),
        .I2(uniform[60]),
        .I3(uniform[66]),
        .I4(uniform[65]),
        .I5(uniform[64]),
        .O(\sample[2]_INST_0_i_62_n_0 ));
  LUT6 #(
    .INIT(64'h34FF3F3FFFFFFFFF)) 
    \sample[2]_INST_0_i_63 
       (.I0(uniform[69]),
        .I1(uniform[66]),
        .I2(uniform[65]),
        .I3(uniform[68]),
        .I4(uniform[64]),
        .I5(uniform[67]),
        .O(\sample[2]_INST_0_i_63_n_0 ));
  LUT6 #(
    .INIT(64'h1FFFFFFFFFFFFFFF)) 
    \sample[2]_INST_0_i_64 
       (.I0(uniform[71]),
        .I1(uniform[69]),
        .I2(uniform[66]),
        .I3(uniform[70]),
        .I4(uniform[64]),
        .I5(uniform[65]),
        .O(\sample[2]_INST_0_i_64_n_0 ));
  LUT6 #(
    .INIT(64'h6C8FFF0F5C8FFF0F)) 
    \sample[2]_INST_0_i_65 
       (.I0(uniform[69]),
        .I1(uniform[68]),
        .I2(uniform[65]),
        .I3(uniform[66]),
        .I4(uniform[64]),
        .I5(uniform[70]),
        .O(\sample[2]_INST_0_i_65_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair38" *) 
  LUT4 #(
    .INIT(16'h7FFF)) 
    \sample[2]_INST_0_i_66 
       (.I0(uniform[62]),
        .I1(uniform[59]),
        .I2(uniform[63]),
        .I3(uniform[61]),
        .O(\sample[2]_INST_0_i_66_n_0 ));
  LUT6 #(
    .INIT(64'h01FF00FF00FFFF00)) 
    \sample[2]_INST_0_i_67 
       (.I0(uniform[62]),
        .I1(uniform[64]),
        .I2(uniform[63]),
        .I3(uniform[56]),
        .I4(uniform[60]),
        .I5(uniform[59]),
        .O(\sample[2]_INST_0_i_67_n_0 ));
  LUT6 #(
    .INIT(64'hF8FFFFFFFFFFFFFF)) 
    \sample[2]_INST_0_i_7 
       (.I0(uniform[10]),
        .I1(uniform[13]),
        .I2(uniform[12]),
        .I3(uniform[9]),
        .I4(uniform[8]),
        .I5(uniform[7]),
        .O(\sample[2]_INST_0_i_7_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair51" *) 
  LUT4 #(
    .INIT(16'h0455)) 
    \sample[2]_INST_0_i_8 
       (.I0(uniform[4]),
        .I1(uniform[5]),
        .I2(uniform[6]),
        .I3(uniform[2]),
        .O(\sample[2]_INST_0_i_8_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair23" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[2]_INST_0_i_9 
       (.I0(uniform[10]),
        .I1(uniform[12]),
        .O(\sample[2]_INST_0_i_9_n_0 ));
  LUT6 #(
    .INIT(64'h00000000AAAABBFB)) 
    \sample[3]_INST_0 
       (.I0(\sample[3]_INST_0_i_1_n_0 ),
        .I1(uniform[20]),
        .I2(\sample[3]_INST_0_i_2_n_0 ),
        .I3(\sample[3]_INST_0_i_3_n_0 ),
        .I4(\sample[3]_INST_0_i_4_n_0 ),
        .I5(\sample[3]_INST_0_i_5_n_0 ),
        .O(sample[3]));
  LUT6 #(
    .INIT(64'h001500150F150015)) 
    \sample[3]_INST_0_i_1 
       (.I0(uniform[14]),
        .I1(uniform[13]),
        .I2(uniform[16]),
        .I3(uniform[15]),
        .I4(uniform[17]),
        .I5(uniform[19]),
        .O(\sample[3]_INST_0_i_1_n_0 ));
  LUT6 #(
    .INIT(64'h00000000222FCCCC)) 
    \sample[3]_INST_0_i_10 
       (.I0(uniform[23]),
        .I1(uniform[21]),
        .I2(uniform[24]),
        .I3(uniform[25]),
        .I4(uniform[19]),
        .I5(uniform[22]),
        .O(\sample[3]_INST_0_i_10_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair18" *) 
  LUT2 #(
    .INIT(4'h1)) 
    \sample[3]_INST_0_i_11 
       (.I0(uniform[25]),
        .I1(uniform[24]),
        .O(\sample[3]_INST_0_i_11_n_0 ));
  LUT6 #(
    .INIT(64'h7FFFFFFFFFFFFFFF)) 
    \sample[3]_INST_0_i_12 
       (.I0(uniform[39]),
        .I1(uniform[40]),
        .I2(\sample[3]_INST_0_i_27_n_0 ),
        .I3(uniform[38]),
        .I4(uniform[41]),
        .I5(\sample[3]_INST_0_i_28_n_0 ),
        .O(\sample[3]_INST_0_i_12_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF7FFFFFFF)) 
    \sample[3]_INST_0_i_13 
       (.I0(uniform[66]),
        .I1(uniform[64]),
        .I2(\sample[3]_INST_0_i_29_n_0 ),
        .I3(\sample[3]_INST_0_i_30_n_0 ),
        .I4(\sample[3]_INST_0_i_31_n_0 ),
        .I5(\sample[3]_INST_0_i_32_n_0 ),
        .O(\sample[3]_INST_0_i_13_n_0 ));
  LUT5 #(
    .INIT(32'h00008000)) 
    \sample[3]_INST_0_i_14 
       (.I0(uniform[22]),
        .I1(uniform[45]),
        .I2(uniform[32]),
        .I3(uniform[54]),
        .I4(\sample[3]_INST_0_i_33_n_0 ),
        .O(\sample[3]_INST_0_i_14_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair33" *) 
  LUT5 #(
    .INIT(32'h44055405)) 
    \sample[3]_INST_0_i_15 
       (.I0(uniform[20]),
        .I1(uniform[21]),
        .I2(uniform[19]),
        .I3(uniform[17]),
        .I4(uniform[22]),
        .O(\sample[3]_INST_0_i_15_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFFAAAAABAA)) 
    \sample[3]_INST_0_i_16 
       (.I0(\sample[3]_INST_0_i_34_n_0 ),
        .I1(uniform[23]),
        .I2(uniform[24]),
        .I3(uniform[15]),
        .I4(\sample[3]_INST_0_i_35_n_0 ),
        .I5(\sample[4]_INST_0_i_15_n_0 ),
        .O(\sample[3]_INST_0_i_16_n_0 ));
  LUT5 #(
    .INIT(32'hFFFFBAFF)) 
    \sample[3]_INST_0_i_17 
       (.I0(\sample[3]_INST_0_i_36_n_0 ),
        .I1(uniform[13]),
        .I2(uniform[15]),
        .I3(uniform[10]),
        .I4(\sample[3]_INST_0_i_37_n_0 ),
        .O(\sample[3]_INST_0_i_17_n_0 ));
  LUT6 #(
    .INIT(64'hBFFFBFFFFFFFBFFF)) 
    \sample[3]_INST_0_i_18 
       (.I0(\sample[1]_INST_0_i_6_n_0 ),
        .I1(uniform[8]),
        .I2(uniform[11]),
        .I3(\sample[3]_INST_0_i_38_n_0 ),
        .I4(uniform[15]),
        .I5(uniform[18]),
        .O(\sample[3]_INST_0_i_18_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair30" *) 
  LUT4 #(
    .INIT(16'h0007)) 
    \sample[3]_INST_0_i_19 
       (.I0(uniform[16]),
        .I1(uniform[13]),
        .I2(uniform[15]),
        .I3(uniform[14]),
        .O(\sample[3]_INST_0_i_19_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFFFF0D0000)) 
    \sample[3]_INST_0_i_2 
       (.I0(\sample[3]_INST_0_i_6_n_0 ),
        .I1(\sample[3]_INST_0_i_7_n_0 ),
        .I2(\sample[3]_INST_0_i_8_n_0 ),
        .I3(\sample[3]_INST_0_i_9_n_0 ),
        .I4(uniform[22]),
        .I5(\sample[3]_INST_0_i_10_n_0 ),
        .O(\sample[3]_INST_0_i_2_n_0 ));
  LUT6 #(
    .INIT(64'h003400000000FFFF)) 
    \sample[3]_INST_0_i_20 
       (.I0(uniform[35]),
        .I1(uniform[33]),
        .I2(uniform[34]),
        .I3(uniform[32]),
        .I4(uniform[30]),
        .I5(uniform[28]),
        .O(\sample[3]_INST_0_i_20_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair43" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \sample[3]_INST_0_i_21 
       (.I0(uniform[28]),
        .I1(uniform[32]),
        .O(\sample[3]_INST_0_i_21_n_0 ));
  LUT6 #(
    .INIT(64'h88888888A8A8A8AA)) 
    \sample[3]_INST_0_i_22 
       (.I0(\sample[3]_INST_0_i_39_n_0 ),
        .I1(\sample[3]_INST_0_i_40_n_0 ),
        .I2(\sample[3]_INST_0_i_41_n_0 ),
        .I3(\sample[3]_INST_0_i_42_n_0 ),
        .I4(\sample[3]_INST_0_i_43_n_0 ),
        .I5(\sample[3]_INST_0_i_44_n_0 ),
        .O(\sample[3]_INST_0_i_22_n_0 ));
  LUT6 #(
    .INIT(64'h00E0FFFFFFFFFFFF)) 
    \sample[3]_INST_0_i_23 
       (.I0(uniform[37]),
        .I1(uniform[38]),
        .I2(uniform[36]),
        .I3(uniform[35]),
        .I4(\sample[3]_INST_0_i_45_n_0 ),
        .I5(uniform[30]),
        .O(\sample[3]_INST_0_i_23_n_0 ));
  LUT6 #(
    .INIT(64'h1115002233333333)) 
    \sample[3]_INST_0_i_24 
       (.I0(uniform[34]),
        .I1(uniform[33]),
        .I2(uniform[37]),
        .I3(uniform[36]),
        .I4(uniform[35]),
        .I5(uniform[30]),
        .O(\sample[3]_INST_0_i_24_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair32" *) 
  LUT3 #(
    .INIT(8'h40)) 
    \sample[3]_INST_0_i_25 
       (.I0(uniform[31]),
        .I1(uniform[27]),
        .I2(uniform[28]),
        .O(\sample[3]_INST_0_i_25_n_0 ));
  LUT6 #(
    .INIT(64'h7FFF7F7F7FFF7FFF)) 
    \sample[3]_INST_0_i_26 
       (.I0(\sample[3]_INST_0_i_27_n_0 ),
        .I1(uniform[24]),
        .I2(uniform[23]),
        .I3(uniform[27]),
        .I4(uniform[29]),
        .I5(uniform[28]),
        .O(\sample[3]_INST_0_i_26_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair11" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \sample[3]_INST_0_i_27 
       (.I0(uniform[25]),
        .I1(uniform[26]),
        .O(\sample[3]_INST_0_i_27_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair66" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \sample[3]_INST_0_i_28 
       (.I0(uniform[58]),
        .I1(uniform[60]),
        .O(\sample[3]_INST_0_i_28_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair4" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \sample[3]_INST_0_i_29 
       (.I0(uniform[51]),
        .I1(uniform[53]),
        .O(\sample[3]_INST_0_i_29_n_0 ));
  LUT6 #(
    .INIT(64'h4D4D4D4FFFFFFFFF)) 
    \sample[3]_INST_0_i_3 
       (.I0(uniform[19]),
        .I1(uniform[22]),
        .I2(uniform[21]),
        .I3(uniform[23]),
        .I4(\sample[3]_INST_0_i_11_n_0 ),
        .I5(uniform[17]),
        .O(\sample[3]_INST_0_i_3_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair55" *) 
  LUT2 #(
    .INIT(4'h2)) 
    \sample[3]_INST_0_i_30 
       (.I0(uniform[65]),
        .I1(uniform[68]),
        .O(\sample[3]_INST_0_i_30_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair7" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \sample[3]_INST_0_i_31 
       (.I0(uniform[52]),
        .I1(uniform[55]),
        .O(\sample[3]_INST_0_i_31_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF7FFFFFFF)) 
    \sample[3]_INST_0_i_32 
       (.I0(uniform[48]),
        .I1(uniform[56]),
        .I2(uniform[57]),
        .I3(uniform[59]),
        .I4(\sample[3]_INST_0_i_46_n_0 ),
        .I5(\sample[2]_INST_0_i_20_n_0 ),
        .O(\sample[3]_INST_0_i_32_n_0 ));
  LUT6 #(
    .INIT(64'hFFF7FFFFFFFFFFFF)) 
    \sample[3]_INST_0_i_33 
       (.I0(uniform[43]),
        .I1(uniform[47]),
        .I2(uniform[69]),
        .I3(uniform[70]),
        .I4(\sample[3]_INST_0_i_47_n_0 ),
        .I5(\sample[3]_INST_0_i_48_n_0 ),
        .O(\sample[3]_INST_0_i_33_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair50" *) 
  LUT4 #(
    .INIT(16'hFEFF)) 
    \sample[3]_INST_0_i_34 
       (.I0(uniform[94]),
        .I1(uniform[96]),
        .I2(uniform[95]),
        .I3(uniform[1]),
        .O(\sample[3]_INST_0_i_34_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair33" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[3]_INST_0_i_35 
       (.I0(uniform[20]),
        .I1(uniform[19]),
        .O(\sample[3]_INST_0_i_35_n_0 ));
  LUT3 #(
    .INIT(8'hEF)) 
    \sample[3]_INST_0_i_36 
       (.I0(uniform[72]),
        .I1(uniform[73]),
        .I2(uniform[0]),
        .O(\sample[3]_INST_0_i_36_n_0 ));
  LUT4 #(
    .INIT(16'h7FFF)) 
    \sample[3]_INST_0_i_37 
       (.I0(uniform[7]),
        .I1(uniform[4]),
        .I2(uniform[12]),
        .I3(uniform[9]),
        .O(\sample[3]_INST_0_i_37_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair51" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \sample[3]_INST_0_i_38 
       (.I0(uniform[2]),
        .I1(uniform[5]),
        .O(\sample[3]_INST_0_i_38_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair17" *) 
  LUT5 #(
    .INIT(32'hEEB0EE90)) 
    \sample[3]_INST_0_i_39 
       (.I0(uniform[37]),
        .I1(uniform[38]),
        .I2(uniform[35]),
        .I3(uniform[36]),
        .I4(uniform[39]),
        .O(\sample[3]_INST_0_i_39_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF10FFFFFF)) 
    \sample[3]_INST_0_i_4 
       (.I0(\sample[3]_INST_0_i_12_n_0 ),
        .I1(\sample[3]_INST_0_i_13_n_0 ),
        .I2(\sample[3]_INST_0_i_14_n_0 ),
        .I3(uniform[15]),
        .I4(uniform[16]),
        .I5(\sample[3]_INST_0_i_15_n_0 ),
        .O(\sample[3]_INST_0_i_4_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair42" *) 
  LUT4 #(
    .INIT(16'h777F)) 
    \sample[3]_INST_0_i_40 
       (.I0(uniform[37]),
        .I1(uniform[36]),
        .I2(\sample[3]_INST_0_i_49_n_0 ),
        .I3(uniform[39]),
        .O(\sample[3]_INST_0_i_40_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair14" *) 
  LUT3 #(
    .INIT(8'h7F)) 
    \sample[3]_INST_0_i_41 
       (.I0(uniform[40]),
        .I1(uniform[38]),
        .I2(uniform[42]),
        .O(\sample[3]_INST_0_i_41_n_0 ));
  LUT6 #(
    .INIT(64'h00000000BBBA888A)) 
    \sample[3]_INST_0_i_42 
       (.I0(\sample[3]_INST_0_i_50_n_0 ),
        .I1(\sample[3]_INST_0_i_51_n_0 ),
        .I2(\sample[3]_INST_0_i_52_n_0 ),
        .I3(\sample[3]_INST_0_i_53_n_0 ),
        .I4(\sample[3]_INST_0_i_54_n_0 ),
        .I5(\sample[3]_INST_0_i_55_n_0 ),
        .O(\sample[3]_INST_0_i_42_n_0 ));
  LUT6 #(
    .INIT(64'h0303BFBF13734F4F)) 
    \sample[3]_INST_0_i_43 
       (.I0(uniform[46]),
        .I1(uniform[44]),
        .I2(uniform[41]),
        .I3(uniform[47]),
        .I4(uniform[43]),
        .I5(uniform[45]),
        .O(\sample[3]_INST_0_i_43_n_0 ));
  LUT6 #(
    .INIT(64'h02395F3908395D39)) 
    \sample[3]_INST_0_i_44 
       (.I0(uniform[38]),
        .I1(uniform[41]),
        .I2(uniform[42]),
        .I3(uniform[40]),
        .I4(uniform[39]),
        .I5(uniform[43]),
        .O(\sample[3]_INST_0_i_44_n_0 ));
  LUT2 #(
    .INIT(4'h8)) 
    \sample[3]_INST_0_i_45 
       (.I0(uniform[33]),
        .I1(uniform[34]),
        .O(\sample[3]_INST_0_i_45_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair64" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \sample[3]_INST_0_i_46 
       (.I0(uniform[62]),
        .I1(uniform[63]),
        .O(\sample[3]_INST_0_i_46_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair28" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \sample[3]_INST_0_i_47 
       (.I0(uniform[17]),
        .I1(uniform[21]),
        .O(\sample[3]_INST_0_i_47_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair46" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \sample[3]_INST_0_i_48 
       (.I0(uniform[33]),
        .I1(uniform[36]),
        .O(\sample[3]_INST_0_i_48_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair14" *) 
  LUT5 #(
    .INIT(32'h00005D00)) 
    \sample[3]_INST_0_i_49 
       (.I0(uniform[38]),
        .I1(uniform[41]),
        .I2(uniform[42]),
        .I3(uniform[40]),
        .I4(uniform[39]),
        .O(\sample[3]_INST_0_i_49_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFFFEFEFEFF)) 
    \sample[3]_INST_0_i_5 
       (.I0(\sample[3]_INST_0_i_16_n_0 ),
        .I1(\sample[3]_INST_0_i_17_n_0 ),
        .I2(\sample[3]_INST_0_i_18_n_0 ),
        .I3(uniform[14]),
        .I4(\sample[3]_INST_0_i_19_n_0 ),
        .I5(\sample[4]_INST_0_i_14_n_0 ),
        .O(\sample[3]_INST_0_i_5_n_0 ));
  LUT5 #(
    .INIT(32'hD7005500)) 
    \sample[3]_INST_0_i_50 
       (.I0(uniform[48]),
        .I1(uniform[49]),
        .I2(uniform[50]),
        .I3(uniform[41]),
        .I4(uniform[46]),
        .O(\sample[3]_INST_0_i_50_n_0 ));
  LUT6 #(
    .INIT(64'h00101010FFFFFFFF)) 
    \sample[3]_INST_0_i_51 
       (.I0(uniform[48]),
        .I1(uniform[49]),
        .I2(uniform[46]),
        .I3(uniform[51]),
        .I4(uniform[50]),
        .I5(uniform[47]),
        .O(\sample[3]_INST_0_i_51_n_0 ));
  LUT6 #(
    .INIT(64'hA8AA888888888888)) 
    \sample[3]_INST_0_i_52 
       (.I0(\sample[3]_INST_0_i_29_n_0 ),
        .I1(\sample[3]_INST_0_i_56_n_0 ),
        .I2(\sample[3]_INST_0_i_57_n_0 ),
        .I3(\sample[3]_INST_0_i_58_n_0 ),
        .I4(\sample[3]_INST_0_i_59_n_0 ),
        .I5(uniform[50]),
        .O(\sample[3]_INST_0_i_52_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFFF1F1F0FF)) 
    \sample[3]_INST_0_i_53 
       (.I0(\sample[3]_INST_0_i_60_n_0 ),
        .I1(uniform[53]),
        .I2(\sample[3]_INST_0_i_61_n_0 ),
        .I3(\sample[3]_INST_0_i_62_n_0 ),
        .I4(uniform[51]),
        .I5(\sample[3]_INST_0_i_63_n_0 ),
        .O(\sample[3]_INST_0_i_53_n_0 ));
  LUT6 #(
    .INIT(64'h0000000008880000)) 
    \sample[3]_INST_0_i_54 
       (.I0(uniform[41]),
        .I1(uniform[46]),
        .I2(uniform[51]),
        .I3(uniform[52]),
        .I4(uniform[48]),
        .I5(uniform[50]),
        .O(\sample[3]_INST_0_i_54_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair41" *) 
  LUT3 #(
    .INIT(8'h7F)) 
    \sample[3]_INST_0_i_55 
       (.I0(uniform[44]),
        .I1(uniform[43]),
        .I2(uniform[45]),
        .O(\sample[3]_INST_0_i_55_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair7" *) 
  LUT5 #(
    .INIT(32'hFFFFFF40)) 
    \sample[3]_INST_0_i_56 
       (.I0(\sample[3]_INST_0_i_64_n_0 ),
        .I1(uniform[52]),
        .I2(uniform[55]),
        .I3(\sample[3]_INST_0_i_65_n_0 ),
        .I4(\sample[3]_INST_0_i_66_n_0 ),
        .O(\sample[3]_INST_0_i_56_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF07000600)) 
    \sample[3]_INST_0_i_57 
       (.I0(uniform[60]),
        .I1(uniform[58]),
        .I2(uniform[59]),
        .I3(uniform[57]),
        .I4(uniform[61]),
        .I5(\sample[3]_INST_0_i_67_n_0 ),
        .O(\sample[3]_INST_0_i_57_n_0 ));
  LUT6 #(
    .INIT(64'hFFFF11D1FFFFFFFF)) 
    \sample[3]_INST_0_i_58 
       (.I0(\sample[3]_INST_0_i_68_n_0 ),
        .I1(uniform[60]),
        .I2(\sample[3]_INST_0_i_69_n_0 ),
        .I3(\sample[3]_INST_0_i_70_n_0 ),
        .I4(\sample[3]_INST_0_i_71_n_0 ),
        .I5(uniform[58]),
        .O(\sample[3]_INST_0_i_58_n_0 ));
  LUT2 #(
    .INIT(4'h8)) 
    \sample[3]_INST_0_i_59 
       (.I0(uniform[55]),
        .I1(uniform[54]),
        .O(\sample[3]_INST_0_i_59_n_0 ));
  LUT6 #(
    .INIT(64'h11115551FFFFFFFF)) 
    \sample[3]_INST_0_i_6 
       (.I0(\sample[3]_INST_0_i_20_n_0 ),
        .I1(\sample[3]_INST_0_i_21_n_0 ),
        .I2(\sample[3]_INST_0_i_22_n_0 ),
        .I3(\sample[3]_INST_0_i_23_n_0 ),
        .I4(\sample[3]_INST_0_i_24_n_0 ),
        .I5(uniform[29]),
        .O(\sample[3]_INST_0_i_6_n_0 ));
  LUT6 #(
    .INIT(64'hA808A808A8882888)) 
    \sample[3]_INST_0_i_60 
       (.I0(uniform[50]),
        .I1(uniform[54]),
        .I2(uniform[52]),
        .I3(uniform[55]),
        .I4(uniform[57]),
        .I5(uniform[56]),
        .O(\sample[3]_INST_0_i_60_n_0 ));
  LUT6 #(
    .INIT(64'h0000088800000000)) 
    \sample[3]_INST_0_i_61 
       (.I0(uniform[56]),
        .I1(uniform[48]),
        .I2(uniform[54]),
        .I3(uniform[57]),
        .I4(uniform[55]),
        .I5(uniform[52]),
        .O(\sample[3]_INST_0_i_61_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair44" *) 
  LUT2 #(
    .INIT(4'h2)) 
    \sample[3]_INST_0_i_62 
       (.I0(uniform[50]),
        .I1(uniform[52]),
        .O(\sample[3]_INST_0_i_62_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair12" *) 
  LUT5 #(
    .INIT(32'h4E5F4A5F)) 
    \sample[3]_INST_0_i_63 
       (.I0(uniform[49]),
        .I1(uniform[51]),
        .I2(uniform[48]),
        .I3(uniform[46]),
        .I4(uniform[50]),
        .O(\sample[3]_INST_0_i_63_n_0 ));
  LUT6 #(
    .INIT(64'hFFF0FF00F75FF000)) 
    \sample[3]_INST_0_i_64 
       (.I0(uniform[59]),
        .I1(uniform[60]),
        .I2(uniform[58]),
        .I3(uniform[56]),
        .I4(uniform[54]),
        .I5(uniform[57]),
        .O(\sample[3]_INST_0_i_64_n_0 ));
  LUT6 #(
    .INIT(64'h0000000000E00000)) 
    \sample[3]_INST_0_i_65 
       (.I0(uniform[58]),
        .I1(uniform[57]),
        .I2(uniform[52]),
        .I3(uniform[56]),
        .I4(uniform[54]),
        .I5(uniform[55]),
        .O(\sample[3]_INST_0_i_65_n_0 ));
  LUT6 #(
    .INIT(64'h0080000000800080)) 
    \sample[3]_INST_0_i_66 
       (.I0(uniform[52]),
        .I1(uniform[58]),
        .I2(uniform[54]),
        .I3(uniform[57]),
        .I4(\sample[3]_INST_0_i_72_n_0 ),
        .I5(uniform[59]),
        .O(\sample[3]_INST_0_i_66_n_0 ));
  LUT6 #(
    .INIT(64'h01000000FFFFFFFF)) 
    \sample[3]_INST_0_i_67 
       (.I0(uniform[60]),
        .I1(uniform[58]),
        .I2(\sample[0]_INST_0_i_63_n_0 ),
        .I3(uniform[57]),
        .I4(uniform[59]),
        .I5(uniform[52]),
        .O(\sample[3]_INST_0_i_67_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair38" *) 
  LUT3 #(
    .INIT(8'h7E)) 
    \sample[3]_INST_0_i_68 
       (.I0(uniform[61]),
        .I1(uniform[63]),
        .I2(uniform[62]),
        .O(\sample[3]_INST_0_i_68_n_0 ));
  LUT6 #(
    .INIT(64'hEFAAEFEFAAAAAAAA)) 
    \sample[3]_INST_0_i_69 
       (.I0(\sample[3]_INST_0_i_73_n_0 ),
        .I1(\sample[3]_INST_0_i_74_n_0 ),
        .I2(\sample[3]_INST_0_i_75_n_0 ),
        .I3(\sample[3]_INST_0_i_76_n_0 ),
        .I4(uniform[64]),
        .I5(\sample[3]_INST_0_i_77_n_0 ),
        .O(\sample[3]_INST_0_i_69_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair32" *) 
  LUT5 #(
    .INIT(32'h4400F700)) 
    \sample[3]_INST_0_i_7 
       (.I0(uniform[31]),
        .I1(uniform[27]),
        .I2(uniform[30]),
        .I3(uniform[28]),
        .I4(uniform[29]),
        .O(\sample[3]_INST_0_i_7_n_0 ));
  LUT6 #(
    .INIT(64'h15000055AAFFAAFF)) 
    \sample[3]_INST_0_i_70 
       (.I0(uniform[62]),
        .I1(uniform[65]),
        .I2(uniform[64]),
        .I3(uniform[59]),
        .I4(uniform[63]),
        .I5(uniform[61]),
        .O(\sample[3]_INST_0_i_70_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair65" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[3]_INST_0_i_71 
       (.I0(uniform[57]),
        .I1(uniform[56]),
        .O(\sample[3]_INST_0_i_71_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair35" *) 
  LUT2 #(
    .INIT(4'h1)) 
    \sample[3]_INST_0_i_72 
       (.I0(uniform[60]),
        .I1(uniform[61]),
        .O(\sample[3]_INST_0_i_72_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair63" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[3]_INST_0_i_73 
       (.I0(uniform[59]),
        .I1(uniform[62]),
        .O(\sample[3]_INST_0_i_73_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair55" *) 
  LUT3 #(
    .INIT(8'h2A)) 
    \sample[3]_INST_0_i_74 
       (.I0(uniform[68]),
        .I1(uniform[69]),
        .I2(uniform[65]),
        .O(\sample[3]_INST_0_i_74_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair3" *) 
  LUT5 #(
    .INIT(32'hE0000000)) 
    \sample[3]_INST_0_i_75 
       (.I0(uniform[67]),
        .I1(uniform[68]),
        .I2(uniform[63]),
        .I3(uniform[64]),
        .I4(uniform[66]),
        .O(\sample[3]_INST_0_i_75_n_0 ));
  LUT6 #(
    .INIT(64'hFF5FC05FFFF00000)) 
    \sample[3]_INST_0_i_76 
       (.I0(uniform[68]),
        .I1(uniform[69]),
        .I2(uniform[67]),
        .I3(uniform[66]),
        .I4(uniform[65]),
        .I5(uniform[63]),
        .O(\sample[3]_INST_0_i_76_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair5" *) 
  LUT5 #(
    .INIT(32'hEAAFAFFF)) 
    \sample[3]_INST_0_i_77 
       (.I0(uniform[64]),
        .I1(uniform[67]),
        .I2(uniform[63]),
        .I3(uniform[65]),
        .I4(uniform[66]),
        .O(\sample[3]_INST_0_i_77_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFFFF7F0000)) 
    \sample[3]_INST_0_i_8 
       (.I0(uniform[32]),
        .I1(uniform[30]),
        .I2(uniform[29]),
        .I3(uniform[33]),
        .I4(\sample[3]_INST_0_i_25_n_0 ),
        .I5(\sample[3]_INST_0_i_26_n_0 ),
        .O(\sample[3]_INST_0_i_8_n_0 ));
  LUT6 #(
    .INIT(64'h003F3C3C383F3C3C)) 
    \sample[3]_INST_0_i_9 
       (.I0(uniform[28]),
        .I1(uniform[25]),
        .I2(uniform[26]),
        .I3(uniform[23]),
        .I4(uniform[24]),
        .I5(uniform[27]),
        .O(\sample[3]_INST_0_i_9_n_0 ));
  LUT6 #(
    .INIT(64'h55555554FFFFFFFF)) 
    \sample[4]_INST_0 
       (.I0(\sample[4]_INST_0_i_1_n_0 ),
        .I1(\sample[4]_INST_0_i_2_n_0 ),
        .I2(\sample[4]_INST_0_i_3_n_0 ),
        .I3(\sample[4]_INST_0_i_4_n_0 ),
        .I4(\sample[4]_INST_0_i_5_n_0 ),
        .I5(\sample[4]_INST_0_i_6_n_0 ),
        .O(sample[4]));
  LUT6 #(
    .INIT(64'hFFFFFFFF00505544)) 
    \sample[4]_INST_0_i_1 
       (.I0(\sample[4]_INST_0_i_7_n_0 ),
        .I1(uniform[56]),
        .I2(uniform[54]),
        .I3(uniform[57]),
        .I4(uniform[53]),
        .I5(\sample[4]_INST_0_i_8_n_0 ),
        .O(\sample[4]_INST_0_i_1_n_0 ));
  LUT6 #(
    .INIT(64'hF7FFFFFFF7F7F7F7)) 
    \sample[4]_INST_0_i_10 
       (.I0(uniform[56]),
        .I1(uniform[62]),
        .I2(\sample[4]_INST_0_i_17_n_0 ),
        .I3(uniform[60]),
        .I4(uniform[64]),
        .I5(uniform[63]),
        .O(\sample[4]_INST_0_i_10_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair31" *) 
  LUT5 #(
    .INIT(32'hFFDFFFFF)) 
    \sample[4]_INST_0_i_11 
       (.I0(uniform[65]),
        .I1(uniform[66]),
        .I2(uniform[61]),
        .I3(uniform[67]),
        .I4(uniform[64]),
        .O(\sample[4]_INST_0_i_11_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair0" *) 
  LUT2 #(
    .INIT(4'h2)) 
    \sample[4]_INST_0_i_12 
       (.I0(uniform[54]),
        .I1(uniform[60]),
        .O(\sample[4]_INST_0_i_12_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair62" *) 
  LUT3 #(
    .INIT(8'h04)) 
    \sample[4]_INST_0_i_13 
       (.I0(uniform[63]),
        .I1(uniform[60]),
        .I2(uniform[62]),
        .O(\sample[4]_INST_0_i_13_n_0 ));
  LUT5 #(
    .INIT(32'hFFFFFFFE)) 
    \sample[4]_INST_0_i_14 
       (.I0(uniform[74]),
        .I1(uniform[76]),
        .I2(uniform[77]),
        .I3(uniform[75]),
        .I4(\sample[4]_INST_0_i_24_n_0 ),
        .O(\sample[4]_INST_0_i_14_n_0 ));
  LUT5 #(
    .INIT(32'hFFFFFFFE)) 
    \sample[4]_INST_0_i_15 
       (.I0(uniform[85]),
        .I1(uniform[84]),
        .I2(uniform[83]),
        .I3(uniform[82]),
        .I4(\sample[4]_INST_0_i_25_n_0 ),
        .O(\sample[4]_INST_0_i_15_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair50" *) 
  LUT3 #(
    .INIT(8'hFE)) 
    \sample[4]_INST_0_i_16 
       (.I0(uniform[95]),
        .I1(uniform[96]),
        .I2(uniform[94]),
        .O(\sample[4]_INST_0_i_16_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair37" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[4]_INST_0_i_17 
       (.I0(uniform[59]),
        .I1(uniform[58]),
        .O(\sample[4]_INST_0_i_17_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFF7FFF)) 
    \sample[4]_INST_0_i_18 
       (.I0(uniform[35]),
        .I1(uniform[34]),
        .I2(uniform[41]),
        .I3(uniform[42]),
        .I4(\sample[4]_INST_0_i_26_n_0 ),
        .I5(\sample[4]_INST_0_i_27_n_0 ),
        .O(\sample[4]_INST_0_i_18_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFFF7FFFFFF)) 
    \sample[4]_INST_0_i_19 
       (.I0(uniform[8]),
        .I1(uniform[11]),
        .I2(\sample[4]_INST_0_i_28_n_0 ),
        .I3(uniform[2]),
        .I4(uniform[6]),
        .I5(\sample[4]_INST_0_i_29_n_0 ),
        .O(\sample[4]_INST_0_i_19_n_0 ));
  LUT6 #(
    .INIT(64'h2233223303033303)) 
    \sample[4]_INST_0_i_2 
       (.I0(\sample[4]_INST_0_i_9_n_0 ),
        .I1(\sample[4]_INST_0_i_10_n_0 ),
        .I2(\sample[4]_INST_0_i_11_n_0 ),
        .I3(uniform[61]),
        .I4(uniform[60]),
        .I5(uniform[63]),
        .O(\sample[4]_INST_0_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hF7FFFFFFFFFFFFFF)) 
    \sample[4]_INST_0_i_20 
       (.I0(uniform[38]),
        .I1(uniform[40]),
        .I2(\sample[4]_INST_0_i_30_n_0 ),
        .I3(\sample[4]_INST_0_i_31_n_0 ),
        .I4(uniform[22]),
        .I5(uniform[19]),
        .O(\sample[4]_INST_0_i_20_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFF7FFFFFFF)) 
    \sample[4]_INST_0_i_21 
       (.I0(uniform[3]),
        .I1(uniform[37]),
        .I2(uniform[24]),
        .I3(uniform[26]),
        .I4(\sample[4]_INST_0_i_32_n_0 ),
        .I5(\sample[4]_INST_0_i_33_n_0 ),
        .O(\sample[4]_INST_0_i_21_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFFBFFFFFFF)) 
    \sample[4]_INST_0_i_22 
       (.I0(\sample[4]_INST_0_i_34_n_0 ),
        .I1(uniform[39]),
        .I2(uniform[0]),
        .I3(uniform[25]),
        .I4(uniform[10]),
        .I5(\sample[4]_INST_0_i_35_n_0 ),
        .O(\sample[4]_INST_0_i_22_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFF3383)) 
    \sample[4]_INST_0_i_23 
       (.I0(uniform[62]),
        .I1(uniform[54]),
        .I2(uniform[56]),
        .I3(uniform[58]),
        .I4(\sample[3]_INST_0_i_37_n_0 ),
        .I5(\sample[4]_INST_0_i_36_n_0 ),
        .O(\sample[4]_INST_0_i_23_n_0 ));
  LUT5 #(
    .INIT(32'hFFFFFFFE)) 
    \sample[4]_INST_0_i_24 
       (.I0(uniform[93]),
        .I1(uniform[92]),
        .I2(uniform[90]),
        .I3(uniform[91]),
        .I4(\sample[4]_INST_0_i_37_n_0 ),
        .O(\sample[4]_INST_0_i_24_n_0 ));
  LUT4 #(
    .INIT(16'hFFFE)) 
    \sample[4]_INST_0_i_25 
       (.I0(uniform[80]),
        .I1(uniform[81]),
        .I2(uniform[78]),
        .I3(uniform[79]),
        .O(\sample[4]_INST_0_i_25_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair58" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[4]_INST_0_i_26 
       (.I0(uniform[50]),
        .I1(uniform[55]),
        .O(\sample[4]_INST_0_i_26_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair40" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[4]_INST_0_i_27 
       (.I0(uniform[47]),
        .I1(uniform[48]),
        .O(\sample[4]_INST_0_i_27_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair19" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[4]_INST_0_i_28 
       (.I0(uniform[28]),
        .I1(uniform[30]),
        .O(\sample[4]_INST_0_i_28_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair59" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[4]_INST_0_i_29 
       (.I0(uniform[46]),
        .I1(uniform[45]),
        .O(\sample[4]_INST_0_i_29_n_0 ));
  LUT6 #(
    .INIT(64'h3000800000008000)) 
    \sample[4]_INST_0_i_3 
       (.I0(\sample[4]_INST_0_i_12_n_0 ),
        .I1(uniform[59]),
        .I2(uniform[56]),
        .I3(uniform[61]),
        .I4(uniform[58]),
        .I5(\sample[4]_INST_0_i_13_n_0 ),
        .O(\sample[4]_INST_0_i_3_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair68" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[4]_INST_0_i_30 
       (.I0(uniform[43]),
        .I1(uniform[44]),
        .O(\sample[4]_INST_0_i_30_n_0 ));
  LUT2 #(
    .INIT(4'h8)) 
    \sample[4]_INST_0_i_31 
       (.I0(uniform[13]),
        .I1(uniform[16]),
        .O(\sample[4]_INST_0_i_31_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair52" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \sample[4]_INST_0_i_32 
       (.I0(uniform[14]),
        .I1(uniform[17]),
        .O(\sample[4]_INST_0_i_32_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair57" *) 
  LUT2 #(
    .INIT(4'h7)) 
    \sample[4]_INST_0_i_33 
       (.I0(uniform[51]),
        .I1(uniform[52]),
        .O(\sample[4]_INST_0_i_33_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair47" *) 
  LUT4 #(
    .INIT(16'h7FFF)) 
    \sample[4]_INST_0_i_34 
       (.I0(uniform[18]),
        .I1(uniform[15]),
        .I2(uniform[29]),
        .I3(uniform[27]),
        .O(\sample[4]_INST_0_i_34_n_0 ));
  LUT5 #(
    .INIT(32'hBFFFFFFF)) 
    \sample[4]_INST_0_i_35 
       (.I0(\sample[4]_INST_0_i_38_n_0 ),
        .I1(uniform[5]),
        .I2(uniform[31]),
        .I3(uniform[1]),
        .I4(uniform[49]),
        .O(\sample[4]_INST_0_i_35_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair22" *) 
  LUT3 #(
    .INIT(8'h7F)) 
    \sample[4]_INST_0_i_36 
       (.I0(uniform[23]),
        .I1(uniform[20]),
        .I2(uniform[21]),
        .O(\sample[4]_INST_0_i_36_n_0 ));
  LUT4 #(
    .INIT(16'hFFFE)) 
    \sample[4]_INST_0_i_37 
       (.I0(uniform[87]),
        .I1(uniform[86]),
        .I2(uniform[88]),
        .I3(uniform[89]),
        .O(\sample[4]_INST_0_i_37_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair15" *) 
  LUT3 #(
    .INIT(8'h7F)) 
    \sample[4]_INST_0_i_38 
       (.I0(uniform[32]),
        .I1(uniform[36]),
        .I2(uniform[33]),
        .O(\sample[4]_INST_0_i_38_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair54" *) 
  LUT4 #(
    .INIT(16'h0407)) 
    \sample[4]_INST_0_i_4 
       (.I0(uniform[54]),
        .I1(uniform[53]),
        .I2(uniform[57]),
        .I3(uniform[56]),
        .O(\sample[4]_INST_0_i_4_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair29" *) 
  LUT5 #(
    .INIT(32'hAAAAAABA)) 
    \sample[4]_INST_0_i_5 
       (.I0(\sample[4]_INST_0_i_7_n_0 ),
        .I1(uniform[56]),
        .I2(uniform[58]),
        .I3(uniform[59]),
        .I4(uniform[60]),
        .O(\sample[4]_INST_0_i_5_n_0 ));
  LUT5 #(
    .INIT(32'h00000001)) 
    \sample[4]_INST_0_i_6 
       (.I0(\sample[4]_INST_0_i_14_n_0 ),
        .I1(\sample[4]_INST_0_i_15_n_0 ),
        .I2(uniform[72]),
        .I3(uniform[73]),
        .I4(\sample[4]_INST_0_i_16_n_0 ),
        .O(\sample[4]_INST_0_i_6_n_0 ));
  LUT6 #(
    .INIT(64'h0000000000000008)) 
    \sample[4]_INST_0_i_7 
       (.I0(uniform[53]),
        .I1(uniform[56]),
        .I2(uniform[57]),
        .I3(uniform[60]),
        .I4(uniform[61]),
        .I5(\sample[4]_INST_0_i_17_n_0 ),
        .O(\sample[4]_INST_0_i_7_n_0 ));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFFFFFE)) 
    \sample[4]_INST_0_i_8 
       (.I0(\sample[4]_INST_0_i_18_n_0 ),
        .I1(\sample[4]_INST_0_i_19_n_0 ),
        .I2(\sample[4]_INST_0_i_20_n_0 ),
        .I3(\sample[4]_INST_0_i_21_n_0 ),
        .I4(\sample[4]_INST_0_i_22_n_0 ),
        .I5(\sample[4]_INST_0_i_23_n_0 ),
        .O(\sample[4]_INST_0_i_8_n_0 ));
  LUT6 #(
    .INIT(64'h0820000000200008)) 
    \sample[4]_INST_0_i_9 
       (.I0(uniform[66]),
        .I1(uniform[65]),
        .I2(uniform[68]),
        .I3(uniform[69]),
        .I4(uniform[67]),
        .I5(uniform[70]),
        .O(\sample[4]_INST_0_i_9_n_0 ));
endmodule

(* STRUCTURAL_NETLIST = "yes" *)
module base_sampler_pla_reg
   (clk,
    uniform,
    sample);
  input clk;
  input [71:0]uniform;
  output [4:0]sample;

  wire \<const0> ;
  wire \<const1> ;
  wire [4:0]_sample;
  wire [71:0]_uniform;
  wire clk;
  wire [4:0]sample;
  wire [71:0]uniform;

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
  base_sampler_pla inst
       (.sample(_sample),
        .uniform({\<const0> ,\<const0> ,\<const0> ,\<const0> ,\<const0> ,\<const0> ,\<const0> ,\<const0> ,\<const0> ,\<const0> ,\<const0> ,\<const0> ,\<const0> ,\<const0> ,\<const0> ,\<const0> ,\<const0> ,\<const0> ,\<const0> ,\<const0> ,\<const0> ,\<const0> ,\<const0> ,\<const0> ,\<const0> ,_uniform}));
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
endmodule
`endif
