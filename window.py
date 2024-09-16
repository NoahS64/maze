import pygame,sys



pygame.init()


fps = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000


def main_window():
    window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
    pygame.display.set_caption("Title")
    
def intro_window():
    pass