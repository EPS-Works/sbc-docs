# Led

```python
from time import sleep
from machine import Pin
from sbc import Led

led = Led(pin=Pin(1, Pin.OUT))
led.on()

led.blink()
sleep(1)
led.halt()

led.blink(times=10, period=500)
```

```{eval-rst}
.. automodule:: sbc.led
   :members:
```
