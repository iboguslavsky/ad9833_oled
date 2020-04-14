# ad9833_oled
CLI for Orange Pi "hat" with AD9833 frequency generator and OLED display

### Components:

* Orange Pi Zero 512Mb
* AD9833 on SPI bus: **/dev/spidev1.0**
* SSD1306 on an I2C bus: **/dev/i2c-1**

Usage:
```
$ ./freq.pl --sine 1_000_000
Waveform : sine
Freq: 1 MHz
```
<img src="https://github.com/iboguslavsky/ad9833_oled/blob/master/ssd1306.jpg" width="260">&nbsp;<img src="https://github.com/iboguslavsky/ad9833_oled/blob/master/sine_1MHz.png"  width="582">
