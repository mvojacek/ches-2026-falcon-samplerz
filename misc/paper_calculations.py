# Run from the repository root: python3 misc/paper_calculations.py
P = 0.575752
RESOURCES = ("LUT", "FF", "DSP", "BRAM36")

# Values identical to paper tables 5 and 6
# TTFS/TTNS in clock cycles, area in LUT/FF/DSP/BRAM36
IMPLEMENTATIONS = {
    "KA23": dict(ttfs=1807, ttns=1807, mhz=121, model="serial", loops=1,
                 area=(4068, 3202, 9, 2)),
    "YSZ+24": dict(ttfs=104, ttns=104, mhz=83, model="serial", loops=1,
                   area=(4761, 692, 9, 0)),
    "OZZ+25": dict(ttfs=67, ttns=40, mhz=185, model="serial", loops=1,
                   area=(9368, 4527, 76, 0)),
    "ZASM25": dict(ttfs=59, ttns=34, mhz=150, model="reported", loops=1, pair_cycles=106.1,
                   area=(7603, 3880, 85, 0)),
    "PMKA25 C1": dict(ttfs=22, ttns=22, mhz=135, model="serial", loops=1,
                      area=(7000, 4000, 94, 2.5)),
    "PMKA25 C3": dict(ttfs=22, ttns=22, mhz=131, model="serial", loops=3,
                      area=(15000, 9000, 254, 7.5)),
    "This work": dict(ttfs=19, ttns=1, mhz=222, model="alternating", loops=1,
                      area=(7039, 3431, 30, 1.5)),
}

# Counters from measured hardware runs: sw/reports/many_oneshots2.txt:50-56, sw/reports/long_continuous.txt:149-157
MEASURED = {
    "oneshot": dict(busy_cycles=2148650955, pairs=97000001, bits=17969370040),
    "continuous": dict(busy_cycles=39401813069859, z1=11335203828541, z2=11335201672628,
                       bits=354098286711432),
}

# Equations 5-8 from the paper
def serial(ttfs, ttns, p=P):
    # Unsimplified (paper) form: 2 * (p * ttfs + (1 - p) * (ttfs + ttns / p))
    return 2 * (ttfs + (1 - p) * ttns / p)

def alternating(ttfs, ttns, p=P):
    # Unsimplified (paper) form: p * (ttfs + (2 / p - 1) * ttns)
    #        + (1 - p) * (ttfs + ttns / p + (2 / p - 1) * ttns)
    return ttfs + (3 - 2 * p) * ttns / p

def parallel_last(ttfs, ttns, p=P):
    # Unsimplified (paper) form: p ** 2 * ttfs + 2 * p * (1 - p) * (ttfs + ttns / p)
    #        + (1 - p) ** 2 * (ttfs + (2 / p - 1 / (1 - (1 - p) ** 2)) * ttns)
    return ttfs + (1 - p) * (3 - p) * ttns / (p * (2 - p))

def parallel_both(ttfs, ttns, p=P):
    # Unsimplified (paper) form: p ** 2 * ttfs + (1 - p ** 2) * (ttfs + ttns / p ** 2)
    return ttfs + (1 - p ** 2) * ttns / p ** 2

def parallel_probability(loops, p=P):
    return 1 - (1 - p) ** loops


def cycles_to_ns(cycles, mhz):
    return cycles * 1000 / mhz

def time_area(ns, area):
    return tuple(ns * count for count in area)


def characteristics(implementation):
    p = parallel_probability(implementation["loops"])
    if implementation["model"] == "reported":
        cycles = implementation["pair_cycles"]
    elif implementation["model"] == "alternating":
        cycles = alternating(implementation["ttfs"], implementation["ttns"], p)
    else:
        cycles = serial(implementation["ttfs"], implementation["ttns"], p)
    ns = cycles_to_ns(cycles, implementation["mhz"])
    return cycles, ns, time_area(ns, implementation["area"])


def main():
    _, baseline_ns, baseline_products = characteristics(IMPLEMENTATIONS["This work"])
    print(f"p={P}; TTFS/TTNS in cycles; RIPST per pair; ratios relative to This work")
    print("\nSampling latency and time ratios")
    print(f"{'Implementation':<14} {'Model':<12} {'TTFS':>6} {'TTNS':>6} {'MHz':>6} {'Loops':>5} {'RIPST(cyc)':>11} {'RIPST(ns)':>12} {'Time ratio':>10}")
    for name, implementation in IMPLEMENTATIONS.items():
        cycles, ns, products = characteristics(implementation)
        print(f"{name:<14} {implementation['model']:<12} {implementation['ttfs']:6,} {implementation['ttns']:6,} {implementation['mhz']:6,} {implementation['loops']:5,} {cycles:11,.3f} {ns:12,.3f} {ns / baseline_ns:10,.3f}")
    print("\nTime-area products (ns × resource); parentheses: normalized product")
    print(f"{'Implementation':<14}" + "".join(f"{resource:>28}" for resource in RESOURCES))
    for name, implementation in IMPLEMENTATIONS.items():
        cycles, ns, products = characteristics(implementation)
        print(f"{name:<14}" + "".join(f"{product:17,.1f} ({product / baseline:7,.3f}x)" for product, baseline in zip(products, baseline_products)))
    one, continuous = MEASURED["oneshot"], MEASURED["continuous"]
    samples = continuous["z1"] + continuous["z2"]
    print("\nHardware run statistics")
    print(f"One-shot:   {one['busy_cycles'] / one['pairs']:,.6f} busy cycles/pair; {one['bits'] / one['pairs']:,.6f} bits/pair; {one['pairs']:,} pairs")
    print(f"Continuous: {continuous['busy_cycles'] / samples:,.6f} busy cycles/sample; {continuous['bits'] / samples:,.6f} bits/sample; {samples:,} samples")


if __name__ == "__main__":
    main()
