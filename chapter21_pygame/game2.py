import pygame

FRAME_REFRESH_RATE = 30
BLUE = (0, 0, 255)
BACKGROUND = (255, 255, 255)  # White
WIDTH = 10
HEIGHT = 10


def main():
    print('Initialising PyGame')
    pygame.init()  # Required by every PyGame application

    print('Initialising Box Game')
    display_surface = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('Box Game')
    print('Update display')
    pygame.display.update()
    print('Setup the Clock')
    clock = pygame.time.Clock()
    # Clear the screen of current contents
    display_surface.fill(BACKGROUND)

    print('Starting main Game Playing Loop')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('Received Quit Event:', event)
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print('Received Mouse Event', event)
                x, y = event.pos
                pygame.draw.rect(display_surface, BLUE, [x, y, WIDTH, HEIGHT])

        # Update the display
        pygame.display.update()

        # Defines the frame rate - the number of frames per second
        # Should be called once per frame (but only once)
        clock.tick(FRAME_REFRESH_RATE)

    print('Game Over')
    # Now tidy up and quit Python
    pygame.quit()


if __name__ == '__main__':
    main()
