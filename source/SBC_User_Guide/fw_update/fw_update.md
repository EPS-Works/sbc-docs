# SBC firmware update

The SBC firmware is developed by ArduSimple and contains the low level functionalities to let you focus on the application high level programming in microPython.  
We recommend to always use the latest version of the SBC firmware since it contains new features and bug fixes.  
If you have any suggestions related to the firmware, please [contact us](../contact.md).

> **Note:**  
> You can find your SBC current firmware and hardware version by typing in the terminal:
> 
```python

from sbc import __platform__, __firmware__, __version__, __sdk__, __revision__

print(__revision__)    # e.g. R04 (hardware revision, only on SBC)
print(__platform__)    # e.g. simpleRTK2B-SBC-R04
print(__firmware__)    # e.g. 3.4.0; MicroPython v1.24.1-dirty on 2025-04-30
print(__version__)     # e.g. 0.1.0
```

To update your SBC firmware, you will need:

- SBC and USB C cable 
- Latest SBC firmware (download below)  
- STM32 Cube Programmer ([download here](https://www.st.com/en/development-tools/stm32cubeprog.html#overview&secondary=st-get-software))

> ⚠️ **Warning:**  
> Before updating the SBC firmware, make sure you backup the content of the SBC internal memory.

---

## Method 1: Using SBC button

1. Press and keep pressed the SBC button  
2. Connect the USB cable to the SBC and to your computer  
3. Release the SBC button  
4. Open STM32 Cube Programmer  
5. Select USB from the dropdown menu  
6. Click the refresh icon and wait for port detection  
7. Click the **CONNECT** button  
8. Click **Open file**  
9. Browse and select `firmware_mboot.hex`  
10. Click **Download** and wait for completion  
11. Press and keep pressed the SBC button, reset your device, then release the button  
12. Click the refresh icon again  
13. Click **CONNECT**  
14. Open and select `firmware.hex`  
15. Click **Download**  
16. Done! Your firmware is updated ✅

---

## Method 2: No access to SBC button (e.g. inside enclosure)

1. Connect USB cable  
2. Open a MicroPython terminal (**do NOT put this code in `main.py`!**)
3. Run:
    ```python
    import machine
    import time
    print("Entering bootloader in 10 seconds, press CTRL+C to cancel")
    time.sleep(10)
    machine.bootloader(True)
    ```
4. Open STM32 Cube Programmer  
5. Select USB and click refresh  
6. Click **CONNECT**  
7. Open `firmware_mboot.hex`, then click **Download**  
8. Reset the device, repeat step 3  
9. Refresh ports, click **CONNECT**  
10. Open `firmware.hex`, click **Download**  
11. Done! ✅

---

## Method 3: Programmatically (e.g. FOTA)

> ⚠️ **Warning:**  
> Make sure the microSD card is **NOT** plugged in.

> 💡 **Note:**  
> This works only if `firmware_mboot.hex` is already installed.

1. Copy `firmware.dfu.gz` to the SBC flash memory  
2. Run:
    ```python
    import sbc
    sbc.mboot.fw_update("firmware.dfu.gz")
    # Output:
    # hdr b'DfuSe\x01'
    # Fw update from firmware.dfu.gz . It will take about 30 seconds
    ```
3. Wait ~30 seconds, SBC will reboot automatically ✅

---

## Download Firmware

**Latest Release:**

- [FW1.07-20230323](releases/FW1.07.zip)

**Old Versions:**

- [FW1.05-20220701](releases/FW1.05.zip)  
- [FW1.04-20220628](releases/FW1.04.zip)  
- [FW1.03-20220609](releases/FW1.03.zip)  
- [FW1.02-20220204](releases/FW1.02.zip)  
- [FW1.01-20210401](releases/FW1.01.zip)

---

## Firmware Changelog

### 2023-03-23 - FW1.07
**Fixes:**

- Increased PointPerfect maximum buffer size

### 2022-07-09 - FW1.05
**New features:**

- FTPlib implemented

### 2022-06-28 - FW1.04
**Fixes:**

- MahonyAHRS numerical issue solved

### 2022-06-09 - FW1.03
**New features:**

- Added MQTT Client  
- PointPerfect ready

**Fixes:**

- Documentation updates (schematic, loading procedure, method examples)

### 2022-02-04 - FW1.02
**New features:**

- Added uasyncio with Semaphores & Queues  
- Added `ubx.builder` for UBX message composition  
- Added safety USB fallback to RS232#1  
- Added MicroWebSrv2  
- Drag&drop `.dfu.gz` firmware update  
- UDP connections, NTRIP client/server, async TCP client  
- Flashing via `.dfu`

**Fixes:**

- IMU FIFO flush, SPI DMA IRQ bug fix, gyro scale fix  
- RXM-RAWX message parsing

### 2021-04-01 - FW1.01

- First official firmware release

---

## Hardware Changelog

### R03
- First official hardware version
