from parse_test_vector import load_samplerz_1024_json, float64_to_hex, float64_to_bitstring

samplerz = load_samplerz_1024_json()

# get mu and sigmas for verilog testbench
sigma_to_mus = {}
for sz in samplerz:
    sigma = sz['1/sigma']
    mu = sz['mu']
    if sigma not in sigma_to_mus:
        sigma_to_mus[sigma] = []
    sigma_to_mus[sigma].append(mu)
sigma_to_mus = [x for x in sigma_to_mus.items() if len(x[1]) == 2]
sigma_to_mus.sort(key=lambda x: x[0])

with open('samplerz1024_sigma_mus_dataset.sv', 'w') as file:
    file.write("""
typedef struct {
    logic [63:0] sigma_inv, mu1, mu2;
} testcase_sigma_mu_t;

""")
    file.write(f"testcase_sigma_mu_t testcases_sigma_mu [{len(sigma_to_mus)}] = '{"{"}\n")

    for i, (sigma, mus) in enumerate(sigma_to_mus):
        if len(mus) == 2:
            file.write("    '{64'h%s, 64'h%s, 64'h%s}%s\n" % (
                float64_to_hex(sigma),
                float64_to_hex(mus[0]),
                float64_to_hex(mus[1]),
                ',' if i < len(sigma_to_mus) - 1 else ''
            ))

    file.write("};\n")
