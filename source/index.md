# simpleRTK2B-SBC Documentation

Welcome!  
This is the documentation for **ArduSimple SBC**, a customizable dual-band GPS/GNSS RTK Single Board Computer.  
It’s based on **u-blox ZED-F9** module and allows you to build any application using its centimeter-level accuracy.

## User Guide

If this is the first time using the SBC, we suggest you check out these sections.

### Hardware Overview

Find a detailed description of how to power and communicate with your device in the [Hardware Overview](hardware/hardware.md). It includes descriptions of all components and peripherals for your applications.

### Mechanical Integration

Refer to the [Mechanical Integration](mechanical_integration/mechanical.md) section for SBC mechanical specs like weight, dimensions, and 2D/3D models to help with integration. It also includes enclosure options available in our store.

### Firmware

Our engineers continuously improve the SBC firmware to deliver the latest features. Learn how to update your firmware in the [Firmware](firmware/firmware.md) section.

In this section, you’ll find:

- [Download Firmware](firmware/update.md) – Get the latest firmware version.
- [Firmware Changelog](firmware/update.md) – Track new features and improvements in each firmware update.
- [Hardware Changelog](firmware/update.md) – Track new features and improvements in SBC hardware versions.

### Load Your Application

Discover how to upload and launch your own application by following the steps in the [Load Your Application](sw_update/sw_update.md) section.

### MicroPython IDEs

We provide some recommended options and tutorials for a better experience in the [MicroPython IDEs](ides/ides.md) section, although any MicroPython IDE can be used.

### SDK Developer Guide

If you're already familiar with the SBC hardware, jump directly to our [SDK Developer Guide](sdk/index.md).

## How to Connect...

This section helps you connect third-party devices to the SBC:

- [Relays](how_to_connect/relays) – Use the SBC to switch high-power devices.
- [Motors](how_to_connect/motors) – Easily control servo, stepper, and DC motors.

## Need Help?

If you have questions or suggestions, feel free to **[Contact Us](contact)**.

```{toctree}
:maxdepth: 2
:hidden:

hardware/hardware.md
mechanical_integration/mechanical.md
firmware/firmware.md
ides/ides.md
application/application.md
sdk/index.md
