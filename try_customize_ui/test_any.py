import inspect
from hardwaregate import HardwardGate
from controller import Controller



def test_hardwaregate_dummy():
    instance  = HardwardGate()
    value = instance._dummy_hal_read_pin('joint.0.pos-fb')
    pass

def test_controller_dummy():
    instance = Controller(None)
    instance.onUpdate()
    pass