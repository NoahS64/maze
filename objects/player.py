import objects.images
import pygame

class player(objects.images.still):
    def __init__(self, x, y, width, height, image_to_use, speed):
        super().__init__(x, y, width, height, image_to_use)
        self.speed=speed
        
    def key_pressed(self):
        
        key_Input = pygame.key.get_pressed()
        self.movex = (key_Input[pygame.K_a]*-self.speed) + (key_Input[pygame.K_d]*self.speed)
        self.movey = (key_Input[pygame.K_w]*-self.speed) + (key_Input[pygame.K_s]*self.speed)
        self.rect.x += self.movex
        self.rect.y += self.movey
        
    def back(self):
        self.rect.x -= self.movex
        self.rect.y -= self.movey