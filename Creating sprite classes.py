class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, health):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # Замените на реальные спрайты персонажей
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = health

    def update(self):
        # Обновление состояния персонажа
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)
