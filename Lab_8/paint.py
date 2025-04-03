import pygame, sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))  
    caption = pygame.display.set_caption(('Painter'))  #
    clock = pygame.time.Clock()

    radius = 30
    x, y = 0, 0  
    points = []

    ORANGE = (100,65,0)
    BLUE  = (0, 0, 255)
    RED   = (255, 0, 0)
    GREEN = (0, 255, 0)
    YELLOW = (255,255,0)
    PURPLE = (160,32,240)
    PINK = (255, 192, 203)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    canvas = pygame.Surface((800, 600))
    canvas.fill(WHITE) 
    mode = BLUE  

    list_of_colors = [BLACK, RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, PINK]
    color_rects = [(30 + i * 30, 20, 20, 20) for i in range(len(list_of_colors))] # прямоугольники со цветами

    eraser = pygame.image.load(r'eraser.png')
    eraser_rect = eraser.get_rect(center = (265,19))

    start_pos = (0,0)
    rect_position = pygame.Rect((0,0,0,0))
    circle_center = (0,0)
    circle_radius = 0

    drawing = False  
    drawing_rect = False 
    drawing_circle = False  

    while True:
        screen.blit(canvas, (0,0)) 

        pygame.draw.rect(screen, WHITE, pygame.Rect(0,0,800,60)) 
        pygame.draw.line(screen, BLACK, (0, 60), (800, 60), 1) 
        colors(screen, list_of_colors) 
        screen.blit(eraser, (265,19)) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_c:  
                    drawing_circle = True
                elif event.key == pygame.K_r: 
                    drawing_rect = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                color_selected = False  
                start_pos = event.pos

                for i, rect in enumerate(color_rects):
                    if pygame.Rect(rect).collidepoint(x, y):
                        mode = list_of_colors[i]  
                        color_selected = True  
                        break

                if eraser_rect.collidepoint(x, y):
                    mode = WHITE  
                    color_selected = True 

                if not color_selected:
                    if drawing_circle:
                        circle_center = event.pos
                    elif drawing_rect:
                        rect_position.topleft = event.pos
                    else:
                        drawing = True
                        last_pos = event.pos

            if event.type == pygame.MOUSEMOTION:
                if drawing and last_pos:
                    pygame.draw.line(canvas, mode, last_pos, event.pos, radius)  
                    last_pos = event.pos
                if drawing_rect:
                    end_pos = event.pos
                    rect_position.width = abs(start_pos[0] - end_pos[0])
                    rect_position.height = abs(start_pos[1] - end_pos[1])
                if drawing_circle:
                    end_pos = event.pos
                    circle_radius = int(((end_pos[0] - circle_center[0])**2 + (end_pos[1] - circle_center[1])**2)**0.5) 

            if event.type == pygame.MOUSEBUTTONUP:
                if drawing_rect:
                    pygame.draw.rect(canvas, BLACK, rect_position, 2) 
                    drawing_rect = False
                if drawing_circle:
                    pygame.draw.circle(canvas, BLACK, circle_center, circle_radius, 2)  
                    drawing_circle = False
                drawing = False  
        
        clock.tick(100)
        pygame.display.flip()

def colors(screen, list_of_colors):
    pos = 30
    for i in range(len(list_of_colors)):
        pygame.draw.circle(screen, list_of_colors[i], (pos, 30), 10)
        pos += 30

main()