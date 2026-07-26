import sys
import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Sprite Adventure")

clock = pygame.time.Clock()

BLACK = (20, 20, 20)
WHITE = (255, 255, 255)
RED = (235, 64, 52)
GREEN = (52, 235, 122)
BLUE = (52, 149, 235)
YELLOW = (235, 220, 52)

sprite_width = 60
sprite_height = 60
sprite_x = (WIDTH - sprite_width) // 2
sprite_y = (HEIGHT - sprite_height) // 2
sprite_speed = 6
current_color = BLUE  # Initial solid color

target_rect = pygame.Rect(350, 50, 100, 100)

running = True
while running:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True
            pygame.quit()
            sys.exit()

    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        sprite_x -= sprite_speed
    if keys[pygame.K_RIGHT]:
        sprite_x += sprite_speed
    if keys[pygame.K_UP]:
        sprite_y -= sprite_speed
    if keys[pygame.K_DOWN]:
        sprite_y += sprite_speed

    if sprite_x <= 0:
        sprite_x = 0
        current_color = RED

    elif sprite_x + sprite_width >= WIDTH:
        sprite_x = WIDTH - sprite_width
        current_color = GREEN

    if sprite_y <= 0:
        sprite_y = 0
        current_color = YELLOW

    elif sprite_y + sprite_height >= HEIGHT:
        sprite_y = HEIGHT - sprite_height
        current_color = BLUE

    player_rect = pygame.Rect(sprite_x, sprite_y, sprite_width, sprite_height)

    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, target_rect, width=3)

    pygame.draw.rect(screen, current_color, player_rect, width=0)

    pygame.display.flip()

    clock.tick(60)