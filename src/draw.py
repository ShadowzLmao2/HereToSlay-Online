import pygame
import os

from spriteClasses import *
from screens import *
import main
import cards

#Options are:
#TEST: draw a bunch of test stuff
#MENU: menu screen
#SETTINGS: settings screen
#CARDS: list of cards
current_screen = "TEST"
#To be used when switching screens, if it is not the same as current when starting the draw, unload old sprites and load new ones
previous_screen = ""

fullscreen = False
class gameEngine:
    def __init__(self):
        pygame.init()
        self.font = pygame.font.Font(size=34)
        self.clicked = False
        screen = pygame.display.set_mode((1280,720))
        self.clock = pygame.time.clock()
        self.state_timer = 0
        self.running = True
        self.info = pygame.display.Info()
        
    def run(self):
        while self.running:
            deltaTime = self.clock.tick(framerate)/100.0
            self.handleInput()
            self.update(deltaTime)
            self.render()

            all_sprites.update(pygame.event.get())

            match current_screen:
                case "TEST":
                    test(screen, all_sprites)
            # flip() the display to put your work on screen
            pygame.display.flip()
        pygame.quit
        pass

    def handleInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                self.running = False

            elif event.type == pygame.VIDEORESIZE:
                w, h = pygame.display.get_surface().get_size() #This needs to have a delay, it prints way too much
                print("Window is now " + str(w) + "x" + str(h))

            #Key Presses
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode((screen.get_width(),screen.get_height()), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((1280,720), pygame.RESIZABLE)

    def update(self, deltaTime: float):
        self.state_timer += deltaTime

    def render(self):
        pass

w = 0
h = 0

os.environ['SDL_VIDEO_CENTERED'] = '1' #What does this do?

w, h = info.current_w, info.current_h

screen = pygame.display.set_mode((1280,720), pygame.RESIZABLE, pygame.SCALED)
#screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

card = "Abyss Queen"
background = MonsterCard(Cards[card]["Image"],200,280,0,0)
#background = MonsterCard(0,200,280,0,0)
button = Button(400,400,100,100,lambda:background.fetch_image(card),(128,128,128))

textBoard = TextBoard(200,400,"this is a sign",100,40)

#screen.blit(background, (0, 0))

all_sprites = pygame.sprite.Group()
all_sprites.add(background)
all_sprites.add(button)
all_sprites.add(textBoard)
pygame.quit()