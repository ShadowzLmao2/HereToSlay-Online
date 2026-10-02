import pygame

class MonsterCard(pygame.sprite.Sprite):

    #Constructor, define all the aspects of the sprite
    #Aspects:
    #xpos, ypos, image, name
    def __init__(self, imagePath, width, height, x, y):
        #Call parent class to construct
        pygame.sprite.Sprite.__init__(self)

        #Create image of sprite
        self.image = pygame.image.load(imagePath).convert()
        self.image = pygame.transform.smoothscale(self.image, (width, height))

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)