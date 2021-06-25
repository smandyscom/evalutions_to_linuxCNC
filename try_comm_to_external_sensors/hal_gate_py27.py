#!/usr/bin/env python2
from __future__ import print_function
from importlib.util import find_spec
from os import getpid

__is_hal_existed = find_spec('hal') is not None
if __is_hal_existed :
    import hal
    
    instanized_comp = hal.componenet('delegation_{}'.format(getpid())) # must be create first then read value
    
    def hal_read_value(pin_name):
        return hal.get_value(pin_name)
        
    def hal_set_value(pin_name,value):
        return hal.set_p(pin_name,value)

def dummy_echo(arg):
    return arg

def is_hal_existed():
    return __is_hal_existed