import pygame
import subprocess
import sys

# Инициализация окна и основных настроек
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Игровое меню')
screen = pygame.display.set_mode((960, 540), 0, 32)

# Настройки шрифта
font = pygame.font.SysFont(None, 30)

# Загрузка фоновой картинки
background = pygame.image.load('assests/imgs/menu.png')  # Замените 'path/to/your/image.jpg' на путь к вашей картинке

# Загрузка изображения для кнопки "ИГРАТЬ"
play_button_image = pygame.image.load('assests/imgs/playbutton.png')  # Замените 'path/to/your/button.png' на путь к вашей картинке

# Загрузка изображения для кнопки "Настройки"
settings_button_image = pygame.image.load('assests/imgs/settings.png')  # Замените 'path/to/your/settings_button.png' на путь к вашей картинке


# Функция для вывода текста на экране и кнопках
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Переменная для отслеживания действий
click = False

# Основная функция, содержащая кнопки и игровые функции
def main_menu():
    while True:
        screen.blit(background, (0, 0))  # Отрисовка фоновой картинки

        mx, my = pygame.mouse.get_pos()

        # Создание кнопки "ИГРАТЬ"
        button_play = pygame.Rect(160, 115, play_button_image.get_width(), play_button_image.get_height())

        # Создание кнопки "Настройки"
        button_settings = pygame.Rect(180, 5, settings_button_image.get_width(), settings_button_image.get_height())

        # Определение функции при нажатии на кнопку "ИГРАТЬ"
        if button_play.collidepoint((mx, my)):
            # if click:
            game()

        # Определение функции при нажатии на кнопку "Настройки"
        if button_settings.collidepoint((mx, my)):
            # if click:
            options()

        # Отрисовка изображения на кнопке "ИГРАТЬ"
        screen.blit(play_button_image, (160, 115))

        # Отрисовка изображения на кнопке "Настройки"
        screen.blit(settings_button_image, (230, 280))

        # Обработка событий
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

# Функция вызывается при нажатии кнопки "ИГРАТЬ"
def game():
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text('ИГРОВОЙ ЭКРАН', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
       
        pygame.display.update()
        mainClock.tick(60)

# Функция вызывается при нажатии кнопки "ОПЦИИ"
import os
import subprocess

# Функция вызывается при нажатии кнопки "ОПЦИИ"
def options():
    subprocess.call(['python', 'options.py'])  # Запускаем options.py из подпапки "options"

# Запуск основного меню
main_menu()