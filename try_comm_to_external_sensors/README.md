# Online Communication To External Devices

## RS274 G-Code Parser Side

- Flag Out (Digital Out)
  1. Through [*M62 - M65*](http://linuxcnc.org/docs/2.8/html/gcode/m-code.html#mcode:m62-m65) Digital Output Control. 
     - Note : Quote for synchronized motion, The actual change of the specified outputs will happen at the beginning of the next motion command.
- Flag In (Digital In)
  - Block execution
    1. Through [*M66*](http://linuxcnc.org/docs/2.8/html/gcode/m-code.html#mcode:m66) Wait on Input
  - Non-Block execution
    1. [*#<_hal[Hal item]>*](http://linuxcnc.org/docs/2.8/html/gcode/overview.html#gcode:ini-hal-params) allows to be read
- Numerics In
  1. *#<_hal[Hal item]>* allows to be read
- Numerics Out
  1. [*M67*](http://linuxcnc.org/docs/2.8/html/gcode/m-code.html#mcode:m67) Analog Output,Synchronized
  2. [*M68*](http://linuxcnc.org/docs/2.8/html/gcode/m-code.html#mcode:m68) Analog Output, Immediate
  3. [*M100 - M199*](http://linuxcnc.org/docs/2.8/html/gcode/m-code.html#mcode:m100-m199) User Defined Commands, which can be used to trigger external programe, but limited to only 2 parameters can be taken.
     - Note: external programe can be BASH script or Python script, depends on the fist environment indicator. i.e *#!/bin/bash*

Also can refer to [Motion](http://linuxcnc.org/docs/2.8/html/config/core-components.html#_options) to get how to configure numbers of DIO/AIO of motion module.

## User Space Side (Python)

- Over NML channel through EMCTasker, to change I/O, Analog status of *motion componenet*, initialize command interface like this:

   ```python
   import linuxcnc
   c = linuxcnc.command()
   ```

   - Read Flag, *din*
   - Acknowledge Flag, *set_digital_output(int, int)*
   - Send Numeric, *set_analog_output(int, float)*
   - Read Numeric, *ain*

- Through [*HAL*](http://linuxcnc.org/docs/2.8/html/hal/halmodule.html)
   - easy and consistent way to access : 
   ```python
   #!/usr/bin/env python
   import hal, time
   h = hal.component("passthrough")
   h.newpin("in", hal.HAL_FLOAT, hal.HAL_IN)
   h.newpin("out", hal.HAL_FLOAT, hal.HAL_OUT)
   h.ready()
   try:
       while 1:
           time.sleep(1)
           h['out'] = h['in']
    except KeyboardInterrupt:
        raise SystemExit
   ```
