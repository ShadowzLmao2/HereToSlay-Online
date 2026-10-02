import pygame

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