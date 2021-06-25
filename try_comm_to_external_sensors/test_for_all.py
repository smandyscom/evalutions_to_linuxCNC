from switcher import Swither
from random import random
from hal_gate_py27 import dummy_echo
from os import getcwd
from sys import path

def test_dummy_echo():
    puz = random()
    assert puz == dummy_echo(puz)
    pass

def test_channel():
    instance = Swither()
    channel = instance.create_channel('hal_gate_py27','dummy_echo',python_version='')

    for x in range(0,10):
        puz = random()
        channel.send([str(puz)]) #need to embrace arguments by a list
        recv = channel.receive()
        assert  str(puz) == recv
    pass

def test_channel_hal_py27():
    instance = Swither()
    read_channel = instance.create_channel('hal_gate_py27','hal_read_value',python_version='2.7')
    write_channel = instance.create_channel('hal_gate_py27','hal_set_value',python_version='2.7')
    
    pin_name = 'motion.analog-in-00'
    for x in range(0,10):
        value = random()

        write_channel.send([pin_name,str(value)])
        write_channel.receive()

        read_channel.send([pin_name]) #need to embrace arguments by a list
        recv = read_channel.receive()
        assert recv == value
    pass


def test_channel_is_hal_existed():
    instance = Swither()
    pass


def test_switcher_hal_funcs():
    instance = Swither()

    value = instance.read_trigger()
    value = instance.read_ackowledge()
    value = instance.read_pos_index()
    value = instance.read_pos_current_mach()

    instance.write_acknowledge(True)
    instance.write_pos_comp_mach([0,1,2])
    pass