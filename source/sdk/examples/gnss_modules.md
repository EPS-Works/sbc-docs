# Using GNSS modules

This example demonstrates how to work with pre-configured GNSS module (GNSS_1) that's ready to use immediately, and adding new modules to available GPSx sockets.

**Supported GNSS Modules**: `Ublox ZED-F9P` and `Unicore UM98x`

```python
from sbc import GNSS_1, GPS1, GPS2, GNSS_MODULES

data = GNSS_1.read()  # GNSS1 is already ready to use

# Create new GNSS modules installed in board's GPSx ports
GNSS_2 = GNSS_MODULES.ZED_F9P(socket=GPS2)  # Ublox ZED-F9P module
GNSS_3 = GNSS_MODULES.UM98x(socket=GPS3)    # Unicore UM98x module

GNSS_2.on()  # GPSx sockets share power -> GNSS_2.on() == GNSS_3.on()
```
