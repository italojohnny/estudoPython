from PIL import Image
im = Image.open('joycar.png')

pixels = list(im.getdata())
width, height = im.size
pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]


for y, pixel in enumerate(pixels):
    for x, color in enumerate(pixel):
        if color < 255:
            print "u8g.setColorIndex(%s);u8g.drawPixel(%s,%s);" % (color, x, y)
