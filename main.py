import pygame
import numpy as np
import time

width = 800
scale = 250

pygame.init()
w = pygame.display.set_mode((width, width))
font = pygame.font.SysFont(None, 24)

points = []
turn = (1 + np.sqrt(5))/2 - 1 - 0.005

def update():
    global points
    dist = 0
    angle = 0
    iters = 1000
    points = []
    for i in range(iters):
        dist += .001
        # print(point)
        angle += turn * 2 * np.pi
        if angle > 2 * np.pi: angle -= 2 * np.pi
        points.append(np.array([dist * np.cos(angle), dist * np.sin(angle)]))

running = True
while running:
    w.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    update()
    turn += 0.000001

    for point in points:
        pygame.draw.circle(surface=w, color=(255, 0, 0), center=(point[0] * scale + width / 2, point[1] * scale + width / 2), radius=3)
    turn_text = font.render(str(turn), True, (255, 255, 255))
    w.blit(turn_text, (0, 0))

    pygame.display.update()
    time.sleep(1/60)