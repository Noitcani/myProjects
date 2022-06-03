# Set up pygame for .mp3 control
import pygame

pygame.init()
pygame.mixer.init()

# Set up time, for sleep
import time

# Create ping object and control volume for ping
ping = pygame.mixer.Sound('ping.mp3')
ping.set_volume(0.1)   # Now plays at 90% of full volume.    

# Breathing timer
## Loop infinite

def start_app():

    loop = True

    while loop:

        ## Breathe in (4sec)
        ping.play()
        time.sleep(4)

        ## Hold (7sec)
        ping.play()
        time.sleep(7)

        ## Breathe out (8sec)
        ping.play()
        time.sleep(8)

start_app()

