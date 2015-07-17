#!/usr/bin/python2

from PIL import Image
filename = raw_input('please input the gif you want to convert:\n')
im = Image.open(filename)

try:
    while 1:
        im.convert('RGB').save('gif2jpg'+str(im.tell())+'.jpg')
        im.seek(im.tell()+1)
except EOFError:
    pass
