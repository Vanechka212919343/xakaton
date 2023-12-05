import pygame
import sys

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.Font(None, 36)
mainClock = pygame.time.Clock()

# Загрузка изображения фона
background = pygame.image.load('background.jpg')

# Функция рисования текста на экране
def draw_text(text, font, color, x, y):
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))

# Функция меню опций
def options_menu():
    running = True
    selected_option = 0  # 0: Mouse Sensitivity, 1: Graphics Quality
    options_values = [50, "High"]  # Исходные значения чувствительности мыши и графики

    fake_options_values = [75, "Ultra"]  # Фейковые значения для демонстрации

    while running:
        screen.fill((0, 0, 0))

        # Отображение текста и текущих настроек
        draw_text('OPTIONS MENU', font, (255, 255, 255), 20, 20)
        # Используем фейковые значения для демонстрации
        draw_text('Mouse Sensitivity: {}%'.format(fake_options_values[0]), font, (255, 255, 255), 20, 100)
        draw_text('Graphics Quality: {}'.format(fake_options_values[1]), font, (255, 255, 255), 20, 150)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % 2
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % 2
                elif event.key == pygame.K_LEFT:
                    if selected_option == 0:
                        options_values[0] = max(0, options_values[0] - 10)  # Уменьшаем чувствительность мыши
                    else:
                        if options_values[1] == "High":
                            options_values[1] = "Medium"  # Изменяем графику на Medium
                        elif options_values[1] == "Medium":
                            options_values[1] = "Low"  # Изменяем графику на Low
                elif event.key == pygame.K_RIGHT:
                    if selected_option == 0:
                        options_values[0] = min(100, options_values[0] + 10)  # Увеличиваем чувствительность мыши
                    else:
                        if options_values[1] == "Low":
                            options_values[1] = "Medium"  # Изменяем графику на Medium
                        elif options_values[1] == "Medium":
                            options_values[1] = "High"  # Изменяем графику на High
                elif event.key == pygame.K_RETURN:
                    # Сохраняем настройки и выходим из меню
                    save_options(options_values)
                    running = False

        # Отображение выбранного пункта
        if selected_option == 0:
            draw_text('>', font, (255, 255, 255), 0, 100)
        else:
            draw_text('>', font, (255, 255, 255), 0, 150)

        pygame.display.update()
        mainClock.tick(60)

# Функция сохранения настроек (в данном случае просто вывод информации об изменениях)
def save_options(options_values):
    print("Mouse Sensitivity set to {}%".format(options_values[0]))
    print("Graphics Quality set to {}".format(options_values[1]))

# Главный цикл игры
def main_game_loop():
    running = True
    while running:
        screen.blit(background, (0, 0))  # Отображение фона
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                mx, my = pygame.mouse.get_pos()
                # Проверка нажатия на кнопку "Настройки"
                if 180 <= mx <= 180 + settings_button_image.get_width() and 5 <= my <= 5 + settings_button_image.get_height():
                    options()  # Вызываем функцию options() при клике на кнопку "Настройки"
        # Отображение обновлений на экран
        pygame.display.update()
        mainClock.tick(60)


# Запуск игры
main_game_loop()
