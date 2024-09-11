length_x_axis = 4
length_y_axis = 4
length = 20
decay_threshold = 3
decay_time = 2

length_x_axis = length_x_axis+2
length_y_axis = length_y_axis+2

new_picture = [0,0,0,0,
               0,0,0,0,
               0,0,0,0,
               0,0,0,0]

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

new_picture = append_picture(new_picture, length_x_axis, length_y_axis)
print(new_picture)
weight = 0
for y in range(length_y_axis - 2):
    for x in range(length_x_axis - 2):
        weight = weight + new_picture[(y+1)*(length_x_axis) + x+1]
weight = weight / ((length_y_axis-2)*(length_x_axis-2))
print(1-weight)