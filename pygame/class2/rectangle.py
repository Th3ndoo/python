import pygame
pygame.init()

screen = pygame.display.set_mode((400,300))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        pygame.draw.rect(screen,'red',pygame.Rect(30,30,100,60))
        pygame.display.flip()