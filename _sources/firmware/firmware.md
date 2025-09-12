# Firmware

The SBC comes preloaded with firmware developed by ArduSimple, providing all essential low-level functionality to manage the hardware. This allows you to focus entirely on high-level application development in MicroPython, without worrying about peripheral setup or hardware abstraction.

To ensure stability and access to the latest features, we strongly recommend using the latest firmware version, which includes ongoing bug fixes, performance improvements, and new capabilities.

:::{tip}
You can find your current firmware and hardware version by typing in the terminal

```python
from sbc import __platform__, __firmware__, __version__, __revision__

print(__platform__) # simpleRTK2B-SBC-R04
print(__firmware__) # 3.4.0; MicroPython v1.24.1-dirty on 2025-04-30
print(__revision__) # R04 (only in SBC)
print(__version__) # 0.1.0
:::

## Firmware Update

Keeping your SBC firmware up to date ensures access to the latest features, bug fixes, and performance enhancements.

Depending on your hardware setup and how you access the SBC, there are 2 supported methods for updating the firmware. This guide will walk you through each option so you can choose the most suitable approach for your use case.

You will need:

- The SBC and a USB-C cable
- The latest firmware files (available below)
- [STM32 Cube Programmer](https://www.st.com/en/development-tools/stm32cubeprog.html#overview&secondary=st-get-software)

:::{warning}
Before updating, make sure to back up any important files stored on the SBC’s internal flash or microSD card.
:::

### Method 1: Using SBC button

This method uses the onboard button to place the SBC into bootloader mode for firmware flashing via STM32CubeProgrammer.

1. **Press and hold** the SBC button.
2. Connect the USB cable between the SBC and your computer.
3. Release the SBC button — the board will now be in bootloader mode.
4. Launch `STM32CubeProgrammer`.
5. In the connection side panel, select USB from the dropdown. If the board doesn't appear yet, click the refresh icon and wait for port detection.
6. Click the *Connect* button
7. Under the *Erasing & Programming section*, click *Browse* and select the firmware file.
8. Click *Start Programming* and wait for completion.
9. Done! 🎉

### Method 2: Without access to SBC button

If the SBC button is not physically accessible, you can enter bootloader mode through MicroPython.

1. Connect the SBC to your computer via USB.
2. Open a MicroPython terminal
3. Execute the following:
    ```python
    import machine
    machine.bootloader(True)
    ```

    :::{warning}
    Do not place this code in `boot.py` or `main.py`, or the board will enter bootloader mode on every boot!
    :::

4. Launch `STM32CubeProgrammer`.
5. In the connection side panel, select USB from the dropdown. If the board doesn't appear yet, click the refresh icon and wait for port detection.
6. Click the *Connect* button
7. Under the *Erasing & Programming section*, click *Browse* and select the firmware file.
8. Click *Start Programming* and wait for completion.
9. Done! 🎉

## Download Firmware

**Latest Release:**

**Old Versions:**
