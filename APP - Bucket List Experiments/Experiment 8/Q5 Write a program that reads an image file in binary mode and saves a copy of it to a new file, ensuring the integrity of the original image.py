""" Write a program that reads an image file in binary mode and saves a copy of it to a new file, ensuring the
integrity of the original image. """

with open("original_image.jpg", "rb") as original_file:
    image_data = original_file.read()

with open("copied_image.jpg", "wb") as copied_file:
    copied_file.write(image_data)

print("Image copied successfully to copied_image.jpg")
