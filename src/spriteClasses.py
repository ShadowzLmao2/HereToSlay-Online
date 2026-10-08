import pygame

#Classes for cards
class MonsterCard(pygame.sprite.Sprite):

    #Constructor, define all the aspects of the sprite
    #Aspects:
    #xpos, ypos, image, name
    def __init__(self, imagePath, width, height, x, y):
        #Call parent class to construct
        pygame.sprite.Sprite.__init__(self)

        #Create image of sprite
        #If its an image path, assign image with bitmap of where path leads
        if type(imagePath) is str:
            self.image = pygame.image.load(imagePath).convert()
            self.image = pygame.transform.smoothscale(self.image, (width, height))
        #Must be an image variable from another monster sprite, so assign that
        else:
            try:
                self.image = imagePath
                self.image = pygame.transform.smoothscale(self.image, (width, height))
            #If its not an image or a path, its invalid, assign error image
            except:
                print(str(imagePath) + " is not an image or path, default image assigned")
                self.image = pygame.image.load('src/card_images/404_error.png').convert()
                self.image = pygame.transform.smoothscale(self.image, (width, height))

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def getImage(self):
        return self.image

class LeaderCard(pygame.sprite.Sprite):

    #Constructor, define all the aspects of the sprite
    #Aspects:
    #xpos, ypos, image, name
    def __init__(self, imagePath, width, height, x, y):
        #Call parent class to construct
        pygame.sprite.Sprite.__init__(self)

        #Create image of sprite
        #If its an image path, assign image with bitmap of where path leads
        if type(imagePath) is str:
            self.image = pygame.image.load(imagePath).convert()
            self.image = pygame.transform.smoothscale(self.image, (width, height))
        #Must be an image variable from another monster sprite, so assign that
        else:
            try:
                self.image = imagePath
                self.image = pygame.transform.smoothscale(self.image, (width, height))
            #If its not an image or a path, its invalid, assign error image
            except:
                print(str(imagePath) + " is not an image or path, default image assigned")
                self.image = pygame.image.load('src/card_images/404_error.png').convert()
                self.image = pygame.transform.smoothscale(self.image, (width, height))

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def getImage(self):
        return self.image

class NormalCard(pygame.sprite.Sprite):

    #Constructor, define all the aspects of the sprite
    #Aspects:
    #xpos, ypos, image, name
    def __init__(self, imagePath, width, height, x, y):
        #Call parent class to construct
        pygame.sprite.Sprite.__init__(self)

        #Create image of sprite
        #If its an image path, assign image with bitmap of where path leads
        if type(imagePath) is str:
            self.image = pygame.image.load(imagePath).convert()
            self.image = pygame.transform.smoothscale(self.image, (width, height))
        #Must be an image variable from another monster sprite, so assign that
        else:
            try:
                self.image = imagePath
                self.image = pygame.transform.smoothscale(self.image, (width, height))
            #If its not an image or a path, its invalid, assign error image
            except:
                print(str(imagePath) + " is not an image or path, default image assigned")
                self.image = pygame.image.load('src/card_images/404_error.png').convert()
                self.image = pygame.transform.smoothscale(self.image, (width, height))

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def getImage(self):
        return self.image

#Basic Button Class
#What it needs to do:
#1. Draw to screen
#2. Check when mouse is clicked
#3. Check if mouse is over it
#4. Is it drawn
#5. If it is drawn, then activate method it is linked to
class Button(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, method, color):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((width, height))
        self.color = color
        self.image.fill(self.color)

        self.method = method
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    # Used to process events specific to this sprite
    def update(self, event_list):
        for event in event_list:
            #Check for mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                #print("mouse_clicked")
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    #print("over_button")
                    self.handle_click()

    def handle_click(self):
        #print("clicked_button")
        self.method()


class TextBoard(pygame.sprite.Sprite):

    def __init__(self, x, y, text, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.text = text
        # Initialize font (None uses the default system font)
        self.font = pygame.font.SysFont("Arial", 12)
        self.textSurf = self.font.render(text, 1, (0,0,0))

        #Set background to grey
        self.image = pygame.Surface((width, height))
        self.color = (128,128,128)
        self.image.fill(self.color)

        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image.blit(self.textSurf, [width/2 - W/2, height/2 - H/2])
        
        #Assign and fetch pos
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)