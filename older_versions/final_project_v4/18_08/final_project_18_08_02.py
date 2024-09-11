from PIL import Image
import os
import cv2
import sys
import glob


def convert_image_to_list(image_name, pixelate_factor, white_threshold):
#definition to turn a picture into a list of binary values to be processed further

    #open image in Pillow, convert it to grayscale and pixelise it
    image = Image.open(image_name)
    image = image.convert("L")
    width, height = image.size
    rescale_dimensions = (int(width / pixelate_factor), int(height / pixelate_factor))
    image = image.resize(rescale_dimensions)

    #convert Pillow Data to a List for us to work with it
    image_list = list(image.getdata())

    # reduce the bit-depth to binary
    binary_image_list = []
    for n in range(len(image_list)):
        if image_list[n] >= white_threshold:
            binary_image_list.append(1)
        else:
            binary_image_list.append(0)

    #return "new_image_list" and dimensions of the new image
    return binary_image_list, rescale_dimensions, width, height


def convert_list_to_image(image_list, lenght_xy_axis, rescale, width, height):
    #initialize a new image
    new_image = Image.new("1", [int(lenght_xy_axis[0]), int(lenght_xy_axis[1])], int(1))
    #write image data to image
    new_image.putdata(image_list)
    if rescale == True:
        new_image = new_image.resize((width, height))
    return new_image


def generate_empty_decay_list(length_xy_axis, image):
    empty_decay_list = []
    for n in range(length_xy_axis[0] * length_xy_axis[1]):
        empty_decay_list.append(0)
    return empty_decay_list


def generate_appending_list(image, length_xy_axis):
    # generate appending_list based on given image with the sum of the pixel-values of the 8 appending pixels for each pixel
    appending_list = []
    for y in range(length_xy_axis[1]):
        for x in range(length_xy_axis[0]):
            if y == 0:
                if x == 0:
                    appending_list.append(round(
                        image[length_xy_axis[0] * length_xy_axis[1] - 1] * 0.7
                        + image[(length_xy_axis[1] - 1) * length_xy_axis[0]]
                        + image[(length_xy_axis[1] - 1) * length_xy_axis[0] + 1] * 0.7

                        + image[length_xy_axis[0] - 1]
                        + image[1]

                        + image[2 * length_xy_axis[0] - 1] * 0.7
                        + image[length_xy_axis[0]]
                        + image[length_xy_axis[0] + 1] * 0.7
                    , 1)
                    )

                elif x == (length_xy_axis[0] - 1):
                    appending_list.append(round(
                        image[(length_xy_axis[1] - 1) * length_xy_axis[0] + (x - 1)] * 0.7
                        + image[(length_xy_axis[1] - 1) * length_xy_axis[0] + x]
                        + image[(length_xy_axis[1] - 1) * length_xy_axis[0]] * 0.7

                        + image[x - 1]
                        + image[0]

                        + image[length_xy_axis[0] + (x - 1)] * 0.7
                        + image[length_xy_axis[0] + x]
                        + image[length_xy_axis[0]] * 0.7
                    , 1))

                else:
                    appending_list.append(round(
                        image[(length_xy_axis[1] - 1) * length_xy_axis[0] + (x - 1)] * 0.7
                        + image[(length_xy_axis[1] - 1) * length_xy_axis[0] + x]
                        + image[(length_xy_axis[1] - 1) * length_xy_axis[0] + (x + 1)] * 0.7

                        + image[(x - 1)]
                        + image[(x + 1)]

                        + image[length_xy_axis[0] + (x - 1)] * 0.7
                        + image[length_xy_axis[0] + x]
                        + image[length_xy_axis[0] + (x + 1)] * 0.7
                    , 1))

            elif y == (length_xy_axis[1] - 1):
                if x == 0:
                    appending_list.append(round(
                        image[(y - 1) * length_xy_axis[0] + (length_xy_axis[0] - 1)] * 0.7
                        + image[(y - 1) * length_xy_axis[0]]
                        + image[(y - 1) * length_xy_axis[0] + 1] * 0.7

                        + image[y * length_xy_axis[0] + (length_xy_axis[0] - 1)]
                        + image[y * length_xy_axis[0] + 1]

                        + image[(length_xy_axis[0] - 1)] * 0.7
                        + image[0]
                        + image[1] * 0.7
                    , 1))

                elif x == length_xy_axis[0] - 1:
                    appending_list.append(round(
                        image[(y - 1) * length_xy_axis[0] + (x - 1)] * 0.7
                        + image[(y - 1) * length_xy_axis[0] + x]
                        + image[(y - 1) * length_xy_axis[0]] * 0.7

                        + image[y * length_xy_axis[0] + (x - 1)]
                        + image[y * length_xy_axis[0]]

                        + image[(x - 1)] * 0.7
                        + image[x]
                        + image[0] * 0.7
                    , 1))

                else:
                    appending_list.append(round(
                        image[(y - 1) * length_xy_axis[0] + (x - 1)] * 0.7
                        + image[(y - 1) * length_xy_axis[0] + x]
                        + image[(y - 1) * length_xy_axis[0] + (x + 1)] * 0.7

                        + image[y * length_xy_axis[0] + (x - 1)]
                        + image[y * length_xy_axis[0] + (x + 1)]

                        + image[(x - 1)] * 0.7
                        + image[x]
                        + image[(x + 1)] * 0.7
                    , 1))


            else:
                if x == 0:
                    appending_list.append(round(
                        image[(y - 1) * length_xy_axis[0] + (length_xy_axis[0] - 1)] * 0.7
                        + image[(y - 1) * length_xy_axis[0]]
                        + image[(y - 1) * length_xy_axis[0] + 1] * 0.7

                        + image[y * length_xy_axis[0] + (length_xy_axis[0] - 1)]
                        + image[y * length_xy_axis[0] + 1]

                        + image[(y + 1) * length_xy_axis[0] + (length_xy_axis[0] - 1)] * 0.7
                        + image[(y + 1) * length_xy_axis[0]]
                        + image[(y + 1) * length_xy_axis[0] + 1] * 0.7
                    , 1))

                elif x == (length_xy_axis[0] - 1):
                    appending_list.append(round(
                        image[(y - 1) * length_xy_axis[0] + (x - 1)] * 0.7
                        + image[(y - 1) * length_xy_axis[0] + x]
                        + image[(y - 1) * length_xy_axis[0]] * 0.7

                        + image[y * length_xy_axis[0] + (x - 1)]
                        + image[y * length_xy_axis[0]]

                        + image[(y + 1) * length_xy_axis[0] + (x - 1)] * 0.7
                        + image[(y + 1) * length_xy_axis[0] + x]
                        + image[(y + 1) * length_xy_axis[0]] * 0.7
                    , 1))

                else:
                    appending_list.append(round(
                        image[(y - 1) * length_xy_axis[0] + (x - 1)] * 0.7
                        + image[(y - 1) * length_xy_axis[0] + x]
                        + image[(y - 1) * length_xy_axis[0] + (x + 1)] * 0.7

                        + image[y * length_xy_axis[0] + (x - 1)]
                        + image[y * length_xy_axis[0] + (x + 1)]

                        + image[(y + 1) * length_xy_axis[0] + (x - 1)] * 0.7
                        + image[(y + 1) * length_xy_axis[0] + x]
                        + image[(y + 1) * length_xy_axis[0] + (x + 1)] * 0.7
                    , 1))
    return appending_list


def generate_weight(image):
    # generate "weight"-value (float (0-1)), representing the balance between black and white Pixels in the given image
    weight = 0
    for n in range(len(image)):
        weight += image[n]
    weight = float(weight / len(image))
    return weight


def generate_image(image_list, appending_list, weight, decay_list, weight_factor, decay_factor):
    new_image_list = []
    for n in range(len(image_list)):
        value = round(
            appending_list[n]
            + (weight-0.5) * (-1) * weight_factor
            + decay_list[n] * (-0.1) * decay_factor
        , 1)

        if appending_list[n] == 6.8 and image_list[n] == 1:
            new_image_list.append(1)
        elif appending_list[n] == 0 and image_list[n] == 0:
            new_image_list.append(0)
        else:
            if value <= 2.7:
                new_image_list.append(0)
            elif value >= 4.1:
                new_image_list.append(1)
            else:
                new_image_list.append(image_list[n])

    return new_image_list


def generate_new_decay_list(old_decay_list, image_list,):
    new_decay_list = []
    for n in range(len(old_decay_list)):
        if image_list[n] == 1:
            new_decay_list.append(old_decay_list[n] + 1)
        else:
            new_decay_list.append(old_decay_list[n] - 1)
    return new_decay_list




def infinity_morpher(fp_image, iterations, pixelate_factor = (10), white_threshold = (127), rescale = True, weight_factor = 1, decay_factor = 1):

    if type(fp_image) != str:
        print(f'"fp_image" must be string')
        quit()
    if type(pixelate_factor) != int:
        print(f'"pixelate_factor" must be integer')
        quit()
    if type(white_threshold) != int:
        print(f'"white_threshold" must be integer')
        quit()
    if type(iterations) != int:
        print(f'"iterations" must be integer')
        quit()
    if type(rescale) != bool:
        print(f'"rescale" must be boolean')
        quit()
    if not type(weight_factor) == int or type(weight_factor) == float:
        print(f'"weight_factor" must be integer or float')
        quit()
    print(type(decay_factor))
    if not type(decay_factor) == int or type(decay_factor) == float:
        print(f'"decay_factor" must be integer or float')
        quit()

    if pixelate_factor < 1:
        print(f'"pixelate_factor" out of range')
        quit()
    if white_threshold < 0 or white_threshold > 255:
        print(f'"white_threshold" out of range')
        quit()
    if iterations < 0:
        print(f'"iterations" out of range')
        quit()
    if weight_factor < 0:
        print(f'Funky "weight_factor"! Lets see, how this turns out...')
    if decay_factor < 0:
        print(f'Funky "weight_factor"! Lets see, how this turns out...')

    if os.path.exists("infinity_morpher_images"):
        print("Image folder detected")
    else:
        print("Creating new image folder")
        os.makedirs("infinity_morpher_images")

    image_list, length_xy_axis, width, height = convert_image_to_list(fp_image, pixelate_factor, white_threshold)
    print("Image Dimensions(x/y):", length_xy_axis)

    new_image = convert_list_to_image(image_list, length_xy_axis, rescale, width, height)
    new_image.save(f"infinity_morpher_images/0.png")
    print("Image converted")

    print("Generating images...")
    decay_list = generate_empty_decay_list(length_xy_axis, image_list)
    for n in range(iterations):
        weight = generate_weight(image_list)
        appending_list = generate_appending_list(image_list, length_xy_axis)
        new_image_list = generate_image(image_list, appending_list, weight, decay_list, weight_factor, decay_factor)
        decay_list = generate_new_decay_list(decay_list, image_list)
        image_list = new_image_list

        new_image = convert_list_to_image(image_list, length_xy_axis, True, width, height)
        new_image.save(f"infinity_morpher_images/{n+1}.png")
        print(n+1, end="\r")
    print("Image generation successfull")









    img_array = []

    def get_key(fp):
        """This function will order the key by numerical order"""
        filename = os.path.splitext(os.path.basename(fp))[0]
        int_part = filename.split()[0]
        return int(int_part)

    for filename in sorted(glob.glob(f'infinity_morpher_images/*.png'), key=get_key):
        print(filename)
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)

    # create the video directory if the directory does not exist
    if not os.path.exists("video"):
        os.makedirs("video")

    out = cv2.VideoWriter('video/example.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 10, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()


infinity_morpher("/Users/macmannott/Documents/creative_applications/final_project_v4/18_08/test.png", 600, 4, 30, True, 1, 1)