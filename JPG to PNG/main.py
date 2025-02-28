from PIL import Image

im = Image.open("image.jpg").convert("RGB")
im.save("image.png", "png")
