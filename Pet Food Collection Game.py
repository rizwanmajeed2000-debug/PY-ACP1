import pygame

pygame.init()

# Screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pet Food Collection Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
YELLOW = (255, 255, 0)

# Background
background = pygame.Surface((WIDTH, HEIGHT))
background.fill((150, 200, 255))


# Pet Sprite
class Pet(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)

        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if keys[pygame.K_UP]:
            self.rect.y -= self.speed

        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Keep pet inside screen
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT


# Food Sprite
class Food(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface((30, 30))
        self.image.fill(YELLOW)

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


# Create pet
pet = Pet()

# Sprite groups
pet_group = pygame.sprite.Group()
food_group = pygame.sprite.Group()

pet_group.add(pet)

# Create food
food1 = Food(150, 150)
food2 = Food(650, 150)
food3 = Food(150, 450)
food4 = Food(650, 450)

food_group.add(food1, food2, food3, food4)

# Named font
font = pygame.font.SysFont("Arial", 40)

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # Update pet
    pet_group.update()

    # Detect collision with food
    collected = pygame.sprite.spritecollide(
        pet,
        food_group,
        True
    )

    # Draw background
    screen.blit(background, (0, 0))

    # Draw sprites
    food_group.draw(screen)
    pet_group.draw(screen)

    # Check if all food has been collected
    if len(food_group) == 0:

        message = font.render(
            "All Food Collected!",
            True,
            BLACK
        )

        # Center message
        message_rect = message.get_rect(
            center=(WIDTH // 2, HEIGHT // 2)
        )

        screen.blit(message, message_rect)

    pygame.display.update()

    clock.tick(60)

pygame.quit()