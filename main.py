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
speedx=0
speedy=0
player_x=25
player_y=25
speed = 2
timer=0
walls=[]
img_bgr = pygame.image.load('images/baconator.jpg') #with .png or .jpb included in the name
img_bgr = pygame.transform.scale(img_bgr, (99, 99))  #resize image Where 35 ,35 is the size, (x,y)
font = pygame.font.SysFont('Consolas', 30)
#Setup of Starting objects

window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("Title")
def display():
    window.fill((0,0,0)) #White background
    global speedx, speedy, timer, bgr, finish
    speedx+=.02*timer
    speedy+=.02*timer
    timer+=.01
    window.blit(font.render(f"{timer}", True, (123, 255, 78)), (200,160))
    
    walls.append(pygame.draw.rect(window,(255,255,255),(0,0,speedx,speedy)))
    walls.append(pygame.draw.rect(window,(255,0,255),(0,0,WINDOW_WIDTH,10)))
    walls.append(pygame.draw.rect(window,(255,0,255),(0,0,10,WINDOW_HEIGHT)))
    walls.append(pygame.draw.rect(window,(255,0,255),(0,WINDOW_HEIGHT-10,WINDOW_WIDTH,10)))
    walls.append(pygame.draw.rect(window,(255,0,255),(WINDOW_WIDTH-10,0,10,WINDOW_HEIGHT)))
    walls.append(pygame.draw.rect(window,(255,0,255),(0,150,350,10)))
    walls.append(pygame.draw.rect(window,(255,0,255),(500,0,10,300)))
    walls.append(pygame.draw.rect(window,(255,0,255),(0,450,350,10)))
    walls.append(pygame.draw.rect(window,(255,0,255),(150,300,360,10)))
    walls.append(pygame.draw.rect(window,(255,0,255),(500,450,10,250)))
    walls.append(pygame.draw.rect(window,(255,0,255),(350,450,10,125)))
    walls.append(pygame.draw.rect(window,(255,0,255),(200,700,310,10)))
    walls.append(pygame.draw.rect(window,(255,0,255),(0,700,100,10)))
    walls.append(pygame.draw.rect(window,(255,0,255),(200,575,10,125)))
    walls.append(pygame.draw.rect(window,(255,0,255),(650,150,10,300)))
    walls.append(pygame.draw.rect(window,(255,0,255),(650,150,200,10)))
    walls.append(pygame.draw.rect(window,(255,0,255),(800,350,10,300)))
    walls.append(pygame.draw.rect(window,(255,0,255),(800,800,10,200)))
    walls.append(pygame.draw.rect(window,(255,0,255),(500,900,10,200)))
    walls.append(pygame.draw.rect(window,(255,0,255),(300,700,10,150)))
    walls.append(pygame.draw.rect(window,(255,0,255),(500,700,160,10)))
    walls.append(pygame.draw.rect(window,(255,0,255),(650,600,10,100)))
    walls.append(pygame.draw.rect(window,(255,0,255),(0,0,0,0)))
    walls.append(pygame.draw.rect(window,(255,0,255),(0,0,0,0)))
    walls.append(pygame.draw.rect(window,(255,0,255),(0,0,0,0)))
    walls.append(pygame.draw.rect(window,(255,0,255),(0,0,0,0)))
    
    finish=pygame.draw.rect(window, (0,255,0),(10,890,100,100))
    
    
    
    bgr=window.blit(img_bgr,(player_x, player_y))
    window.blit(font.render("BACONATOR", True, (123, 255, 78)), (0,160))
    
    
def collision(object1, object2):
    return object1.colliderect(object2)

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
    key_Input = pygame.key.get_pressed()
    movex = (key_Input[pygame.K_a]*-speed) + (key_Input[pygame.K_d]*speed)
    movey = (key_Input[pygame.K_w]*-speed) + (key_Input[pygame.K_s]*speed)
    player_x += movex
    player_y += movey
    #gridHelp(window,WINDOW_WIDTH,WINDOW_HEIGHT)
    
    for wall in walls:
        if collision(wall,bgr):
            print("Game over")
            exit()
    if collision(finish,bgr):
        print("YOU WON!!")
        exit()
    
    for event in pygame.event.get():
    # if user  QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
       
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw