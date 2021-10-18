import pygame
import numpy as np

width = 800
scale = 250

pygame.init()
w = pygame.display.set_mode((width, width))
font = pygame.font.SysFont(None, 24)

points = []
turn = np.square(np.sqrt(2) + 1)
dist = 0
angle = 0
iters = 1000

turn_text = font.render(str(turn), True, (255, 255, 255))
w.blit(turn_text, (0, 0))

for i in range(iters):
    dist += .001
    point = np.array([dist * np.cos(angle), dist * np.sin(angle)])
    print(point)
    angle += turn * 2 * np.pi
    if angle > 2 * np.pi: angle -= 2 * np.pi
    points.append(point)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for point in points:
        pygame.draw.circle(surface=w, color=(255, 0, 0), center=(point[0] * scale + width / 2, point[1] * scale + width / 2), radius=3)

    pygame.display.update()