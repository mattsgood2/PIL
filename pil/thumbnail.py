from PIL import Image
import glob, os

photo = Image.open('photo1.jpg')

# print(photo.size)
# print(photo.mode)
p2 = photo.copy()
p2.thumbnail((400, 300))
p2.save('photo1.jpg')
