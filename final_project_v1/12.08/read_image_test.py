# https://stackoverflow.com/questions/1109422/getting-list-of-pixel-values-from-pil

from PIL import Image
im = Image.open('test_2.jpeg')

pixels = list(im.getdata())
print(pixels[0])
tuple1 = pixels[0]
print(tuple1[0])

length_x_axis, length_y_axis = im.size
print(length_x_axis, length_y_axis)
#width, height = im.size
#pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]
