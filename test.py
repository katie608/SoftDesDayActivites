import pygame

pygame.init()

# Set the width and height of the screen
screen = pygame.display.set_mode((1000, 800))

#Sets the caption at the top
pygame.display.set_caption("A fun caption")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #Background color
    screen.fill((0,0,150))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
exit()
