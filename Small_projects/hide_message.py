# hide a text message in an image file

import pygame
import color

pygame.init()

# make the smallest window possible since we dont actually need it
win = pygame.display.set_mode((1,1))

# load an image
image = pygame.image.load("bug.jpg").convert_alpha()

# iterate over all pixels and make the red value even
for y in range(image.get_height()):
        for x in range(image.get_width()):
            # get the color
            (r,g,b,a) = image.get_at((x,y))
            if r % 2 == 1:
                # odd red value
                r -= 1
            image.set_at((x,y), (r,g,b))
# all pixels have even red values

# NEXT: embed a message
# create a pygame font object
font = pygame.font.SysFont("Veranda", 60)

# create an image surface containing some text
# False turns off anti-aliasing (no smoothing at the edges of the text)
# True turns on anti-aliasing (smooths corners of the text to look nicer)
msg = font.render("well", False, color.black)

# TODO interate overall all pixels in the message. If the pixel is black,
# set the corresponding pixel in the image to be odd
for y in range(msg.get_height()):
    for x in range (msg.get_width()):
        # get the rgb value
        (r,g,b,a) = msg.get_at((x, y))

        # check if black (part of the text)
        if (r,g,b) == color.black:
            # get the corresponding image pixel
            (ir, ig, ib, ia) = image.get_at((x, y))
            # add one to make ir 0dd
            ir += 1
            # set the updated pixel
            image.set_at((x, y), (ir, ig, ib))

print("done")




# save the image back to a file
pygame.image.save(image, "hidden_message.png")
print("Done")