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
velocity = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    y += velocity
    if velocity > 0 and y + robot.get_height() >= WINDOW_HEIGHT:
        velocity = -velocity
    if velocity < 0 and y <= 0:
        velocity = -velocity

    dt.tick(60)
