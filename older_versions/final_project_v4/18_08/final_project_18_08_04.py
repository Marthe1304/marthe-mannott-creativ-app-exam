from PIL import Image
import os
import cv2
import glob
import time

def convert_image_to_list(image_fp, pixelate_factor, white_threshold):
#definition to turn a picture into a list of binary values to be processed further

    #open image in Pillow, convert it to grayscale and pixelise it
    image = Image.open(image_fp)
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

    #return "binary_image_list" the dimensions of the new image and the original dimensions
    return binary_image_list, rescale_dimensions, width, height


def convert_list_to_image(image_list, lenght_xy_axis, width, height):
    #initialize a new image in Pillow
    new_image = Image.new("1", [int(lenght_xy_axis[0]), int(lenght_xy_axis[1])], int(1))
    #write pixel information from image_list to the image
    new_image.putdata(image_list)
    #resize the new image to the size of the originaly given image
    new_image = new_image.resize((width, height))
    return new_image


def generate_empty_decay_list(length_xy_axis):
    #generateing a list of zeros with the length of the image_list
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
                if x == 0: #y=0 and x=0 -> top left corner
                    appending_list.append(round(
                        image[length_xy_axis[0] * length_xy_axis[1] - 1]
                        + image[(length_xy_axis[1] - 1) * length_xy_axis[0]]
                        + image[(length_xy_axis[1] - 1) * length_xy_axis[0] + 1]

                        + image[length_xy_axis[0] - 1]
                        + image[1]

                        + image[2 * length_xy_axis[0] - 1]
                        + image[length_xy_axis[0]]
                        + image[length_xy_axis[0] + 1]
                    , 1)
                    )

                elif x == (length_xy_axis[0] - 1): #top right corner
                    appending_list.append(round(
                        image[(length_xy_axis[1] - 1) * length_xy_axis[0] + (x - 1)]
                        + image[(length_xy_axis[1] - 1) * length_xy_axis[0] + x]
                        + image[(length_xy_axis[1] - 1) * length_xy_axis[0]]

                        + image[x - 1]
                        + image[0]

                        + image[length_xy_axis[0] + (x - 1)]
                        + image[length_xy_axis[0] + x]
                        + image[length_xy_axis[0]]
                    , 1))

                else: #top edge
                    appending_list.append(round(
                        image[(length_xy_axis[1] - 1) * length_xy_axis[0] + (x - 1)]
                        + image[(length_xy_axis[1] - 1) * length_xy_axis[0] + x]
                        + image[(length_xy_axis[1] - 1) * length_xy_axis[0] + (x + 1)]

                        + image[(x - 1)]
                        + image[(x + 1)]

                        + image[length_xy_axis[0] + (x - 1)]
                        + image[length_xy_axis[0] + x]
                        + image[length_xy_axis[0] + (x + 1)]
                    , 1))

            elif y == (length_xy_axis[1] - 1):
                if x == 0: #bottom left corner
                    appending_list.append(round(
                        image[(y - 1) * length_xy_axis[0] + (length_xy_axis[0] - 1)]
                        + image[(y - 1) * length_xy_axis[0]]
                        + image[(y - 1) * length_xy_axis[0] + 1]

                        + image[y * length_xy_axis[0] + (length_xy_axis[0] - 1)]
                        + image[y * length_xy_axis[0] + 1]

                        + image[(length_xy_axis[0] - 1)]
                        + image[0]
                        + image[1]
                    , 1))

                elif x == length_xy_axis[0] - 1: #bottom right corner
                    appending_list.append(round(
                        image[(y - 1) * length_xy_axis[0] + (x - 1)]
                        + image[(y - 1) * length_xy_axis[0] + x]
                        + image[(y - 1) * length_xy_axis[0]]

                        + image[y * length_xy_axis[0] + (x - 1)]
                        + image[y * length_xy_axis[0]]

                        + image[(x - 1)]
                        + image[x]
                        + image[0]
                    , 1))

                else: #bottom edge
                    appending_list.append(round(
                        image[(y - 1) * length_xy_axis[0] + (x - 1)]
                        + image[(y - 1) * length_xy_axis[0] + x]
                        + image[(y - 1) * length_xy_axis[0] + (x + 1)]

                        + image[y * length_xy_axis[0] + (x - 1)]
                        + image[y * length_xy_axis[0] + (x + 1)]

                        + image[(x - 1)]
                        + image[x]
                        + image[(x + 1)]
                    , 1))


            else:
                if x == 0: #left edge
                    appending_list.append(round(
                        image[(y - 1) * length_xy_axis[0] + (length_xy_axis[0] - 1)]
                        + image[(y - 1) * length_xy_axis[0]]
                        + image[(y - 1) * length_xy_axis[0] + 1]

                        + image[y * length_xy_axis[0] + (length_xy_axis[0] - 1)]
                        + image[y * length_xy_axis[0] + 1]

                        + image[(y + 1) * length_xy_axis[0] + (length_xy_axis[0] - 1)]
                        + image[(y + 1) * length_xy_axis[0]]
                        + image[(y + 1) * length_xy_axis[0] + 1]
                    , 1))

                elif x == (length_xy_axis[0] - 1): #right edge
                    appending_list.append(round(
                        image[(y - 1) * length_xy_axis[0] + (x - 1)]
                        + image[(y - 1) * length_xy_axis[0] + x]
                        + image[(y - 1) * length_xy_axis[0]]

                        + image[y * length_xy_axis[0] + (x - 1)]
                        + image[y * length_xy_axis[0]]

                        + image[(y + 1) * length_xy_axis[0] + (x - 1)]
                        + image[(y + 1) * length_xy_axis[0] + x]
                        + image[(y + 1) * length_xy_axis[0]]
                    , 1))

                else: #all but the edge and corner pixels
                    appending_list.append(round(
                        image[(y - 1) * length_xy_axis[0] + (x - 1)]
                        + image[(y - 1) * length_xy_axis[0] + x]
                        + image[(y - 1) * length_xy_axis[0] + (x + 1)]

                        + image[y * length_xy_axis[0] + (x - 1)]
                        + image[y * length_xy_axis[0] + (x + 1)]

                        + image[(y + 1) * length_xy_axis[0] + (x - 1)]
                        + image[(y + 1) * length_xy_axis[0] + x]
                        + image[(y + 1) * length_xy_axis[0] + (x + 1)]
                    , 1))
    return appending_list

def generate_initial_weight(image_list):
    # generate "inital_weight"-value (float (0-1)), representing the balance between black and white Pixels in the first image
    image_sum = 0
    for n in range(len(image_list)):
        image_sum += image_list[n]
    weight = image_sum/len(image_list)

    return weight


def generate_weight(image_list, initial_weight):
    # generate "weight"-value (float (0-1)), representing the balance between black and white Pixels in the given image cmopared to the first image
    image_sum = 0
    for n in range(len(image_list)):
        image_sum += image_list[n]

    a = initial_weight
    x = image_sum/len(image_list)
    if image_sum/len(image_list) <= a:
        weight = x / (2 * a)
    else:
        weight = (x-a) / (2 * (1 - a)) + 0.5
    return weight


def generate_image(image_list, appending_list, weight, decay_list, weight_factor, decay_factor):
    new_image_list = []
    for n in range(len(image_list)):
        # generating a value based on a pixels age, the number of black and white pixels and the weight factor
        value = round(
            appending_list[n]
            + (weight - 0.5) * (-4)
            + (weight - 0.5) * (-2) * (weight_factor)
            + (image_list[n]-0.5) * (-2) * decay_list[n] * (0.2) * decay_factor
            , 1)

        if appending_list[n] == 8 and image_list[n] == 1: # if a pixel is surrounded only by similar colored pixels, it can´t change its color
            new_image_list.append(1)
        elif appending_list[n] == 0 and image_list[n] == 0:
            new_image_list.append(0)
        else: #comparing the generated value to two threshold-values, determining if a pixels color is changed
            if value <= 3:
                new_image_list.append(0)
            elif value >= 5:
                new_image_list.append(1)
            else:
                new_image_list.append(image_list[n])

    return new_image_list


def generate_new_decay_list(old_decay_list, old_image_list, new_image_list,):
    #if a pixel changed its color, it´s decay_list value is reset to 0 else it is increased by 1
    new_decay_list = []
    for n in range(len(old_decay_list)):
        if old_image_list[n] != new_image_list[n]:
            new_decay_list.append(0)
        else:
            new_decay_list.append(old_decay_list[n] + 1)
    return new_decay_list

def check_values(fp_image, iterations, pixelate_factor, white_threshold, frame_rate, weight_factor, decay_factor):
    #this function checks if the given variables are the right Datatype and Range
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
    if type(frame_rate) != int:
        print(f'"frame_rate" must be interger')
    if not type(weight_factor) == int and not type(weight_factor) == float:
        print(f'"weight_factor" must be integer or float')
        quit()
    if not type(decay_factor) == int and not type(decay_factor) == float:
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

def render_video(now_str, image_fp, frame_rate):

    img_array = []

    def get_key(fp):
        """This function will order the key by numerical order"""
        filename = os.path.splitext(os.path.basename(fp))[0]
        int_part = filename.split()[0]
        return int(int_part)

    for filename in sorted(glob.glob(f'{image_fp}/*.png'), key=get_key):
        print(filename, end="\r")
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)

    # create the video directory
    video_fp = f'im_video_{now_str}'
    os.makedirs(video_fp)

    out = cv2.VideoWriter(f'{video_fp}/im_{now_str}.mp4', cv2.VideoWriter_fourcc(*'mp4v'), frame_rate, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()

def infinity_morpher(fp_image, iterations, pixelate_factor, white_threshold, frame_rate, weight_factor, decay_factor):

    check_values(fp_image, iterations, pixelate_factor, white_threshold, frame_rate, weight_factor, decay_factor)

    # creating an image folder
    now_str = time.strftime("%Y%m%d%H%M%S")
    image_fp = f'im_images_{now_str}'
    os.makedirs(image_fp)

    # convert the given image to given specifications and generate image_list
    image_list, length_xy_axis, width, height = convert_image_to_list(fp_image, pixelate_factor, white_threshold)
    print("Image Dimensions(x/y):", length_xy_axis)

    # saving the first image
    new_image = convert_list_to_image(image_list, length_xy_axis, width, height)
    new_image.save(f"{image_fp}/0.png")
    print("Image converted")

    # generating and saving new Image n times
    print("Generating images...")
    decay_list = generate_empty_decay_list(length_xy_axis)
    initial_weight = generate_initial_weight(image_list)
    print(initial_weight )
    for n in range(iterations):
        weight = generate_weight(image_list, initial_weight)
        appending_list = generate_appending_list(image_list, length_xy_axis)
        new_image_list = generate_image(image_list, appending_list, weight, decay_list, weight_factor, decay_factor)
        decay_list = generate_new_decay_list(decay_list, image_list, new_image_list)
        image_list = new_image_list

        new_image = convert_list_to_image(image_list, length_xy_axis, width, height)
        new_image.save(f"{image_fp}/{n+1}.png")
        print(n+1, end="\r")
    print("Image generation successfull")

    # render Video
    print("Rendering...")
    render_video(now_str, image_fp, frame_rate)
    print("Successfull")

infinity_morpher("test.jpeg", 50, 16, 25, 10,1, 0.25)