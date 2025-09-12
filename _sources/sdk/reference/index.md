# API Reference

This section documents all the modules and classes included in the Ardusimple SDK.

The SDK is organized into several modules, each targeting a different area of functionality: hardware access, data streaming, GNSS communication, and common utilities.

## Core classes

Interact with onboard hardware and communication interfaces.

- [AnalogIn](ain.md) – Reads analog voltage levels through ADC.
- [CANBus](canbus.md) – Interface for CAN bus communication.
- [DigitalIO](dio.md) – Controls digital pins as input or output.
- [Ethernet](ethernet.md) – Manages Ethernet connectivity and DHCP/static config.
- [FlashDrive](flash.md) – Exposes onboard flash drive.
- [Forwarder](forward.md) – Forwards serial data between serial interfaces.
- [Led](led.md) – Controls onboard or external status LEDs.
- [PWM](pwm.md) – Outputs PWM signals for dimming, motor control, etc.
- [SerialBuffer](serial.md) – Buffered reader/writer for UART and stream-based interfaces.
- [Storage](storage.md) – Filesystem interface for persistent storage.
- [Stream](stream.md) – Monitors a serial interface and parses all incoming data in real-time.
- [UsbHub](usb.md) – Manage USB hub configuration.

## Modules

Drivers and interfaces for supported hardware modules.

- [Ublox](ublox.md) - Interface for u-blox GNSS modules.
- [BNO08x](bno08x.md) - Drivers for BNO08x IMUs.

## Parsers

Parsers for GNSS protocols.

- [NMEA](nmea.md) - Handles standard NMEA 0183 GNSS sentences.
- [UBX](ubx.md) - Handles binary UBX messages from u-blox devices.

## NTRIP

NTRIP functionality for RTK corrections over internet.

- [NTRIPClient](ntrip.md) - Handles connection and data reception.
- [RTKBridge](ntrip.md) - Forwards correction data over a serial interface.

## Utils

Convenience decorators and helper tools.

- [Encoder](encoder.md) - Encodes string using a salt-based substitution cipher.
- [OTA](ota.md) – Simple over-the-air update interface.
- [@retry](retry.md) – Retries a function on failure.
- [@periodic](periodic.md) – Runs a function at a fixed interval.
- [@debounce](debounce.md) – Debounces repeated calls (e.g. from noisy inputs).

## Filters

Signal processing utilities.

- [ExponentialMovingAverage](ain.md#noise-reduction) – Simple exponential moving average filter.

```{toctree}
:maxdepth: 2
:hidden:

ain.md
bno08x.md
canbus.md
debounce.md
dio.md
encoder.md
ethernet.md
flash.md
forward.md
led.md
nmea.md
ntrip.md
ota.md
periodic.md
pwm.md
retry.md
serial.md
storage.md
stream.md
usb.md
ublox.md
ubx.md
