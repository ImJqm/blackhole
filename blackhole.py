import pygame
import sys

pygame.init()

width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Black Hole")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

running = True

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    screen_rect = screen.get_rect()

    center = screen_rect.center

    pygame.draw.circle(
        surface=screen, color=RED, center=center, radius=50
    )

    pygame.display.flip()

    print(center)

    clock.tick(60)

pygame.quit()
sys.exit()
