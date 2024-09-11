from PIL import Image
pixelate_factor = 10
image = Image.open("Mona_Lisa.jpg")
width, height = image.size
rescale_dimensions = (int(width/pixelate_factor), int(height/pixelate_factor))
image = image.resize(rescale_dimensions)
print(list(image.getdata()))
image = image.convert("L")
print(list(image.getdata()))


print("Image Dimensions:", image.size)
