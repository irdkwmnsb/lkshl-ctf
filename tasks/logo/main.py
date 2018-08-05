bits = "01001100 01001011 01010011 01001000 01001100 01111011 01010101 01011111 00110101 01100001 01110111 01011111 01110100 01101000 00110000 00110101 00110011 01011111 01101100 00110001 01110100 01110100 01101100 00110011 01011111 01100010 00110001 01110100 00110101 01111101"
bits = bits.split()
bits = "".join(bits)
#print(bits)

import PIL
from PIL import Image, ImageDraw

#I dont use this
flag = "LKSHL{U_5aw_th053_l1ttl3_b1t5}"
#Just for look

image = Image.open("lkl_logo.png")
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()
line = height - 4

index = 0
r = pix[0, 0][0] - 40
g = pix[0, 0][1] 
b = pix[0, 0][2] 
print(r, g, b)
for num in bits:
    if num == '0':
        index += 4
    else:
        draw.point((index, line), (r, g, b))
        draw.point((index, line + 1), (r, g, b))
        draw.point((index, line + 2), (r, g, b))
        draw.point((index, line + 3), (r, g, b))
        
        draw.point((index + 1, line), (r, g, b))
        draw.point((index + 1, line + 1), (r, g, b))
        draw.point((index + 1, line + 2), (r, g, b))
        draw.point((index + 1, line + 3), (r, g, b))

        draw.point((index + 2, line), (r, g, b))
        draw.point((index + 2, line + 1), (r, g, b))
        draw.point((index + 2, line + 2), (r, g, b))
        draw.point((index + 2, line + 3), (r, g, b))

        draw.point((index + 3, line), (r, g, b))
        draw.point((index + 3, line + 1), (r, g, b))
        draw.point((index + 3, line + 2), (r, g, b))
        draw.point((index + 3, line + 3), (r, g, b))
        index += 4
print(index)
image.save("lkl_logo.png", "PNG")
del draw
