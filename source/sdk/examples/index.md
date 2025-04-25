# Code Examples

This page contains example scripts that demonstrate how to use the SDK to build real-world applications by combining different components. These examples go beyond basic class usage and showcase more complete integrations.

> For usage examples of individual classes, see their respective pages in the [API Reference](../reference/index.md).

## Micropython Basics

All examples in this guide are written in [MicroPython](https://micropython.org/) — a lean implementation of Python 3 optimized to run on embedded devices. If you are already familiar with Python, you'll find MicroPython very similar, with a few differences and limitations. Check out the [Micropython Reference](https://docs.micropython.org/en/latest/reference/index.html) to know more.

When the board powers up or resets, it runs two files automatically if they exist:

`boot.py`: Executed first. Used to configure low-level settings (e.g. USB mode, pins). Runs once at startup.

`main.py`: Executed after boot.py. This is where your application logic goes.

The SDK is fully available in both files and can be used right away.
