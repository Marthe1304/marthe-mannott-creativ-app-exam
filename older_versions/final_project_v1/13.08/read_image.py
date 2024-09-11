# https://datagy.io/python-resize-image-pillow/
from PIL import Image

def rescale_image(image, max_width, max_height):
    width, height = image.size
    if width > max_width or height > max_height:
        factor = 1
        while True:
            if width/(factor) <= max_width and height/(factor) <= max_height:
                break
            else:
                factor += 1
    print("Rescale Factor:", factor)
    rescale_dimensions = (int(width/factor), int(height/factor))
    image = image.resize(rescale_dimensions)
    print("Image Dimensions:", image.size)
    return image, rescale_dimensions[0], rescale_dimensions[1]


def convert_image_to_swlist(image):
    pixel_inf = list(image.getdata())

    sw_image_list = []
    for n in range(len(pixel_inf)):
        sw_pixel_value = (((pixel_inf[n])[0]) + ((pixel_inf[n])[1]) + ((pixel_inf[n])[2]))
        sw_image_list.append(sw_pixel_value)
    print("Pixel Count:", len(sw_image_list))
    return sw_image_list


def reduce_depth(sw_image_list):
    sum = 0
    for n in range(len(sw_image_list)):
        sum += sw_image_list[n]
    list = []
    for n in range(len(sw_image_list)):
        if sw_image_list[n] > sum/len(sw_image_list):
            list.append(0)
        else:
            list.append(1)
    return list

def convert_image_to_list(image_name, max_width, max_height):
    image = Image.open(image_name)
    image, length_x_axis, length_y_axis = rescale_image(image, max_width, max_height)
    sw_image_list = convert_image_to_swlist(image)
    list = reduce_depth(sw_image_list)
    return list, length_x_axis, length_y_axis

print(convert_image_to_list("Mona_Lisa.jpg", 100, 100))
