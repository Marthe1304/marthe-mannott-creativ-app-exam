length_x_axis = 11
length_y_axis = 11
length = 20

x_offset = length_x_axis*length*0.5
y_offset = length_y_axis*length*0.5

appending_count = 0

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




def write_new_picture(picture):
    new_picture = []

    for x in range(length_x_axis): # append a row of "0" at the top
        new_picture.append(0)

    for y in range(length_y_axis-2):
        new_picture.append(0) # append a "0" at the left of each row

        for x in range(length_x_axis-2):
            appending_count = 0
            if picture[(y+1)*length_y_axis+x+1] == 1:
                new_picture.append(0)
            else:
                new_picture.append(1)
        new_picture.append(0) # append a "0" at the right of each row

    for x in range(length_x_axis): # append a row of "0" at the bottom
        new_picture.append(0)

    return new_picture

picture = write_new_picture(picture)

print(picture)