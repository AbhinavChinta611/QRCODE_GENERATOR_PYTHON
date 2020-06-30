# QRCODE_GENERATOR_PYTHON
Let’s see how to generate QR code in Python using pyqrcode module.  pyqrcode module is a QR code generator. The module automates most of the building process for creating QR codes. This module attempts to follow the QR code standard as closely as possible. The terminology and the encodings used in pyqrcode come directly from the standard.

# CODE : 
import pyqrcode
import png
from pyqrcode import QRCode
s = str(input("Enter URL : "))
name = str(input("Enter website Name : "))
#GENERATE QRCODE
url = pyqrcode.create(s)
url.svg(name+".svg",scale = 8) #SAVE SVG FILE
url.png(name+".png", scale = 6) #SAVE PNG FILE


# To use the above given code you need to install the following modules:

pip install pyqrcode

pip install pypng
