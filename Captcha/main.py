from captcha.image import ImageCaptcha
from random import randint, choice
import string


image = ImageCaptcha(width = 280, height = 90)
 
char = string.ascii_letters + string.digits + string.punctuation

captcha_text = "".join(choice(char) for x in range(randint(4, 6)))
 
data = image.generate(captcha_text)  
 
image.write(captcha_text, 'CAPTCHA.png')
