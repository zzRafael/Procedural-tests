import pygame
from pygame.locals import *
import math

from game_objects import Player, Planet, Line

def render(screen, game):
    screen.fill((0, 0, 0))

    for planet in game.planets:
        pygame.draw.circle(screen, (255, 255, 255), planet.pos, planet.size)

    for line in game.lines:
        pygame.draw.line(screen, line.color, line.start, line.end, 1)

    pygame.draw.circle(screen, (0, 0, 255), game.player.pos, game.player.size)