import pygame, sys
import manager
import objects.button
import interfaces.game
import objects.images
import objects.text

def output(window):
    font = pygame.font.SysFont('Consolas', 30)
    #creates button variables
    btn_game=objects.button.no_background(20,350,'Consolas', 30,(0,0,0),(255,0,255),"GAME")
    btn_credits=objects.button.with_images(300,350,100,100,"images/credits.png","images/credits_h.png")
    btn_x=objects.button.with_images(800,800,100,100,"images/exit.png","images/exit_h.png")
    
    window.blit(font.render("ENTER NAME BELOW", True, (123, 255, 78)), (80,170))
    text_name=objects.text.input(80,200,300,50,'Consolas',24,(255,40,123),(123,40,255),"")
    
    run=True
    while run:
        window.fill((255,255,255))
       #DRAW
        btn_game.draw(window)
        btn_credits.draw(window)
        btn_x.draw(window)
        text_name.draw(window)
        
        for event in pygame.event.get():
            #when click on btn bring you to corresponding screen
            if btn_game.update(pygame.mouse.get_pos(),event):
                run=False
                manager.level=1
            if btn_credits.update(pygame.mouse.get_pos(),event):
                run=False
                manager.level=2
            if btn_x.update(pygame.mouse.get_pos(),event):
                pygame.quit()
                sys.exit()
            text_name.update(pygame.mouse.get_pos(),event)
                
            # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw