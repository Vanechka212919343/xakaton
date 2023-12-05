import pygame
import sys

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
background = pygame.image.load('assests/imgs/background.jpg')
sprite_images = [pygame.image.load('assests/imgs/sprite1.png'), pygame.image.load('assests/imgs/sprite1.png')]  # Загрузка изображений спрайта
sprite1_images = [pygame.image.load('assests/imgs/sprite1.png'), pygame.image.load('assests/imgs/sprite1.png')]  # Загрузка изображений спрайта

# Позиция спрайта
sprite_x = 300
sprite_y = 300
sprite1_x = 300
sprite1_y = 300
sprite_x_change = 0
asprite_x_change = 0
asprite_y_change = 0
sprite_y_change = 0
sprite_image_index = 0  # Индекс текущего изображения спрайта
sprite1_image_index = 0  # Индекс текущего изображения спрайта

health = [0,0]

# Главный цикл игры
running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                sprite_x_change = -5
            if event.key == pygame.K_RIGHT:
                sprite_x_change = 5
            if event.key == pygame.K_UP:
                sprite_y_change = -5
            if event.key == pygame.K_DOWN:
                sprite_y_change = 5
            if event.key == pygame.K_SPACE:
                health[1] -= 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                sprite_x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                sprite_y_change = 0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                asprite_x_change = -5
            if event.key == pygame.K_d:
                asprite_x_change = 5
            if event.key == pygame.K_w:
                asprite_y_change = -5
            if event.key == pygame.K_s:
                asprite_y_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                asprite_x_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                asprite_y_change = 0

    sprite_x += sprite_x_change
    sprite_y += sprite_y_change

    sprite1_x = asprite_x_change
    sprite1_y += asprite_y_change

    # Ограничение движения спрайта в пределах экрана
    if sprite_x <= -736:
        sprite_x = -736
    elif sprite_x >= 736:
        sprite_x = 736
    if sprite_y <= 0:
        sprite_y = 0
    elif sprite_y >= 536:
        sprite_y = 536

    if sprite1_x <= -736:
        sprite1_x = -736
    elif sprite1_x >= 736:
        sprite1_x = 736
    if sprite1_y <= 0:
        sprite1_y = 0
    elif sprite1_y >= 536:
        sprite1_y = 536

    font = pygame.font.Font(None, 36)
    text = font.render(f"Player 1 Health: {health[0]}", True, (255, 0, 0)) 
    screen.blit(text, (10, 10))
    text = font.render(f"Player 2 Health: {health[1]}", True, (0, 0, 255))
    screen.blit(text, (800 - text.get_width() - 10, 10))

    # Отображение спрайта и анимации
    screen.blit(sprite_images[sprite_image_index], (sprite_x, sprite_y))
    screen.blit(sprite1_images[sprite1_image_index], (sprite1_x, sprite1_y))
    sprite_image_index = (sprite_image_index + 1) % 2  # Смена изображения для анимации
    sprite1_image_index = (sprite1_image_index + 1) % 2  # Смена изображения для анимации

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
