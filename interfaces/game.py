import pygame,sys
import objects.images
import objects.player
import manager
import textstuff
import interfaces.credits
import objects.button
import interfaces.intro


#method allows variables to be easily trandfered
def output(window):
    #creates background and player
    bg=objects.images.still(0,0,manager.WINDOW_WIDTH,manager.WINDOW_HEIGHT,"images/backwalls.png")
    bgr=objects.player.player(25,25,99,99,'images/baconator.png',2)

    font = pygame.font.SysFont('Consolas', 30)

#Highscore variable
    old_high_score=float(textstuff.strings_read('txt_file.txt')[0])
#intro btn
    btn_intro=objects.button.with_background(10,900,300,100,'Consolas',30,(0,255,0),(255,0,255),(0,255,0),(255,0,255),"PRESS TO RETURN")
    
    
    def gridHelp():
            spacer = 50
            font = pygame.font.SysFont('Consolas', 10)
            for gridX in range(0, manager.WINDOW_WIDTH, spacer):        
                window.blit(pygame.transform.rotate(font.render(str(gridX), True, (0, 0, 0)),90),(gridX,0))
            for gridY in range(0, manager.WINDOW_HEIGHT, spacer):
                window.blit(font.render(str(gridY), True, (0, 0, 0)), (0, gridY))
            for gridX in range(0, manager.WINDOW_WIDTH, spacer):
                pygame.draw.line(window,(255,0,0),(gridX,0),(gridX,manager.WINDOW_HEIGHT))
            for gridY in range(0, manager.WINDOW_HEIGHT, spacer):
                pygame.draw.line(window,(255,0,0),(0,gridY),(manager.WINDOW_WIDTH,gridY))  


    def display():
        window.fill((255,255,255)) #White background
        #draws background, player, and button
        bg.draw(window)
        #time variables
        manager.timer+=.01
        manager.timer = float('{0:.2f}'.format(manager.timer))
        bgr.draw(window)
        btn_intro.draw(window)


        window.blit(font.render("FINISH", True, (123, 255, 78)), (600,900))
        #displays score
        window.blit(font.render(f"HIGHSCORE: {old_high_score}", True, (123, 255, 78)), (700,200))

        window.blit(font.render(f"{format(manager.timer)}", True, (123, 255, 78)), (200,160))




    run=True
    while run:
        display()
        #gridHelp(window,WINDOW_WIDTH,WINDOW_HEIGHT)
        bgr.key_pressed()

#collision
        if pygame.sprite.collide_mask(bgr,bg):
            bgr.back()
            display()



        for event in pygame.event.get():\
            #changes to intro screen
            if btn_intro.update(pygame.mouse.get_pos(),event):
                run=False
                manager.level=0
        # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw