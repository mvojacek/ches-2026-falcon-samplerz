import numpy as np
from parse_test_vector import load_samplerz_1024_json, float64_to_bitstring

samplerz = load_samplerz_1024_json()

# generate verilog testcases from samplerz mu and r
with open('float_fractional_samplerzkat_testcases.sv', 'w') as file:
    for sz in samplerz:
        mu = sz['mu']
        r = sz['r']
        s = sz['s']
        f = mu
        num = s
        frac = r

        print(f"mu: {mu}, r: {r}, s: {s}, num: {num}, frac: {frac}")

        file.write(f'// Test case: {f} = {num} + {frac}\n')
        file.write(f'in   = 64\'b{float64_to_bitstring(f)};\n')
        file.write(f'ex   = 64\'b{float64_to_bitstring(frac)};\n')
        sign = '' if num >= 0 else '-'
        file.write(f'n_ex = {sign}64\'d{np.abs(np.int64(num))};\n')
        file.write(f'@(posedge clk);\n\n')
