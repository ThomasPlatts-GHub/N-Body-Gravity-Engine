import pygame
import numpy as np

WIDTH, HEIGHT = 1800, 900
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0,0,0))
    pygame.display.flip()

pygame.quit()