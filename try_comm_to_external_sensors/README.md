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

## Demo of Visual Alignment System

### Techniques

- [] Qt Designer to draw UI frame

### Infra

Interconnected LinuxCNC with External Vision System.
By assiting of vision system, the local coordiante (G54?) can be aligned with real where the workpiece is.  
Pixel point and angle from vision system should be transformed to be represented in mechanical system before being applied in compensation. To do so, the Transformation matrix should be build up in Calibration phase.

Transformation matrix and relevent calculations is maintained at external side since implementation on Python is relativly easier than G-code parser.

- A table to store 9 points pairs to represent the linkage of mechanical system and vision.

- A channel consisted following facilities per external vision. All of them build on linuxCNC side.
   1. 3 float out from linuxCNC to external vision. To send X,Y,$\theta$ of mech sys as current position.
      - ? Any present facilite?
   2. 3 float in from external vision to linuxCNC.To receive X,Y,$\theta$
   3. A flag set consisted
      - 1 digital IN from linuxCNC to external. As TRIGGER.
      - 1 digital OUT from external to linuxCNC. As ACK. 

