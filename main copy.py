#Name: Noah Sluiman
#Date: September 9th 2024
#MAZE
import pygame,sys
import textstuff
import manager
import interfaces.intro
import interfaces.game
import interfaces.credits

pygame.init()

run=False
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

window = pygame.display.set_mode((manager.WINDOW_WIDTH,manager.WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("Title")

interfaces.credits.output(window)
interfaces.intro.output(window)
interfaces.game.output(window)