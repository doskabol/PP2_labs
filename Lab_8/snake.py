import pygame
import time
import random
import sys

snake_speed = 10

window_x, window_y = 400, 400

black, white, red, green, blue, yellow, cyan = (0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255)
background_colors = [black, blue, yellow, cyan]
current_bg_color = black

pygame.init()

pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()

snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

def generate_food():
    while True:
        position = [random.randrange(1, window_x // 10) * 10, random.randrange(1, window_y // 10) * 10]
        if position not in snake_body:
            return position

fruit_position = generate_food()
fruit_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0
level = 1

def show_score_and_level(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(f'Score: {score}', True, color)
    level_surface = score_font.render(f'Level: {level}', True, color)
    game_window.blit(score_surface, score_surface.get_rect(topleft=(10, 10)))
    game_window.blit(level_surface, level_surface.get_rect(topright=(window_x - 10, 10)))

def game_over():
    font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = font.render(f'Your Score: {score}', True, red)
    game_over_rect = game_over_surface.get_rect(center=(window_x/2, window_y/4))
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

def check_wall_collision(): 
    if snake_position[0] < 0 or snake_position[0] >= window_x or snake_position[1] < 0 or snake_position[1] >= window_y:
        game_over()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    elif change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    elif change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    elif change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_position[1] -= 10
    elif direction == 'DOWN':
        snake_position[1] += 10
    elif direction == 'LEFT':
        snake_position[0] -= 10
    elif direction == 'RIGHT':
        snake_position[0] += 10


    check_wall_collision()

    snake_body.insert(0, list(snake_position))
    if snake_position == fruit_position: #если змейка ест еду
        score += 10
        fruit_spawn = False #еда пропадает
        
        if score % 50 == 0: #если счет кратен на 50
            snake_speed += 2 #
            current_bg_color = background_colors[(score // 50) % len(background_colors)] #
            level += 1 #
        if score < 50:
            snake_body.append(snake_body[-1]) #при каждом поедании еды растет на 1
        else:
            for _ in range(random.randint(2, 3)):
                snake_body.append(snake_body[-1]) #после 50 растет на 2 или 3 рандомно
    else:
        snake_body.pop() #по сути ниче не меняет, но змейка росла бы с каждым кадром 

    if not fruit_spawn: #заново генерирует еду
        fruit_position = generate_food()
    fruit_spawn = True

    game_window.fill(current_bg_color)
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    if any(block == snake_position for block in snake_body[1:]): #столкновение с телом змейки
        game_over()

    show_score_and_level(white, 'times new roman', 35)
    pygame.display.update()
    fps.tick(snake_speed)