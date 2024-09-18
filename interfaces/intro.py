import pygame, sys
import manager
import objects.button
import interfaces.game

def output(window):
    font = pygame.font.SysFont('Consolas', 30)
    btn_game=objects.button.no_background(20,350,'Consolas', 30,(0,0,0),(255,0,255),"GAME")
    
    run=True
    while run:
        window.fill((255,255,255))
        window.blit(font.render("PRESS A KEY TO CONTINUE", True, (123, 255, 78)), (10,850))
        btn_game.draw(window)
        
        
        for event in pygame.event.get():
            if btn_game.update(pygame.mouse.get_pos(),event):
                run=False
                manager.level=1
            # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw