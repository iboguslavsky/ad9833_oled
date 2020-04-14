# ad9833_oled
CLI for Orange Pi "hat" with AD9833 frequency generator and OLED display

### Components:

* Orange Pi Zero 512Mb
* AD9833 on SPI bus (/dev/spidev1.0)
* SSD1306 on an I2C bus (/dev/i2c-1)

Usage:
```
$ ./freq.pl --since 1_000_000
Waveform : sine
Freq: 1 MHz
```
