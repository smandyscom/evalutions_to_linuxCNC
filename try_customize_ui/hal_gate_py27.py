#!/usr/bin/env python2
from __future__ import print_function
from imp import find_module
from os import getpid

#default as non-sense list
_linuxcnc_stats_attr_list = ['estop','enabled','homed','joints','interp_state','in-pos','task_state','task_mode']
_linuxcnc_command_attr_list = ['command{}'.format(x) for x in range(0,10)]

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

    
    stat_channel = linuxcnc.stat() # create a connection to the status channel
    command_channel = linuxcnc.command()
    _linuxcnc_stats_attr_list = [x for x in dir(stat_channel) if not x.startswith('_')]
    _linuxcnc_stats_attr_list.remove('poll')
    _linuxcnc_stats_attr_list.remove('tool_table')
    _linuxcnc_command_attr_list =   [x for x in dir(command_channel) if not x.startswith('_')]  
    def linuxcnc_read_stat(attr):
        global _linuxcnc_stats_attr_list

        stat_channel.poll() # get current values

        if attr in _linuxcnc_stats_attr_list:
            return getattr(stat_channel,attr)
        
        return 0

    def linuxcnc_command(cmd,*args):
        global _linuxcnc_command_attr_list
        
        if cmd in _linuxcnc_command_attr_list :
            return getattr(command_channel,cmd)(*args)
        
        return 0


def dummy_echo(arg):
    return arg

def is_hal_existed():
    return _is_hal_existed

def linuxcnc_command_attr_list():
    return _linuxcnc_command_attr_list

def linuxcnc_stats_attr_list():
    return _linuxcnc_stats_attr_list


if __name__ == '__main__':

    linuxcnc_read_stat('empty')
    linuxcnc_command('empty')
    linuxcnc_command('state',2)

    from random import random
    value = hal_read_value('joint.0.pos-fb')
    hal_set_value('motion.analog-in-00',random())
    hal_set_value('motion.digital-in-00',1) # for boolean type this is ok
    hal_set_value('motion.digital-in-00',False) # for boolean type this is ok
    instanized_comp.exit() # this will kill components

    
    pass