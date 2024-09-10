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
speedr=0
player_x=50
player_y=50
speed = 2
timer=0
walls=[]
img_bgr = pygame.image.load('images/baconator.jpg') #with .png or .jpb included in the name
img_bgr = pygame.transform.scale(img_bgr, (100, 100))  #resize image Where 35 ,35 is the size, (x,y)
font = pygame.font.SysFont('Consolas', 30)
#Setup of Starting objects

window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("Title")
def display():
    window.fill((0,0,0)) #White background
    global speedr, timer
    speedr+=.01*timer
    timer+=.01
    window.blit(font.render(f"{timer}", True, (123, 255, 78)), (200,160))
    
    nameOfObject=pygame.draw.circle(window, (0,0,255), (0,0), speedr)
    #object_draw_name=pygame.draw.rect(window,(255,255,255),(0,0,box_speedx,box_speedy))
    walls.append(pygame.draw.rect(window,(255,0,255),(0,0,WINDOW_WIDTH,10)))
    walls.append(pygame.draw.rect(window,(255,0,255),(0,0,10,WINDOW_HEIGHT)))
    walls.append(pygame.draw.rect(window,(255,0,255),(0,WINDOW_HEIGHT-10,WINDOW_WIDTH,10)))
    walls.append(pygame.draw.rect(window,(255,0,255),(WINDOW_WIDTH-10,0,10,WINDOW_HEIGHT)))
    walls.append(pygame.draw.rect(window,(255,0,255),(0,0,0,0)))
    walls.append(pygame.draw.rect(window,(255,0,255),(0,0,0,0))    )
    walls.append(pygame.draw.rect(window,(255,0,255),(0,0,0,0)))
    walls.append(pygame.draw.rect(window,(255,0,255),(0,0,0,0)))
    walls.append(pygame.draw.rect(window,(255,0,255),(0,0,0,0)))
    walls.append(pygame.draw.rect(window,(255,0,255),(0,0,0,0)))
    
    
    
    nameOfObject=window.blit(img_bgr,(player_x, player_y))
    window.blit(font.render("BACONATOR", True, (123, 255, 78)), (0,160))
    
    
def collision(object1, object2):
    return object1.colliderect(object2)


while True:
    display()
    key_Input = pygame.key.get_pressed()
    movex = (key_Input[pygame.K_a]*-speed) + (key_Input[pygame.K_d]*speed)
    movey = (key_Input[pygame.K_w]*-speed) + (key_Input[pygame.K_s]*speed)
    player_x += movex
    player_y += movey
    
    for wall in walls:
        if collision(wall,img_bgr):
            player_x-=movex
            player_y-=movey
    
    for event in pygame.event.get():
    # if user  QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
       
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw