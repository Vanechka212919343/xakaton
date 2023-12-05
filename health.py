class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, health, damage):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.health = health
        self.damage = damage

    def update(self):
        self.check_health()

    def check_health(self):
        if self.health <= 0:
            self.kill()
def run_game():
    # код до цикла
    font = pygame.font.Font(None, 36)

    # Основной игровой цикл
    running = True
    while running:
        # код до обработки пользовательского ввода
        player_health_text = font.render("Player Health: {}".format(player.health), True, (255, 255, 255))
        computer_health_text = font.render("Computer Health: {}".format(computer.health), True, (255, 255, 255))
        screen.blit(player_health_text, (10, 10))
        screen.blit(computer_health_text, (screen_width - computer_health_text.get_width() - 10, 10))
        # Обработка пользовательского ввода
        # код после обработки пользовательского ввода
        pygame.display.flip()
