import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        # movimento
        self.velocity_y = 0
        self.gravity = 0.8
        self.jump_speed = -15
        self.on_ground = False

    def update(self):
        # aplica a gravidade
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        # verifica a colisao com o chao
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.velocity_y = 0
            self.on_ground = True
    
    def jump(self):
        if self.on_ground:
            self.velocity_y = self.jump_speed
            self.on_ground = False

    def move(self, dx):
        self.rect.x += dx
