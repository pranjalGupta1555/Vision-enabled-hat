import PIL
from PIL import Image
# open an image file (.bmp,.jpg,.png,.gif)
# change image filename to something you have in the working folder
im1 = Image.open("2018-10-06_09-21-56.jpg")
# rotate 60 degrees counter-clockwise
im2 = im1.rotate(180)
# brings up the modified image in a viewer, simply saves the image as
# a bitmap to a temporary file and calls viewer associated with .bmp
# make certain you have an image viewer associated with this file type
im2.show()
# save the rotated image as d.gif to the working folder
# you can save in several different image formats, try d.jpg or d.png
# PIL is pretty powerful stuff and figures it out from the extension
im2.save("d.jpg")
