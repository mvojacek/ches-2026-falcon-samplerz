


"""
Unit Tests for the samplerz_axi register model Python Wrapper

This code was generated from the PeakRDL-python package version 1.1.0
"""


from typing import Union, cast

import unittest
from unittest.mock import Mock

import random
from enum import IntEnum

from ..sim_lib.register import Register,MemoryRegister
from ..sim_lib.field import Field

from ._samplerz_axi_sim_test_base import samplerz_axi_SimTestCase, samplerz_axi_SimTestCase_BlockAccess
from ._samplerz_axi_sim_test_base import __name__ as base_name

class samplerz_axi_single_access(samplerz_axi_SimTestCase): # type: ignore[valid-type,misc]

    def test_register_read_and_write(self) -> None:
        """
        Walk the register map and check every register can be read and written to correctly
        """
        # test access operations (read and/or write) to register:
        # samplerz_axi.marker
        with self.subTest(msg='register: samplerz_axi.marker'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.marker')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.marker.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.marker.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.marker.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.control
        with self.subTest(msg='register: samplerz_axi.control'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.control')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.control.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.control.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.control.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.control.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.control.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.control.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(self.dut.control.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.busy_cycles
        with self.subTest(msg='register: samplerz_axi.busy_cycles'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.busy_cycles')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.busy_cycles.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.busy_cycles.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.busy_cycles.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            self.dut.busy_cycles.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            self.dut.busy_cycles.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            self.dut.busy_cycles.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(self.dut.busy_cycles.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.consumed_bits
        with self.subTest(msg='register: samplerz_axi.consumed_bits'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.consumed_bits')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.consumed_bits.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.consumed_bits.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.consumed_bits.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            self.dut.consumed_bits.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            self.dut.consumed_bits.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            self.dut.consumed_bits.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(self.dut.consumed_bits.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sginv
        with self.subTest(msg='register: samplerz_axi.sginv'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sginv')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sginv.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sginv.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sginv.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            self.dut.sginv.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            self.dut.sginv.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            self.dut.sginv.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(self.dut.sginv.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.mu1
        with self.subTest(msg='register: samplerz_axi.mu1'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.mu1')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.mu1.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.mu1.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.mu1.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            self.dut.mu1.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            self.dut.mu1.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            self.dut.mu1.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(self.dut.mu1.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.mu2
        with self.subTest(msg='register: samplerz_axi.mu2'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.mu2')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.mu2.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.mu2.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.mu2.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            self.dut.mu2.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            self.dut.mu2.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            self.dut.mu2.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(self.dut.mu2.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.z1
        with self.subTest(msg='register: samplerz_axi.z1'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.z1')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.z1.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.z1.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.z1.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.z2
        with self.subTest(msg='register: samplerz_axi.z2'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.z2')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.z2.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.z2.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.z2.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.prng.seed[0]
        with self.subTest(msg='register: samplerz_axi.prng.seed[0]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.prng.seed[0]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[0].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[0].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.prng.seed[0].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.prng.seed[0].write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.prng.seed[0].write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.prng.seed[0].write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(self.dut.prng.seed[0].read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.prng.seed[1]
        with self.subTest(msg='register: samplerz_axi.prng.seed[1]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.prng.seed[1]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[1].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[1].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.prng.seed[1].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.prng.seed[1].write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.prng.seed[1].write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.prng.seed[1].write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(self.dut.prng.seed[1].read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.prng.seed[2]
        with self.subTest(msg='register: samplerz_axi.prng.seed[2]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.prng.seed[2]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[2].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[2].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.prng.seed[2].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.prng.seed[2].write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.prng.seed[2].write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.prng.seed[2].write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(self.dut.prng.seed[2].read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.prng.seed[3]
        with self.subTest(msg='register: samplerz_axi.prng.seed[3]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.prng.seed[3]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[3].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[3].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.prng.seed[3].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.prng.seed[3].write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.prng.seed[3].write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.prng.seed[3].write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(self.dut.prng.seed[3].read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.prng.seed[4]
        with self.subTest(msg='register: samplerz_axi.prng.seed[4]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.prng.seed[4]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[4].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[4].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.prng.seed[4].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.prng.seed[4].write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.prng.seed[4].write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.prng.seed[4].write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(self.dut.prng.seed[4].read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.prng.seed[5]
        with self.subTest(msg='register: samplerz_axi.prng.seed[5]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.prng.seed[5]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[5].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[5].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.prng.seed[5].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.prng.seed[5].write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.prng.seed[5].write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.prng.seed[5].write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(self.dut.prng.seed[5].read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.prng.seed[6]
        with self.subTest(msg='register: samplerz_axi.prng.seed[6]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.prng.seed[6]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[6].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[6].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.prng.seed[6].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.prng.seed[6].write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.prng.seed[6].write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.prng.seed[6].write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(self.dut.prng.seed[6].read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.prng.seed[7]
        with self.subTest(msg='register: samplerz_axi.prng.seed[7]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.prng.seed[7]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[7].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[7].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.prng.seed[7].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.prng.seed[7].write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.prng.seed[7].write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.prng.seed[7].write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(self.dut.prng.seed[7].read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.prng.seed[8]
        with self.subTest(msg='register: samplerz_axi.prng.seed[8]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.prng.seed[8]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[8].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[8].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.prng.seed[8].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.prng.seed[8].write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.prng.seed[8].write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.prng.seed[8].write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(self.dut.prng.seed[8].read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.prng.seed[9]
        with self.subTest(msg='register: samplerz_axi.prng.seed[9]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.prng.seed[9]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[9].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[9].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.prng.seed[9].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.prng.seed[9].write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.prng.seed[9].write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.prng.seed[9].write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(self.dut.prng.seed[9].read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.prng.seed[10]
        with self.subTest(msg='register: samplerz_axi.prng.seed[10]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.prng.seed[10]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[10].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[10].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.prng.seed[10].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.prng.seed[10].write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.prng.seed[10].write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            self.dut.prng.seed[10].write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(self.dut.prng.seed[10].read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.prng.counter
        with self.subTest(msg='register: samplerz_axi.prng.counter'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.prng.counter')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.counter.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.counter.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.prng.counter.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            self.dut.prng.counter.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            self.dut.prng.counter.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            self.dut.prng.counter.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(self.dut.prng.counter.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[0]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[0]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[0]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[0].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[0].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[0].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[1]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[1]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[1]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[1].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[1].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[1].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[2]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[2]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[2]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[2].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[2].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[2].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[3]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[3]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[3]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[3].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[3].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[3].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[4]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[4]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[4]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[4].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[4].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[4].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[5]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[5]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[5]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[5].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[5].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[5].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[6]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[6]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[6]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[6].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[6].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[6].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[7]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[7]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[7]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[7].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[7].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[7].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[8]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[8]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[8]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[8].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[8].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[8].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[9]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[9]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[9]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[9].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[9].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[9].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[10]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[10]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[10]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[10].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[10].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[10].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[11]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[11]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[11]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[11].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[11].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[11].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[12]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[12]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[12]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[12].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[12].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[12].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[13]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[13]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[13]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[13].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[13].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[13].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[14]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[14]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[14]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[14].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[14].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[14].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[15]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[15]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[15]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[15].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[15].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[15].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[16]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[16]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[16]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[16].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[16].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[16].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[17]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[17]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[17]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[17].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[17].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[17].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[18]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[18]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[18]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[18].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[18].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[18].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[19]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[19]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[19]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[19].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[19].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[19].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[20]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[20]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[20]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[20].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[20].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[20].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[21]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[21]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[21]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[21].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[21].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[21].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[22]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[22]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[22]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[22].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[22].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[22].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[23]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[23]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[23]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[23].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[23].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[23].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[24]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[24]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[24]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[24].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[24].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[24].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[25]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[25]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[25]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[25].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[25].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[25].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[26]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[26]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[26]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[26].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[26].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[26].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[27]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[27]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[27]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[27].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[27].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[27].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[28]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[28]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[28]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[28].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[28].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[28].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[29]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[29]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[29]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[29].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[29].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[29].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[30]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[30]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[30]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[30].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[30].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[30].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[31]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[31]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[31]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[31].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[31].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[31].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[32]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[32]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[32]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[32].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[32].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[32].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[33]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[33]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[33]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[33].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[33].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[33].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[34]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[34]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[34]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[34].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[34].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[34].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[35]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[35]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[35]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[35].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[35].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[35].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[36]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[36]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[36]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[36].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[36].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[36].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[37]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[37]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[37]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[37].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[37].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[37].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[38]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[38]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[38]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[38].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[38].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[38].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[39]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].histogram[39]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[39]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[39].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[39].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].histogram[39].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].pivot_value
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].pivot_value'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].pivot_value')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].pivot_value.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].pivot_value.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].pivot_value.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].pivot_index
        with self.subTest(msg='register: samplerz_axi.sample_histograms[0].pivot_index'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].pivot_index')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].pivot_index.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].pivot_index.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[0].pivot_index.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[0]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[0]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[0]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[0].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[0].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[0].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[1]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[1]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[1]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[1].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[1].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[1].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[2]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[2]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[2]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[2].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[2].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[2].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[3]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[3]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[3]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[3].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[3].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[3].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[4]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[4]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[4]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[4].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[4].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[4].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[5]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[5]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[5]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[5].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[5].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[5].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[6]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[6]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[6]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[6].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[6].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[6].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[7]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[7]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[7]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[7].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[7].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[7].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[8]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[8]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[8]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[8].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[8].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[8].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[9]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[9]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[9]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[9].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[9].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[9].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[10]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[10]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[10]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[10].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[10].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[10].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[11]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[11]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[11]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[11].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[11].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[11].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[12]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[12]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[12]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[12].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[12].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[12].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[13]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[13]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[13]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[13].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[13].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[13].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[14]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[14]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[14]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[14].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[14].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[14].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[15]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[15]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[15]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[15].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[15].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[15].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[16]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[16]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[16]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[16].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[16].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[16].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[17]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[17]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[17]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[17].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[17].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[17].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[18]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[18]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[18]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[18].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[18].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[18].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[19]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[19]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[19]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[19].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[19].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[19].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[20]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[20]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[20]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[20].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[20].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[20].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[21]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[21]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[21]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[21].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[21].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[21].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[22]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[22]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[22]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[22].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[22].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[22].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[23]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[23]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[23]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[23].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[23].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[23].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[24]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[24]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[24]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[24].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[24].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[24].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[25]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[25]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[25]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[25].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[25].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[25].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[26]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[26]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[26]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[26].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[26].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[26].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[27]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[27]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[27]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[27].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[27].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[27].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[28]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[28]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[28]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[28].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[28].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[28].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[29]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[29]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[29]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[29].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[29].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[29].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[30]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[30]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[30]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[30].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[30].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[30].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[31]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[31]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[31]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[31].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[31].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[31].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[32]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[32]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[32]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[32].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[32].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[32].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[33]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[33]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[33]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[33].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[33].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[33].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[34]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[34]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[34]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[34].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[34].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[34].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[35]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[35]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[35]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[35].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[35].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[35].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[36]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[36]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[36]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[36].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[36].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[36].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[37]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[37]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[37]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[37].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[37].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[37].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[38]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[38]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[38]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[38].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[38].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[38].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[39]
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].histogram[39]'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[39]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[39].read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[39].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].histogram[39].read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].pivot_value
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].pivot_value'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].pivot_value')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].pivot_value.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].pivot_value.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].pivot_value.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].pivot_index
        with self.subTest(msg='register: samplerz_axi.sample_histograms[1].pivot_index'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].pivot_index')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].pivot_index.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].pivot_index.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(self.dut.sample_histograms[1].pivot_index.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        

    def test_field_read_and_write(self) -> None:
        """
        Walk the register map and check every field can be read and written to correctly
        """
        random_field_value: Union[int, IntEnum]
        # test access operations (read and/or write) to register:
        # samplerz_axi.marker.data
        with self.subTest(msg='field: samplerz_axi.marker.data'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.marker')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.marker.data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.marker.data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(self.dut.marker.data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.marker.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.marker.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.control.falcon1024
        with self.subTest(msg='field: samplerz_axi.control.falcon1024'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.control')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.control.falcon1024')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x1) >> 0
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.control.falcon1024.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0x1+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFE) | (random_field_value << 0))
            
            self.assertEqual(self.dut.control.falcon1024.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x1) >> 0
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.control.falcon1024.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x1) >> 0
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.control.falcon1024.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0x1+1)
            
            self.dut.control.falcon1024.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFE) | (0x1 & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0x1+1)
            
            self.dut.control.falcon1024.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFE) | (0x1 & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFFFE) | (0x1 & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0x1+1)
            
            self.dut.control.falcon1024.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFE) | (0x1 & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.control.done
        with self.subTest(msg='field: samplerz_axi.control.done'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.control')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.control.done')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x2) >> 1
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.control.done.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0x1+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFD) | (random_field_value << 1))
            
            self.assertEqual(self.dut.control.done.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x2) >> 1
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.control.done.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x2) >> 1
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.control.done.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.control.start
        with self.subTest(msg='field: samplerz_axi.control.start'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.control')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.control.start')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x4) >> 2
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.control.start.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0x1+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFB) | (random_field_value << 2))
            
            self.assertEqual(self.dut.control.start.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x4) >> 2
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.control.start.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x4) >> 2
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.control.start.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0x1+1)
            
            self.dut.control.start.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFB) | (0x4 & (random_field_value << 2)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0x1+1)
            
            self.dut.control.start.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFB) | (0x4 & (random_field_value << 2)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFFFB) | (0x4 & (random_field_value << 2)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0x1+1)
            
            self.dut.control.start.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFB) | (0x4 & (random_field_value << 2)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.control.stop
        with self.subTest(msg='field: samplerz_axi.control.stop'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.control')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.control.stop')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x8) >> 3
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.control.stop.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0x1+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFF7) | (random_field_value << 3))
            
            self.assertEqual(self.dut.control.stop.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x8) >> 3
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.control.stop.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x8) >> 3
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.control.stop.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0x1+1)
            
            self.dut.control.stop.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFF7) | (0x8 & (random_field_value << 3)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0x1+1)
            
            self.dut.control.stop.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFF7) | (0x8 & (random_field_value << 3)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFFF7) | (0x8 & (random_field_value << 3)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0x1+1)
            
            self.dut.control.stop.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFF7) | (0x8 & (random_field_value << 3)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.control.continuous
        with self.subTest(msg='field: samplerz_axi.control.continuous'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.control')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.control.continuous')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x10) >> 4
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.control.continuous.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0x1+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFEF) | (random_field_value << 4))
            
            self.assertEqual(self.dut.control.continuous.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x10) >> 4
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.control.continuous.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x10) >> 4
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.control.continuous.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0x1+1)
            
            self.dut.control.continuous.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFEF) | (0x10 & (random_field_value << 4)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0x1+1)
            
            self.dut.control.continuous.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFEF) | (0x10 & (random_field_value << 4)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFFEF) | (0x10 & (random_field_value << 4)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0x1+1)
            
            self.dut.control.continuous.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFEF) | (0x10 & (random_field_value << 4)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.control.reset
        with self.subTest(msg='field: samplerz_axi.control.reset'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.control')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.control.reset')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x20) >> 5
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.control.reset.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0x1+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFDF) | (random_field_value << 5))
            
            self.assertEqual(self.dut.control.reset.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x20) >> 5
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.control.reset.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x20) >> 5
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.control.reset.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0x1+1)
            
            self.dut.control.reset.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFDF) | (0x20 & (random_field_value << 5)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0x1+1)
            
            self.dut.control.reset.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFDF) | (0x20 & (random_field_value << 5)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFFDF) | (0x20 & (random_field_value << 5)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0x1+1)
            
            self.dut.control.reset.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFDF) | (0x20 & (random_field_value << 5)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.control.busy
        with self.subTest(msg='field: samplerz_axi.control.busy'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.control')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.control.busy')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x40) >> 6
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.control.busy.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0x1+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFBF) | (random_field_value << 6))
            
            self.assertEqual(self.dut.control.busy.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x40) >> 6
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.control.busy.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x40) >> 6
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.control.busy.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.control.rand_full
        with self.subTest(msg='field: samplerz_axi.control.rand_full'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.control')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.control.rand_full')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x80) >> 7
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.control.rand_full.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0x1+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFF7F) | (random_field_value << 7))
            
            self.assertEqual(self.dut.control.rand_full.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x80) >> 7
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.control.rand_full.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x80) >> 7
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.control.rand_full.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.busy_cycles.low
        with self.subTest(msg='field: samplerz_axi.busy_cycles.low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.busy_cycles')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.busy_cycles.low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.busy_cycles.low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.busy_cycles.low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.busy_cycles.low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.busy_cycles.low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.busy_cycles.low.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF00000000) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.busy_cycles.low.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF00000000) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFFFF00000000) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.busy_cycles.low.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF00000000) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.busy_cycles.high
        with self.subTest(msg='field: samplerz_axi.busy_cycles.high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.busy_cycles')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.busy_cycles.high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.busy_cycles.high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.busy_cycles.high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.busy_cycles.high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.busy_cycles.high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.busy_cycles.high.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF) | (0xFFFFFFFF00000000 & (random_field_value << 32)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.busy_cycles.high.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF) | (0xFFFFFFFF00000000 & (random_field_value << 32)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFFFF) | (0xFFFFFFFF00000000 & (random_field_value << 32)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.busy_cycles.high.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF) | (0xFFFFFFFF00000000 & (random_field_value << 32)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.consumed_bits.low
        with self.subTest(msg='field: samplerz_axi.consumed_bits.low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.consumed_bits')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.consumed_bits.low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.consumed_bits.low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.consumed_bits.low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.consumed_bits.low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.consumed_bits.low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.consumed_bits.low.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF00000000) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.consumed_bits.low.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF00000000) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFFFF00000000) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.consumed_bits.low.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF00000000) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.consumed_bits.high
        with self.subTest(msg='field: samplerz_axi.consumed_bits.high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.consumed_bits')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.consumed_bits.high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.consumed_bits.high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.consumed_bits.high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.consumed_bits.high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.consumed_bits.high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.consumed_bits.high.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF) | (0xFFFFFFFF00000000 & (random_field_value << 32)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.consumed_bits.high.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF) | (0xFFFFFFFF00000000 & (random_field_value << 32)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFFFF) | (0xFFFFFFFF00000000 & (random_field_value << 32)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.consumed_bits.high.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF) | (0xFFFFFFFF00000000 & (random_field_value << 32)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sginv.low
        with self.subTest(msg='field: samplerz_axi.sginv.low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sginv')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sginv.low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sginv.low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sginv.low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sginv.low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sginv.low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.sginv.low.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF00000000) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.sginv.low.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF00000000) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFFFF00000000) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.sginv.low.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF00000000) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sginv.high
        with self.subTest(msg='field: samplerz_axi.sginv.high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sginv')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sginv.high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sginv.high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sginv.high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sginv.high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sginv.high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.sginv.high.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF) | (0xFFFFFFFF00000000 & (random_field_value << 32)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.sginv.high.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF) | (0xFFFFFFFF00000000 & (random_field_value << 32)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFFFF) | (0xFFFFFFFF00000000 & (random_field_value << 32)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.sginv.high.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF) | (0xFFFFFFFF00000000 & (random_field_value << 32)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.mu1.low
        with self.subTest(msg='field: samplerz_axi.mu1.low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.mu1')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.mu1.low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.mu1.low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.mu1.low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.mu1.low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.mu1.low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.mu1.low.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF00000000) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.mu1.low.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF00000000) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFFFF00000000) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.mu1.low.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF00000000) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.mu1.high
        with self.subTest(msg='field: samplerz_axi.mu1.high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.mu1')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.mu1.high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.mu1.high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.mu1.high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.mu1.high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.mu1.high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.mu1.high.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF) | (0xFFFFFFFF00000000 & (random_field_value << 32)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.mu1.high.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF) | (0xFFFFFFFF00000000 & (random_field_value << 32)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFFFF) | (0xFFFFFFFF00000000 & (random_field_value << 32)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.mu1.high.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF) | (0xFFFFFFFF00000000 & (random_field_value << 32)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.mu2.low
        with self.subTest(msg='field: samplerz_axi.mu2.low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.mu2')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.mu2.low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.mu2.low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.mu2.low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.mu2.low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.mu2.low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.mu2.low.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF00000000) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.mu2.low.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF00000000) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFFFF00000000) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.mu2.low.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF00000000) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.mu2.high
        with self.subTest(msg='field: samplerz_axi.mu2.high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.mu2')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.mu2.high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.mu2.high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.mu2.high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.mu2.high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.mu2.high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.mu2.high.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF) | (0xFFFFFFFF00000000 & (random_field_value << 32)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.mu2.high.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF) | (0xFFFFFFFF00000000 & (random_field_value << 32)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFFFF) | (0xFFFFFFFF00000000 & (random_field_value << 32)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.mu2.high.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF) | (0xFFFFFFFF00000000 & (random_field_value << 32)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.z1.data
        with self.subTest(msg='field: samplerz_axi.z1.data'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.z1')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.z1.data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.z1.data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(self.dut.z1.data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.z1.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.z1.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.z2.data
        with self.subTest(msg='field: samplerz_axi.z2.data'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.z2')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.z2.data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.z2.data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(self.dut.z2.data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.z2.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.z2.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.prng.seed[0].data
        with self.subTest(msg='field: samplerz_axi.prng.seed[0].data'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.prng.seed[0]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.prng.seed[0].data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[0].data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(self.dut.prng.seed[0].data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.prng.seed[0].data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[0].data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.seed[0].data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.seed[0].data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.seed[0].data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.prng.seed[1].data
        with self.subTest(msg='field: samplerz_axi.prng.seed[1].data'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.prng.seed[1]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.prng.seed[1].data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[1].data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(self.dut.prng.seed[1].data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.prng.seed[1].data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[1].data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.seed[1].data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.seed[1].data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.seed[1].data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.prng.seed[2].data
        with self.subTest(msg='field: samplerz_axi.prng.seed[2].data'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.prng.seed[2]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.prng.seed[2].data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[2].data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(self.dut.prng.seed[2].data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.prng.seed[2].data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[2].data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.seed[2].data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.seed[2].data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.seed[2].data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.prng.seed[3].data
        with self.subTest(msg='field: samplerz_axi.prng.seed[3].data'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.prng.seed[3]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.prng.seed[3].data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[3].data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(self.dut.prng.seed[3].data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.prng.seed[3].data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[3].data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.seed[3].data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.seed[3].data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.seed[3].data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.prng.seed[4].data
        with self.subTest(msg='field: samplerz_axi.prng.seed[4].data'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.prng.seed[4]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.prng.seed[4].data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[4].data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(self.dut.prng.seed[4].data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.prng.seed[4].data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[4].data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.seed[4].data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.seed[4].data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.seed[4].data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.prng.seed[5].data
        with self.subTest(msg='field: samplerz_axi.prng.seed[5].data'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.prng.seed[5]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.prng.seed[5].data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[5].data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(self.dut.prng.seed[5].data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.prng.seed[5].data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[5].data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.seed[5].data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.seed[5].data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.seed[5].data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.prng.seed[6].data
        with self.subTest(msg='field: samplerz_axi.prng.seed[6].data'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.prng.seed[6]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.prng.seed[6].data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[6].data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(self.dut.prng.seed[6].data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.prng.seed[6].data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[6].data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.seed[6].data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.seed[6].data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.seed[6].data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.prng.seed[7].data
        with self.subTest(msg='field: samplerz_axi.prng.seed[7].data'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.prng.seed[7]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.prng.seed[7].data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[7].data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(self.dut.prng.seed[7].data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.prng.seed[7].data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[7].data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.seed[7].data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.seed[7].data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.seed[7].data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.prng.seed[8].data
        with self.subTest(msg='field: samplerz_axi.prng.seed[8].data'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.prng.seed[8]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.prng.seed[8].data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[8].data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(self.dut.prng.seed[8].data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.prng.seed[8].data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[8].data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.seed[8].data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.seed[8].data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.seed[8].data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.prng.seed[9].data
        with self.subTest(msg='field: samplerz_axi.prng.seed[9].data'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.prng.seed[9]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.prng.seed[9].data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[9].data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(self.dut.prng.seed[9].data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.prng.seed[9].data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[9].data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.seed[9].data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.seed[9].data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.seed[9].data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.prng.seed[10].data
        with self.subTest(msg='field: samplerz_axi.prng.seed[10].data'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.prng.seed[10]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.prng.seed[10].data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[10].data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(self.dut.prng.seed[10].data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.prng.seed[10].data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.seed[10].data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.seed[10].data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.seed[10].data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.seed[10].data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.prng.counter.low
        with self.subTest(msg='field: samplerz_axi.prng.counter.low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.prng.counter')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.prng.counter.low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.counter.low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.prng.counter.low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.prng.counter.low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.counter.low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.counter.low.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF00000000) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.counter.low.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF00000000) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFFFF00000000) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.counter.low.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF00000000) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.prng.counter.high
        with self.subTest(msg='field: samplerz_axi.prng.counter.high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.prng.counter')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.prng.counter.high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.counter.high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.prng.counter.high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.prng.counter.high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.prng.counter.high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.counter.high.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF) | (0xFFFFFFFF00000000 & (random_field_value << 32)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.counter.high.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF) | (0xFFFFFFFF00000000 & (random_field_value << 32)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFFFF) | (0xFFFFFFFF00000000 & (random_field_value << 32)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            self.dut.prng.counter.high.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFF) | (0xFFFFFFFF00000000 & (random_field_value << 32)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[0].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[0].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[0]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[0].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[0].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[0].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[0].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[0].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[0].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[0].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[0]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[0].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[0].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[0].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[0].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[0].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[1].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[1].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[1]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[1].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[1].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[1].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[1].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[1].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[1].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[1].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[1]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[1].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[1].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[1].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[1].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[1].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[2].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[2].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[2]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[2].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[2].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[2].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[2].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[2].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[2].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[2].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[2]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[2].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[2].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[2].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[2].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[2].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[3].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[3].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[3]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[3].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[3].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[3].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[3].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[3].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[3].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[3].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[3]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[3].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[3].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[3].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[3].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[3].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[4].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[4].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[4]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[4].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[4].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[4].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[4].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[4].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[4].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[4].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[4]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[4].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[4].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[4].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[4].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[4].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[5].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[5].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[5]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[5].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[5].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[5].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[5].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[5].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[5].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[5].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[5]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[5].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[5].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[5].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[5].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[5].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[6].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[6].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[6]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[6].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[6].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[6].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[6].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[6].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[6].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[6].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[6]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[6].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[6].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[6].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[6].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[6].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[7].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[7].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[7]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[7].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[7].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[7].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[7].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[7].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[7].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[7].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[7]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[7].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[7].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[7].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[7].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[7].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[8].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[8].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[8]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[8].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[8].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[8].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[8].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[8].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[8].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[8].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[8]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[8].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[8].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[8].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[8].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[8].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[9].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[9].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[9]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[9].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[9].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[9].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[9].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[9].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[9].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[9].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[9]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[9].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[9].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[9].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[9].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[9].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[10].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[10].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[10]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[10].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[10].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[10].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[10].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[10].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[10].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[10].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[10]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[10].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[10].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[10].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[10].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[10].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[11].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[11].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[11]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[11].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[11].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[11].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[11].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[11].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[11].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[11].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[11]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[11].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[11].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[11].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[11].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[11].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[12].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[12].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[12]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[12].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[12].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[12].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[12].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[12].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[12].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[12].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[12]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[12].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[12].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[12].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[12].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[12].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[13].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[13].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[13]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[13].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[13].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[13].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[13].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[13].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[13].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[13].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[13]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[13].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[13].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[13].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[13].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[13].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[14].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[14].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[14]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[14].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[14].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[14].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[14].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[14].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[14].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[14].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[14]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[14].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[14].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[14].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[14].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[14].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[15].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[15].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[15]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[15].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[15].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[15].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[15].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[15].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[15].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[15].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[15]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[15].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[15].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[15].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[15].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[15].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[16].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[16].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[16]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[16].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[16].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[16].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[16].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[16].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[16].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[16].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[16]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[16].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[16].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[16].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[16].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[16].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[17].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[17].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[17]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[17].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[17].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[17].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[17].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[17].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[17].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[17].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[17]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[17].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[17].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[17].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[17].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[17].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[18].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[18].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[18]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[18].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[18].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[18].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[18].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[18].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[18].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[18].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[18]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[18].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[18].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[18].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[18].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[18].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[19].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[19].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[19]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[19].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[19].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[19].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[19].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[19].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[19].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[19].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[19]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[19].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[19].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[19].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[19].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[19].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[20].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[20].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[20]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[20].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[20].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[20].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[20].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[20].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[20].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[20].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[20]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[20].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[20].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[20].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[20].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[20].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[21].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[21].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[21]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[21].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[21].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[21].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[21].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[21].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[21].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[21].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[21]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[21].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[21].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[21].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[21].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[21].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[22].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[22].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[22]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[22].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[22].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[22].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[22].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[22].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[22].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[22].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[22]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[22].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[22].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[22].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[22].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[22].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[23].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[23].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[23]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[23].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[23].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[23].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[23].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[23].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[23].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[23].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[23]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[23].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[23].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[23].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[23].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[23].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[24].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[24].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[24]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[24].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[24].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[24].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[24].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[24].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[24].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[24].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[24]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[24].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[24].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[24].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[24].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[24].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[25].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[25].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[25]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[25].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[25].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[25].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[25].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[25].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[25].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[25].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[25]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[25].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[25].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[25].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[25].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[25].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[26].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[26].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[26]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[26].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[26].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[26].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[26].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[26].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[26].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[26].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[26]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[26].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[26].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[26].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[26].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[26].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[27].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[27].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[27]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[27].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[27].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[27].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[27].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[27].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[27].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[27].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[27]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[27].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[27].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[27].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[27].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[27].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[28].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[28].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[28]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[28].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[28].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[28].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[28].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[28].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[28].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[28].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[28]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[28].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[28].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[28].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[28].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[28].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[29].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[29].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[29]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[29].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[29].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[29].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[29].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[29].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[29].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[29].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[29]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[29].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[29].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[29].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[29].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[29].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[30].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[30].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[30]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[30].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[30].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[30].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[30].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[30].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[30].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[30].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[30]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[30].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[30].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[30].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[30].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[30].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[31].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[31].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[31]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[31].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[31].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[31].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[31].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[31].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[31].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[31].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[31]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[31].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[31].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[31].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[31].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[31].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[32].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[32].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[32]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[32].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[32].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[32].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[32].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[32].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[32].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[32].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[32]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[32].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[32].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[32].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[32].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[32].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[33].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[33].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[33]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[33].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[33].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[33].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[33].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[33].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[33].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[33].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[33]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[33].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[33].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[33].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[33].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[33].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[34].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[34].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[34]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[34].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[34].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[34].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[34].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[34].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[34].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[34].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[34]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[34].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[34].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[34].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[34].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[34].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[35].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[35].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[35]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[35].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[35].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[35].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[35].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[35].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[35].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[35].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[35]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[35].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[35].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[35].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[35].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[35].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[36].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[36].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[36]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[36].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[36].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[36].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[36].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[36].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[36].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[36].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[36]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[36].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[36].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[36].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[36].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[36].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[37].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[37].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[37]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[37].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[37].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[37].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[37].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[37].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[37].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[37].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[37]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[37].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[37].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[37].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[37].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[37].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[38].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[38].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[38]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[38].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[38].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[38].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[38].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[38].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[38].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[38].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[38]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[38].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[38].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[38].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[38].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[38].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[39].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[39].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[39]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[39].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[39].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[39].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[39].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[39].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].histogram[39].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].histogram[39].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].histogram[39]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].histogram[39].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[39].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[0].histogram[39].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].histogram[39].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].histogram[39].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].pivot_value.data
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].pivot_value.data'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].pivot_value')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].pivot_value.data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].pivot_value.data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].pivot_value.data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].pivot_value.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].pivot_value.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[0].pivot_index.data
        with self.subTest(msg='field: samplerz_axi.sample_histograms[0].pivot_index.data'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[0].pivot_index')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[0].pivot_index.data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].pivot_index.data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[0].pivot_index.data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[0].pivot_index.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[0].pivot_index.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[0].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[0].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[0]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[0].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[0].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[0].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[0].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[0].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[0].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[0].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[0]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[0].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[0].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[0].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[0].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[0].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[1].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[1].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[1]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[1].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[1].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[1].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[1].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[1].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[1].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[1].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[1]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[1].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[1].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[1].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[1].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[1].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[2].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[2].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[2]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[2].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[2].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[2].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[2].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[2].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[2].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[2].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[2]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[2].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[2].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[2].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[2].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[2].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[3].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[3].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[3]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[3].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[3].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[3].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[3].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[3].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[3].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[3].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[3]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[3].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[3].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[3].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[3].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[3].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[4].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[4].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[4]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[4].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[4].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[4].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[4].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[4].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[4].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[4].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[4]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[4].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[4].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[4].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[4].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[4].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[5].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[5].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[5]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[5].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[5].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[5].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[5].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[5].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[5].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[5].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[5]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[5].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[5].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[5].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[5].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[5].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[6].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[6].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[6]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[6].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[6].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[6].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[6].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[6].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[6].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[6].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[6]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[6].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[6].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[6].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[6].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[6].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[7].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[7].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[7]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[7].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[7].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[7].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[7].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[7].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[7].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[7].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[7]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[7].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[7].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[7].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[7].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[7].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[8].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[8].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[8]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[8].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[8].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[8].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[8].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[8].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[8].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[8].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[8]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[8].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[8].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[8].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[8].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[8].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[9].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[9].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[9]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[9].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[9].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[9].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[9].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[9].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[9].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[9].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[9]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[9].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[9].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[9].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[9].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[9].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[10].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[10].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[10]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[10].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[10].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[10].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[10].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[10].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[10].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[10].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[10]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[10].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[10].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[10].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[10].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[10].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[11].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[11].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[11]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[11].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[11].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[11].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[11].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[11].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[11].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[11].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[11]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[11].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[11].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[11].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[11].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[11].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[12].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[12].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[12]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[12].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[12].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[12].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[12].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[12].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[12].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[12].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[12]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[12].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[12].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[12].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[12].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[12].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[13].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[13].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[13]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[13].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[13].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[13].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[13].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[13].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[13].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[13].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[13]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[13].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[13].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[13].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[13].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[13].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[14].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[14].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[14]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[14].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[14].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[14].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[14].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[14].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[14].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[14].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[14]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[14].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[14].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[14].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[14].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[14].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[15].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[15].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[15]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[15].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[15].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[15].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[15].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[15].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[15].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[15].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[15]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[15].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[15].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[15].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[15].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[15].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[16].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[16].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[16]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[16].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[16].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[16].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[16].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[16].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[16].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[16].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[16]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[16].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[16].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[16].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[16].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[16].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[17].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[17].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[17]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[17].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[17].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[17].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[17].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[17].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[17].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[17].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[17]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[17].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[17].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[17].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[17].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[17].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[18].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[18].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[18]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[18].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[18].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[18].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[18].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[18].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[18].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[18].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[18]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[18].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[18].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[18].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[18].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[18].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[19].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[19].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[19]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[19].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[19].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[19].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[19].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[19].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[19].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[19].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[19]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[19].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[19].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[19].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[19].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[19].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[20].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[20].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[20]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[20].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[20].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[20].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[20].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[20].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[20].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[20].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[20]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[20].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[20].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[20].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[20].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[20].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[21].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[21].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[21]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[21].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[21].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[21].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[21].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[21].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[21].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[21].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[21]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[21].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[21].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[21].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[21].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[21].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[22].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[22].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[22]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[22].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[22].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[22].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[22].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[22].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[22].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[22].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[22]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[22].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[22].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[22].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[22].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[22].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[23].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[23].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[23]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[23].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[23].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[23].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[23].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[23].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[23].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[23].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[23]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[23].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[23].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[23].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[23].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[23].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[24].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[24].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[24]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[24].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[24].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[24].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[24].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[24].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[24].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[24].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[24]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[24].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[24].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[24].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[24].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[24].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[25].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[25].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[25]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[25].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[25].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[25].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[25].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[25].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[25].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[25].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[25]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[25].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[25].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[25].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[25].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[25].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[26].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[26].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[26]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[26].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[26].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[26].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[26].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[26].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[26].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[26].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[26]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[26].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[26].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[26].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[26].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[26].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[27].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[27].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[27]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[27].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[27].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[27].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[27].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[27].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[27].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[27].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[27]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[27].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[27].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[27].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[27].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[27].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[28].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[28].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[28]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[28].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[28].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[28].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[28].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[28].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[28].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[28].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[28]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[28].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[28].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[28].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[28].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[28].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[29].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[29].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[29]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[29].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[29].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[29].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[29].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[29].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[29].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[29].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[29]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[29].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[29].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[29].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[29].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[29].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[30].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[30].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[30]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[30].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[30].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[30].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[30].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[30].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[30].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[30].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[30]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[30].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[30].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[30].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[30].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[30].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[31].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[31].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[31]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[31].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[31].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[31].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[31].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[31].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[31].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[31].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[31]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[31].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[31].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[31].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[31].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[31].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[32].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[32].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[32]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[32].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[32].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[32].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[32].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[32].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[32].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[32].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[32]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[32].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[32].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[32].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[32].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[32].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[33].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[33].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[33]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[33].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[33].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[33].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[33].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[33].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[33].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[33].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[33]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[33].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[33].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[33].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[33].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[33].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[34].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[34].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[34]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[34].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[34].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[34].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[34].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[34].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[34].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[34].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[34]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[34].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[34].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[34].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[34].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[34].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[35].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[35].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[35]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[35].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[35].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[35].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[35].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[35].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[35].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[35].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[35]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[35].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[35].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[35].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[35].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[35].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[36].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[36].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[36]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[36].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[36].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[36].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[36].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[36].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[36].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[36].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[36]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[36].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[36].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[36].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[36].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[36].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[37].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[37].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[37]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[37].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[37].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[37].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[37].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[37].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[37].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[37].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[37]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[37].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[37].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[37].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[37].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[37].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[38].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[38].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[38]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[38].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[38].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[38].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[38].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[38].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[38].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[38].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[38]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[38].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[38].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[38].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[38].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[38].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[39].low
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[39].low'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[39]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[39].low')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[39].low.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF00000000) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[39].low.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[39].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[39].low.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].histogram[39].high
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].histogram[39].high'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].histogram[39]')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].histogram[39].high')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[39].high.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFF) | (random_field_value << 32))
            
            self.assertEqual(self.dut.sample_histograms[1].histogram[39].high.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].histogram[39].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFFFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF00000000) >> 32
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].histogram[39].high.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].pivot_value.data
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].pivot_value.data'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].pivot_value')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].pivot_value.data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].pivot_value.data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].pivot_value.data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].pivot_value.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].pivot_value.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # samplerz_axi.sample_histograms[1].pivot_index.data
        with self.subTest(msg='field: samplerz_axi.sample_histograms[1].pivot_index.data'):
            sim_register = self.sim.register_by_full_name('samplerz_axi.sample_histograms[1].pivot_index')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('samplerz_axi.sample_histograms[1].pivot_index.data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].pivot_index.data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(self.dut.sample_histograms[1].pivot_index.data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(self.dut.sample_histograms[1].pivot_index.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(self.dut.sample_histograms[1].pivot_index.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        


    



class samplerz_axi_block_access(samplerz_axi_SimTestCase_BlockAccess): # type: ignore[valid-type,misc]
    """
    tests for all the block access methods
    """

    

if __name__ == '__main__':

    unittest.main()




