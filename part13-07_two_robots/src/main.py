# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # X and Y

robot = pygame.image.load("robot.png")


robot_width = robot.get_width()
robot_height = robot.get_height()
dt = pygame.time.Clock()
robot_a_x = 0
robot_b_x = 0

robot_a_y = robot.get_height() // 2
robot_b_y = robot.get_height() * 1.5

robot_a_velocity = 1
robot_b_velocity = 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (robot_a_x, robot_a_y))
    window.blit(robot, (robot_b_x, robot_b_y))
    pygame.display.flip()

    robot_a_x += robot_a_velocity
    robot_b_x += robot_b_velocity
    if robot_b_velocity > 0 and robot_b_x + robot.get_width() >= WINDOW_WIDTH:
        robot_b_velocity = -robot_b_velocity
    if robot_b_velocity < 0 and robot_b_x <= 0:
        robot_b_velocity = -robot_b_velocity

    if robot_a_velocity > 0 and robot_a_x + robot.get_width() >= WINDOW_WIDTH:
        robot_a_velocity = -robot_a_velocity
    if robot_a_velocity < 0 and robot_a_x <= 0:
        robot_a_velocity = -robot_a_velocity

    dt.tick(60)
