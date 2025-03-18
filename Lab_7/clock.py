import pygame, datetime

pygame.init()

w = 800
h = 600
c = (w // 2, h // 2)

COLOR_WHITE = (255, 255, 255)

screen = pygame.display.set_mode((w, h))

running = True

image = pygame.image.load('clock.png').convert_alpha()
image_min = pygame.image.load('min_hand.png').convert_alpha()
image_sec = pygame.image.load('sec_hand.png').convert_alpha()

image_rect = image.get_rect(center = (w // 2, h // 2))

clock = pygame.time.Clock()

angle_sec = 0
angle_min = 0

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(COLOR_WHITE)

    current = datetime.datetime.now() 
    angle_sec = current.second * 6
    angle_min = current.minute * 6 + current.second * 0.1

    rotated_min = pygame.transform.rotate(image_min, -angle_min - 51.5)
    rotated_min_rect = rotated_min.get_rect(center = c)

    rotated_sec = pygame.transform.rotate(image_sec, -angle_sec + 51.5)
    rotated_sec_rect = rotated_sec.get_rect(center = c)

    screen.blit(image, image_rect)
    screen.blit(rotated_min, rotated_min_rect)
    screen.blit(rotated_sec, rotated_sec_rect)

    pygame.display.flip()
    clock.tick(60)