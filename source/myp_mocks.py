"""MicroPython mocking utilities for Sphinx autodoc."""

# pylint: disable=missing-docstring,unused-argument,too-few-public-methods,multiple-statements

import sys
import builtins


def setup_micropython_mocks():
    """Setup all MicroPython mocks for documentation generation."""

    # Mock const function
    builtins.const = lambda x: x  # type: ignore

    # Create proper machine module mock with working Pin constants
    class MockPin:
        # Pin modes
        IN = 1
        OUT = 2
        OPEN_DRAIN = 4
        ALT = 8
        ALT_OPEN_DRAIN = 16
        ANALOG = 32

        # Pull modes
        PULL_UP = 1
        PULL_DOWN = 2

        # Drive modes
        DRIVE_0 = 0
        DRIVE_1 = 1

        # IRQ triggers - these need to be integers that work with bitwise operations
        IRQ_RISING = 1
        IRQ_FALLING = 2

        def __init__(self, *args, **kwargs): ...
        def on(self): ...
        def off(self): ...
        def irq(self, **kwargs): ...
        def value(self, v=None): return 0 if v is None else None

    class MockADC:
        def __init__(self, *args): ...
        def read_u16(self): return 0

    class MockI2C:
        def __init__(self, *args, **kwargs): ...
        def writeto(self, *args): ...
        def readfrom(self, *args): return b''
        def readfrom_into(self, *args): ...
        def writeto_mem(self, *args): ...
        def readfrom_mem(self, *args): return b''
        def readfrom_mem_into(self, *args): ...

    class MockTimer:
        ONE_SHOT = 1
        PERIODIC = 2

        def __init__(self, *args): ...
        def init(self, *args, **kwargs): ...
        def deinit(self): ...

    class MockUART:
        IRQ_RXIDLE = 16

        def __init__(self, *args, **kwargs): ...
        def init(self, *args, **kwargs): ...
        def deinit(self): ...
        def any(self): return 0
        def read(self): return b''
        def readchar(self): return -1
        def readinto(self, buf): return 0
        def write(self, data): return len(data)
        def irq(self, **kwargs): ...
        def flush(self): ...

    class MockMachine:
        Pin = MockPin
        ADC = MockADC
        I2C = MockI2C
        Timer = MockTimer
        UART = MockUART

    # Replace the machine module in sys.modules before importing SDK
    sys.modules['machine'] = MockMachine() # type: ignore
