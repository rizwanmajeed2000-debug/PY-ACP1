import random
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invader - Part 1")
font = pygame.font.SysFont(None, 36)

score = 0

player_rect = pygame.Rect(380, 500, 40, 40)

enemies = []
for _ in range(7):
    x = random.randint(0, 760)
    y = random.randint(50, 200)
    enemies.append(pygame.Rect(x, y, 40, 40))

running = True
clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT] and player_rect.right < 800:
        player_rect.x += 5
    if keys[pygame.K_UP] and player_rect.top > 0:
        player_rect.y -= 5
    if keys[pygame.K_DOWN] and player_rect.bottom < 600:
        player_rect.y += 5

    for enemy in enemies:
        if player_rect.colliderect(enemy):
            score += 1
            enemy.x = random.randint(0, 760)
            enemy.y = random.randint(50, 200)

        pygame.draw.rect(screen, (255, 0, 0), enemy)

    pygame.draw.rect(screen, (0, 255, 0), player_rect) 

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()