#Imports
import pygame, sys
from pygame.locals import *
import random, time

#Инициализация
pygame.init()

#Настройка кадров в секунду
FPS = 60
FramePerSec = pygame.time.Clock()

#Создание цветов
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Другие переменные для использования в программе
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
POINT = 0
#Настройка шрифтов
font = pygame.font.SysFont("Verdana", 60) 
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load(r'AnimatedStreet.png') #загружаем фон

#Создание белого экрана
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Racer")

coin_sound = pygame.mixer.Sound("coin.wav")  # звук монеты

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r'Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE 
        self.rect.move_ip(0, SPEED)   # Двигает врага вниз
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Monet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r'Monet.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

    def move(self):
        global POINT
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    def reset(self): #когда монету собирает игрок
        self.rect.top = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r'Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0) 
        if self.rect.top > 0 and pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if self.rect.bottom < SCREEN_HEIGHT and pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
                  

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
M1 = Monet()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
enemies.add(E1)
coins.add(M1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(M1)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Game Loop
while True:
    
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK) #
    points = font_small.render(str(POINT), True, RED) #
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(points, (380,10))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect) 
    
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies): # если элементы P1 и Enemies сталкиваются 
          pygame.mixer.Sound(r'lab8_materials_crash.wav').play() 
          time.sleep(1)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250)) #игра заканчивается
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() #удаляет спрайт из всех групп, в которых он состоит
          time.sleep(1)
          pygame.quit()
          sys.exit()  

    if pygame.sprite.spritecollideany(E1, coins) :
        all_sprites.sprites()[2].reset()
        
    if pygame.sprite.spritecollideany(P1, coins):  
        coin_sound.play()  # Воспроизводим звук
        POINT += 1

    pygame.display.update()
    FramePerSec.tick(FPS)