import pygame
import sys


################################################################################
# IMPORTANT:
# Do this ENTIRE PROJECT by following the associated videos for Moving Smile.
################################################################################


def main():
    pygame.init()
    pygame.display.set_caption("Moving Smile")
    screen = pygame.display.set_mode((640, 480))

    # TODO 7: Make a pygame.time.Clock and set the clock speed to 60 fps
    clock = pygame.time.Clock()

    eye_x = 0
    eye_y = 0

    while True:
        clock.tick(60)
        events = pygame.event.get()  # List of events on this cycle of game loop
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            # TODO 4: Make a print statement for Up, Down, Left, and Right keys
            # TODO 5: Make the eye pupils move with Up, Down, Left, and Right keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print("Up")
                    eye_y = eye_y - 2
                elif event.key == pygame.K_DOWN:
                    print("Down")
                    eye_y = eye_y + 2
                elif event.key == pygame.K_LEFT:
                    print("Left")
                    eye_x = eye_x - 2
                elif event.key == pygame.K_RIGHT:
                    print("Right")
                    eye_x = eye_x + 2

        # TODO 6: Make the eye pupils move while holding down the w/a/s/d keys

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w]:
            eye_y = eye_y - 1
        if keys_pressed[pygame.K_s]:
            eye_y = eye_y + 1
        if keys_pressed[pygame.K_a]:
            eye_x = eye_x - 1
        if keys_pressed[pygame.K_d]:
            eye_x = eye_x + 1

        screen.fill((255, 255, 255))  # white


        # API --> pygame.draw.circle(screen, color, (x, y), radius, optional width)

        pygame.draw.circle(screen, (255, 255, 0), (320, 240), 210)  # yellow circle
        pygame.draw.circle(screen, (0, 0, 0), (320, 240), 210, 4)  # black outline

        pygame.draw.circle(screen, (225, 225, 225), (240, 160), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (240, 160), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), (242 + eye_x, 162 + eye_y), 7)  # black pupil

        pygame.draw.circle(screen, (225, 225, 225), (400, 160), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (400, 160), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), (398 + eye_x, 162 + eye_y), 7)  # black pupil

        # TODO 1: Draw a nose
        # Suggestion: color (80,0,0) location (320,245), radius 10
        # API --> pygame.draw.circle(screen, (r,g,b), (x, y), radius, optional width)
        pygame.draw.circle(screen, (80, 0, 0), (320, 245), 10)

        # TODO 2: Draw a mouth
        # Suggestion: color (0,0,0), x 230, y 320, width 180, height 30
        # API --> pygame.draw.rect(screen, (r,g,b), (x, y, width, height), optional width)
        pygame.draw.rect(screen, (0, 0, 0), (230, 320, 180, 30))

        # TODO 3: Draw using a line (anything you want using the pygame.draw.line method)
        pygame.draw.line(screen, (0, 128, 128), (100, 100), (150, 125))
        pygame.display.update()


main()
