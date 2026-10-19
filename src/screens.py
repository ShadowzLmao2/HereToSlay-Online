from draw_pygame import *

def menu():
    pass

def settings():
    pass

def cards():
    pass

def test(screen, all_sprites):
     # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    all_sprites.draw(screen)
    #screen.blit(background, (0, 0))

def switch_screen(newScreen):
    global previous_screen
    global current_screen
    previous_screen = current_screen
    current_screen = newScreen
    return None