
from .lib import NormalCallbackSet

from .reg_model.samplerz_axi import samplerz_axi_cls
from .sim.samplerz_axi import samplerz_axi_simulator_cls

if __name__ == '__main__':

    sim = samplerz_axi_simulator_cls(address=0)

    # create an instance of the class
    reg_model = samplerz_axi_cls(callbacks=NormalCallbackSet(read_callback=sim.read,
                                                                       write_callback=sim.write))