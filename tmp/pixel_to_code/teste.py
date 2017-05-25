#!/usr/bin/python

import sys
import math
import numpy
from PIL import Image

def pixel_to_bit(pixel,threshold=128):
    """Convert the pixel value to a bit."""
    if pixel > threshold:
        return 1
    else:
        return 0

def convert(im,center,inner_radius,outer_radius,fill=255,mark=False):
    pix = im.load()
    result = []
    for theta in numpy.linspace(0.0,2*numpy.pi,num=256,endpoint=False):
        spokedata = []
        for r in numpy.linspace(inner_radius,outer_radius,num=32):
            i = int(center[0] + r*math.cos(theta))
            j = int(center[1] + r*math.sin(theta))
            if i >= im.size[0] or i < 0 or j >= im.size[1] or j < 0:
                pixel = fill
            else:
                pixel = pix[i,j]
                if not mark is False:
                    pix[i,j] = 255-pix[i,j]
            bit = pixel_to_bit(pixel)
            spokedata.append(bit)
        result.append(spokedata)
    return result


def use():
    print "Use: ledconvert.py  imagefile [cx=center_x cy=center_y ri=inner_radius ro=outer_radius fill=fill_value mark=0 or 1]"
    print "Default value of the keyword arguments:"
    print "cx : center of the image"
    print "cy : center of the image"
    print "ri : 2"
    print "ro : half the width of the image"
    print "fill : value of the upper left corner of the image"
    print "mark : 0 (meaning False; use 1 for True)"

       

#
# Main script begins here.
#
# First check for keyword arguments on the command line.
#

kwargs = {'cx':None, 'cy':None, 'ri':None, 'ro':None, 'fill':None, 'mark':None }

if len(sys.argv) > 2:
    for kwa in sys.argv[2:]:
        if not '=' in kwa:
            print "Invalid keyword argument '%s'." % kwa
            print "All arguments after imagefile must be keyword arguments."
            use()
            exit(-1)
        (w,v) = kwa.split('=')
        if w in kwargs:
            kwargs[w]=int(v)
        else:
            print "Unknown keyword argument '%s'." % kwa
            use()
            exit(-1)

#
# Open the image file and get the basic information about it.
#
try:
    im = Image.open(sys.argv[1])
except:
    # Eventually this should give more useful information (e.g. file does not
    # exist, or not an image file, or ...
    print "Unable to open %s" % sys.argv[1]
    exit(-1)

print "format: %s   mode: %s   palette: %s" % (im.format,im.mode,im.palette)
width,height = im.size
print "The image is %d x %d" % im.size
if im.mode == "RGB":
    print sys.stderr, "Sorry, this program can't handle RGB images yet."
    exit(0)

#
# Set the default options for any that were not given on the command line.
# (Do this after opening the file, because some of the default options depend
# on the image data.)
#
if kwargs['cx'] is None:
    kwargs['cx'] = width/2
if kwargs['cy'] is None:
    kwargs['cy'] = height/2
if kwargs['ri'] is None:
    kwargs['ri'] = 2
if kwargs['ro'] is None:
    kwargs['ro'] = width/2
if kwargs['fill'] is None:
    pix = im.load()
    kwargs['fill'] = pix[0,0]
if kwargs['mark'] is None:
    kwargs['mark'] = 0

#
# Do it!
#
samples = convert(im,(kwargs['cx'],kwargs['cy']),kwargs['ri'],kwargs['ro'],
                fill=kwargs['fill'],mark=kwargs['mark'])

#
# Write the data to a new file.
# This part needs to be rewritten to put the output file into the desired form.
# For now, just write something readable to "radial_samples.dat"
#
f = open("radial_samples.dat",'w')
for d in samples:
    for b in d:
        f.write("%d " % b)
    f.write('\n')
f.close()

#
# If mark was set, the sampled pixels have been inverted.
# Save the image to a new file, so we can look at the sample pattern.
#
if kwargs['mark'] != 0:
    im.save("tmp.png")
