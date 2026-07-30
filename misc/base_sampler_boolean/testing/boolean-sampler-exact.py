#!/usr/bin/env sage --python

from sage.all import RealField

def parse_espresso_line(line):
    line = line.strip()
    parts = line.split()
    if len(parts) != 2:
        return None, None, None  # skip if malformed
    left, right = parts
    total_bits = len(left)
    dash_count = left.count('-')
    return total_bits, dash_count, right


R = RealField(400)
RP = RealField(64)
output_probabilities = {}
used_bits_probabilities = {}

with open("tree.txt", 'r') as f:
    for raw_line in f:
        line = raw_line.strip()

        if not line or line.startswith('.') or line.startswith('#'):
            continue

        total_bits, dash_count, out_val = parse_espresso_line(line)
        # If malformed or no tokens, skip
        if total_bits is None:
            continue

        defined_bits = total_bits - dash_count
        probability = R(1) / (2 ** defined_bits)

        if out_val not in output_probabilities:
            output_probabilities[out_val] = R(0)
        output_probabilities[out_val] += probability

        if defined_bits not in used_bits_probabilities:
            used_bits_probabilities[defined_bits] = R(0)
        used_bits_probabilities[defined_bits] += probability

print("Output PDT (2^72):")
for out_pattern, prob in sorted(output_probabilities.items()):
    print(f"{out_pattern} -> {int(prob * (R(2) ** 72))}")
print(f"Total: {int(sum(output_probabilities.values()) * (R(2) ** 72))}")
print("\nUsed bits PDT (1.0):")
for used_bits, prob in sorted(used_bits_probabilities.items()):
    print(f"{used_bits} -> {RP(prob)}")
print(f"Total: {RP(sum(used_bits_probabilities.values()))}")
print(f"Expected value: {RP(sum(used_bits * prob for used_bits, prob in used_bits_probabilities.items()))}")