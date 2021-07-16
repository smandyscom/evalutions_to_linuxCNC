#!/usr/bin/env python2
from __future__ import print_function
from imp import find_module
from os import getpid

try :
    find_module('hal') 
    _is_hal_existed = True
except ImportError:
    _is_hal_existed = False 

if _is_hal_existed :
    import hal,linuxcnc
    
    instanized_comp = hal.component('delegation_{}'.format(getpid())) # must be create first then read value
    
    def hal_read_value(pin_name):
        return hal.get_value(pin_name)
        
    def hal_set_value(pin_name,value):
        return hal.set_p(pin_name,str(value)) # write value must be string

    stats_attr_list = None
    command_attr_list = None
    def linuxcnc_read_stat(attr):
        global stats_attr_list

        stat_channel = linuxcnc.stat() # create a connection to the status channel
        stat_channel.poll() # get current values

        if stats_attr_list is None :
            stats_attr_list = [x for x in dir(stat_channel) if not x.startswith('_')]

        if attr in stats_attr_list:
            return getattr(stat_channel,attr)
        
        return 0

    def linuxcnc_command(cmd,*args):
        global command_attr_list

        command_channel = linuxcnc.command()

        if command_attr_list is None:
            command_attr_list = [x for x in dir(command_channel) if not x.startswith('_')]
        
        if cmd in command_attr_list :
            return getattr(command_channel,cmd)(args)
        
        return 0


def dummy_echo(arg):
    return arg

def is_hal_existed():
    return _is_hal_existed


if __name__ == '__main__':

    linuxcnc_read_stat('empty')
    linuxcnc_command('empty')

    from random import random
    value = hal_read_value('joint.0.pos-fb')
    hal_set_value('motion.analog-in-00',random())
    hal_set_value('motion.digital-in-00',1) # for boolean type this is ok
    hal_set_value('motion.digital-in-00',False) # for boolean type this is ok
    instanized_comp.exit() # this will kill components

    
    pass