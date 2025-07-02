# Load your application

There are 3 ways to load your MicroPython application

1. Run it directly from your [preferred IDE or terminal](../ides/ides.md).

  This option is perfect during the development of your code since it will allow you to iterate fast during the coding process.
  If you use this option, when you reset the power of your SBC, your application will not run since it is not stored in the non-volatile memory.

1. Rename your application *.py* file as `main.py` and drag and drop it to the SBC memory which is accessible with the Windows explorer as an external drive.

  After rebooting your SBC, your application will run automatically.

  This method is great to deploy your application.

3. Compile your *.py* file and name it **main.mpy**, drag and drop it to the SBC memory which is accessible with the Windows explorer as an external drive.
  After rebooting your SBC, your application will run automatically.

  This method is great to deploy your application while hiding its content to the final customer to prevent any modifications.
  Follow this [instructions](https://www.ardusimple.com/distribute-mpy-precompiled-files) on how to generate compiled *mpy* files.

:::{important}
By using methods **2** or **3** you can lock temporaly the SBC (e.g.: if you use a watchdog without feeding it, the SBC will reset continuously).

If this happens, try to:

- If you are using the microSD memory, remove the microSD card and delete/rename the main.py/mpy file on it by inserting the card directly to your computer.
- If you are using the SBC internal memory, reset the SBC and remove/rename the main.py/mpy as soon as the SBC memory is available.
- Sometimes the SBC resets too fast and it is not possible to remove/rename the main.py/mpy. If this is your case you will need to return the SBC to its default setting by [loading the firmware](../firmware/firmware.md) again.
:::
