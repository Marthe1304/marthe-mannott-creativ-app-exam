from turtle import *
import turtle
import time
from PIL import Image

def append_picture(new_picture, length_x_axis, length_y_axis): # funktion to ad a row of "0" on each side of the picture
    picture = []
    for x in range(length_x_axis):  # append a row of "0" at the top
        picture.append(0)

    for y in range(length_y_axis-2):
        picture.append(0)  # append a "0" at the left of each row
        for x in range(length_x_axis-2): #append the original contend of the picture
            picture.append(new_picture[y * (length_x_axis-2) + x])
        picture.append(0)  # append a "0" at the right of each row

    for x in range(length_x_axis):  # append a row of "0" at the bottom
        picture.append(0)
    return picture

def create_blank_picture(length_x_axis, length_y_axis): # create a blanck "new_picture"
    picture = []
    for n in range(length_x_axis*length_y_axis):
        picture.append(0)
    return picture

def pixel(length, square_colour):
    t.pendown()
    t.color(square_colour)
    t.begin_fill()
    for x in range(4):
        t.forward(length)
        t.right(90)
    t.end_fill()
    t.penup()

def display_picture(old_picture, new_picture, length_x_axis, length_y_axis, length):
    turtle.tracer(0, 0)
    for y in range(length_y_axis):
        for x in range(length_x_axis):
            if new_picture[y*length_x_axis + x] != old_picture[y*length_x_axis + x]:
                if new_picture[y*length_x_axis+x] == 1:
                    t.penup()
                    t.goto(x * length - x_offset, y * length * (-1) + y_offset)
                    t.pendown()
                    pixel(length, "Black")
                else:
                    t.penup()
                    t.goto(x * length - x_offset, y * length * (-1) + y_offset)
                    t.pendown()
                    pixel(length, "white")
    turtle.update()
    time.sleep(1/10)


def generate_new_picture(old_picture, appending_list, decay_list, length_x_axis, length_y_axis):
    new_picture = []
    # generate "weight" value
    weight = 0
    for y in range(length_y_axis - 2):
        for x in range(length_x_axis - 2):
            weight = weight + old_picture[(y + 1) * (length_x_axis) + x + 1]
    weight = weight / ((length_y_axis - 2) * (length_x_axis - 2))

    # append a row of "0" at the top
    for x in range(length_x_axis):
        new_picture.append(0)

    for y in range(length_y_axis - 2):
        new_picture.append(0)  # append a "0" at the left of each row

        for x in range(length_x_axis - 2):      #decide, if a pixel is changed or not
            if decay_list[y*(length_x_axis-2) + x] == 0:
                if old_picture[(y+1)*length_x_axis + (x+1)] == 1:
                    if appending_list[y * (length_x_axis-2) + x] < 8 - (2+(1-weight)*1):
                        new_picture.append(0)
                    else:
                        new_picture.append(1)
                else:
                    if appending_list[y * (length_x_axis-2) + x] > 2+weight*1:
                        new_picture.append(1)
                    else:
                        new_picture.append(0)
                #if appending_list[y * (length_x_axis-2) + x] > :
                 #   new_picture.append(0)
                #elif appending_list[y * (length_x_axis-2) + x] < :
                 #   new_picture.append(1)
                #else:
                 #   new_picture.append(old_picture[(y+1)*length_x_axis + (x+1)])
            else:
                new_picture.append(old_picture[(y+1)*length_x_axis + (x+1)])

        new_picture.append(0)  # append a "0" at the right of each row

    for x in range(length_x_axis):  # append a row of "0" at the bottom
        new_picture.append(0)

    return new_picture

def generate_appending_list(picture, length_x_axis, length_y_axis):
    appending_list = []
    for y in range (length_y_axis-2):
        for x in range (length_x_axis-2):
            appending_list.append(
                picture[(y*length_x_axis + x)] +
                picture[(y*length_x_axis + x+1)] +
                picture[(y*length_x_axis + x+2)] +
                picture[((y+1)*length_x_axis + x)] +
                picture[((y+1)*length_x_axis + x+2)] +
                picture[((y+2) * length_x_axis + x)] +
                picture[((y+2)* length_x_axis + x + 1)] +
                picture[((y+2) * length_x_axis + x + 2)]
            )
    return appending_list

def generate_empty_decay_list(length_x_axis, length_y_axis):
    decay_list=[]
    for n in range((length_x_axis-2) * (length_y_axis-2)):
        decay_list.append(0)
    return decay_list

def generate_decay_list(new_picture, old_picture, old_decay_list, length_x_axis, length_y_axis):
    decay_list = []
    for y in range(length_y_axis-2):
        for x in range(length_x_axis-2):
            if new_picture[(y+1)*length_x_axis + (x+1)] != old_picture[(y+1)*length_x_axis + (x+1)]:
                decay_list.append(decay_time)
            elif old_decay_list[y*(length_x_axis-2) + x] > 0:
                decay_list.append(old_decay_list[y*(length_x_axis-2) + x]-1)
            else:
                decay_list.append(0)
    return decay_list


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


t=Turtle()
t.speed("fastest")
turtle.tracer(0, 0)

length = 5
decay_time = 10

new_picture, length_x_axis, length_y_axis = convert_image_to_list("test.jpeg", 2304, 2304)

length_x_axis = length_x_axis+2
length_y_axis = length_y_axis+2
x_offset = length_x_axis*length*0.5
y_offset = length_y_axis*length*0.5


new_picture = append_picture(new_picture, length_x_axis, length_y_axis) #extend the original image to be drawn
old_picture = create_blank_picture(length_x_axis, length_y_axis) # create a blank picture
decay_list = generate_empty_decay_list(length_x_axis, length_y_axis)
#display_picture(old_picture, new_picture, length_x_axis, length_y_axis, length) #draw the picture, comparing the picture and new_picture

for n in range(5):
    old_picture = new_picture
    appending_list = generate_appending_list(old_picture, length_x_axis, length_y_axis)
    new_picture = generate_new_picture(old_picture, appending_list, decay_list, length_x_axis, length_y_axis)
    #display_picture(old_picture, new_picture, length_x_axis, length_y_axis, length)
    old_decay_list = decay_list
    decay_list = generate_decay_list(new_picture, old_picture, old_decay_list, length_x_axis, length_y_axis)
    print(n)
done()