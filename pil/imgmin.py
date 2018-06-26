from PIL import Image

# To run on Atom with windows and correct package installed use ctrl+shft+b

photo = Image.open('img/hotel3.jpg')

photo.show()
print(photo.size)
