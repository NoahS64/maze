import pygame, sys
import manager


def output(window):
    font = pygame.font.SysFont('Consolas', 30)
    while True:
        window.fill((255,255,255))
        window.blit(font.render("PRESS A KEY TO CONTINUE", True, (123, 255, 78)), (10,850))
        key_input = pygame.key.get_pressed()
        if key_input.__contains__(True):
            break
        for event in pygame.event.get():
            # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw