import pygame
import random

pygame.init()
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # X and Y

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))
robot_width = robot.get_width()
robot_height = robot.get_height()


def robot_row(amount: int):
    for i in range(amount):
        x = random.randint(0, WINDOW_WIDTH)
        y = random.randint(0, WINDOW_HEIGHT)
        window.blit(robot, (x, y))


robot_row(1000)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
