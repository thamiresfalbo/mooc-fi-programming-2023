from shutil import move
import pygame

pygame.init()
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # X and Y

robot = pygame.image.load("robot.png")


robot_width = robot.get_width()
robot_height = robot.get_height()
dt = pygame.time.Clock()
x = 0
y = 0
x_velocity = 1
y_velocity = 0
direction = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    x += x_velocity
    y += y_velocity

    if x_velocity > 0 and x + robot.get_width() >= WINDOW_WIDTH:
        x_velocity = 0
        y_velocity = 1
    if y_velocity > 0 and y + robot.get_height() >= WINDOW_HEIGHT:
        y_velocity = 0
        x_velocity = 1
        x_velocity = -x_velocity
    if x_velocity < 0 and x <= 0:
        y_velocity = 1
        x_velocity = 0
        y_velocity = -y_velocity
    if y_velocity < 0 and y <= 0:
        y_velocity = 0
        x_velocity = 1

    dt.tick(60)
