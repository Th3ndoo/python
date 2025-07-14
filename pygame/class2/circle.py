import pygame
pygame.init()


screen = pygame.display.set_mode((400,400))
pygame.draw.circle(screen,'cyan',(300,200),50,3)
pygame.draw.circle(screen,'teal',(100,200),50)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
        pygame.display.flip()