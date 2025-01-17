
#Date: September 9th 2024
#MAZE
import pygame,sys
import textstuff
import manager
import interfaces.intro
import interfaces.game
import interfaces.credits

pygame.init()

#Asks user if they would like to reset the highscore or not
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



#window setup
window = pygame.display.set_mode((manager.WINDOW_WIDTH,manager.WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("MAZE")

#changes screen
while True:
    if manager.level==2:
        interfaces.credits.output(window)
    elif manager.level==0:
        interfaces.intro.output(window)
    elif manager.level==1:
        interfaces.game.output(window)
    elif manager.level==-1:
        pygame.quit()
        sys.exit()