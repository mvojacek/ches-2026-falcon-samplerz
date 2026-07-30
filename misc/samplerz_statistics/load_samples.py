import os
import struct
from dataclasses import dataclass

from saga import parse_univariate_file

def hex_to_float64(h):
    unpacked = int(h, 16)
    packed = struct.pack('>Q', unpacked)
    f = struct.unpack('>d', packed)[0]
    return f

@dataclass
class Samples:
    sigma: float
    mu: float
    samples: list[int]|None
    histogram: tuple[list[int], list[int]]|None
    filename: str|None

def parse_file(filepath):
    parts = os.path.splitext(os.path.basename(filepath))[0].split("_")
    sigma_inv = hex_to_float64(parts[0])
    mu = hex_to_float64(parts[1])

    with open(filepath, "r") as f:
        samples = [int(line.strip(), 10) for line in f if line.strip()]

    return Samples(1/sigma_inv, mu, samples, None, filepath)

def parse_saga_file(filepath):
    data = parse_univariate_file(filepath)
    return [Samples(sigma, mu, samples, None, filepath) for mu, sigma, samples in data]

def load_samples_sim():
    samplings = []
    for filename in os.listdir('samples_sim/'):
        if filename.endswith('.txt'):
            samplings.append(parse_file(os.path.join('samples_sim', filename)))
    samplings.sort(key=lambda s: (s.sigma, s.mu))
    return samplings

def load_samples_hw():
    samplings = []
    for filename in os.listdir('samples_hw/'):
        if filename.endswith('.txt'):
            samplings.append(parse_file(os.path.join('samples_hw', filename)))
    samplings.sort(key=lambda s: (s.sigma, s.mu))
    return samplings

def parse_hw_histogram(filepath):
    parts = os.path.splitext(os.path.basename(filepath))[0].split("_")
    sigma_inv = hex_to_float64(parts[0])
    mu = hex_to_float64(parts[1])

    with open(filepath, "r") as f:
        lines = f.readlines()

    unique_values = []
    counts = []
    for line in lines:
        parts = line.split(":")
        if len(parts) != 2:
            continue
        key, value = parts
        key = int(key.strip())
        value = int(value.strip())
        if value != 0:
            unique_values.append(key)
            counts.append(value)

    return Samples(1/sigma_inv, mu, None, (unique_values, counts), filepath)

def load_histograms_hw():
    samplings = []
    for filename in os.listdir('samples_hw_hist/'):
        if filename.endswith('.txt'):
            samplings.append(parse_hw_histogram(os.path.join('samples_hw_hist', filename)))
    samplings.sort(key=lambda s: (s.sigma, s.mu))
    return samplings
