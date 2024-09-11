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

def pixel(length, square_colour):
    t.pendown()
    t.color(square_colour)
    t.begin_fill()
    for x in range(4):
        t.forward(length)
        t.right(90)
    t.end_fill()
    t.penup()

def draw_picture(length_x_axis, length_y_axis, length):
    for y in range(length_y_axis):
        for x in range(length_x_axis):
            if picture[y*length_x_axis+x] == 1:
                t.penup()
                t.goto(x * length - x_offset, y * length * (-1) + y_offset)
                t.pendown()
                pixel(length, "Black")

draw_picture(length_x_axis, length_y_axis, length)

done()