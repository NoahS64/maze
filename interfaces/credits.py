import pygame,sys
import manager




def output(window):
    font = pygame.font.SysFont('Consolas', 30)
    key_Input = pygame.key.get_pressed()
    while True:
        window.fill((255,255,255))
        window.blit(font.render("CREDITS", True, (123, 255, 78)), (200,250))
        window.blit(font.render("CREATOR-NOAH SLUIMAN", True, (123, 255, 78)), (200,350))
        window.blit(font.render("TEACHER-MATTHEW DUSOME", True, (123, 255, 78)), (200,400))
        window.blit(font.render("ASISTANT-RILEY HELPED A LITTLE", True, (123, 255, 78)), (200,450))
        window.blit(font.render("PICTURES-WENDY'S", True, (123, 255, 78)), (200,500))
        
        window.blit(font.render("PRESS ESC TO CONTINUE", True, (123, 255, 78)), (200,700))
        key_input = pygame.key.get_pressed()
        if (key_Input[pygame.K_ESCAPE]):
            break
        for event in pygame.event.get():
            # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw

