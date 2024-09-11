from turtle import *

t=Turtle()
t.speed(0)

length_x_axis = 11
length_y_axis = 11
length = 20

x_offset = length_x_axis*length*0.5
y_offset = length_y_axis*length*0.5

picture = [0,0,0,0,1,1,1,0,0,0,0,
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
new_picture = []

def pixel(length, square_colour):
    t.pendown()
    t.color(square_colour)
    t.begin_fill()
    for x in range(4):
        t.forward(length)
        t.right(90)
    t.end_fill()
    t.penup()

def draw_picture(length_x_axis, length_y_axis, length, picture):
    for y in range(length_y_axis):
        for x in range(length_x_axis):
            if picture[y*length_x_axis+x] == 1:
                t.penup()
                t.goto(x * length - x_offset, y * length * (-1) + y_offset)
                t.pendown()
                pixel(length, "Black")

def write_new_list(picture, length_x_axis, length_y_axis):
    new_picture = []
    for p in range(picture.count(1) + picture.count(0)):
        # count the appending black pixels
        appending_count = 0
        if p == length_y_axis*length_x_axis-1:
            if picture[p - 1] == 1:
                appending_count = appending_count + 1
            if picture[p - length_x_axis] == 1:
                appending_count = appending_count + 1

        elif p >= ((length_y_axis-1)*length_x_axis):
            if picture[p - 1] == 1:
                appending_count = appending_count + 1
            if picture[p + 1] == 1:
                appending_count = appending_count + 1
            if picture[p - length_y_axis] == 1:
                appending_count = appending_count + 1

        else:
            if picture[p - 1] == 1:
                appending_count = appending_count + 1
            if picture[p + 1] == 1:
                appending_count = appending_count + 1
            if picture[p - length_x_axis] == 1:
                appending_count = appending_count + 1
            if picture[p + length_x_axis] == 1:
                appending_count = appending_count + 1

        # if appending pixels are 1: make this pixel black; if they are 4 make it white
        if picture[p] == 0:
            if appending_count == 1:
                new_picture.append(1)
            else:
                new_picture.append(0)
        else:
            if appending_count == 4:
                new_picture.append(0)
            else:
                new_picture.append(1)
    return (new_picture)
    #picture = new_picture



write_new_list(picture, length_x_axis, length_y_axis)

print(new_picture)
#draw_picture(length_x_axis, length_y_axis, length, new_picture)

done()