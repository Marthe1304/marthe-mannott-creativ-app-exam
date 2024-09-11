from PIL import Image
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


def generate_empty_age_list(length_xy_axis):
    empty_age_list = []
    for n in range(length_xy_axis[0] * length_xy_axis[1]):
        empty_age_list.append(0)
    return empty_age_list


def generate_new_image(image_list, age_list, length_xy_axis):

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


    def generate_image(image_list, appending_list, weight, age_list):
        new_image_list = []
        max_age= 10
        for n in range(len(image_list)):
            if image_list[n] == 1:
                if appending_list[n] <= round((-2)*(weight**2) + 5*weight + (age_list[n]/max_age)*weight*2 + 2):
                    new_image_list.append(0)
                else:
                    new_image_list.append(1)
            else:
                if appending_list[n] >= round(2*(weight**2) + weight + (age_list[n]/max_age)*(weight-1)*2 + 3):
                    new_image_list.append(1)
                else:
                    new_image_list.append(0)
        return new_image_list


    def generate_new_age_list(old_age_list, old_image_list, new_image_list):
        new_age_list = []
        max_age = 10
        for n in range(len(old_age_list)):
            if old_age_list[n] == max_age:
                new_age_list.append(max_age)
            elif new_image_list[n] != old_image_list[n]:
                new_age_list.append(0)
            else:
                new_age_list.append(old_age_list[n] + 1)
        return new_age_list


    # generate appending_list with the sum of the pixel-values of the 8 appending pixels
    appending_list = generate_appending_list(image_list, length_xy_axis)

    # generate "weight"-value (float (0-1)), representing the balance between black and white Pixels in the image
    weight = generate_weight(image_list)

    # generate a new_image based on the decay_list, appending_list and weight
    new_image_list = generate_image(image_list, appending_list, weight, age_list)

    # generate age_list comparing the new_image to the old_image representing the time since each pixel was changed
    new_age_list = generate_new_age_list(age_list, image_list, new_image_list)

    # returning new_image and decay_list
    return new_image_list, new_age_list









image_list, length_xy_axis, width, height = convert_image_to_list("Mona_Lisa.jpg", 10, 70)
new_image = convert_list_to_image(image_list, length_xy_axis, True, width, height)
new_image.show()
age_list = generate_empty_age_list(length_xy_axis)

for n in range(1):
    image_list, age_list = generate_new_image(image_list, age_list, length_xy_axis)
new_image = convert_list_to_image(image_list, length_xy_axis, True, width, height)
new_image.show()

for n in range(10):
    image_list, age_list = generate_new_image(image_list, age_list, length_xy_axis)
new_image = convert_list_to_image(image_list, length_xy_axis, True, width, height)
new_image.show()

for n in range(100):
    image_list, age_list = generate_new_image(image_list, age_list, length_xy_axis)
new_image = convert_list_to_image(image_list, length_xy_axis, True, width, height)
new_image.show()

