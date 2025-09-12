
# Power

There are two ways to power the SBC, via the [USB C connector](#usb-c-connector) or via the [5-24V DC Molex microfit connector](#v-dc-molex-micro-fit-connector).

## USB-C connector

Simply plug in the provided USB-C cable and connect it to your computer or a USB wall charger.
The USB-C interface can power the SBC and all its accessories, including the 4G modem, Bluetooth, and Wi-Fi. You only need to ensure that the wall charger or computer USB port can supply enough power.

![SBC Pinout](img/port_usb.jpg)

:::{note}
You can use the USB-C connector to power the SBC with any commercial USB power bank. This is an easy way to ensure your SBC is tolerant of power interruptions.
:::

### Power consumption in different configurations

- Minimum power (microcontroller only, no USB hub and no GPS/GNSS receivers): 0.48W (40mA @ 12V, measured at 25ºC)
- 1 GPS/GNSS receiver: 1.56W (130mA @ 12V, measured at 25ºC)
- 2 GPS/GNSS receivers: 1.98W (165mA @ 12V, measured at 25ºC)
- 3 GPS/GNSS receivers: 2.4W (200mA @ 12V, measured at 25ºC)
- 3 GPS/GNSS receiver + 4G NTRIP client + XLR radio: 3.9W (325mA @ 12V, measured at 25ºC)

:::{important}
We do not recommend using the USB-C interface to power the SBC for applications involving vibrations, such as heavy machinery or drones, since this connector may become loose. We recommend using the heavy-duty [Micro-Fit connector](#v-dc-molex-micro-fit-connector) connector instead.
:::

## 5-24V DC Molex Micro-Fit connector

Plug the Molex Micro-Fit connector into the SBC, then connect the black (ground) and red (positive) wires to a DC power source ranging from 5V to 24V.
This type of connector is designed to withstand strong vibrations, making it the perfect choice for an SBC that must work in a harsh environment.

![SBC Pinout](img/power_molex.jpg)

:::{note}
You can power the SBC directly with a 12V or 24V automotive lead-acid battery. The internal voltage regulators in the SBC will handle the variable voltage of these batteries while they are charging.
:::
