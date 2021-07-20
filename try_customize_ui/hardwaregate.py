import importlib
from importlib.util import find_spec
from random import random,seed
from datetime import datetime
from execnet import makegateway
from functools import reduce

seed(datetime.now())
class HardwardGate(object):
    def __init__(self, *args):
        super(HardwardGate, self).__init__(*args)

        self.linuxcnc_command_attr_list = []
        self.linuxcnc_stats_attr_list = []
        #create attribute list
        for x in ['linuxcnc_command_attr_list','linuxcnc_stats_attr_list']:
            channel = self._create_channel('hal_gate_py27',x,python_version='2.7', selection='one_shot')
            channel.send([])
            self.__setattr__(x,list(channel.receive()))
        
        #setup dummy functions as default
        self.hal_read_pin = self._dummy_hal_read_pin
        self.hal_write_pin = self._dummy_hal_write_pin
        self.linuxcnc_read_stat = self._dummy_linuxcnc_read_stat
        self.linuxcnc_write_command = self._dummy_linuxcnc_command

        if self._is_hal_existed() :
            
            self._hal_channel_read = self._create_channel('hal_gate_py27','hal_read_value',python_version='2.7')
            self._hal_channel_write = self._create_channel('hal_gate_py27', 'hal_set_value',python_version='2.7')

            self._linuxcnc_channel_read_stat = self._create_channel('hal_gate_py27','linuxcnc_read_stat',python_version='2.7')
            self._linuxcnc_channel_command = self._create_channel('hal_gate_py27','linuxcnc_command',python_version='2.7')

            #override the dummy function
            self.hal_read_pin = self._real_hal_read_pin
            self.hal_write_pin = self._real_hal_write_pin
            self.linuxcnc_read_stat = self._real_linuxcnc_read_stat
            self.linuxcnc_write_command = self._real_linuxcnc_command

            pass
        pass
    
    def _create_channel(self,module_name,function_name,python_version='3.9',selection='looping'):

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
        try:
            gateway = makegateway('popen//python=python{}'.format(python_version))
        except :
            gateway = makegateway()
        channel = gateway.remote_exec(context.format(module_name,function_name))
        return channel
    
    def _is_hal_existed(self):
        #check from python 2.y if hal existed
        try :
            

            channel = self._create_channel('hal_gate_py27','is_hal_existed',python_version='2.7', selection='one_shot')
            channel.send([])
            result = bool(channel.receive())
        except : 
            result = False
        return result

    def _real_hal_read_pin(self,pin_name):
        self._hal_channel_read.send([pin_name])
        return self._hal_channel_read.receive()

    def _real_hal_write_pin(self,pin_name,value):
        self._hal_channel_write.send([pin_name,str(value)])
        return self._hal_channel_write.receive()

    def _real_linuxcnc_read_stat(self,attr_name : str):
        self._linuxcnc_channel_read_stat.send([attr_name])
        return self._linuxcnc_channel_read_stat.receive()

    def _real_linuxcnc_command(self,cmd_name : str, *args):
        self._linuxcnc_channel_command.send([cmd_name,args])
        return self._linuxcnc_channel_command.receive()

    def _dummy_hal_read_pin(self,pin_name : str):

        if not hasattr(self,'_dummy_pos_current_mach') :
            self._dummy_pos_current_mach = [random() for x in range(0,3)]

        def _simu_dice_pos_values():
            self._dummy_pos_current_mach =  [x+ random() for x in self._dummy_pos_current_mach]

        if not hasattr(self,'_dict_hal_keys'):
            self.dict_hal_keys = {
            }

        if 'pos-fb' in pin_name:
            _simu_dice_pos_values()
            index = int(pin_name.split('.')[1])
            return self._dummy_pos_current_mach[index]
            pass
        elif False :
            pass

        return 1

    def _dummy_hal_write_pin(self,pin_name,value):
        return 1

    def _dummy_linuxcnc_read_stat(self,attr_name : str):
        if 'homed' in attr_name :
            return [bool(True)]*len(self._dummy_pos_current_mach)
        return 1

    def _dummy_linuxcnc_command(self,cmd_name : str, *args):
        return 1
    
    """ def hal_read_current_pos(self):
        return [ self.hal_read_pin('joint.{}.pos-fb'.format(x)) for x in range(0,3)]
    def hal_write_comp_pos(self,pos=[]):
        for index in range(len(pos)):
            self.hal_write_pin('motion.analog-in-0{}'.format(index),pos[index]) """


    pass