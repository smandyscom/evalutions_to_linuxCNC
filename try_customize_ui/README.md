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

### Notes

1. Only available for points related to G00