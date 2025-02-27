# Digital IO

```python
from machine import Pin
from sbc import DigitalIO

dout = DigitalIO(pin=Pin(1, Pin.OUT))
dout.high()

din = DigitalIO(pin=Pin(2, Pin.IN))
din.attach(
    trigger=DigitalIO.RISING,
    handler=lambda _: print("Rising edge")
)
```

```{eval-rst}
.. automodule:: sbc.dio
   :members:
```
