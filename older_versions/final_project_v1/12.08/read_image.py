from PIL import Image

im = Image.open('test_4.jpeg')

length_x_axis, length_y_axis = im.size


def read_image(lenght_x_axis, length_y_axis):
    pixels = list(im.getdata())


    sw_image = []
    for n in range(len(pixels)):
        sw_pixel_value = (((pixels[n])[0]) + ((pixels[n])[1]) + ((pixels[n])[2]))
        sw_image.append(sw_pixel_value)

    brightness = 0
    for n in range(len(new_image)):
        brightness = brightness + new_image[n]
    brightness = brightness/len(new_image)
    print(brightness)



read_image(length_x_axis, length_y_axis)