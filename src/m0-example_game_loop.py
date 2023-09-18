import pygame
import sys

pygame.init()
pygame.display.set_caption("Hello World")
screen = pygame.display.set_mode((640, 480))

while True:

    events = pygame.event.get()  # List of events on this cycle of game loop
    for event in events:
        print(event)  # Used for an example here
        if event.type == pygame.QUIT:
            sys.exit()
        # Additional interactions

    # Draw things on the screen
    screen.fill((0, 0, 0))  # black

    pygame.display.update()
