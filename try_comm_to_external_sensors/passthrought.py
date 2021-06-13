#!/usr/bin/env python
import hal, time
h = hal.component("passthrough") #can be created when linuxcnc is running, this would created USERSPACE process
h.newpin("in", hal.HAL_FLOAT, hal.HAL_IN)
h.newpin("out", hal.HAL_FLOAT, hal.HAL_OUT)
h.ready()
try:
    while 1:
        time.sleep(1)
        h['out'] = h['in']
except KeyboardInterrupt:
    raise SystemExit