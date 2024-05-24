import pygame
import random

# Class Snake
class Snake:
    def __init__(self):
        self.elements = [[100, 50]]
        self.radius = 10
        self.dx = 5
        self.dy = 0
        self.size = 1

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, black, element, self.radius)

    def move(self):
        head = list(self.elements[0])
        head[0] += self.dx
        head[1] += self.dy
        self.elements.insert(0, head)

        if len(self.elements) > self.size:
            self.elements.pop()

    def eat(self):
        self.size += 1

# Class Food
class Food:
    def __init__(self):
        self.x = random.randint(0, screen_width - self.radius)
        self.y = random.randint(0, screen_height - self.radius)
        self.radius = 10

    def draw(self):
        pygame.draw.circle(screen, red, (self.x, self.y), self.radius)

# Function to check collision
def is_collision(x1, y1, x2, y2, bsize):
    if x2-5 <= x1 <= x2+bsize+5 and y2-5 <= y1 <= y2+bsize+5:
        return True
    return False

# Function to handle game over
def game_over():
    font = pygame.font.SysFont(None, 100)
    text = font.render('Game Over', True, red)