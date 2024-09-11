image = [1, 0, 1, 0, 1,
         0, 1, 0, 1, 0,
         1, 0, 1, 0, 1,
         0, 1, 0, 1, 0,
         1, 0, 1, 0, 1]
length_xy_axis = [5, 5]
appending_list = []
for y in range(length_xy_axis[1]):
    for x in range(length_xy_axis[0]):
        print(x, y)
        appending_value = 0
        if y == 0:
            if x == 0:
                appending_list.append(
                    image[length_xy_axis[0] * length_xy_axis[1] - 1]
                    + image[(length_xy_axis[1] - 1) * length_xy_axis[0] + x]
                    + image[(length_xy_axis[1] - 1) * length_xy_axis[0] + (x + 1)]

                    + image[y * length_xy_axis[0] + (length_xy_axis[0] - 1)]
                    + image[y * length_xy_axis[0] + (x + 1)]

                    + image[(y + 1) * length_xy_axis[0] + (length_xy_axis[0] - 1)]
                    + image[(y + 1) * length_xy_axis[0] + x]
                    + image[(y + 1) * length_xy_axis[0] + (x + 1)]
                )

            elif x == (length_xy_axis[0]-1):
                appending_list.append(
                    image[(length_xy_axis[1] - 1) * length_xy_axis[0] + (x - 1)]
                    + image[(length_xy_axis[1] - 1) * length_xy_axis[0] + x]
                    + image[(length_xy_axis[1]-1)*length_xy_axis[0]]

                    + image[y * length_xy_axis[0] + (x - 1)]
                    + image[y * length_xy_axis[0] + (x - (length_xy_axis[0] - 1))]

                    + image[(y + 1) * length_xy_axis[0] + (x - 1)]
                    + image[(y + 1) * length_xy_axis[0] + x]
                    + image[(y + 1) * length_xy_axis[0] + (x - (length_xy_axis[0] - 1))]
                )

            else:
                appending_list.append(
                    image[(length_xy_axis[1] - 1) * length_xy_axis[0] + (x - 1)]
                    + image[(length_xy_axis[1] - 1) * length_xy_axis[0] + x]
                    + image[(length_xy_axis[1] - 1) * length_xy_axis[0] + (x + 1)]

                    + image[y * length_xy_axis[0] + (x - 1)]
                    + image[y * length_xy_axis[0] + (x + 1)]

                    + image[(y + 1) * length_xy_axis[0] + (x - 1)]
                    + image[(y + 1) * length_xy_axis[0] + x]
                    + image[(y + 1) * length_xy_axis[0] + (x + 1)]
                )


        elif y == (length_xy_axis[1] - 1):
            if x == 0:
                appending_list.append(
                    image[(y - 1) * length_xy_axis[0] + (length_xy_axis[0] - 1)]
                    + image[(y - 1) * length_xy_axis[0] + x]
                    + image[(y - 1) * length_xy_axis[0] + (x + 1)]

                    + image[y * length_xy_axis[0] + (length_xy_axis[0] - 1)]
                    + image[y * length_xy_axis[0] + (x + 1)]

                    + image[(length_xy_axis[0] - 1)]
                    + image[x]
                    + image[(x + 1)]
                )

            elif x == length_xy_axis[0] - 1:
                appending_list.append(
                    image[(y - 1) * length_xy_axis[0] + (x - 1)]
                    + image[(y - 1) * length_xy_axis[0] + x]
                    + image[(y - 1) * length_xy_axis[0] + (x - (length_xy_axis[0]-1))]

                    + image[y * length_xy_axis[0] + (x - 1)]
                    + image[y * length_xy_axis[0] + (x - (length_xy_axis[0]-1))]

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
                    + image[(y - 1) * length_xy_axis[0] + x]
                    + image[(y - 1) * length_xy_axis[0] + (x + 1)]

                    + image[y * length_xy_axis[0] + (length_xy_axis[0] - 1)]
                    + image[y * length_xy_axis[0] + (x + 1)]

                    + image[(y + 1) * length_xy_axis[0] + (length_xy_axis[0] - 1)]
                    + image[(y + 1) * length_xy_axis[0] + x]
                    + image[(y + 1) * length_xy_axis[0] + (x + 1)]
                )

            elif x == (length_xy_axis[0]-1):
                appending_list.append(
                    image[(y - 1) * length_xy_axis[0] + (x - 1)]
                    + image[(y - 1) * length_xy_axis[0] + x]
                    + image[(y - 1) * length_xy_axis[0] + (x - (length_xy_axis[0]-1))]

                    + image[y * length_xy_axis[0] + (x - 1)]
                    + image[y * length_xy_axis[0] + (x - (length_xy_axis[0]-1))]

                    + image[(y + 1) * length_xy_axis[0] + (x - 1)]
                    + image[(y + 1) * length_xy_axis[0] + x]
                    + image[(y + 1) * length_xy_axis[0] + (x - (length_xy_axis[0]-1))]
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
        #appending_list.append(appending_value)

print(appending_list[0:5])
print(appending_list[5:10])
print(appending_list[10:15])
print(appending_list[15:20])
print(appending_list[20:25])

#[4, 5, 3, 5, 4]
#[5, 4, 4, 4, 5]
#[3, 4, 4, 4, 3]
#[5, 4, 4, 4, 5]
#[4, 5, 3, 5, 4]