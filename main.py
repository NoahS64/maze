#Name: Noah Sluiman
#Date: September 9th 2024
#MAZE
import pygame,sys


pygame.init()

# Game Setup
fps = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

#Setup of Starting objects

window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("Title")
def display():
    window.fill((255,255,255)) #White background
    object_draw_name=pygame.draw.rect(window,(0,0,255),(10,10,100,50))
   
   

while True:
    display()
    for event in pygame.event.get():
    # if user  QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
  
       
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw