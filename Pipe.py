import random
import pygame


class Pipe:
    swidth = 0
    sheight = 0
    pwidth = 50
    x = 0
    gap = 150
    bottom_y = 0
    speed = -2

    def __init__(self, width, height):
        self.swidth = width
        self.sheight = height
        self.x = self.swidth + self.pwidth
        self.bottom_y = random.randrange(self.gap + 50, self.sheight)

    def update(self):
        self.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, pygame.Color(
            "green"), (self.x, self.bottom_y, self.pwidth, self.sheight))
        pygame.draw.rect(screen, pygame.Color("green"),
                         (self.x, 0, self.pwidth, self.bottom_y - self.gap))
