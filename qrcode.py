import pyqrcode
import png
from pyqrcode import QRCode
s = str(input("Enter URL : "))
name = str(input("Enter website Name : "))
#GENERATE QRCODE
url = pyqrcode.create(s)
url.svg(name+".svg",scale = 8) #SAVE SVG FILE
url.png(name+".png", scale = 6) #SAVE PNG FILE
