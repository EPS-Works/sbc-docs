# Board Hardware Module

Each device ships with its own pre-configured board-specific hardware module that make onboard components instantly available —no pin mapping, no manual initialization- so you can use hardware right away and focus on application logic, not setup.

For SBC (Single Board Computer) devices, the board-specific module is called `sbc`. To see what hardware instances are available on your specific board, you can inspect the module.

```python
import sbc

# List all available hardware instances
print(dir(sbc))

# Get information about a specific instance
help(sbc.GNSS1)
```

Setting up embedded hardware manually requires knowing every pin, port, and timing parameter — and getting their initialization order right. It’s slow, error-prone, and distracts from your actual goals.

<!-- markdownlint-disable-next-line MD036 -->
**Using the generic SDK (requires manual configuration)**

```python
# Manual configuration required
from sdk import Led, XBeeSocket
from sdk.modules.gnss import Ublox

LedGreen = Led(pin="LEDGREEN")
GNSS1 = Ublox(socket=XBeeSocket(port=8, baudrate=115200))
XBEE_A = XBeeSocket(port=1, baudrate=115200)

LedGreen.on()
GNSS1.stream(messages=['GGA'])
UART2.write(b'Hello World')
```

<!-- markdownlint-disable-next-line MD036 -->
**Using the board-specific module (zero configuration)**

```python
# Hardware is already configured and ready to use
from sbc import LedGreen, GNSS1, XBEE_A

LedGreen.on()
GNSS1.stream(messages=['GGA'])
XBEE_A.write(b'Hello World')
```

## Best Practices

Always prefer board-specific instances over manual SDK configuration.

```python
# ✅ Preferred: Use board-specific instance
from sbc import GNSS1
GNSS1.stream(messages=['GGA'])

# ❌ Avoid: Manual configuration (unless necessary)
from sdk import XBeeSocket
from sdk.modules import Ublox
gnss = Ublox(socket=XBeeSocket(port=8, baudrate=115200))
```

Board modules provide hardware instances, but you can still use SDK classes for additional functionality.

```python
from sbc import GNSS1
from sdk import SerialBuffer, Stream
from sdk.parsers.nmea import Parser

# Use board hardware with SDK utilities
buffer = SerialBuffer(GNSS1)
cursor = buffer.cursor('__stream__');
with Stream(serial=cursor, parsers=[Parser()]) as stream:
    for message in stream:
        print(message)
```

Use manual SDK configuration when:

- Working with external hardware not on the board
- Needing custom configuration not available in board instances
- Provided instances lack a specific functionality

```{eval-rst}
.. nextprev::
```
