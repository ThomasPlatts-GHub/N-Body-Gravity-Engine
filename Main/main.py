import pygame
import numpy as np
import vector

pygame.init()
WIDTH, HEIGHT = 1800, 900
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

number_of_planets = 5
planets = []

list_of_colours = [(128, 48, 32), (58, 255, 0), (213, 255, 145), (0, 56, 255), (49, 152, 207)]
list_of_radii = [10, 20, 30, 40, 50]

# Polar coordinates vector 
polar_coordinates = vector.array({
    "rho": np.random.exponential(5, 10000),
    "phi": np.random.uniform(-np.pi, np.pi, 10000)
})

print(polar_coordinates)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0,0,0))

    # Draw star
    pygame.draw.circle(window, (255,255,0), (WIDTH//2, HEIGHT//2), 50)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()