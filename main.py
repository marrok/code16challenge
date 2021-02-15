import pygame
import random
pygame.init()
display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('#Code16Challenge')
state = [pygame.time.Clock(), [800 / 2, 600 / 2], [0, 0], 0, [round(random.randrange(0, 800 - 10) / 10) * 10, round(random.randrange(0, 600 - 10) / 10) * 10]]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: quit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT: state[2] = [-10, 0]
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT: state[2] = [10, 0]
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP: state[2] = [0, -10]
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN: state[2] = [0, 10]
    state[1] = [state[1][0] + state[2][0], state[1][1] + state[2][1]]
    if not (0 < state[1][0] < 800 and 0 < state[1][1] < 600): quit()
    if state[1][0] == state[4][0] and state[1][1] == state[4][1]: state[3:4] = [state[3] + 1, [round(random.randrange(0, 800 - 10) / 10) * 10.0, round(random.randrange(0, 600 - 10) / 10) * 10.0]]
    display.fill((255, 255, 255))
    display.blit(pygame.font.SysFont(None, 50).render("Score: " + str(state[3]), True, (255, 255, 102)), [0, 0])
    pygame.draw.rect(display, (0, 0, 0), [state[1][0], state[1][1], 10, 10])
    pygame.draw.rect(display, (0, 255, 0), [state[4][0], state[4][1], 10, 10])
    pygame.display.update()
    state[0].tick(10)
