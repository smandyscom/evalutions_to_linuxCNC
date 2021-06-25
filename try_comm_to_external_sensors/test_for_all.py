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