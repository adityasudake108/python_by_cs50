import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "output.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)
# In this we use Pillow library to create an animated GIF file from a list of image files.
# This code reads image files from the command line, creates a list of Image objects, and saves the images as an animated GIF file.
# The first image is saved with the name output.gif, and the second image is appended to it.
