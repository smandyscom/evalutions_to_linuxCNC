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
        self.write_acknowledge = lambda x: self.__setattr__('dummy_io_acknowledge',x)
        self.read_ackowledge = lambda : self.dummy_io_acknowledge
        """ lambda x=False: (
            self.dummy_io_acknowledge := '5',
            )[-1] """

        self.read_pos_current_mach = lambda : self.dummy_pos_current_mach
        self.write_pos_comp_mach = lambda x:self.__setattr__('dummy_pos_comp_mach',x)
        """ lambda pos: (self.dummy_pos_comp_mach:=pos)[0] """

        self.is_hal_exists = find_spec('hal') is not None
        self.is_linuxcnc_exists = find_spec('linuxcnc') is not None

        if self.is_hal_exists and self.is_linuxcnc_exists:
            import hal, linuxcnc
            #change read/write function to connect linuxCNC
            pass
        pass
    
    def dice_values(self):
        for index in range(len(self.dummy_pos_current_mach)):
            self.dummy_pos_current_mach[index] =  random()*1000
        pass
    pass