import pygame

pygame.init()

w = 500
h = 500
x = 200
y = 200

sc = pygame.display.set_mode((w, h))
fps = pygame.time.Clock()

def draw():
    sc.fill((55, 155, 255))
    pygame.draw.circle(sc,((20, 20 ,20)), (x, y), 20)
    pygame.display.update()

def mowe():
    global x
    x += 1
    if x == 650:
        x = 50

while True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            exit()

    draw()
    mowe()
    fps.tick(60)