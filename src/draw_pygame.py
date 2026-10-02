import pygame
from sprites import *
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
#background = MonsterCard('src/card_images/WarriorsAndDruids/Cards/majestelk.png',200,280,0,0)
background = MonsterCard(0,200,280,0,0)
#screen.blit(background, (0, 0))
all_sprites = pygame.sprite.Group()
all_sprites.add(background)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            running = False

     # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    all_sprites.draw(screen)
    #screen.blit(background, (0, 0))

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)

def startPygame():
    return

pygame.quit()