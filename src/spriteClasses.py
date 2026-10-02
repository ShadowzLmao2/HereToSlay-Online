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
class Button(pygame.sprite.Sprite):

    #Constructor
    def __init__(self, x, y, text, name, method):
        #call parent class to construct
        pygame.sprite.Sprite.__init__(self)

        #Assign name, text, and method
        self.name = name
        self.text = text
        self.method = method

        #Set background to grey
        self.image = pygame.Surface((50, 50))
        self.color = (128,128,128)
        self.image.fill(self.color)

        # Initialize font (None uses the default system font)
        self.font = pygame.font.Font(None, 12)

        #Update text
        self.update_text(text)

        #Assign and fetch pos
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    #Check mouse pos to see if its over the button
    def update(self):
        #Check if the mouse is hovering over the button.
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.image = self.image_hover
        else:
            self.image = self.image_normal

    #If mouse over the button, and mouse clicked, button pressed
    def handle_event(self, event):
        #Process click events passed down from the main loop.
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.method()  # Execute the button's unique logic