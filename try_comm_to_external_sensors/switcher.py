import importlib
from importlib.util import find_spec
from random import random

dummy_io_trigger = bool()
dummy_io_acknowledge = bool()
dummy_io_pos_index = int(-1)

dummy_pos_current_mach = [float()]*3 # x,y,theta, from CNC
dummy_pos_comp_mach = [float()]*3 # to CNC

class Swither(object):
    def __init__(self, *args):
        super(Swither, self).__init__(*args)

        global dummy_io_trigger
        global dummy_io_acknowledge
        global dummy_io_pos_index

        #interfaces 
        self.read_trigger = lambda : dummy_io_trigger
        self.read_pos_index = lambda : dummy_io_pos_index
        self.write_acknowledge = lambda x=False: (dummy_io_acknowledge:=x)[0]

        self.read_pos_current_mach = lambda : dummy_pos_current_mach
        self.write_pos_comp_mach = lambda pos: (dummy_pos_comp_mach:=pos)[0]

        is_hal_exists = find_spec('hal') is not None
        is_linuxcnc_exists = find_spec('linuxcnc') is not None

        if is_hal_exists and is_linuxcnc_exists:
            import hal, linuxcnc
            #change read/write function to connect linuxCNC
            pass
        pass
    
    def dice_values(self):
        global dummy_pos_current_mach

        for pos in dummy_pos_current_mach:
            pos = random()*1000

        pass
    pass