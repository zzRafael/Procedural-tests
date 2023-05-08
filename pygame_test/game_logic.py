# game_logic.py

import random
import math
from game_objects import Player, Planet, Line

class Game:
    def __init__(self, num_planets):
        self.player = Player()
        self.planets = []
        self.lines = []

        for i in range(num_planets):
            x = random.randint(-4000, 4000)
            y = random.randint(-4000, 4000)
            self.planets.append(Planet(x, y))

    def update(self):
        self.player.update()

        for planet in self.planets:
            distance = math.dist(self.player.pos, planet.pos)
            self.lines.append(Line(planet.pos, self.player.pos, (255, 255, 0)))
            self.lines.append(Line((planet.x, self.player.y), planet.pos, (0, 255, 0)))
            self.lines.append(Line((self.player.x, planet.y), self.player.pos, (255, 0, 200)))

    def get_elements(self):
        return [self.player] + self.planets
                 