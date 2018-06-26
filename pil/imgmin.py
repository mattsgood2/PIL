from PIL import Image

size = (400, 300)

photo = Image.open('img/hotel3.jpg')


print(photo.size)
print(photo.mode)

photo.resize(size, resample=3).show()
