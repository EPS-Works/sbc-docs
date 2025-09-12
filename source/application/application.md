# Load your application

There are 2 ways to load and run your MicroPython application on the SBC

## Execute on-the-fly

You can run your script directly using your [preferred IDE or terminal](../ides/ides.md). This method works great during development, allowing quick iteration and testing. Keep in mind that the script is not stored in non-volatile memory and will not run automatically after a power cycle or reset.

## From SBC storage

Rename your application file to `main.py` and copy it to the SBC's storage drive.
After reboot, the SBC will automatically run main.py.

:::{tip}
You can [precompile](https://www.ardusimple.com/distribute-mpy-precompiled-files) your main file into bytecode `main.mpy`.

Precompiled .mpy files offer several benefits over plain .py files. They load faster and consume less memory by skipping the on-the-fly compilation step. It also prevents easy inspection or modification of the code, which is good to protect your code, but makes debugging and updating more difficult without access to the original .py source.
:::

:::{important}
This method can temporarily lock the SBC, for example if your script enables a watchdog timer without feeding it, causing continuous resets.

**If using a microSD card:**
Remove the card, insert it into your computer, and delete or rename main.py or main.mpy.

**If using internal flash memory:**
Power cycle the SBC and quickly delete or rename the file once the drive mounts. If the SBC resets too fast to access storage, you'll need to [restore the firmware](../firmware/firmware.md) to factory defaults.
:::
