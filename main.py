import pygame
from pygame.constants import DOUBLEBUF
from Bird import Bird
from Pipe import Pipe
pygame.init()

myimage = pygame.image.load("Assets/background5.png")
myimage = pygame.transform.scale(myimage, (512, 512))
print(myimage.get_size())
FPS = 60
width, height = 512, 512
screen = pygame.display.set_mode((width, height))
player = Bird(width, height)
clock = pygame.time.Clock()
pipes = []
pipes.append(Pipe(width, height))
count = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.yVel = -6
    screen.blit(myimage, [0, 0])
    player.draw(screen)
    player.update()
    if count == FPS * 2:
        pipes.append(Pipe(width, height))
        count = 0
    count += 1
    for pipe in pipes:
        pipe.draw(screen)
        pipe.update()
        if pipe.x + pipe.pwidth < 0:
            pipes.remove(pipe)
    pygame.display.update()
    clock.tick(FPS)
