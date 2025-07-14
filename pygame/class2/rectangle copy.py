import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Key Detection")
screen.fill('red')
done = False
x = 200
y = 200
color = 'cyan'
while not done:
    screen.fill('red')
    pygame.draw.rect(screen,color,pygame.Rect(x,y,70,68))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_LEFT]:
            x -=5
        if key_input[pygame.K_RIGHT]:
            x +=5
        if key_input[pygame.K_UP]:
            y -=5
        if key_input[pygame.K_DOWN]:
            y +=5
        x = min(max(0,x),500-30)
        y = min(max(0,y),500-30)
        if x == 0:
            color = 'blue'
        if y == 0:
            color = 'pink'
        pygame.display.flip()