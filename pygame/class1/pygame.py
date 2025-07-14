# pygame window
import pygame

pygame.init()
font = pygame.font.Font(None,36)
screen = pygame.display.set_mode((400,500))
pygame.display.set_caption("A pygae window")
screen.fill("purple")

backround = pygame.image.load("grave.jpg").convert()
surface = pygame.transform.scale(backround,(400,500))
image1 = pygame.image.load("cross.jpg").convert()
image1_surf = pygame.transform.scale(image1,(200,200))

text_surf = font.render("#1*",True,'Black')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(surface,(0,0))
    screen.blit(image1_surf,(100,100))
    screen.blit(text_surf,(100,300))
    pygame.display.flip()