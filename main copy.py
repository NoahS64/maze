#Name: Noah Sluiman
#Date: September 9th 2024
#MAZE
import pygame,sys
import textstuff
import objects.images

pygame.init()

# Game Setup
fps = 120
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
player_x=25
player_y=25
speed = 2
timer=0

font = pygame.font.SysFont('Consolas', 30)

old_high_score=float(textstuff.strings_read('txt_file.txt')[0])
#Setup of Starting objects

window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("Title")
bg=objects.images.still(0,0,WINDOW_WIDTH,WINDOW_HEIGHT,"images/backwalls.png")


def display():
    window.fill((255,255,255)) #White background
    global timer
    bg.draw(window)
    timer+=.01
    timer = float('{0:.2f}'.format(timer))

    
    
    
    window.blit(font.render("FINISH", True, (123, 255, 78)), (10,850))
    window.blit(font.render(f"HIGHSCORE: {old_high_score}", True, (123, 255, 78)), (700,200))
    
    window.blit(font.render(f"{format(timer)}", True, (123, 255, 78)), (200,160))


def gridHelp(window,WINDOW_WIDTH,WINDOW_HEIGHT):
        spacer = 50
        font = pygame.font.SysFont('Consolas', 10)
        for gridX in range(0, WINDOW_WIDTH, spacer):        
            window.blit(pygame.transform.rotate(font.render(str(gridX), True, (0, 0, 0)),90),(gridX,0))
        for gridY in range(0, WINDOW_HEIGHT, spacer):
            window.blit(font.render(str(gridY), True, (0, 0, 0)), (0, gridY))
        for gridX in range(0, WINDOW_WIDTH, spacer):
            pygame.draw.line(window,(255,0,0),(gridX,0),(gridX,WINDOW_HEIGHT))
        for gridY in range(0, WINDOW_HEIGHT, spacer):
            pygame.draw.line(window,(255,0,0),(0,gridY),(WINDOW_WIDTH,gridY))  

while True:
    display()
    #gridHelp(window,WINDOW_WIDTH,WINDOW_HEIGHT)
    
    for event in pygame.event.get():
    # if user  QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
       
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw