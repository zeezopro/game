import pygame
pygame.init()
window = pygame.display.set_mode((700, 500))

pygame.display.set_caption("zezo")

x = 100
y = 200
height = 50
width = 50

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)



while True:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    pygame.draw.rect(window, BLUE, (x, y, width, height))
    pygame.display.update()