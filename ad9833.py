#!/usr/bin/python3

import spidev
from quantiphy import Quantity

SPI_SPEED = 1000000

SHAPE_ID = {
    'square': 0x2020,
    'triangle': 0x2002,
    'sine': 0x2000
}

class AD9833(object):

    # Chip Clock Frequency
    ClockFreq = 25000000

    def __init__(self, major, minor):
        self.spi = spidev.SpiDev()
        self.spi.open(major, minor);

    def set_shape(self, shape):
        self.shape = shape if shape in SHAPE_ID else 'sine'

    def set_freq(self, freq):
        self.freq = freq

    def send(self):
        # Calculate frequency word to send
        pulse = self.freq if self.shape is not 'square' else self.freq * 2
        word = hex(int(round((pulse*2**28)/self.ClockFreq)))

        # Split frequency word onto its seperate bytes
        MSB = (int(word, 16) & 0xFFFC000) >> 14
        LSB = int(word, 16) & 0x3FFF

        # Set control bits DB15 = 0 and DB14 = 1; for frequency register 0
        MSB |= 0x4000
        LSB |= 0x4000

        xfer = [byte 
            for word in (0x2100, LSB, MSB, SHAPE_ID[self.shape])
                for byte in word.to_bytes(2, 'big')]

        self.spi.xfer2(xfer, SPI_SPEED)

    def print(self):
        pretty_freq = Quantity(f"{self.freq} Hz")
        return {
                'shape': f"Waveform : {self.shape}", 
                'freq': f"Freq: {pretty_freq}"}