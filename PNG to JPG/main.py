 from PIL import Image

im = Image.open("image.png").convert("RGB")
im.save("image.jpg", "jpeg")
