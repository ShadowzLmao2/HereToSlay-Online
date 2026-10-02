import pygame

from spriteClasses import *
from screens import *

#Options are:
#TEST: draw a bunch of test stuff
#MENU: menu screen
#SETTINGS: settings screen
#CARDS: list of cards
current_screen = "TEST"

pygame.init()

screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True


background = MonsterCard('src/card_images/WarriorsAndDruids/Cards/majestelk.png',200,280,0,0)
#background = MonsterCard(0,200,280,0,0)

button = Button(400,400, "hello", "test", print("hello"))

#screen.blit(background, (0, 0))

all_sprites = pygame.sprite.Group()
all_sprites.add(background)
all_sprites.add(button)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            running = False

    # RENDER YOUR GAME HERE
    match current_screen:
        case "TEST":
            test(screen, all_sprites)
    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)

def startPygame():
    return

pygame.quit()