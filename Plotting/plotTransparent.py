# -*- coding: utf-8 -*-
"""
Created on Thu July 5 11:05:07 2018

@author: Nicholas Sotiriou - github: @nsotiriou88
"""

from PIL import Image
from resizeimage import resizeimage

# img = Image.open('Rider02.png')
# img = img.convert("RGBA")
# datas = img.getdata()

# newData = []
# for item in datas:
#     if not(item[0] == 0 and item[1] == 0 and item[2] == 255):
#         newData.append((255, 255, 255, 0))
#     else:
#         newData.append(item)

# img.putdata(newData)
# img.save("RealRider2.png", "PNG")


with open('RealRider1.png', 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image, [640, 400])
        cover.save('test-image-cover.jpeg', image.format)
