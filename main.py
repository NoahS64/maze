#Name: Noah Sluiman
#Date: September 9th 2024
#MAZE
import pygame,sys


pygame.init()

# Game Setup
fps = 120
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
x=10
y=100
img_bgr = pygame.image.load('images/baconator.jpg') #with .png or .jpb included in the name
img_bgr = pygame.transform.scale(img_bgr, (100, 100))  #resize image Where 35 ,35 is the size, (x,y)
font = pygame.font.SysFont('Consolas', 30)
#Setup of Starting objects

window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("Title")
def display():
    window.fill((0,0,0)) #White background
    global x
    global y
    x+=.25/4
    y+=.15/4
    object_draw_name=pygame.draw.rect(window,(255,255,255),(WINDOW_HEIGHT/2-x/2,WINDOW_WIDTH/2-y/2,x,y))
    nameOfObject=window.blit(img_bgr,(0, 200))
    window.blit(font.render("BACONATOR", True, (123, 255, 78)), (0, 160))

while True:
    display()
    for event in pygame.event.get():
    # if user  QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
  
       
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw