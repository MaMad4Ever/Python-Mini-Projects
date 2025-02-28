from PIL import Image

file = "image.jpg"
img = Image.open(file)

img = img.convert("L")
img.save("./new_img.jpg")
