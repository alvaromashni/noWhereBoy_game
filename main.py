import pygame
import sys
from player import Player


pygame.init()
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
WHITE = pygame.rgb(255, 255, 255)
BLUE = pygame.rgb(44, 196, 219)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
runnning = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            running = False

keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    player.move(-5)
if keys[pygame.K_RIGHT]:
    player.move(5)
if keys[pygame.K_SPACE]:
    player.jump()

# atualiza todos os sprites
all_sprites.updates()

screen.fill(WHITE)
all_sprites.draw(screen)


pygame.display.flip()
clock.tick(60)

pygame.quit()
sys.exit()
