import os
import board
from luma.core.interface.serial import i2c, spi, pcf8574
from luma.core.interface.parallel import bitbang_6800
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1309, ssd1325, ssd1331, sh1106, sh1107, ws0010

from dotenv import load_dotenv

load_dotenv()

SDApin = os.getenv('SDA') 
SCLpin = os.getenv('SCL')

sda_pin = getattr(board, SDApin)
scl_pin = getattr(board, SCLpin)


serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)

with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="white", fill="black")
    draw.text((30, 40), "Hello World", fill="white")