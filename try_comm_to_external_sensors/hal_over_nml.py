import linuxcnc

command_interface = linuxcnc.command()
command_interface.set_analog_output(0,128) #will change motion.analog-out-00