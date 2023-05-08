#importando o que precisa
import pygame
from pygame.locals import *
import random
from random import randint

random.seed(123)

#criando as classes
class Tela():
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Player():
    def __init__(self,  color = (255,0,0),xpos = 100, ypos = 100, radius = 2):
        self.xpos = xpos
        self.ypos = ypos
        self.center = (xpos, ypos)
        self.radius = radius
        self.color = color

class Planet():
    def __init__(self,  color = (0,0,255),xpos = 500, ypos = 250, radius = 2):
        self.xpos = xpos + vectorx
        self.ypos = ypos + vectory
        self.center = (xpos, ypos)
        self.radius = radius
        self.color = color

class Line():
    def __init__(self, start_pos, end_pos, color, width=1):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.color = color
        self.width = width

def get_distance(object_1, object_2):
    #definindo catetos:
    cat_adjacente = object_2.xpos - object_1.xpos
    cat_oposto = object_1.ypos - object_2.ypos
    print(f'Cateto oposto: {cat_oposto}')
    print(f'Cateto adjacente: {cat_adjacente}')
    #definindo a hipotenusa:
    hipotenusa = (cat_oposto**2 + cat_adjacente**2) ** (1/2)
    distance = hipotenusa
    return distance

def createPlanets(planets_number,surface):
    border = 10
    planets_xyloc = []
    for i in range(planets_number):
        num_xloc = randint(-40000,40000-border)
        num_yloc = randint(-40000,40000-border)
        num_xyloc = (num_xloc,num_yloc)
        planets_xyloc.append(num_xyloc)
    return planets_xyloc

#declrando a tela
tela = Tela(1300,700)
window = pygame.display.set_mode((tela.width, tela.height))

#definindo relogio
clock = pygame.time.Clock()

#chamando a função createPlanets() para criar os outros planetas
other_planets = createPlanets(5000,tela)

#vector
vectorx = 0
vectory = 0
speed = 5

#loop principal
while True:
    #fps
    clock.tick(60)
    #pintando a tela de preto para ser desenhada novamente
    window.fill((0,0,0))
    #se apertar para fechar, o prgrama vai fechar
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    #posição do mouse
    (mouse_xpos, mouse_ypos) = pygame.mouse.get_pos()
    mouse_pos = (mouse_xpos, mouse_ypos)

    ##########criando os elementos
    planet = Planet()
    player = Player(xpos=mouse_xpos, ypos=mouse_ypos)
    #linhas
    hipotenusa = Line(start_pos=(planet.center[0], planet.center[1]), end_pos=(player.center[0], player.center[1]), color=(255,255,0))
    cat_adjacente = Line(start_pos=(planet.center[0], planet.center[1]), end_pos=(player.center[0], planet.center[1]), color=(0,255,0))
    cat_oposto = Line(start_pos=(player.center[0], planet.center[1]), end_pos=(player.center[0], player.center[1]), color=(255,0,200))

    #controlando a camera
    #vector
    if pygame.key.get_pressed()[K_LEFT]:
        vectorx += speed
    if pygame.key.get_pressed()[K_RIGHT]:
        vectorx -= speed
    if pygame.key.get_pressed()[K_UP]:
        vectory += speed
    if pygame.key.get_pressed()[K_DOWN]:
        vectory -= speed

    # movimentação do planeta ou player
    if pygame.key.get_pressed()[K_w]:
        planet.ypos -= speed
    if pygame.key.get_pressed()[K_s]:
        planet.ypos += speed
    if pygame.key.get_pressed()[K_a]:
        planet.xpos -= speed
    if pygame.key.get_pressed()[K_d]:
        planet.xpos += speed

    #desenhado os elementos na tela
        #outros planetas
    counter = 0
    for i in other_planets:
        pygame.draw.rect(window, (255,255,255), (other_planets[counter][0]+vectorx,other_planets[counter][1]+vectory, 50,50))   
        counter += 1
    #planetpg = pygame.draw.circle(surface=window, center=(planet.center), radius=planet.radius, color=planet.color)
    planetpg = pygame.draw.circle(surface=window, color=(255,0,0), center=(planet.xpos+vectorx,planet.ypos+vectory), radius=planet.radius)
    playerpg = pygame.draw.circle(surface=window, center=(player.center), radius=player.radius, color=player.color)
    #hipo_line = pygame.draw.line(surface=window, start_pos=(hipotenusa.start_pos), end_pos=(hipotenusa.end_pos), color=hipotenusa.color, width = hipotenusa.width)
    #cat_adjacente_line = pygame.draw.line(surface=window, start_pos=(cat_adjacente.start_pos), end_pos=(cat_adjacente.end_pos), color=cat_adjacente.color, width = cat_adjacente.width)
    #cat_oposto_line = pygame.draw.line(surface=window, start_pos=(cat_oposto.start_pos), end_pos=(cat_oposto.end_pos), color=cat_oposto.color, width = cat_oposto.width)
    ##########

    #Mostrando a distancia entre o player e o planeta
    distance = get_distance(planet,player)


    #fazendo update da tela
    pygame.display.flip()