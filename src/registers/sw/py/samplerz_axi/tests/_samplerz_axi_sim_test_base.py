


"""
Unit Tests for the samplerz_axi register model Python Wrapper

This code was generated from the PeakRDL-python package version 1.1.0
"""


import unittest



from ..lib import RegisterWriteVerifyError

from ..lib import NormalCallbackSet


from ._samplerz_axi_test_base import samplerz_axi_TestCase, samplerz_axi_TestCase_BlockAccess

from ..reg_model.samplerz_axi import samplerz_axi_cls
from ..sim.samplerz_axi import samplerz_axi_simulator_cls

class samplerz_axi_SimTestCase(samplerz_axi_TestCase): # type: ignore[valid-type,misc]

    def setUp(self) -> None:
        self.sim = samplerz_axi_simulator_cls(address=0)
        self.dut = samplerz_axi_cls(callbacks=NormalCallbackSet(read_callback=self.sim.read,
                                                          write_callback=self.sim.write))

class samplerz_axi_SimTestCase_BlockAccess(samplerz_axi_TestCase_BlockAccess): # type: ignore[valid-type,misc]

    def setUp(self) -> None:
        self.sim = samplerz_axi_simulator_cls(address=0)
        self.dut = samplerz_axi_cls(callbacks=NormalCallbackSet(read_callback=self.sim.read,
                                                          write_callback=self.sim.write,
                                                          read_block_callback=self.sim.read_block,
                                                          write_block_callback=self.sim.write_block))




if __name__ == '__main__':
    pass