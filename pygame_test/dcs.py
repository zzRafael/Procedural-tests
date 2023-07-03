import pygame
from pygame.locals import*
from sys import exit
import random

pygame.init()

width = 1300
height = 700
window = pygame.display.set_mode((width,height))
pygame.display.set_caption('Game')

class Vector:
    def __init__(self, speed = 10, xpos = 0, ypos = 0):
        self.xpos = xpos
        self.ypos = ypos
        self.speed = speed

    def move(self):
        #vector
        if pygame.key.get_pressed()[K_LEFT]:
            vector.xpos += vector.speed
        if pygame.key.get_pressed()[K_RIGHT]:
            vector.xpos -= vector.speed
        if pygame.key.get_pressed()[K_UP]:
            vector.ypos += vector.speed
        if pygame.key.get_pressed()[K_DOWN]:
            vector.ypos -= vector.speed

class RectObj:
    def __init__(self, xpos = 100, ypos = 100, speed = 10, color = (255,0,0), width = 10, height = 10, border = 2):
        self.xpos = xpos + vector.xpos
        self.ypos = ypos + vector.ypos
        self.speed = speed
        self.color = color
        self.width = width
        self.height = height
        self.border = border
        #player
        self.default_player_speed = speed
    
    def move(self):
        # player move
        if pygame.key.get_pressed()[K_w]:
            self.ypos -= self.speed
            vector.ypos += self.speed
        if pygame.key.get_pressed()[K_s]:
            self.ypos += self.speed
            vector.ypos -= self.speed
        if pygame.key.get_pressed()[K_a]:
            self.xpos -= self.speed
            vector.xpos += self.speed
        if pygame.key.get_pressed()[K_d]:
            self.xpos += self.speed
            vector.xpos -= self.speed
        #speed control
        if pygame.key.get_pressed()[K_q]:
            if self.speed >= 0:
                self.speed += self.default_player_speed
        if pygame.key.get_pressed()[K_e]:
            if self.speed > 0:
                self.speed -= self.default_player_speed
        if pygame.key.get_pressed()[K_r]:
                self.speed = self.default_player_speed

    def draw(self):
        pygame.draw.rect(window, self.color, pygame.Rect(self.xpos+vector.xpos, self.ypos+vector.ypos, self.width, self.height))
    def drawBorder(self):
        pygame.draw.rect(window, self.color, pygame.Rect(self.xpos+vector.xpos, self.ypos+vector.ypos, self.width, self.height), self.border)

class Chunk():
    def __init__(self, star_amount = 10, star_size = 2,seed = 123, star_color = (255,255,255),border_color = (255,255,0), chunk_pixel_size = 1000, border = 2, xpos = 0, ypos = 0):
        self.xpos = xpos + vector.xpos
        self.ypos = ypos + vector.ypos
        self.border_color = border_color
        self.star_color = star_color
        self.chunk_pixel_size = chunk_pixel_size
        self.width = self.chunk_pixel_size
        self.height = self.chunk_pixel_size
        self.border = border
        self.seed = seed
        self.star_amount = star_amount
        self.star_size = star_size
        self.star_width = star_size
        self.star_height = star_size

    def get_coordenate(self,obj):
        current_pixel_coordenate = [obj.xpos, obj.ypos]
        chunk_xcoordenate = (current_pixel_coordenate[0] // self.chunk_pixel_size)
        chunk_ycoordenate = (current_pixel_coordenate[1] // self.chunk_pixel_size)
        current_chunk_coordenate = [[chunk_xcoordenate,chunk_ycoordenate]]
        #print(f' Chunk Coordenate: {current_chunk_coordenate}')
        #print(f'Coordenate : {current_chunk_coordenate}    Pixel : {current_pixel_coordenate}')
        return current_chunk_coordenate

    def drawBorder(self, coordenate):
        # peferível que seja a coordenada do get_coordenate(obj):
        xpos = coordenate[0][0] * self.chunk_pixel_size
        ypos = coordenate[0][1] * self.chunk_pixel_size
        pygame.draw.rect(window, self.border_color, pygame.Rect((xpos + vector.xpos) - self.chunk_pixel_size, (ypos + vector.ypos) - self.chunk_pixel_size, self.width, self.height), self.border)
        pygame.draw.rect(window, self.border_color, pygame.Rect(xpos + vector.xpos, ypos + vector.ypos, self.width, self.height), self.border)
        pygame.draw.rect(window, self.border_color, pygame.Rect((xpos + vector.xpos) + self.chunk_pixel_size, ypos + vector.ypos, self.width, self.height), self.border)
        pygame.draw.rect(window, self.border_color, pygame.Rect((xpos + vector.xpos) - self.chunk_pixel_size, ypos + vector.ypos, self.width, self.height), self.border)
        pygame.draw.rect(window, self.border_color, pygame.Rect(xpos + vector.xpos, (ypos + vector.ypos) + self.chunk_pixel_size, self.width, self.height), self.border)
        pygame.draw.rect(window, self.border_color, pygame.Rect(xpos + vector.xpos, (ypos + vector.ypos) - self.chunk_pixel_size, self.width, self.height), self.border)
        pygame.draw.rect(window, self.border_color, pygame.Rect((xpos + vector.xpos) + self.chunk_pixel_size, (ypos + vector.ypos) - self.chunk_pixel_size, self.width, self.height), self.border)
        pygame.draw.rect(window, self.border_color, pygame.Rect((xpos + vector.xpos) + self.chunk_pixel_size, (ypos + vector.ypos) + self.chunk_pixel_size, self.width, self.height), self.border)
        pygame.draw.rect(window, self.border_color, pygame.Rect((xpos + vector.xpos) - self.chunk_pixel_size, (ypos + vector.ypos) + self.chunk_pixel_size, self.width, self.height), self.border)

    def generateStars(self, coordenate):
        xpos = coordenate[0][0] * self.chunk_pixel_size
        ypos = coordenate[0][1] * self.chunk_pixel_size

        chunks = [
            [f'{xpos-1}{ypos-1}', xpos-self.chunk_pixel_size, ypos-self.chunk_pixel_size, ],
            [f'{xpos}{ypos-1}', xpos, ypos-self.chunk_pixel_size],
            [f'{xpos+1}{ypos-1}', xpos+self.chunk_pixel_size, ypos-self.chunk_pixel_size],
            [f'{xpos-1}{ypos}', xpos-self.chunk_pixel_size, ypos],
            [f'{xpos}{ypos}', xpos, ypos],
            [f'{xpos+1}{ypos}', xpos+self.chunk_pixel_size, ypos],
            [f'{xpos-1}{ypos+1}', xpos-self.chunk_pixel_size, ypos+self.chunk_pixel_size],
            [f'{xpos}{ypos+1}', xpos, ypos+self.chunk_pixel_size],
            [f'{xpos+1}{ypos+1}', xpos+self.chunk_pixel_size, ypos+self.chunk_pixel_size],
        ]

        #1VVVVVVV
        coordenate1 = [coordenate[0][0]-1, coordenate[0][1]-1]
        seed = f'{coordenate1}{self.seed}'
        random.seed(seed)
        for i in range (self.star_amount):
            star_size = random.randint(5,10)
            window.blit(marte_img, pygame.Rect(random.randint(chunks[0][1], chunks[0][1]+self.chunk_pixel_size)+vector.xpos, random.randint(chunks[0][2], chunks[0][2]+self.chunk_pixel_size)+vector.ypos, star_size, star_size))
 
        #2VVVVVVV
        coordenate2 = [coordenate[0][0], coordenate[0][1]-1]
        seed = f'{coordenate2}{self.seed}'
        random.seed(seed)
        for i in range (self.star_amount):
            star_size = random.randint(5,10)
            window.blit(marte_img, pygame.Rect(random.randint(chunks[1][1], chunks[1][1]+self.chunk_pixel_size)+vector.xpos, random.randint(chunks[1][2], chunks[1][2]+self.chunk_pixel_size)+vector.ypos, star_size, star_size))

        #3VVVVVVV
        coordenate1 = [coordenate[0][0]+1, coordenate[0][1]-1]
        seed = f'{coordenate1}{self.seed}'
        random.seed(seed)
        for i in range (self.star_amount):
            star_size = random.randint(5,10)
            window.blit(marte_img, pygame.Rect(random.randint(chunks[2][1], chunks[2][1]+self.chunk_pixel_size)+vector.xpos, random.randint(chunks[2][2], chunks[2][2]+self.chunk_pixel_size)+vector.ypos, star_size, star_size))

        #4VVVVVVV
        coordenate1 = [coordenate[0][0]-1, coordenate[0][1]]
        seed = f'{coordenate1}{self.seed}'
        random.seed(seed)
        for i in range (self.star_amount):
            star_size = random.randint(5,10)
            window.blit(marte_img, pygame.Rect(random.randint(chunks[3][1], chunks[3][1]+self.chunk_pixel_size)+vector.xpos, random.randint(chunks[3][2], chunks[3][2]+self.chunk_pixel_size)+vector.ypos, star_size, star_size))

        #5VVVVVVV
        coordenate1 = [coordenate[0][0], coordenate[0][1]]
        seed = f'{coordenate1}{self.seed}'
        random.seed(seed)
        for i in range (self.star_amount):
            star_size = random.randint(5,10)
            window.blit(marte_img, pygame.Rect(random.randint(chunks[4][1], chunks[4][1]+self.chunk_pixel_size)+vector.xpos, random.randint(chunks[4][2], chunks[4][2]+self.chunk_pixel_size)+vector.ypos, star_size, star_size))

        #6VVVVVVV
        coordenate1 = [coordenate[0][0]+1, coordenate[0][1]]
        seed = f'{coordenate1}{self.seed}'
        random.seed(seed)
        for i in range (self.star_amount):
            star_size = random.randint(5,10)
            window.blit(marte_img, pygame.Rect(random.randint(chunks[5][1], chunks[5][1]+self.chunk_pixel_size)+vector.xpos, random.randint(chunks[5][2], chunks[5][2]+self.chunk_pixel_size)+vector.ypos, star_size, star_size))

        #7VVVVVVV
        coordenate1 = [coordenate[0][0]-1, coordenate[0][1]+1]
        seed = f'{coordenate1}{self.seed}'
        random.seed(seed)
        for i in range (self.star_amount):
            star_size = random.randint(5,10)
            window.blit(marte_img, pygame.Rect(random.randint(chunks[6][1], chunks[6][1]+self.chunk_pixel_size)+vector.xpos, random.randint(chunks[6][2], chunks[6][2]+self.chunk_pixel_size)+vector.ypos, star_size, star_size))

        #8VVVVVVV
        coordenate1 = [coordenate[0][0], coordenate[0][1]+1]
        seed = f'{coordenate1}{self.seed}'
        random.seed(seed)
        for i in range (self.star_amount):
            star_size = random.randint(5,10)
            window.blit(marte_img, pygame.Rect(random.randint(chunks[7][1], chunks[7][1]+self.chunk_pixel_size)+vector.xpos, random.randint(chunks[7][2], chunks[7][2]+self.chunk_pixel_size)+vector.ypos, star_size, star_size))

        #9VVVVVVV
        coordenate1 = [coordenate[0][0]+1, coordenate[0][1]+1]
        seed = f'{coordenate1}{self.seed}'
        random.seed(seed)
        for i in range (self.star_amount):
            star_size = random.randint(5,10)
            window.blit(marte_img, pygame.Rect(random.randint(chunks[8][1], chunks[8][1]+self.chunk_pixel_size)+vector.xpos, random.randint(chunks[8][2], chunks[8][2]+self.chunk_pixel_size)+vector.ypos, star_size, star_size))

class Info:
    def __init__(self):
        self.font = 'arial'
        self.font_size = 10
        self.color = (0,255,0)
        self.bold = False
        self.italic = False
        self.antialias = False
        self.pos = (0,0)
        self.font = pygame.font.SysFont(self.font, self.font_size, self.bold, self.italic)
    def showInfo(self):
        infos = [
            f'COORDENATE_X: {current_chunk.get_coordenate(player1)[0][0]}',
            f'COORDENATE_Y: {current_chunk.get_coordenate(player1)[0][1]}',
            f'FPS: {round(clock.get_fps())}',
            f'PLAYER_SPEED: {player1.speed}',
            f'VECTOR_SPEED: {vector.speed}',
            f'STAR_AMOUNT: {current_chunk.star_amount}',
            f'TOTAL_STAR_AMOUNT: {current_chunk.star_amount * 9}',
            f'CHUNK_SIZE: {current_chunk.chunk_pixel_size}',
            f'CHUNK_SEED: {current_chunk.seed}',
            f'BORDER: {border}',
            f'FULLSCREEN: {fullscreen}'
        ]
        self.counter = 0
        for info in infos:
            self.info = infos[self.counter]
            info_formated = self.font.render(self.info, self.antialias, self.color)
            window.blit(info_formated, (self.pos[0], self.pos[1]+(self.counter*10)))
            self.counter += 1


marte_img = pygame.image.load("./images/marte.png").convert_alpha()
marte_width = marte_img.get_rect().width
marte_height = marte_img.get_rect().height
multiple = 0.3
marte_img = pygame.transform.scale(marte_img, (marte_width*multiple, marte_height*multiple))

#random
# vector
vector = Vector(speed = 10)
# Objects
player1 = RectObj(speed = 1, height=2, width =2, ypos=height//2, xpos=width//2)
testplanet = RectObj(color = (0,255,0), xpos=0, ypos=0)
current_chunk = Chunk(star_amount=1, chunk_pixel_size=1000)
info = Info()
border = False
fullscreen = False

# main loop
clock = pygame.time.Clock()
while True:
    clock.tick(100)
    window.fill((0,0,10))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()
    
    vector.move()
    player1.move()

    # drawing border of chunk

    # drawing objects
    current_chunk.generateStars(current_chunk.get_coordenate(player1))
    if border == True:
        current_chunk.drawBorder(current_chunk.get_coordenate(player1))
    testplanet.draw()
    player1.draw()

    #star amount and border controls
    if pygame.key.get_pressed()[K_1]:
        current_chunk.star_amount += 1
    if pygame.key.get_pressed()[K_2]:
        current_chunk.star_amount -= 1
    if pygame.key.get_pressed()[K_b]:
        border = True
    if pygame.key.get_pressed()[K_n]:
        border = False
    #full screen
    if pygame.key.get_pressed()[K_f]:
        if fullscreen == False:
            window = pygame.display.set_mode((window.get_width(), window.get_height()), pygame.FULLSCREEN)
            fullscreen = True
        else:
            window = pygame.display.set_mode((width,height))
            fullscreen = False
        
    #show debugging infos
    info.showInfo()
    # update screen
    pygame.display.update()