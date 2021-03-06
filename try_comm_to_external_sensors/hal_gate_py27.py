#!/usr/bin/env python2
from __future__ import print_function
from imp import find_module
from os import getpid

try :
    find_module('hal') 
    __is_hal_existed = True
except ImportError:
    __is_hal_existed = False 

if __is_hal_existed :
    import hal
    
    instanized_comp = hal.component('delegation_{}'.format(getpid())) # must be create first then read value
    
    def hal_read_value(pin_name):
        return hal.get_value(pin_name)
        
    def hal_set_value(pin_name,value):
        return hal.set_p(pin_name,str(value)) # write value must be string

def dummy_echo(arg):
    return arg

def is_hal_existed():
    return __is_hal_existed


if __name__ == '__main__':
    from random import random
    value = hal_read_value('joint.0.pos-fb')
    hal_set_value('motion.analog-in-00',random())
    hal_set_value('motion.digital-in-00',1) # for boolean type this is ok
    hal_set_value('motion.digital-in-00',False) # for boolean type this is ok
    instanized_comp.exit() # this will kill components
    pass