import pygame
from GameModules.image_system import *

pygame.init()
screen = pygame.display.set_mode((1100, 900)) #1100, 900

my_image = load_image("assets/images/kyon_main.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))

    if my_image:
        screen.blit(my_image, (400,250))

    pygame.display.update()

pygame.quit()
