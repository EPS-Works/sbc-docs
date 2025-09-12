# simpleRTK2B-SBC Documentation

Welcome to the official documentation for the **ArduSimple SBC** — a customizable dual-band GPS/GNSS RTK Single Board Computer built on an **STM32** microcontroller and a **u-blox ZED-F9** module. Designed for flexible and high-performance embedded applications, it offers centimeter-level positioning accuracy.

## Quick Start Guide

**New to the SBC?** Start with our [Getting Started Guide](getting_started/quickstart.md) to quickly get your board up and running.

It covers unboxing, initial setup, and your first positioning fix. Perfect for evaluating the board's capabilities before custom development.

## Platform Overview

Start here to understand the platform capabilities before diving into the details.

The [Hardware Overview](hardware/hardware.md) covers the SBC's core components, including power input options, IO pinout, serial interfaces, RF connectors, memory specifications, and onboard sensors.

Visit the [Mechanical Integration](mechanical_integration/mechanical.md) section for mechanical specifications, 2D/3D models, dimensions, and enclosure options for integrating the SBC into physical projects.

In the [Firmware](firmware/firmware.md) section you'll find how to keep your board up to date with the latest features and bug fixes. It provides update procedures, download links, version compatibility, and troubleshooting recovery scenarios.

## Application Development

The [IDEs & Development Toolset](ides/ides.md) guide will help you setting up your development environment with our recommended tools, extensions, and configurations. It includes setup instructions for popular IDEs with MicroPython support, debugging capabilities, and productivity enhancements.

Once your environment is ready, follow our [Deploy Your Application](application/application.md) guide for uploading, launching, and managing your custom applications on the SBC. You'll find deployment methods, file management, and application lifecycle management.

Get started with our custom SDK to build applications. The [SDK Developer Guide](sdk/index.md) includes a detailed API reference, code examples and best practices to accelerate development.

## Hardware Integration

Interface with third-party components and expand your SBC's functionality.

- [Relays](how_to_connect/relays) — Control high-power devices and switching applications.
- [Motors](how_to_connect/motors) — Interface with servos, steppers, and DC motors.
- [Sensors](how_to_connect/sensors) — Integrate additional sensors and measurement devices.

## Support & Community

**Need assistance?** We're here to help with technical questions, troubleshooting, and project guidance.

For technical support, documentation feedback, or project consultation, please [Contact Us](contact).

```{toctree}
:maxdepth: 2
:hidden:

hardware/hardware.md
mechanical_integration/mechanical.md
firmware/firmware.md
ides/ides.md
application/application.md
sdk/index.md
```
