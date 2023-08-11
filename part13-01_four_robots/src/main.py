import pygame

pygame.init()
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # X and Y

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))
robot_width = robot.get_width()
robot_height = robot.get_height()

# Top left
window.blit(robot, (0, 0))
# Top right
window.blit(robot, (WINDOW_WIDTH - robot_width, 0))
# Bottom left
window.blit(robot, (0, WINDOW_HEIGHT - robot_height))
# Bottom right
window.blit(robot, (WINDOW_WIDTH - robot_width, WINDOW_HEIGHT - robot_height))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
