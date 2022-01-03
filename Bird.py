import pygame


class Bird:
    x = 100
    y = 0
    yVel = 2
    screenH = 0
    screenW = 0
    radius = 25

    def __init__(self, width, height):
        self.screenH = height
        self.width = width

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color(
            "yellow"), (self.x, self.y), self.radius)

    def update(self):
        if self.yVel < 3:
            self.yVel += 0.3
        if self.yVel > 3:
            self.yVel = 3
        self.y += self.yVel
        if self.y + self.radius > self.screenH:
            self.y = self.screenH - self.radius
