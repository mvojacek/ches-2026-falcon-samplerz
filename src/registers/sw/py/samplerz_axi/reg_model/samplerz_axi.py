


"""
Python Wrapper for the samplerz_axi register model

This code was generated from the PeakRDL-python package version 1.1.0

"""

from enum import IntEnum, unique
from typing import Iterator
from typing import Optional
from typing import Union
from typing import Type

from typing import Generator

import warnings



from contextlib import contextmanager

from ..lib import Node
from ..lib import UDPStruct

from ..lib  import AddressMapArray, RegFileArray
from ..lib import Memory, MemoryArray
from ..lib import AddressMap
from ..lib import RegFile
from ..lib  import AddressMapArray
from ..lib  import RegFileArray
from ..lib import MemoryReadOnly, MemoryWriteOnly, MemoryReadWrite
from ..lib import MemoryReadOnlyArray, MemoryWriteOnlyArray, MemoryReadWriteArray
from ..lib import Reg, RegArray
from ..lib import RegReadOnly, RegWriteOnly, RegReadWrite
from ..lib import RegReadOnlyArray, RegWriteOnlyArray, RegReadWriteArray
from ..lib import FieldReadOnly, FieldWriteOnly, FieldReadWrite, Field

from ..lib import ReadableRegister, WritableRegister
from ..lib import ReadableMemory, WritableMemory
from ..lib import ReadableRegisterArray, WriteableRegisterArray
from ..lib import FieldSizeProps, FieldMiscProps


from ..lib import NormalCallbackSet, NormalCallbackSetLegacy
















# regfile, register and field definitions
    
    
    
class samplerz_axi_hw2sw32_data_cls(FieldReadOnly):
    
    """
    Class to represent a register field in the register model

    
    """

    __slots__ : list[str] = []

    

    
    
    

    
    
class samplerz_axi_hw2sw32_cls(RegReadOnly):
    """
    Class to represent a register in the register model

    
    """

    __slots__ : list[str] = ['__data']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AddressMap,RegFile,ReadableMemory]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__data:samplerz_axi_hw2sw32_data_cls = samplerz_axi_hw2sw32_data_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.data',
            inst_name='data')

    @property
    def fields(self) -> Iterator[Union[FieldReadOnly, FieldWriteOnly,FieldReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.data
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def data(self) -> samplerz_axi_hw2sw32_data_cls:
        """
        Property to access data field of the register

        
        """
        return self.__data

    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {
                
            'data':'data',
                
            }

    

    
    
    

    
    
    
class samplerz_axi_hw2sw32_data_0x0x78dc3a9c3a4_cls(FieldReadOnly):
    
    """
    Class to represent a register field in the register model

    
    """

    __slots__ : list[str] = []

    

    
    
    

    
    
class samplerz_axi_hw2sw32_0x0x78dc3a9c398_cls(RegReadOnly):
    """
    Class to represent a register in the register model

    
    """

    __slots__ : list[str] = ['__data']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AddressMap,RegFile,ReadableMemory]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__data:samplerz_axi_hw2sw32_data_0x0x78dc3a9c3a4_cls = samplerz_axi_hw2sw32_data_0x0x78dc3a9c3a4_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.data',
            inst_name='data')

    @property
    def fields(self) -> Iterator[Union[FieldReadOnly, FieldWriteOnly,FieldReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.data
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def data(self) -> samplerz_axi_hw2sw32_data_0x0x78dc3a9c3a4_cls:
        """
        Property to access data field of the register

        
        """
        return self.__data

    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {
                
            'data':'data',
                
            }

    

    
    
    

    
    
    
class samplerz_axi_hw2sw64_high_cls(FieldReadOnly):
    
    """
    Class to represent a register field in the register model

    
    """

    __slots__ : list[str] = []

    

    
    
    

    
    
    
class samplerz_axi_hw2sw64_low_cls(FieldReadOnly):
    
    """
    Class to represent a register field in the register model

    
    """

    __slots__ : list[str] = []

    

    
    
    

    
    
class samplerz_axi_hw2sw64_cls(RegReadOnly):
    """
    Class to represent a register in the register model

    
    """

    __slots__ : list[str] = ['__low', '__high']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AddressMap,RegFile,ReadableMemory]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__low:samplerz_axi_hw2sw64_low_cls = samplerz_axi_hw2sw64_low_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.low',
            inst_name='low')
        self.__high:samplerz_axi_hw2sw64_high_cls = samplerz_axi_hw2sw64_high_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=32,
                msb=63,
                low=32,
                high=63),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.high',
            inst_name='high')

    @property
    def fields(self) -> Iterator[Union[FieldReadOnly, FieldWriteOnly,FieldReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.low
        yield self.high
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def low(self) -> samplerz_axi_hw2sw64_low_cls:
        """
        Property to access low field of the register

        
        """
        return self.__low
    @property
    def high(self) -> samplerz_axi_hw2sw64_high_cls:
        """
        Property to access high field of the register

        
        """
        return self.__high

    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {
                
            'low':'low',
                
                
            'high':'high',
                
            }

    

    
    
class samplerz_axi_hw2sw64_array_cls(RegReadOnlyArray):
    """
    Class to represent a register array in the register model
    """
    __slots__: list[str] = []

    @property
    def _element_datatype(self) -> Type[Node]:
        return samplerz_axi_hw2sw64_cls
    

    
    
class samplerz_axi_sample_histogram_cls(RegFile):
    """
    Class to represent a register file in the register model

    
    """

    __slots__ : list[str] = ['__histogram', '__pivot_value', '__pivot_index']

    NormalCallbackSet

    def __init__(self,
                 address: int,
                 logger_handle:str,
                 inst_name:str,
                 parent:Union[AddressMap,RegFile]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # instance of objects within the class
        
            
        self.__histogram:samplerz_axi_hw2sw64_array_cls = samplerz_axi_hw2sw64_array_cls(address=self.address+0,
                                                                                      accesswidth=32,
                                                                                      width=64,
                                                                                      stride=8,
                                                                                      dimensions=tuple([40]),
                                                                                      logger_handle=logger_handle+'.histogram',
                                                                                      inst_name='histogram', parent=self)
        
            
        self.__pivot_value:samplerz_axi_hw2sw32_0x0x78dc3a9c398_cls = samplerz_axi_hw2sw32_0x0x78dc3a9c398_cls(
                                                                     address=self.address+320,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.pivot_value',
                                                                     inst_name='pivot_value', parent=self)
        
            
        self.__pivot_index:samplerz_axi_hw2sw32_cls = samplerz_axi_hw2sw32_cls(
                                                                     address=self.address+324,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.pivot_index',
                                                                     inst_name='pivot_index', parent=self)
        

    @property
    def size(self) -> int:
        return 328

    # properties for Register and RegisterFiles
    @property
    def histogram(self) -> samplerz_axi_hw2sw64_array_cls:
        """
        Property to access histogram array

        
        """
        return self.__histogram
    
    @property
    def pivot_value(self) -> samplerz_axi_hw2sw32_0x0x78dc3a9c398_cls:
        """
        Property to access pivot_value 

        
        """
        return self.__pivot_value
    
    @property
    def pivot_index(self) -> samplerz_axi_hw2sw32_cls:
        """
        Property to access pivot_index 

        
        """
        return self.__pivot_index
    

    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'histogram':'histogram','pivot_value':'pivot_value','pivot_index':'pivot_index',
            }

    

    
    

    
    def get_registers(self, unroll:bool=False) -> Iterator[Union[Reg, RegArray]]:
        """
        generator that produces all the registers of this node
        """
        
                    
        if unroll:
            for child in self.histogram:
                yield child
        else:
            yield self.histogram
                    
        
                    
        yield self.pivot_value
        
                    
        yield self.pivot_index
        

        # Empty generator in case there are no children of this type
        if False: yield

        
    
    def get_sections(self, unroll:bool=False) -> Iterator[Union[RegFile, RegFileArray]]:
        """
        generator that produces all the RegFile, RegFileArray children of this node
        """
        

        # Empty generator in case there are no children of this type
        if False: yield
    
class samplerz_axi_sample_histogram_array_cls(RegFileArray):
    """
    Class to represent a regfile array in the register model
    """
    __slots__: list[str] = []

    def __init__(self, logger_handle: str, inst_name: str,
                 parent: Union[AddressMap, RegFile],
                 address: int,
                 stride: int,
                 dimensions: tuple[int, ...]):

        super().__init__(logger_handle=logger_handle, inst_name=inst_name,
                         parent=parent, address=address,
                         stride=stride, dimensions=dimensions)

    @property
    def _element_datatype(self) -> Type[Node]:
        return samplerz_axi_sample_histogram_cls
    

    
    
    
class samplerz_axi_prng_counter_high_incr_8dad7f70_cls(FieldReadWrite):
    
    """
    Class to represent a register field in the register model

    
    """

    __slots__ : list[str] = []

    

    
    
    

    
    
    
class samplerz_axi_prng_counter_low_cls(FieldReadWrite):
    
    """
    Class to represent a register field in the register model

    
    """

    __slots__ : list[str] = []

    

    
    
    

    
    
class samplerz_axi_prng_counter_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    
    """

    __slots__ : list[str] = ['__low', '__high']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AddressMap,RegFile,MemoryReadWrite]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__low:samplerz_axi_prng_counter_low_cls = samplerz_axi_prng_counter_low_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=False),
            logger_handle=logger_handle+'.low',
            inst_name='low')
        self.__high:samplerz_axi_prng_counter_high_incr_8dad7f70_cls = samplerz_axi_prng_counter_high_incr_8dad7f70_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=32,
                msb=63,
                low=32,
                high=63),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=False),
            logger_handle=logger_handle+'.high',
            inst_name='high')

    @property
    def fields(self) -> Iterator[Union[FieldReadOnly, FieldWriteOnly,FieldReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.low
        yield self.high
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def low(self) -> samplerz_axi_prng_counter_low_cls:
        """
        Property to access low field of the register

        
        """
        return self.__low
    @property
    def high(self) -> samplerz_axi_prng_counter_high_incr_8dad7f70_cls:
        """
        Property to access high field of the register

        
        """
        return self.__high

    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {
                
            'low':'low',
                
                
            'high':'high',
                
            }

    

    
    
    

    
    
    
class samplerz_axi_sw2hw32_data_cls(FieldReadWrite):
    
    """
    Class to represent a register field in the register model

    
    """

    __slots__ : list[str] = []

    

    
    
    

    
    
class samplerz_axi_sw2hw32_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    
    """

    __slots__ : list[str] = ['__data']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AddressMap,RegFile,MemoryReadWrite]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__data:samplerz_axi_sw2hw32_data_cls = samplerz_axi_sw2hw32_data_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=False),
            logger_handle=logger_handle+'.data',
            inst_name='data')

    @property
    def fields(self) -> Iterator[Union[FieldReadOnly, FieldWriteOnly,FieldReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.data
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def data(self) -> samplerz_axi_sw2hw32_data_cls:
        """
        Property to access data field of the register

        
        """
        return self.__data

    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {
                
            'data':'data',
                
            }

    

    
    
class samplerz_axi_sw2hw32_array_cls(RegReadWriteArray):
    """
    Class to represent a register array in the register model
    """
    __slots__: list[str] = []

    @property
    def _element_datatype(self) -> Type[Node]:
        return samplerz_axi_sw2hw32_cls
    

    
    
class samplerz_axi_prng_cls(RegFile):
    """
    Class to represent a register file in the register model

    
    """

    __slots__ : list[str] = ['__seed', '__counter']

    NormalCallbackSet

    def __init__(self,
                 address: int,
                 logger_handle:str,
                 inst_name:str,
                 parent:Union[AddressMap,RegFile]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # instance of objects within the class
        
            
        self.__seed:samplerz_axi_sw2hw32_array_cls = samplerz_axi_sw2hw32_array_cls(address=self.address+0,
                                                                                      accesswidth=32,
                                                                                      width=32,
                                                                                      stride=4,
                                                                                      dimensions=tuple([11]),
                                                                                      logger_handle=logger_handle+'.seed',
                                                                                      inst_name='seed', parent=self)
        
            
        self.__counter:samplerz_axi_prng_counter_cls = samplerz_axi_prng_counter_cls(
                                                                     address=self.address+48,
                                                                     accesswidth=32,
                                                                     width=64,
                                                                     logger_handle=logger_handle+'.counter',
                                                                     inst_name='counter', parent=self)
        

    @property
    def size(self) -> int:
        return 56

    # properties for Register and RegisterFiles
    @property
    def seed(self) -> samplerz_axi_sw2hw32_array_cls:
        """
        Property to access seed array

        
        """
        return self.__seed
    
    @property
    def counter(self) -> samplerz_axi_prng_counter_cls:
        """
        Property to access counter 

        
        """
        return self.__counter
    

    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'seed':'seed','counter':'counter',
            }

    

    
    

    
    def get_registers(self, unroll:bool=False) -> Iterator[Union[Reg, RegArray]]:
        """
        generator that produces all the registers of this node
        """
        
                    
        if unroll:
            for child in self.seed:
                yield child
        else:
            yield self.seed
                    
        
                    
        yield self.counter
        

        # Empty generator in case there are no children of this type
        if False: yield

        
    
    def get_sections(self, unroll:bool=False) -> Iterator[Union[RegFile, RegFileArray]]:
        """
        generator that produces all the RegFile, RegFileArray children of this node
        """
        

        # Empty generator in case there are no children of this type
        if False: yield
    
    

    
    
    
class samplerz_axi_hw2sw32_data_0x0x78dc3a9c2c0_cls(FieldReadOnly):
    
    """
    Class to represent a register field in the register model

    
    """

    __slots__ : list[str] = []

    

    
    
    

    
    
class samplerz_axi_hw2sw32_0x0x78dc3a9c2ba_cls(RegReadOnly):
    """
    Class to represent a register in the register model

    
    """

    __slots__ : list[str] = ['__data']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AddressMap,RegFile,ReadableMemory]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__data:samplerz_axi_hw2sw32_data_0x0x78dc3a9c2c0_cls = samplerz_axi_hw2sw32_data_0x0x78dc3a9c2c0_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.data',
            inst_name='data')

    @property
    def fields(self) -> Iterator[Union[FieldReadOnly, FieldWriteOnly,FieldReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.data
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def data(self) -> samplerz_axi_hw2sw32_data_0x0x78dc3a9c2c0_cls:
        """
        Property to access data field of the register

        
        """
        return self.__data

    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {
                
            'data':'data',
                
            }

    

    
    
    

    
    
    
class samplerz_axi_hw2sw32_data_0x0x78dc3a9c29c_cls(FieldReadOnly):
    
    """
    Class to represent a register field in the register model

    
    """

    __slots__ : list[str] = []

    

    
    
    

    
    
class samplerz_axi_hw2sw32_0x0x78dc3a9c296_cls(RegReadOnly):
    """
    Class to represent a register in the register model

    
    """

    __slots__ : list[str] = ['__data']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AddressMap,RegFile,ReadableMemory]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__data:samplerz_axi_hw2sw32_data_0x0x78dc3a9c29c_cls = samplerz_axi_hw2sw32_data_0x0x78dc3a9c29c_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.data',
            inst_name='data')

    @property
    def fields(self) -> Iterator[Union[FieldReadOnly, FieldWriteOnly,FieldReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.data
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def data(self) -> samplerz_axi_hw2sw32_data_0x0x78dc3a9c29c_cls:
        """
        Property to access data field of the register

        
        """
        return self.__data

    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {
                
            'data':'data',
                
            }

    

    
    
    

    
    
    
class samplerz_axi_sw2hw64_high_cls(FieldReadWrite):
    
    """
    Class to represent a register field in the register model

    
    """

    __slots__ : list[str] = []

    

    
    
    

    
    
    
class samplerz_axi_sw2hw64_low_cls(FieldReadWrite):
    
    """
    Class to represent a register field in the register model

    
    """

    __slots__ : list[str] = []

    

    
    
    

    
    
class samplerz_axi_sw2hw64_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    
    """

    __slots__ : list[str] = ['__low', '__high']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AddressMap,RegFile,MemoryReadWrite]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__low:samplerz_axi_sw2hw64_low_cls = samplerz_axi_sw2hw64_low_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=False),
            logger_handle=logger_handle+'.low',
            inst_name='low')
        self.__high:samplerz_axi_sw2hw64_high_cls = samplerz_axi_sw2hw64_high_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=32,
                msb=63,
                low=32,
                high=63),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=False),
            logger_handle=logger_handle+'.high',
            inst_name='high')

    @property
    def fields(self) -> Iterator[Union[FieldReadOnly, FieldWriteOnly,FieldReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.low
        yield self.high
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def low(self) -> samplerz_axi_sw2hw64_low_cls:
        """
        Property to access low field of the register

        
        """
        return self.__low
    @property
    def high(self) -> samplerz_axi_sw2hw64_high_cls:
        """
        Property to access high field of the register

        
        """
        return self.__high

    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {
                
            'low':'low',
                
                
            'high':'high',
                
            }

    

    
    
    

    
    
    
class samplerz_axi_sw2hw64_high_0x0x78dc3a9c239_cls(FieldReadWrite):
    
    """
    Class to represent a register field in the register model

    
    """

    __slots__ : list[str] = []

    

    
    
    

    
    
    
class samplerz_axi_sw2hw64_low_0x0x78dc3a9c21e_cls(FieldReadWrite):
    
    """
    Class to represent a register field in the register model

    
    """

    __slots__ : list[str] = []

    

    
    
    

    
    
class samplerz_axi_sw2hw64_0x0x78dc3a9c218_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    
    """

    __slots__ : list[str] = ['__low', '__high']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AddressMap,RegFile,MemoryReadWrite]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__low:samplerz_axi_sw2hw64_low_0x0x78dc3a9c21e_cls = samplerz_axi_sw2hw64_low_0x0x78dc3a9c21e_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=False),
            logger_handle=logger_handle+'.low',
            inst_name='low')
        self.__high:samplerz_axi_sw2hw64_high_0x0x78dc3a9c239_cls = samplerz_axi_sw2hw64_high_0x0x78dc3a9c239_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=32,
                msb=63,
                low=32,
                high=63),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=False),
            logger_handle=logger_handle+'.high',
            inst_name='high')

    @property
    def fields(self) -> Iterator[Union[FieldReadOnly, FieldWriteOnly,FieldReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.low
        yield self.high
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def low(self) -> samplerz_axi_sw2hw64_low_0x0x78dc3a9c21e_cls:
        """
        Property to access low field of the register

        
        """
        return self.__low
    @property
    def high(self) -> samplerz_axi_sw2hw64_high_0x0x78dc3a9c239_cls:
        """
        Property to access high field of the register

        
        """
        return self.__high

    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {
                
            'low':'low',
                
                
            'high':'high',
                
            }

    

    
    
    

    
    
    
class samplerz_axi_sw2hw64_high_0x0x78dc3a9c1fa_cls(FieldReadWrite):
    
    """
    Class to represent a register field in the register model

    
    """

    __slots__ : list[str] = []

    

    
    
    

    
    
    
class samplerz_axi_sw2hw64_low_0x0x78dc3a9c1df_cls(FieldReadWrite):
    
    """
    Class to represent a register field in the register model

    
    """

    __slots__ : list[str] = []

    

    
    
    

    
    
class samplerz_axi_sw2hw64_0x0x78dc3a9c1d9_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    
    """

    __slots__ : list[str] = ['__low', '__high']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AddressMap,RegFile,MemoryReadWrite]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__low:samplerz_axi_sw2hw64_low_0x0x78dc3a9c1df_cls = samplerz_axi_sw2hw64_low_0x0x78dc3a9c1df_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=False),
            logger_handle=logger_handle+'.low',
            inst_name='low')
        self.__high:samplerz_axi_sw2hw64_high_0x0x78dc3a9c1fa_cls = samplerz_axi_sw2hw64_high_0x0x78dc3a9c1fa_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=32,
                msb=63,
                low=32,
                high=63),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=False),
            logger_handle=logger_handle+'.high',
            inst_name='high')

    @property
    def fields(self) -> Iterator[Union[FieldReadOnly, FieldWriteOnly,FieldReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.low
        yield self.high
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def low(self) -> samplerz_axi_sw2hw64_low_0x0x78dc3a9c1df_cls:
        """
        Property to access low field of the register

        
        """
        return self.__low
    @property
    def high(self) -> samplerz_axi_sw2hw64_high_0x0x78dc3a9c1fa_cls:
        """
        Property to access high field of the register

        
        """
        return self.__high

    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {
                
            'low':'low',
                
                
            'high':'high',
                
            }

    

    
    
    

    
    
    
class samplerz_axi_consumed_bits_high_incr_8dad7f70_resetsignal_22c88e8e_cls(FieldReadWrite):
    
    """
    Class to represent a register field in the register model

    
    """

    __slots__ : list[str] = []

    

    
    
    

    
    
    
class samplerz_axi_consumed_bits_low_resetsignal_22c88e8e_cls(FieldReadWrite):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>The number of random bits consumed since the last start</p>     |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    
    

    
    
class samplerz_axi_consumed_bits_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Random Bits Counter Register                                       |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__reset_consumed_bits', '__low', '__high']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AddressMap,RegFile,MemoryReadWrite]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__low:samplerz_axi_consumed_bits_low_resetsignal_22c88e8e_cls = samplerz_axi_consumed_bits_low_resetsignal_22c88e8e_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.low',
            inst_name='low')
        self.__high:samplerz_axi_consumed_bits_high_incr_8dad7f70_resetsignal_22c88e8e_cls = samplerz_axi_consumed_bits_high_incr_8dad7f70_resetsignal_22c88e8e_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=32,
                msb=63,
                low=32,
                high=63),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.high',
            inst_name='high')

    @property
    def fields(self) -> Iterator[Union[FieldReadOnly, FieldWriteOnly,FieldReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.low
        yield self.high
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def low(self) -> samplerz_axi_consumed_bits_low_resetsignal_22c88e8e_cls:
        """
        Property to access low field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>The number of random bits consumed since the last start</p>     |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__low
    @property
    def high(self) -> samplerz_axi_consumed_bits_high_incr_8dad7f70_resetsignal_22c88e8e_cls:
        """
        Property to access high field of the register

        
        """
        return self.__high

    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {
            # doing nothing with signal node: reset_consumed_bits
            
                
            'low':'low',
                
                
            'high':'high',
                
            }

    

    
    
    

    
    
    
class samplerz_axi_busy_cycles_high_incr_8dad7f70_resetsignal_9fa1e13e_cls(FieldReadWrite):
    
    """
    Class to represent a register field in the register model

    
    """

    __slots__ : list[str] = []

    

    
    
    

    
    
    
class samplerz_axi_busy_cycles_low_resetsignal_9fa1e13e_cls(FieldReadWrite):
    
    """
    Class to represent a register field in the register model

    
    """

    __slots__ : list[str] = []

    

    
    
    

    
    
class samplerz_axi_busy_cycles_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Cycle Counter Register                                             |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>The number of cycles the module has been active since the last  |
    |              |      start</p>                                                          |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__reset_busy_cycles', '__low', '__high']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AddressMap,RegFile,MemoryReadWrite]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__low:samplerz_axi_busy_cycles_low_resetsignal_9fa1e13e_cls = samplerz_axi_busy_cycles_low_resetsignal_9fa1e13e_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.low',
            inst_name='low')
        self.__high:samplerz_axi_busy_cycles_high_incr_8dad7f70_resetsignal_9fa1e13e_cls = samplerz_axi_busy_cycles_high_incr_8dad7f70_resetsignal_9fa1e13e_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=32,
                msb=63,
                low=32,
                high=63),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.high',
            inst_name='high')

    @property
    def fields(self) -> Iterator[Union[FieldReadOnly, FieldWriteOnly,FieldReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.low
        yield self.high
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def low(self) -> samplerz_axi_busy_cycles_low_resetsignal_9fa1e13e_cls:
        """
        Property to access low field of the register

        
        """
        return self.__low
    @property
    def high(self) -> samplerz_axi_busy_cycles_high_incr_8dad7f70_resetsignal_9fa1e13e_cls:
        """
        Property to access high field of the register

        
        """
        return self.__high

    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {
            # doing nothing with signal node: reset_busy_cycles
            
                
            'low':'low',
                
                
            'high':'high',
                
            }

    

    
    
    

    
    
    
class samplerz_axi_control_rand_full_cls(FieldReadOnly):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>The module is fully filled with random bits</p>                 |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    
    

    
    
    
class samplerz_axi_control_busy_cls(FieldReadOnly):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>The module is busy</p>                                          |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    
    

    
    
    
class samplerz_axi_control_reset_cls(FieldReadWrite):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Reset the module</p>                                            |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    
    

    
    
    
class samplerz_axi_control_continuous_cls(FieldReadWrite):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Continuous sample generation</p>                                |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    
    

    
    
    
class samplerz_axi_control_stop_cls(FieldReadWrite):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Stop the module</p>                                             |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    
    

    
    
    
class samplerz_axi_control_start_cls(FieldReadWrite):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Start the computation</p>                                       |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    
    

    
    
    
class samplerz_axi_control_done_cls(FieldReadOnly):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>The computation is done</p>                                     |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    
    

    
    
    
class samplerz_axi_control_falcon1024_cls(FieldReadWrite):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>This bit enables Falcon-1024 instead of Falcon-512</p>          |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    
    

    
    
class samplerz_axi_control_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Control Register                                                   |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__falcon1024', '__done', '__start', '__stop', '__continuous', '__reset', '__busy', '__rand_full']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AddressMap,RegFile,MemoryReadWrite]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__falcon1024:samplerz_axi_control_falcon1024_cls = samplerz_axi_control_falcon1024_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=0,
                msb=0,
                low=0,
                high=0),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.falcon1024',
            inst_name='falcon1024')
        self.__done:samplerz_axi_control_done_cls = samplerz_axi_control_done_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=1,
                msb=1,
                low=1,
                high=1),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.done',
            inst_name='done')
        self.__start:samplerz_axi_control_start_cls = samplerz_axi_control_start_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=2,
                msb=2,
                low=2,
                high=2),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.start',
            inst_name='start')
        self.__stop:samplerz_axi_control_stop_cls = samplerz_axi_control_stop_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=3,
                msb=3,
                low=3,
                high=3),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.stop',
            inst_name='stop')
        self.__continuous:samplerz_axi_control_continuous_cls = samplerz_axi_control_continuous_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=4,
                msb=4,
                low=4,
                high=4),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.continuous',
            inst_name='continuous')
        self.__reset:samplerz_axi_control_reset_cls = samplerz_axi_control_reset_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=5,
                msb=5,
                low=5,
                high=5),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.reset',
            inst_name='reset')
        self.__busy:samplerz_axi_control_busy_cls = samplerz_axi_control_busy_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=6,
                msb=6,
                low=6,
                high=6),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.busy',
            inst_name='busy')
        self.__rand_full:samplerz_axi_control_rand_full_cls = samplerz_axi_control_rand_full_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=7,
                msb=7,
                low=7,
                high=7),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.rand_full',
            inst_name='rand_full')

    @property
    def fields(self) -> Iterator[Union[FieldReadOnly, FieldWriteOnly,FieldReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.falcon1024
        yield self.done
        yield self.start
        yield self.stop
        yield self.continuous
        yield self.reset
        yield self.busy
        yield self.rand_full
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def falcon1024(self) -> samplerz_axi_control_falcon1024_cls:
        """
        Property to access falcon1024 field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>This bit enables Falcon-1024 instead of Falcon-512</p>          |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__falcon1024
    @property
    def done(self) -> samplerz_axi_control_done_cls:
        """
        Property to access done field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>The computation is done</p>                                     |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__done
    @property
    def start(self) -> samplerz_axi_control_start_cls:
        """
        Property to access start field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Start the computation</p>                                       |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__start
    @property
    def stop(self) -> samplerz_axi_control_stop_cls:
        """
        Property to access stop field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Stop the module</p>                                             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__stop
    @property
    def continuous(self) -> samplerz_axi_control_continuous_cls:
        """
        Property to access continuous field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Continuous sample generation</p>                                |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__continuous
    @property
    def reset(self) -> samplerz_axi_control_reset_cls:
        """
        Property to access reset field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Reset the module</p>                                            |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__reset
    @property
    def busy(self) -> samplerz_axi_control_busy_cls:
        """
        Property to access busy field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>The module is busy</p>                                          |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__busy
    @property
    def rand_full(self) -> samplerz_axi_control_rand_full_cls:
        """
        Property to access rand_full field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>The module is fully filled with random bits</p>                 |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__rand_full

    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {
                
            'falcon1024':'falcon1024',
                
                
            'done':'done',
                
                
            'start':'start',
                
                
            'stop':'stop',
                
                
            'continuous':'continuous',
                
                
            'reset':'reset',
                
                
            'busy':'busy',
                
                
            'rand_full':'rand_full',
                
            }

    

    
    
    

    
    
    
class samplerz_axi_marker_data_cls(FieldReadOnly):
    
    """
    Class to represent a register field in the register model

    
    """

    __slots__ : list[str] = []

    

    
    
    

    
    
class samplerz_axi_marker_cls(RegReadOnly):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Marker Register                                                    |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__data']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AddressMap,RegFile,ReadableMemory]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__data:samplerz_axi_marker_data_cls = samplerz_axi_marker_data_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=1717793658,
                is_volatile=False),
            logger_handle=logger_handle+'.data',
            inst_name='data')

    @property
    def fields(self) -> Iterator[Union[FieldReadOnly, FieldWriteOnly,FieldReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.data
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def data(self) -> samplerz_axi_marker_data_cls:
        """
        Property to access data field of the register

        
        """
        return self.__data

    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {
                
            'data':'data',
                
            }

    

    
    
    

    
    
class samplerz_axi_cls(AddressMap):
    """
    Class to represent a address map in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      SamplerZ accelerator                                               |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__marker', '__control', '__busy_cycles', '__consumed_bits', '__sginv', '__mu1', '__mu2', '__z1', '__z2', '__prng', '__sample_histograms']

    def __init__(self, *,
                 address:int=0,
                 logger_handle:str='reg_model.samplerz_axi',
                 inst_name:str='samplerz_axi',
                 callbacks: Optional[Union[NormalCallbackSet, NormalCallbackSetLegacy]]=None,
                 parent:Optional[AddressMap]=None):

        if callbacks is not None:
            if not isinstance(callbacks, (NormalCallbackSet, NormalCallbackSetLegacy)):
                raise TypeError(f'callbacks should be NormalCallbackSet, NormalCallbackSetLegacy got {type(callbacks)}')

        super().__init__(callbacks=callbacks,
                         address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        
            
        self.__marker:samplerz_axi_marker_cls = samplerz_axi_marker_cls(
                                                                     address=self.address+0,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.marker',
                                                                     inst_name='marker', parent=self)
        
            
        self.__control:samplerz_axi_control_cls = samplerz_axi_control_cls(
                                                                     address=self.address+4,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.control',
                                                                     inst_name='control', parent=self)
        
            
        self.__busy_cycles:samplerz_axi_busy_cycles_cls = samplerz_axi_busy_cycles_cls(
                                                                     address=self.address+8,
                                                                     accesswidth=32,
                                                                     width=64,
                                                                     logger_handle=logger_handle+'.busy_cycles',
                                                                     inst_name='busy_cycles', parent=self)
        
            
        self.__consumed_bits:samplerz_axi_consumed_bits_cls = samplerz_axi_consumed_bits_cls(
                                                                     address=self.address+16,
                                                                     accesswidth=32,
                                                                     width=64,
                                                                     logger_handle=logger_handle+'.consumed_bits',
                                                                     inst_name='consumed_bits', parent=self)
        
            
        self.__sginv:samplerz_axi_sw2hw64_0x0x78dc3a9c1d9_cls = samplerz_axi_sw2hw64_0x0x78dc3a9c1d9_cls(
                                                                     address=self.address+24,
                                                                     accesswidth=32,
                                                                     width=64,
                                                                     logger_handle=logger_handle+'.sginv',
                                                                     inst_name='sginv', parent=self)
        
            
        self.__mu1:samplerz_axi_sw2hw64_0x0x78dc3a9c218_cls = samplerz_axi_sw2hw64_0x0x78dc3a9c218_cls(
                                                                     address=self.address+32,
                                                                     accesswidth=32,
                                                                     width=64,
                                                                     logger_handle=logger_handle+'.mu1',
                                                                     inst_name='mu1', parent=self)
        
            
        self.__mu2:samplerz_axi_sw2hw64_cls = samplerz_axi_sw2hw64_cls(
                                                                     address=self.address+40,
                                                                     accesswidth=32,
                                                                     width=64,
                                                                     logger_handle=logger_handle+'.mu2',
                                                                     inst_name='mu2', parent=self)
        
            
        self.__z1:samplerz_axi_hw2sw32_0x0x78dc3a9c296_cls = samplerz_axi_hw2sw32_0x0x78dc3a9c296_cls(
                                                                     address=self.address+48,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.z1',
                                                                     inst_name='z1', parent=self)
        
            
        self.__z2:samplerz_axi_hw2sw32_0x0x78dc3a9c2ba_cls = samplerz_axi_hw2sw32_0x0x78dc3a9c2ba_cls(
                                                                     address=self.address+52,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.z2',
                                                                     inst_name='z2', parent=self)
        self.__prng:samplerz_axi_prng_cls = samplerz_axi_prng_cls(
                                                                                address=self.address+64,
                                                                                logger_handle=logger_handle+'.prng',
                                                                                inst_name='prng',
                                                                                parent=self)
        
        self.__sample_histograms:samplerz_axi_sample_histogram_array_cls = samplerz_axi_sample_histogram_array_cls(address=self.address+512,
                                                                                      stride=328,
                                                                                      dimensions=tuple([2]),
                                                                                      logger_handle=logger_handle+'.sample_histograms',
                                                                                      inst_name='sample_histograms', parent=self)
        

    @property
    def size(self) -> int:
        return 1168
    @property
    def marker(self) -> samplerz_axi_marker_cls:
        """
        Property to access marker 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Marker Register                                                    |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__marker
        
    @property
    def control(self) -> samplerz_axi_control_cls:
        """
        Property to access control 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Control Register                                                   |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__control
        
    @property
    def busy_cycles(self) -> samplerz_axi_busy_cycles_cls:
        """
        Property to access busy_cycles 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Cycle Counter Register                                             |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>The number of cycles the module has been active since the last  |
        |              |      start</p>                                                          |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__busy_cycles
        
    @property
    def consumed_bits(self) -> samplerz_axi_consumed_bits_cls:
        """
        Property to access consumed_bits 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Random Bits Counter Register                                       |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__consumed_bits
        
    @property
    def sginv(self) -> samplerz_axi_sw2hw64_0x0x78dc3a9c1d9_cls:
        """
        Property to access sginv 

        
        """
        return self.__sginv
        
    @property
    def mu1(self) -> samplerz_axi_sw2hw64_0x0x78dc3a9c218_cls:
        """
        Property to access mu1 

        
        """
        return self.__mu1
        
    @property
    def mu2(self) -> samplerz_axi_sw2hw64_cls:
        """
        Property to access mu2 

        
        """
        return self.__mu2
        
    @property
    def z1(self) -> samplerz_axi_hw2sw32_0x0x78dc3a9c296_cls:
        """
        Property to access z1 

        
        """
        return self.__z1
        
    @property
    def z2(self) -> samplerz_axi_hw2sw32_0x0x78dc3a9c2ba_cls:
        """
        Property to access z2 

        
        """
        return self.__z2
        
    @property
    def prng(self) -> samplerz_axi_prng_cls:
        """
        Property to access prng 

        
        """
        return self.__prng
        
    @property
    def sample_histograms(self) -> samplerz_axi_sample_histogram_array_cls:
        """
        Property to access sample_histograms array

        
        """
        return self.__sample_histograms
        

    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'marker':'marker','control':'control','busy_cycles':'busy_cycles','consumed_bits':'consumed_bits','sginv':'sginv','mu1':'mu1','mu2':'mu2','z1':'z1','z2':'z2','prng':'prng','sample_histograms':'sample_histograms',
            }

    

    
    

    
    def get_registers(self, unroll:bool=False) -> Iterator[Union[Reg, RegArray]]:
        """
        generator that produces all the registers of this node
        """
        
                    
        yield self.marker
        
                    
        yield self.control
        
                    
        yield self.busy_cycles
        
                    
        yield self.consumed_bits
        
                    
        yield self.sginv
        
                    
        yield self.mu1
        
                    
        yield self.mu2
        
                    
        yield self.z1
        
                    
        yield self.z2
        
        
        

        # Empty generator in case there are no children of this type
        if False: yield
    
    
    def get_sections(self, unroll:bool=False) -> Iterator[Union[AddressMap, RegFile, AddressMapArray, RegFileArray]]:
        """
        generator that produces all the AddressMap, RegFile, AddressMapArray, RegFileArray children of this node
        """
        


                    
        yield self.prng


                    
        if unroll:
            for child in self.sample_histograms:
                yield child
        else:
            yield self.sample_histograms
                    

        # Empty generator in case there are no children of this type
        if False: yield
    
    def get_memories(self, unroll:bool=False) -> Iterator[Union[Memory, MemoryArray]]:
        """
        generator that produces all the Memory, MemoryArray children of this node
        """
        

        # Empty generator in case there are no children of this type
        if False: yield

    
    



if __name__ == '__main__':
    # dummy functions to demonstrate the class
    def read_addr_space(addr: int, width: int, accesswidth: int) -> int:
        """
        Callback to simulate the operation of the package, everytime the read is called, it will
        request the user input the value to be read back.

        Args:
            addr: Address to write to
            width: Width of the register in bits
            accesswidth: Minimum access width of the register in bits

        Returns:
            value inputted by the used
        """
        assert isinstance(addr, int)
        assert isinstance(width, int)
        assert isinstance(accesswidth, int)
        return int(input('value to read from address:0x%X'%addr))

    def write_addr_space(addr: int, width: int, accesswidth: int, data: int) -> None:
        """
        Callback to simulate the operation of the package, everytime the read is called, it will
        request the user input the value to be read back.

        Args:
            addr: Address to write to
            width: Width of the register in bits
            accesswidth: Minimum access width of the register in bits
            data: value to be written to the register

        Returns:
            None
        """
        assert isinstance(addr, int)
        assert isinstance(width, int)
        assert isinstance(accesswidth, int)
        assert isinstance(data, int)
        print('write data:0x%X to address:0x%X'%(data, addr))

    # create an instance of the class
    samplerz_axi = samplerz_axi_cls(callbacks = NormalCallbackSet(read_callback=read_addr_space,
                                                                                                     write_callback=write_addr_space))