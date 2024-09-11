from turtle import *

t=Turtle()
t.speed(0)

length_x_axis = 11
length_y_axis = 11
length = 20

new_picture = [0,0,0,0,1,1,1,0,0,0,0,
           0,0,1,1,1,1,1,1,1,0,0,
           0,1,1,1,1,1,1,1,1,1,0,
           0,1,1,1,1,1,1,1,1,1,0,
           1,1,1,0,1,1,1,0,1,1,1,
           1,1,1,1,1,1,1,1,1,1,1,
           1,1,1,1,1,1,1,1,1,1,1,
           0,1,1,1,1,1,1,1,1,1,0,
           0,1,1,1,1,1,1,1,1,1,0,
           0,0,1,1,1,1,1,1,1,0,0,
           0,0,0,0,1,1,1,0,0,0,0]


length_x_axis = length_x_axis+2
length_y_axis = length_y_axis+2
x_offset = length_x_axis*length*0.5
y_offset = length_y_axis*length*0.5

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


def generate_new_picture(old_picture, length_x_axis, length_y_axis):
    picture = []

    for x in range(length_x_axis):  # append a row of "0" at the top
        picture.append(0)

    for y in range(length_y_axis - 2):
        picture.append(0)  # append a "0" at the left of each row

        for x in range(length_x_axis - 2):
            if old_picture[(y + 1) * length_y_axis + x + 1] == 1:
                picture.append(0)
            else:
                picture.append(1)

        picture.append(0)  # append a "0" at the right of each row

    for x in range(length_x_axis):  # append a row of "0" at the bottom
        picture.append(0)

    return picture

new_picture = append_picture(new_picture, length_x_axis, length_y_axis) #extend the original image to be drawn
old_picture = create_blank_picture(length_x_axis, length_y_axis) # create a blank picture
display_picture(old_picture, new_picture, length_x_axis, length_y_axis, length) #draw the picture, comparing the picture and new_picture

for n in range(2):
    old_picture = new_picture
    new_picture = generate_new_picture(old_picture, length_x_axis, length_y_axis)
    display_picture(old_picture, new_picture, length_x_axis, length_y_axis, length)

done()