import cv2
import numpy as np
import random

# load image
character_image = cv2.imread('autism.png', cv2.IMREAD_UNCHANGED)

# set up initial position and velocity
position = (0, 0)
velocity = [5, 5]

# create a window for displaying the image
cv2.namedWindow('Character', cv2.WINDOW_NORMAL)

# main loop
while True:
    # move the character
    position = (position[0] + velocity[0], position[1] + velocity[1])

    # check if the character has hit the edge of the screen
    if position[0] < 0 or position[0] > 1920:
        velocity[0] = -velocity[0]
    if position[1] < 0 or position[1] > 1080:
        velocity[1] = -velocity[1]

    # randomly display food on the screen
    if random.random() < 0.01:
        food_position = (random.randint(0, 1920), random.randint(0, 1080))
        cv2.circle(character_image, food_position, 10, (0, 0, 255), -1)

    # randomly display a message on the screen
    if random.random() < 0.005:
        message = 'Hello there!'
        cv2.putText(character_image, message, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    # display the character on the screen
    cv2.imshow('Character', character_image)

    # wait for a short time before updating the screen
    cv2.waitKey(10)

    # clear the food and message
    character_image = cv2.imread('autism.png', cv2.IMREAD_UNCHANGED)