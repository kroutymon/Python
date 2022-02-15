# Quick respond gen
import qrcode 
from PIL import Image
import PIL

#
qr = qrcode.QRCode(box_size = 50, border = 5)

# data in qrcode
qr.add_data("test")

# make the picture
img = qr.make_image(fill_color = "black", back_color = "orange")

# save file as "test.png"
pic = Image.open()

pic = pic.save("test.png")