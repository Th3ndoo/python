import pygame
color = 'black'
surface_color = 'red'
movement_speed = 5
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 40)
class mysprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(surface_color)
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
        self.rect = self.image.get_rect()
    def move(self, x_change, y_change):
        self.rect.x = max(min(self.rect.x + x_change, 500 - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, 400 - self.rect.height), 0)
pygame.init()
screen =  pygame.display.set_mode((500,400))
pygame.display.set_caption("collision detection")

as1 = pygame.sprite.Group()
sp1 = mysprite(color,20,30)
sp1.rect.x = 00
sp1.rect.y =  150
color = 'purple'
as2 = pygame.sprite.Group()
sp2 = mysprite(color,20,30)
sp2.rect.x = 00
sp2.rect.y =  50

as1.add(sp1,sp2)

clock = pygame.time.Clock()
exit = True
while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
    key = pygame.key.get_pressed()
    x_change = (key[pygame.K_RIGHT] - key[pygame.K_LEFT]) * movement_speed
    y_change = (key[pygame.K_DOWN] - key[pygame.K_UP]) * movement_speed
    sp2.move(x_change, y_change)
    screen.fill(surface_color)
    as1.draw(screen)
    if sp2.rect.colliderect(sp1.rect):
        as1.remove(sp1)
        as1.remove(sp2)
        win_text = font.render("You win!", True, 'green')
        screen.blit(win_text,(100,100))



    pygame.display.flip()
    clock.tick(120)

pygame.quit()  