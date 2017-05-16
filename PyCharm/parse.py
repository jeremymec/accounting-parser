from PIL import Image
from __init__ import image_to_string
myImage = Image.open("data/bs1.png")
string = image_to_string(myImage)
print(string)