#!/usr/bin/env python3

# Invoked by just zcu-report after Vivado generates the reports.
# Copies over the generated reports from the ZCU104 vivado run into out/reports/

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "out/reports/zcu104-samplerz"


def redact(text):
    text = text.replace(str(ROOT), "<repository>")
    text = re.sub(r"/(?:home|tools)/[^\s\"'<>|;,)]+", "<local-path>", text)
    return re.sub(r"(?m)^(\s*\|?\s*Host\s*:).*$", r"\1 <redacted>", text)


for path in REPORTS.iterdir():
    if path.suffix in (".rpt", ".txt"):
        path.write_text(redact(path.read_text()))

utilization = (REPORTS / "utilization.rpt").read_text()
timing = (REPORTS / "timing-summary.rpt").read_text()
power = (REPORTS / "power.rpt").read_text()


def used(resource):
    return re.search(r"\| " + re.escape(resource) + r"\s*\|\s*([\d.]+)", utilization)[1]


period = re.search(r"(?m)^clk\s+\{[^}]+\}\s+([\d.]+)", timing)[1]
slacks = re.search(r"WNS\(ns\).*\n\s*[-\s]+\n([^\n]+)", timing)[1].split()
watts = re.search(r"Total On-Chip Power \(W\)\s*\|\s*([\d.]+)", power)[1]
summary = (
    f"Area: {used('CLB LUTs')} LUT, {used('CLB Registers')} FF, {used('DSPs')} DSP, {used('Block RAM Tile')} BRAM36\n"
    f"OOC clock period: {period} ns\n"
    f"Setup WNS/TNS: {slacks[0]}/{slacks[1]} ns; hold WHS/THS: {slacks[4]}/{slacks[5]} ns\n"
    f"Pulse-width slack: {slacks[8]} ns\n"
    f"Estimated power: {watts} W (vectorless, not board-measured)\n"
)
(REPORTS / "report_summary.txt").write_text(summary)
print(summary, end="")
