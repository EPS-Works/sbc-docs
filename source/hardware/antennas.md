# RF Antennas

All SBC versions have at least two SMA connectors: SMA1 and SMA2 that are connected internally to GPS1 and GPS2 signal inputs respectively.

![SMA Connectors](img/SMA_connectors.png)
*SMA Connectors*

In addition to that SMA3 and SMA4 can be used to mount external antennas of some of the SBC peripherals.

SMA3 and SMA4 are connected directly to the MMCX connector next to them, so you can use a pigtail to connect the MMCX conenctor to any of the SBC peripherals.

For example, if you plug the 4G NTRIP master modem on the SBC, you may want to improve the signal reception by adding two external antennas.

You would use a uFL to MMCX pigtail to connect the modem signal output to the MMCX connector and then an external antenna to SMA3 and SMA4.

![Pigtail cables](img/pigtails.png)