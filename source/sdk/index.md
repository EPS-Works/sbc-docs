# SDK Developer Guide

Welcome to the Ardusimple's SDK Developer Guide. This guide provides a gentle but thorough introduction to the SDK and shows how to use it effectively to build custom applications.

The Ardusimple's SDK (*Software Development Kit*) provides a high-level MicroPython interface to interact with board's peripherals, hardware modules, and communication systems — all without needing to install anything extra. It comes bundled with the firmware and is ready to use out of the box.

```python
from sdk import Led

led = Led('LED_GREEN')
led.blink(times=4, period=100)
```

Each board also provides its own module with already configured hardware instances, so you don't have to worry about what specific pins or ports are used by each component.

```python
from sbc import LedGreen

LedGreen.blink(times=4, period=100)
```

## Get started with the SDK

If you’re ready to get hands-on with the SDK, follow the [API Reference](reference.md).

If you’re looking for real-world usage examples and code snippets, see the [Code Examples](examples.md).
