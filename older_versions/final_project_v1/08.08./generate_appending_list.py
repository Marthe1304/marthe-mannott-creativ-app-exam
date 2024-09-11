length_x_axis = 11
length_y_axis = 11

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

def generate_appending_list(picture, length_x_axis, length_y_axis):
    appending = []
    for y in range (length_y_axis-2):
        for x in range (length_x_axis-2):
            appending.append(
                picture[(y*length_x_axis + x)] +
                picture[(y*length_x_axis + x+1)] +
                picture[(y*length_x_axis + x+2)] +
                picture[((y+1)*length_x_axis + x)] +
                picture[((y+1)*length_x_axis + x+2)] +
                picture[((y+2) * length_x_axis + x)] +
                picture[((y+2)* length_x_axis + x + 1)] +
                picture[((y+2) * length_x_axis + x + 2)]
            )
    return appending

print(generate_appending_list(new_picture, length_x_axis, length_y_axis))