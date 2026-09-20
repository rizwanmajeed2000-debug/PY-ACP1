import pygame

pygame.init()

# Screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Sprite Adventure")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 100, 255)
YELLOW = (255, 255, 0)

x = 350
y = 250
width = 50
height = 50
speed = 5

sprite_color = BLUE

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed

    if keys[pygame.K_RIGHT]:
        x += speed

    if keys[pygame.K_UP]:
        y -= speed

    if keys[pygame.K_DOWN]:
        y += speed

    if x < 0:
        x = 0
        sprite_color = RED

    if x + width > WIDTH:
        x = WIDTH - width
        sprite_color = GREEN

    if y < 0:
        y = 0
        sprite_color = YELLOW

    if y + height > HEIGHT:
        y = HEIGHT - height
        sprite_color = BLUE

    screen.fill(WHITE)

    pygame.draw.rect(screen, sprite_color, (x, y, width, height))

    pygame.draw.rect(screen, BLACK, (x, y, width, height), 3)

    pygame.display.update()

    clock.tick(60)

pygame.quit()