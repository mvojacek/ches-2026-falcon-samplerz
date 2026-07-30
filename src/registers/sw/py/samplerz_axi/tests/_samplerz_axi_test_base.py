


"""
Unit Tests for the samplerz_axi register model Python Wrapper

This code was generated from the PeakRDL-python package version 1.1.0
"""
from array import array as Array

import unittest



from ..lib import RegisterWriteVerifyError

from ..lib import NormalCallbackSet, NormalCallbackSetLegacy



from ..reg_model.samplerz_axi import samplerz_axi_cls

from ..sim_lib.dummy_callbacks import dummy_read as read_addr_space
from ..sim_lib.dummy_callbacks import dummy_write as write_addr_space
from ..sim_lib.dummy_callbacks import dummy_read_block as read_block_addr_space
from ..sim_lib.dummy_callbacks import dummy_write_block as write_block_addr_space
from ..sim_lib.dummy_callbacks import dummy_read_block_legacy as read_block_addr_space_alt
from ..sim_lib.dummy_callbacks import dummy_write_block_legacy as write_block_addr_space_alt


def read_callback(addr: int, width: int, accesswidth: int) -> int:
    return read_addr_space(addr=addr, width=width, accesswidth=accesswidth)

def read_block_callback(addr: int, width: int, accesswidth: int, length: int) -> list[int]:
    return read_block_addr_space(addr=addr, width=width, accesswidth=accesswidth, length=length)

def read_block_callback_alt(addr: int, width: int, accesswidth: int, length: int) -> Array:
    return read_block_addr_space_alt(addr=addr, width=width, accesswidth=accesswidth, length=length)

def write_callback(addr: int, width: int, accesswidth: int,  data: int) -> None:
    write_addr_space(addr=addr, width=width, accesswidth=accesswidth, data=data)

def write_block_callback(addr: int, width: int, accesswidth: int,  data: list[int]) -> None:
    write_block_addr_space(addr=addr, width=width, accesswidth=accesswidth, data=data)

def write_block_callback_alt(addr: int, width: int, accesswidth: int,  data: Array) -> None:
    write_block_addr_space_alt(addr=addr, width=width, accesswidth=accesswidth, data=data)



TestCaseBase = unittest.TestCase


class samplerz_axi_TestCase(TestCaseBase): # type: ignore[valid-type,misc]

    def setUp(self) -> None:
        self.dut = samplerz_axi_cls(callbacks=NormalCallbackSet(read_callback=read_callback,
                                                          write_callback=write_callback))

    @staticmethod
    def _reverse_bits(value: int, number_bits: int) -> int:
        """

        Args:
            value: value to reverse
            number_bits: number of bits used in the value

        Returns:
            reversed valued
        """
        result = 0
        for i in range(number_bits):
            if (value >> i) & 1:
                result |= 1 << (number_bits - 1 - i)
        return result

class samplerz_axi_TestCase_BlockAccess(TestCaseBase): # type: ignore[valid-type,misc]

    def setUp(self) -> None:
        self.dut = samplerz_axi_cls(callbacks=NormalCallbackSet(read_callback=read_callback,
                                                          write_callback=write_callback,
                                                          read_block_callback=read_block_callback,
                                                          write_block_callback=write_block_callback))

class samplerz_axi_TestCase_AltBlockAccess(TestCaseBase): # type: ignore[valid-type,misc]
    """
    Based test to use with the alternative call backs, this allow the legacy output API to be tested
    with the new callbacks and visa versa.
    """

    def setUp(self) -> None:
        self.dut = samplerz_axi_cls(callbacks=NormalCallbackSetLegacy(
                                                          read_callback=read_callback,
                                                          write_callback=write_callback,
                                                          read_block_callback=read_block_callback_alt,
                                                          write_block_callback=write_block_callback_alt))




if __name__ == '__main__':
    pass



