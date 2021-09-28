from __future__ import print_function

from qtvcp.lib.keybindings import Keylookup
from qtvcp.core import Status, Action

# Set up logging
from qtvcp import logger
LOG = logger.getLogger(__name__)

# Set the log level for this module
#LOG.setLevel(logger.INFO) # One of DEBUG, INFO, WARNING, ERROR, CRITICAL

###########################################
# **** INSTANTIATE LIBRARIES SECTION **** #
###########################################

KEYBIND = Keylookup()
STATUS = Status()
ACTION = Action()

class VCPWindow:
    def __init__(self,halcomp,widgets,paths):
        pass

    def test_button(self):
        print('on testing')


def get_handlers(halcomp,widgets,paths) : 
    return [VCPWindow(halcomp,widgets,paths)]