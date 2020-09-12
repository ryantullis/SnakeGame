import pygame
pygame.init()
(length, width) = (1280, 720)
dis = pygame.display.set_mode((length, width))
pygame.display.update()
pygame.display.set_caption('Snake Game by Ryan Tullis')
gameOver = False
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True



pygame.quit()
