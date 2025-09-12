# RF Antennas

All SBC versions include at least SMA connectors `SMA1` internally connected to GNSS1 signal input.

Additionally, the board provides `SMA2`, `SMA3` and `SMA4`, which are available for connecting external antennas to other SBC peripherals. These are directly linked to nearby MMCX connectors, allowing flexible routing via pigtail cables.

![SMA Connectors](img/connectors_sma.jpg)

For instance, if you install the 4G NTRIP master modem, you can improve signal reception by connecting external antennas. Use a u.FL to MMCX pigtail to route the modem’s RF output to the MMCX and attach external antennas to the respective SMA connector.

This setup ensures optimal signal performance for cellular or other RF-based modules.
