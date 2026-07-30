from __future__ import annotations

import argparse
import operator
from functools import reduce
from typing import TextIO, Callable

from peakrdl.plugins.exporter import ExporterSubcommandPlugin
from systemrdl.node import AddressableNode, FieldNode, AddrmapNode, RegNode, Node, RegfileNode

__all__ = ["SVConstExporter"]

class SVConstExporter(ExporterSubcommandPlugin):
    short_desc = "Export constants for SystemVerilog"

    def __init__(self, indent_str: str = "  ") -> None:
        super().__init__("sv_const_exporter", "0.1")
        self.f: TextIO | None = None
        self._indent_str = indent_str
        self._indent_level = 0

    def do_export(self, top_node: AddrmapNode, options: argparse.Namespace) -> None:
        with open(options.output, "w") as f:
            self.export(top_node, f)

    def export(self, node: AddressableNode, output: TextIO) -> None:
        self.f = output
        pkg_name = f'{node.type_name}_map_pkg'
        self._write_header(pkg_name)
        self._visit(node)
        self._write_footer(pkg_name)
        self.f = None

    @property
    def indent(self) -> str:
        return self._indent_str * self._indent_level

    def indent_push(self) -> None:
        self._indent_level += 1

    def indent_pop(self) -> None:
        self._indent_level = max(0, self._indent_level - 1)

    def _write_header(self, pkg_name) -> None:
        self.f.write(f"package {pkg_name};\n\n")
        self.indent_push()
        self.f.write(f"{self.indent}// *** Auto‑generated. Do *not* hand‑edit. ***\n\n")

    def _write_footer(self, pkg_name) -> None:
        self.indent_pop()
        self.f.write(f"endpackage : {pkg_name}\n")

    def _visit(self, node: Node) -> None:
        if isinstance(node, AddressableNode):
            node.zero_lineage_index()
        if isinstance(node, RegfileNode):
            self._emit_regfile(node)
        if isinstance(node, RegNode):
            self._emit_register(node)
        if isinstance(node, FieldNode):
            self._emit_field(node)

        for child in node.children():  
            self._visit(child)

    # ------------------------------------------------------------------
    # Emission helpers
    # ------------------------------------------------------------------

    def _emit_regfile(self, node: RegfileNode) -> None:
        name = self._sv_name(node)
        self.f.write(
            f"{self.indent}localparam int unsigned {name}__ADDR = 'h{node.raw_absolute_address:X};\n"
        )
        self.f.write(
            f"{self.indent}localparam int unsigned {name}__OFFSET = 'h{node.address_offset:X};\n"
        )
        if node.is_array:
            size = reduce(operator.mul, node.array_dimensions, 1)
            self.f.write(
                f"{self.indent}localparam int unsigned {name}__ARRLEN = {size};\n"
            )
            self.f.write(
                f"{self.indent}localparam int unsigned {name}__STRIDE = {node.array_stride};\n"
            )

    def _emit_register(self, node: RegNode) -> None:
        name = self._sv_name(node)
        self.f.write(
            f"{self.indent}localparam int unsigned {name}__ADDR = 'h{node.raw_absolute_address:X};\n"
        )
        self.f.write(
            f"{self.indent}localparam int unsigned {name}__OFFSET = 'h{node.address_offset:X};\n"
        )
        if node.is_array:
            size = reduce(operator.mul, node.array_dimensions, 1)
            self.f.write(
                f"{self.indent}localparam int unsigned {name}__ARRLEN = {size};\n"
            )
            self.f.write(
                f"{self.indent}localparam int unsigned {name}__STRIDE = {node.array_stride};\n"
            )
    

    def _emit_field(self, field: FieldNode) -> None:  
        field_name = self._sv_name(field)
        reg_access_width = field.parent.get_property('accesswidth')
        acw_offset = field.lsb // reg_access_width
        addr_offset = field.lsb // 8
        self.f.write(
            f"{self.indent}localparam int unsigned {field_name}__REGOFF = 'h{addr_offset:X};\n"
        )
        if not field.parent.is_array:
            self.f.write(
                f"{self.indent}localparam int unsigned {field_name}__ADDR = 'h{field.parent.raw_absolute_address + addr_offset:X};\n"
            )
        lsb = field.lsb - (acw_offset * reg_access_width)
        self.f.write(
            f"{self.indent}localparam int unsigned {field_name}__LSB = {lsb};\n"
        )
        self.f.write(
            f"{self.indent}localparam int unsigned {field_name}__W = {field.width};\n"
        )
        mask = ((1 << field.width) - 1) << lsb
        pad = reg_access_width // 4
        self.f.write(
            f"{self.indent}localparam logic [{reg_access_width - 1}:0] {field_name}__MASK = {reg_access_width}'h{mask:0{pad}X};\n"
        )

    def _sv_name(self, node: Node) -> str:  
        name = node.get_path("__", "", "").upper()
        return name


if __name__ == "__main__":
    from systemrdl import RDLCompiler, RegNode, RegfileNode

    compiler = RDLCompiler()
    compiler.compile_file("../regblock_udps.rdl")
    compiler.compile_file("../samplerz_axi.rdl")
    root = compiler.elaborate()
    with open("../hw/samplerz_axi_map_pkg.sv", "w") as f:
        SVConstExporter().export(root.top, f)

