from PIL import Image, ImageEnhance

image = Image.open("img1.jpg")
image.show()

original = ImageEnhance.Brightness(image)
newImage = original.enhance(2.5)
newImage.show()

original = ImageEnhance.Color(image)
newImage = original.enhance(2.5)
newImage.show()

original = ImageEnhance.Sharpness(image)
newImage = original.enhance(8.3)
newImage.show()