#Name: Noah Sluiman
#Date: September 9th 2024
#MAZE
import pygame,sys
import textstuff
import objects.images
import objects.player
import window

pygame.init()

# Game Setup
fps = 60
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

run=True
while run:
    choice=input("Would you like to start new? Y/N: ").capitalize()
    if choice == "Y":
        run=False
        old_high_score=0
        textstuff.strings_write("0.00", 'txt_file.txt')
    elif choice == "N":
        run=False
    else:
        print("Try again")

#window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
#pygame.display.set_caption("Title")
window.main_window()



bg=objects.images.still(0,0,WINDOW_WIDTH,WINDOW_HEIGHT,"images/backwalls.png")
bgr=objects.player.player(25,25,99,99,'images/baconator.png',2)


def display():
    window.main_window.fill((255,255,255)) #White background
    global timer
    bg.draw(window)
    timer+=.01
    timer = float('{0:.2f}'.format(timer))
    bgr.draw(window)
    
    
    
    window.main_window.blit(font.render("FINISH", True, (123, 255, 78)), (10,850))
    window.main_window.blit(font.render(f"HIGHSCORE: {old_high_score}", True, (123, 255, 78)), (700,200))
    
    window.main_window.blit(font.render(f"{format(timer)}", True, (123, 255, 78)), (200,160))





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
    window.main_window.fill((255,255,255))
    window.main_window.blit(font.render("PRESS A KEY TO CONTINUE", True, (123, 255, 78)), (10,850))
    key_input = pygame.key.get_pressed()
    if key_input.__contains__(True):
        break
    for event in pygame.event.get():
        # if user  QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        
           
        pygame.display.update() #update the display
        fpsClock.tick(fps) #speed of redraw

while True:
    display()
    #gridHelp(window,WINDOW_WIDTH,WINDOW_HEIGHT)
    bgr.key_pressed()
    
    if pygame.sprite.collide_mask(bgr,bg):
        bgr.back()
        display()
        
        
    
    for event in pygame.event.get():
    # if user  QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    
       
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw