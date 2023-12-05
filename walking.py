def run_game():
    # Инициализация pygame и создание экрана
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Tekken 7 Clone")

    # Создание персонажей
    player = Character(200, 300, 100)
    computer = Character(600, 300, 100)

    # Группа спрайтов для отображения персонажей
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player, computer)

    # Основной игровой цикл
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Обработка пользовательского ввода
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.rect.x -= 5
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.rect.x += 5
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.rect.y -= 5
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player.rect.y += 5
        if keys[pygame.K_SPACE]:
            player.attack(computer)  
          if keys[pygame.K_UP] or keys[pygame.K_w]:
    player.rect.y -= 5
if keys[pygame.K_DOWN] or keys[pygame.K_s]:
    player.rect.y += 5

        # Обновление состояния игры
        all_sprites.update()

        # Отрисовка объектов на экране
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)

        # Обновление экрана
        pygame.display.flip()

        # Проверка на победу или поражение
        if player.health <= 0:
            print("Вы проиграли!")
            running = False
        elif computer.health <= 0:
            print("Вы победили!")
            running = False

    pygame.quit()
