import pygame,sys
import manager
import objects.button



def output(window):
    font = pygame.font.SysFont('Consolas', 30)
    btn_intro=objects.button.with_background(20,800,400,150,'Consolas',30,(0,255,0),(255,0,255),(0,255,0),(255,0,255),"PRESS TO RETURN")
    
    run=True
    while run:

        window.fill((255,255,255))
        #credits
        window.blit(font.render("CREDITS", True, (123, 255, 78)), (200,250))
        window.blit(font.render("CREATOR-NOAH SLUIMAN", True, (123, 255, 78)), (200,350))
        window.blit(font.render("TEACHER-MATTHEW DUSOME", True, (123, 255, 78)), (200,400))
        window.blit(font.render("ASISTANT-RILEY HELPED A LITTLE", True, (123, 255, 78)), (200,450))
        window.blit(font.render("BACONATOR-WENDY'S", True, (123, 255, 78)), (200,500))
        window.blit(font.render("CREDITS_BTN-123RF.COM", True, (123, 255, 78)), (200,550))
        window.blit(font.render("EXIT_BTN-FREEPIK.COM", True, (123, 255, 78)), (200,600))
#Draws btn on screen
        btn_intro.draw(window)
        
        for event in pygame.event.get():
            #if btn intro was clicked it displays intro screen
            if btn_intro.update(pygame.mouse.get_pos(),event):
                run=False
                manager.level=0
            # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw

