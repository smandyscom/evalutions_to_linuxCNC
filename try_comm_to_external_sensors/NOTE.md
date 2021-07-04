# Coordinate system

## Tool

### To setup new tool

1. Specify X,Y even orientation of tool under **current** coordinate system
```gcode
G10 L10 P1 X-10 Y-10 Z0 
(Tell machine tool currently is on X-10 Y-10)
```
2. Load tool parameter from preset table
```gcode
G43 H1
```
- NOTE :
    For camera installed on Z-head, which could be preproamed its position by this. 
    After **CALIBRATION** operation done.


## Work Table

### To setup new coordinate system
1. Specify X,Y,Theta offset from machine coordinate system
```gcode
G10 L2 P1 X10 Y10 R20 
(This will set G54)
```
2. Select preset coordiante
```gcode
G54
```