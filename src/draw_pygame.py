import pygame
import draw
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
background = pygame.image.load('src/card_images/WarriorsAndDruids/Cards/majestelk.png').convert()
background = pygame.transform.smoothscale(background, (pygame.Surface.get_width(background)/2, pygame.Surface.get_height(background)/2))
screen.blit(background, (0, 0))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            running = False

     # fill the screen with a color to wipe away anything from last frame
    #screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)

def startPygame():
    return

pygame.quit()