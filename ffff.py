import pygame
pygame.iniy()

W = 500
H = 500


sc = pygame.display.set_mode((W, H))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()