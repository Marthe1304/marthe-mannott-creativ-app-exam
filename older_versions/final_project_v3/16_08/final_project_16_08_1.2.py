from PIL import Image
import random
import time

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
                    appending_list.append(
                        image[length_xy_axis[0] * length_xy_axis[1] - 1]
                        + image[(length_xy_axis[1] - 1) * length_xy_axis[0]]
                        + image[(length_xy_axis[1] - 1) * length_xy_axis[0] + 1]

                        + image[length_xy_axis[0] - 1]
                        + image[1]

                        + image[2 * length_xy_axis[0] - 1]
                        + image[length_xy_axis[0]]
                        + image[length_xy_axis[0] + 1]
                    )

                elif x == (length_xy_axis[0] - 1):
                    appending_list.append(
                        image[(length_xy_axis[1] - 1) * length_xy_axis[0] + (x - 1)]
                        + image[(length_xy_axis[1] - 1) * length_xy_axis[0] + x]
                        + image[(length_xy_axis[1] - 1) * length_xy_axis[0]]

                        + image[x - 1]
                        + image[0]

                        + image[length_xy_axis[0] + (x - 1)]
                        + image[length_xy_axis[0] + x]
                        + image[length_xy_axis[0]]
                    )

                else:
                    appending_list.append(
                        image[(length_xy_axis[1] - 1) * length_xy_axis[0] + (x - 1)]
                        + image[(length_xy_axis[1] - 1) * length_xy_axis[0] + x]
                        + image[(length_xy_axis[1] - 1) * length_xy_axis[0] + (x + 1)]

                        + image[(x - 1)]
                        + image[(x + 1)]

                        + image[length_xy_axis[0] + (x - 1)]
                        + image[length_xy_axis[0] + x]
                        + image[length_xy_axis[0] + (x + 1)]
                    )

            elif y == (length_xy_axis[1] - 1):
                if x == 0:
                    appending_list.append(
                        image[(y - 1) * length_xy_axis[0] + (length_xy_axis[0] - 1)]
                        + image[(y - 1) * length_xy_axis[0]]
                        + image[(y - 1) * length_xy_axis[0] + 1]

                        + image[y * length_xy_axis[0] + (length_xy_axis[0] - 1)]
                        + image[y * length_xy_axis[0] + 1]

                        + image[(length_xy_axis[0] - 1)]
                        + image[0]
                        + image[1]
                    )

                elif x == length_xy_axis[0] - 1:
                    appending_list.append(
                        image[(y - 1) * length_xy_axis[0] + (x - 1)]
                        + image[(y - 1) * length_xy_axis[0] + x]
                        + image[(y - 1) * length_xy_axis[0]]

                        + image[y * length_xy_axis[0] + (x - 1)]
                        + image[y * length_xy_axis[0]]

                        + image[(x - 1)]
                        + image[x]
                        + image[0]
                    )

                else:
                    appending_list.append(
                        image[(y - 1) * length_xy_axis[0] + (x - 1)]
                        + image[(y - 1) * length_xy_axis[0] + x]
                        + image[(y - 1) * length_xy_axis[0] + (x + 1)]

                        + image[y * length_xy_axis[0] + (x - 1)]
                        + image[y * length_xy_axis[0] + (x + 1)]

                        + image[(x - 1)]
                        + image[x]
                        + image[(x + 1)]
                    )


            else:
                if x == 0:
                    appending_list.append(
                        image[(y - 1) * length_xy_axis[0] + (length_xy_axis[0] - 1)]
                        + image[(y - 1) * length_xy_axis[0]]
                        + image[(y - 1) * length_xy_axis[0] + 1]

                        + image[y * length_xy_axis[0] + (length_xy_axis[0] - 1)]
                        + image[y * length_xy_axis[0] + 1]

                        + image[(y + 1) * length_xy_axis[0] + (length_xy_axis[0] - 1)]
                        + image[(y + 1) * length_xy_axis[0]]
                        + image[(y + 1) * length_xy_axis[0] + 1]
                    )

                elif x == (length_xy_axis[0] - 1):
                    appending_list.append(
                        image[(y - 1) * length_xy_axis[0] + (x - 1)]
                        + image[(y - 1) * length_xy_axis[0] + x]
                        + image[(y - 1) * length_xy_axis[0]]

                        + image[y * length_xy_axis[0] + (x - 1)]
                        + image[y * length_xy_axis[0]]

                        + image[(y + 1) * length_xy_axis[0] + (x - 1)]
                        + image[(y + 1) * length_xy_axis[0] + x]
                        + image[(y + 1) * length_xy_axis[0]]
                    )

                else:
                    appending_list.append(
                        image[(y - 1) * length_xy_axis[0] + (x - 1)]
                        + image[(y - 1) * length_xy_axis[0] + x]
                        + image[(y - 1) * length_xy_axis[0] + (x + 1)]

                        + image[y * length_xy_axis[0] + (x - 1)]
                        + image[y * length_xy_axis[0] + (x + 1)]

                        + image[(y + 1) * length_xy_axis[0] + (x - 1)]
                        + image[(y + 1) * length_xy_axis[0] + x]
                        + image[(y + 1) * length_xy_axis[0] + (x + 1)]
                    )
    return appending_list


def generate_weight(image):
    # generate "weight"-value (float (0-1)), representing the balance between black and white Pixels in the given image
    weight = 0
    for n in range(len(image)):
        weight += image[n]
    weight = float(weight / len(image))
    return weight


def generate_image(image_list, appending_list, weight, decay_list):
    new_image_list = []
    for n in range(len(image_list)):
        if appending_list[n] == 8:
            new_image_list.append(1)
        elif appending_list[n] == 0:
            new_image_list.append(0)
        elif appending_list[n] <= 2: # pixel turns white, if 7 or more black pixels are appending
            if decay_list[n] == 0:
                new_image_list.append(1)
            else:
                new_image_list.append(image_list[n])
        elif appending_list[n] <= 5: #pixel turns black, if 3 or more black pixels are appending
            new_image_list.append(0)
        else:
            new_image_list.append(image_list[n]) #pixels stay black or white in any other case (1-2 black pixels appending)

    return new_image_list


def generate_new_decay_list(old_decay_list, old_image_list, new_image_list):
    new_decay_list = []
    for n in range(len(old_decay_list)):
        if old_image_list[n] != new_image_list[n]:
            new_decay_list.append(30)
        else:
            if old_decay_list[n] == 0:
                new_decay_list.append(0)
            else:
                new_decay_list.append(old_decay_list[n]-1)
    return new_decay_list





image_list, length_xy_axis, width, height = convert_image_to_list("Mona_Lisa.jpg", 5, 80)
print(length_xy_axis)
new_image = convert_list_to_image(image_list, length_xy_axis, True, width, height)

new_image.save(f"/Users/macmannott/Documents/creative_applications/final_project_v2/16_08/Images/image_0.png")
decay_list = generate_empty_decay_list(length_xy_axis, image_list)

for n in range(50):
    appending_list = generate_appending_list(image_list, length_xy_axis)
    weight = generate_weight(image_list)
    new_image_list = generate_image(image_list, appending_list, weight, decay_list)
    decay_list = generate_new_decay_list(decay_list, image_list, new_image_list)
    image_list = new_image_list

    new_image = convert_list_to_image(image_list, length_xy_axis, True, width, height)
    new_image.save(f"/Users/macmannott/Documents/creative_applications/final_project_v3/16_08/Images/image_{n+1}.png")
    print(n)

