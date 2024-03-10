import pygame
from pygame.locals import *
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 864
screen_height = 768

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Get to the top")

movement_speed = 0


#load images
background = pygame.image.load('img/bg.png')
char_img = pygame.image.load("img/bird1.png")


run = True
while run:

    clock.tick(fps)

    #draw background
    screen.blit(background, (0,0))

    pygame.draw.rect(screen, (100, 100, 100), (100, 100, 50, 50))

    #char_rect = char_img.get_rect()
    #char_rect.center = (screen_width // 2, screen_height // 2)
    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_LEFT]:
    #    char_rect.x -= movement_speed
    #if keys[pygame.K_RIGHT]:
    #    char_rect.x += movement_speed


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()