import pygame

pygame.init()
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # X and Y

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))
robot_width = robot.get_width()
robot_height = robot.get_height()


def robot_row(amount: int):
    for i in range(10):
        for j in range(amount):
            # x = 75 + robot_width * i
            x = (40 + robot_width * i) + 8 * j
            y = 100 + (robot_height // 4) * j
            window.blit(robot, (x, y))


robot_row(10)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
