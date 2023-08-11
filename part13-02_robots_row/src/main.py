import pygame

pygame.init()
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # X and Y

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))
robot_width = robot.get_width()
robot_height = robot.get_height()


def robot_row():
    for i in range(10):
        window.blit(robot, (45 + i * robot_width, (WINDOW_HEIGHT // 2) - robot_height))


robot_row()
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
