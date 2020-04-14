#!/usr/bin/python3

from ad9833 import AD9833
from oled.device import ssd1306
from oled.render import canvas
from PIL import ImageFont

import click

# i2c bus, device
wave = AD9833(1, 0)

# SPI Oled
oled = ssd1306(port=1, address=0x3C)

@click.command()
@click.option('--sine', '-s', is_flag=True, help='Sinusoid output')
@click.option('--triangle', '-t', is_flag=True, help='Triangle output')
@click.option('--square', '-q', is_flag=True, help='Square output')
@click.argument('freq', type=int)
def generate(sine, triangle, square, freq):

    if triangle:
      wave.set_shape('triangle')
    elif square:
      wave.set_shape('square')
    else:
      wave.set_shape('sine')

    wave.set_freq(freq)

    wave.send()
    diag = wave.print()
    click.echo(diag['shape'])
    click.echo(diag['freq'])

    font = ImageFont.truetype('fonts/C&C Red Alert [INET].ttf', 16)
    with canvas(oled) as draw:
        draw.text((0, 0), diag['shape'], font=font, fill=255)
        draw.text((0, 22), diag['freq'], font=font, fill=255)

generate()
