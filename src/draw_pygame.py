import pygame
import os

from spriteClasses import *
from screens import *
from main import *

#Options are:
#TEST: draw a bunch of test stuff
#MENU: menu screen
#SETTINGS: settings screen
#CARDS: list of cards
current_screen = "TEST"
#To be used when switching screens, if it is not the same as current when starting the draw, unload old sprites and load new ones
previous_screen = ""

fullscreen = False

pygame.init()

w = 0
h = 0

os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()

w, h = info.current_w, info.current_h

screen = pygame.display.set_mode((1280,720), pygame.RESIZABLE, pygame.SCALED)
#screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True


background = MonsterCard('src/card_images/WarriorsAndDruids/Cards/majestelk.png',200,280,0,0)
#background = MonsterCard(0,200,280,0,0)

button = Button(400,400,100,100,lambda:background.fetch_image("Abyss Queen"),(128,128,128))

textBoard = TextBoard(200,400,"this is a sign",100,40)

#screen.blit(background, (0, 0))

all_sprites = pygame.sprite.Group()
all_sprites.add(background)
all_sprites.add(button)
all_sprites.add(textBoard)


while running:
    event_list = pygame.event.get()

    for event in event_list:
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            running = False

        elif event.type == pygame.VIDEORESIZE:
            w, h = pygame.display.get_surface().get_size()
            print("Window is now " + str(w) + "x" + str(h))

        #Key Presses
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((screen.get_width(),screen.get_height()), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((1280,720), pygame.RESIZABLE)

    all_sprites.update(event_list)

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