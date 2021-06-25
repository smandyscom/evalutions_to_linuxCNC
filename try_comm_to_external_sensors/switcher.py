import importlib
from importlib.util import find_spec
from random import random
from execnet import makegateway
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

        self.read_pos_current_mach = lambda : self.dummy_pos_current_mach
        self.write_pos_comp_mach = lambda x:self.__setattr__('dummy_pos_comp_mach',x)

        if self.is_hal_existed() :
            
            self.hal_channel_read = self.create_channel('hal_gate_py27','hal_read_value')
            self.hal_channel_write = self.create_channel('hal_gate_py27', 'hal_set_value')

            #change read/write function to connect linuxCNC
            self.read_trigger = lambda : self.hal_read_pin('')
            self.read_pos_index = lambda : self.hal_read_pin('')
            self.write_acknowledge = lambda value: self.hal_write_pin('',value)
            self.read_ackowledge = lambda : self.hal_read_pin('')
            
            self.read_pos_current_mach = lambda : self.hal_read_pin('')
            self.write_pos_comp_mach = lambda value:self.hal_write_pin('',value)

            pass
        pass
    
    def dice_values(self):
        for index in range(len(self.dummy_pos_current_mach)):
            self.dummy_pos_current_mach[index] =  random()*1000
        pass

    def create_channel(self,module_name,function_name,python_version='3.9',selection='looping'):

        #To create looping or one-shot remote execution
        context = ''
        if selection == 'looping':
            context = """
                from {} import {} as the_function
                while True:
                    channel.send(the_function(*channel.receive()))
                """
        elif selection == 'one_shot':
            context = """
                from {} import {} as the_function
                channel.send(the_function(*channel.receive()))
                """

        #reference
        #'https://stackoverflow.com/questions/27863832/calling-python-2-script-from-python-3'
        gateway = makegateway('popen//python=python{}'.format(python_version))
        channel = gateway.remote_exec(context.format(module_name,function_name))
        return channel
    
    def is_hal_existed(self):
        #check from python 2.y if hal existed
        channel = self.create_channel('hal_gate_py27','is_hal_existed',python_version='2.7', selection='one_shot')
        channel.send()
        return bool(channel.receive())

    def hal_read_pin(self,pin_name):
        self.hal_channel_read.send(pin_name)
        return self.hal_channel_read.receive()

    def hal_write_pin(self,pin_name,value):
        self.hal_channel_write.send(pin_name,value)
        return self.hal_channel_write.receive()

    pass