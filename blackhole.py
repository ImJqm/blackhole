import pygame
import sys
import numpy as np

pygame.init()

width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Black Hole")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


CUBE = np.array([
    [-5,-5,-5]
[5,-5,-5],
[5,5,-5],
[-5,5,-5],
[-5,-5,5],
[-5,5,5],
[5,5,5],
[5,-5,5]
    ])

def draw_to_screen(x,y,z):
    if (z<=0):
        return
    x = x/z
    y = y/z
    screen.set_at((x,y), RED)

def main():
    running = True
    
    clock = pygame.time.Clock()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        screen.fill(BLACK)
    
        screen_rect = screen.get_rect()
    
        center = screen_rect.center
    
        pygame.display.flip()
    
        print(center)
    
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

main()
