import csv
import math
import struct
from dataclasses import dataclass
from typing import Optional

from sage.rings.real_mpfr import RealField

# Set the desired calculation precision in bits
precision_bits = 400
RRR = RealField(precision_bits)
# field for printing outputs
P = RealField(64)

needed_bound_error = RRR(2) ** -43.5
approxexp_bound_err1 = RRR(2) ** -47

# Helper: convert binary string to float using IEEE 754 (as in Python)
def bitstring_to_float64(bstr):
    import struct
    return struct.unpack('>d', int(bstr, 2).to_bytes(8, byteorder='big'))[0]

def hex_to_float64(hstr):
    return struct.unpack('>d', int(hstr, 16).to_bytes(8, byteorder='big'))[0]

# Safe exp
def safeexp(x):
    try:
        return RRR.exp(x)
    except:
        return RRR(0)

# vcdcat -x TestBench_flopoco_ieee_exp_comb_uid1115.vcd testbench_flopoco_ieee_exp_comb_uid1115.x[63:0] testbench_flopoco_ieee_exp_comb_uid1115.r[63:0] > flopoco5-exp-testcases.txt
# format:
_ = """
0 time
1 testbench_flopoco_ieee_exp_comb_uid1115.x[63:0]
2 testbench_flopoco_ieee_exp_comb_uid1115.r[63:0]

0                1                2 
===================================
0                U 3ff0000000000000
10000000 3fe62e42fefa39ef 3fffffffffffffff
20000000                0 3ff0000000000000
30000000 8000000000000000 3ff0000000000000
40000000 3ff0000000000000 4005bf0a8b145769
50000000 4000000000000000 401d8e64b8d4ddae
"""

@dataclass
class TestCase:
    time: int
    x: RRR
    ex: RRR

    s: Optional[RRR] = None
    r: Optional[RRR] = None

    er: Optional[RRR] = None
    er_real: Optional[RRR] = None

    err0: Optional[RRR] = None # abs(er - er_real)
    err1: Optional[RRR] = None # abs((er - er_real) / er_real)

    @classmethod
    def from_line(cls, line: str):
        parts = line.split()
        time = int(parts[0])
        x = hex_to_float64(parts[1])
        ex = hex_to_float64(parts[2])
        return cls(time, RRR(x), RRR(ex))

    def is_finite(self):
        return not any(x.is_infinity() or x.is_NaN() for x in [self.x, self.ex, self.r, self.er, self.er_real, self.err0, self.err1] if x is not None)

tests = []
with open("flopoco5-exp-testcases.txt", "r") as file:
    for line in file:
        if line.startswith("==========="):
            break

    for line in file:
        if 'U' in line or 'X' in line:
            continue
        tests.append(TestCase.from_line(line))

# we only care about x <= 0 for berexp
# also discard any infinities and NaNs
tests = [t for t in tests if t.x <= 0 and not t.x.is_infinity() and not t.x.is_NaN() and not t.ex.is_infinity() and not t.ex.is_NaN()]

# bounds on BerExp input according to "Generic, Efficient and Isochronous Gaussian Sampling over the Integers, Shuo Sun et al"
x_min_berexp = -64 * RRR.log2()
tests = [t for t in tests if x_min_berexp <= t.x <= 0]

print(f"Tests left after filtering with bounds on BerExp input: {len(tests)}")

tests.sort(key=lambda t: t.x)

for t in tests:
    x = t.x
    ex = t.ex
    ex_real = RRR(x).exp()
    t.er = ex
    t.er_real = ex_real
    t.err0 = (ex - ex_real).abs()
    if ex_real != 0:
        t.err1 = ((ex - ex_real) / ex_real).abs()
    else:
        t.err1 = None

# filter out any nans or infinities
tests = [t for t in tests if t.is_finite()]

x_min = min(-t.x for t in tests)
x_max = max(-t.x for t in tests)
print(f"-x_min = {P(x_min)}, -x_max = {P(x_max)}")

x = [-t.x for t in tests]
err0 = [t.err0 for t in tests]
err1 = [t.err1 for t in tests]

err0_max = max([x for x in err0 if x is not None])
err1_max = max([x for x in err1 if x is not None])

print(f"Absolute error max = {P(err0_max)}")
print(f"Relative error max = {P(err1_max)}")
print(f"Relative error max (log2) = {P(err1_max.log2())}")

print(f"Needed bound on relative error: 2^-43.5 = {P(needed_bound_error)}")

if err1_max <= needed_bound_error:
    print("Renyi error bound is satisfied")
else:
    print("Renyi error bound is NOT satisfied")

print(f"Achieved precision is {P(needed_bound_error / err1_max)} times better than needed")

def write_csv(path, tests):
    with open(path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "time",
            "x",
            "neg_x",
            "approx_exp",
            "real_exp",
            "absolute_error",
            "relative_error",
        ])
        for t in tests:
            writer.writerow([
                t.time,
                t.x,
                -t.x,
                t.er,
                t.er_real,
                t.err0,
                "" if t.err1 is None else t.err1,
            ])

write_csv("flopoco5-exp-testcases.csv", tests)
print("Wrote data CSV to flopoco5-exp-testcases.csv")

import matplotlib.pyplot as plt

def log2_tick_label(value, _pos):
    if value <= 0:
        return ""
    exponent = int(round(math.log2(value)))
    return f"$2^{{{exponent}}}$"

def set_base2_y_axis(ax):
    from matplotlib.ticker import FuncFormatter, LogLocator, NullFormatter

    ax.set_yscale("log", base=2)
    ax.yaxis.set_major_locator(LogLocator(base=2, numticks=8))
    ax.yaxis.set_major_formatter(FuncFormatter(log2_tick_label))
    ax.yaxis.set_minor_formatter(NullFormatter())

fig, axs = plt.subplots(2)

axs[0].scatter(x, err0, color='red', label='absolute error', s=1, rasterized=True)
plt.setp(axs[0], ylim=[10 ** -38, 10 ** -15])
axs[1].scatter(x, err1, color='green', label='relative error', s=1, rasterized=True)
axs[1].axhline(
    float(needed_bound_error),
    color="red",
    linestyle="--",
    linewidth=1,
    label="maximum acceptable error",
)
plt.setp(axs[1], ylim=[10 ** -22, float(needed_bound_error) * 2])

for ax in axs:
    set_base2_y_axis(ax)
    ax.set_xscale('linear')
    ax.set_xlabel('-x')
    # ax.set_ylabel('error')
    ax.legend()

fig.tight_layout()
plt.savefig("flopoco5-exp-testcases.svg", dpi=600)
plt.show()
