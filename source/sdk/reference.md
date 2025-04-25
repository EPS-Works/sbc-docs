# API Reference

This section documents all the modules and classes included in the Ardusimple SDK.

The SDK is organized into several modules, each targeting a different area of functionality: hardware access, data streaming, GNSS communication, and common utilities.

## Core classes

Interact with onboard hardware and communication interfaces.

- [AnalogIn](../../sbc-sdk/src/sdk/ain.md) – Reads analog voltage levels through ADC.
- [CANBus](../../sbc-sdk/src/sdk/canbus.md) – Interface for CAN bus communication.
- [DigitalIO](../../sbc-sdk/src/sdk/dio.md) – Controls digital pins as input or output.
- [Ethernet](../../sbc-sdk/src/sdk/ethernet.md) – Manages Ethernet connectivity and DHCP/static config.
- [FlashDrive](../../sbc-sdk/src/sdk/flash.md) – Exposes onboard flash drive.
- [Forwarder](../../sbc-sdk/src/sdk/forward.md) – Forwards serial data between serial interfaces.
- [Led](../../sbc-sdk/src/sdk/led.md) – Controls onboard or external status LEDs.
- [PWM](../../sbc-sdk/src/sdk/pwm.md) – Outputs PWM signals for dimming, motor control, etc.
- [SerialBuffer](../../sbc-sdk/src/sdk/serial.md) – Buffered reader/writer for UART and stream-based interfaces.
- [Storage](../../sbc-sdk/src/sdk/storage.md) – Filesystem interface for persistent storage.
- [Stream](../../sbc-sdk/src/sdk/stream.md) – Monitors a serial interface and parses all incoming data in real-time.
- [UsbHub](../../sbc-sdk/src/sdk/.md) – Manage USB hub configuration.

## Modules

Drivers and interfaces for supported hardware modules.

- [Ublox](../../sbc-sdk/src/sdk/modules/gnss/ublox.md) - Interface for u-blox GNSS modules.
- [BNO08x](../../sbc-sdk/src/sdk/modules/bno08x.md) - Drivers for BNO08x IMUs.

## Parsers

Parsers for GNSS protocols.

- [NMEA](../../sbc-sdk/src/sdk/parsers/nmea.md) - Handles standard NMEA 0183 GNSS sentences.
- [UBX](../../sbc-sdk/src/sdk/parsers/ubx.md) - Handles binary UBX messages from u-blox devices.

## NTRIP

NTRIP functionality for RTK corrections over internet.

- [NTRIPClient](../../sbc-sdk/src/sdk/ntrip/ntrip.md) - Handles connection and data reception.
- [RTKBridge](../../sbc-sdk/src/sdk/ntrip/ntrip.md) - Forwards correction data over a serial interface.

## Utils

Convenience decorators and helper tools.

- [@retry](../../sbc-sdk/src/sdk/utils/retry.md) – Retries a function on failure.
- [@periodic](../../sbc-sdk/src/sdk/utils/periodic.md) – Runs a function at a fixed interval.
- [@debounce](../../sbc-sdk/src/sdk/utils/debounce.md) – Debounces repeated calls (e.g. from noisy inputs).
- [OTA](../../sbc-sdk/src/sdk/utils/ota.md) – Simple over-the-air update interface.
- [Encoder](../../sbc-sdk/src/sdk/utils/encoder.md) - Encodes string using a salt-based substitution cipher.

## Filters

Signal processing utilities.

- [ExponentialMovingAverage](../../sbc-sdk/src/sdk/ain.md#noise-reduction) – Simple exponential moving average filter.
