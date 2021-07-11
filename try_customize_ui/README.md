# Customized UI over NML on EMCTasker

Participatants

- PyQt as the main UI frame.
- EMCTasker module in the linuxCNC as the interface to control behavior of linuxCNC.

## Demo of TEACH System

- Implementing TEACH Points by MDI mode? i.e. send where the user want to get via some commands.
- Jogging mode.

### Purpose

1. let *FAE* able to adjust pre-defined positions, i.e WK feature point ready for vision capturing, or head cleaning point

2. Diagosis machine issue

### Specifications

1. [] activate system without default GUI

2. [] pre-defined position should be persistant.

3. [] feedrate should be able being defined.

4. [] replay pre-defined points should be ok.

5. [] should offer facilities in jog mode to change speed, target, mode

6. use scenerio consist:
    1. list each predefined point in a table
    2. when teaching, one button to record current posisition.
    3. when teaching, offer a control panel to jog axis (X,Y,Z)
    4. after teached, one button to replay recorded point.

### Notes

1. Only available for points related to G00

### Infrastructure

#### NGC side

1. a service routine to receive running composited G-code command?
    - or just simply use MDI mode to send simple G-code command?

#### HMI side
