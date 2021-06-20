import importlib
from importlib.util import find_spec
from random import random

class Swither(object):
    def __init__(self, *args):
        super(Swither, self).__init__(*args)
        
        self.dummy_io_trigger = bool()
        self.dummy_io_acknowledge = bool()
        self.dummy_io_pos_index = int(-1)
        
        self.dummy_pos_current_mach = [float()]*3 # x,y,theta, from CNC
        self.dummy_pos_comp_mach = [float()]*3 # to CNC


        #interfaces 
        self.read_trigger = lambda : self.dummy_io_trigger
        self.read_pos_index = lambda : self.dummy_io_pos_index
        self.write_acknowledge = lambda x: print(x) 
        """ lambda x=False: (
            self.dummy_io_acknowledge := '5',
            )[-1] """

        self.read_pos_current_mach = lambda : self.dummy_pos_current_mach
        self.write_pos_comp_mach = lambda x:print(x)
        """ lambda pos: (self.dummy_pos_comp_mach:=pos)[0] """

        is_hal_exists = find_spec('hal') is not None
        is_linuxcnc_exists = find_spec('linuxcnc') is not None

        if is_hal_exists and is_linuxcnc_exists:
            import hal, linuxcnc
            #change read/write function to connect linuxCNC
            pass
        pass
    
    def dice_values(self):
        for pos in self.dummy_pos_current_mach:
            pos = random()*1000
        pass
    pass