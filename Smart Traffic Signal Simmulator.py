import pygame

pygame.init()

# Screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smart Traffic Signal Simulator")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
YELLOW = (255, 200, 0)
GRAY = (100, 100, 100)

# Custom events
CHANGE_CAR_COLOR = pygame.USEREVENT + 1
CHANGE_SIGNAL = pygame.USEREVENT + 2


# Car Sprite
class Car(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((70, 40))
        self.image.fill(BLUE if False else RED)

        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 280

        # Velocity
        self.velocity = 5

        self.color = RED

    def update(self):
        self.rect.x += self.velocity


# Create car
car = Car()

# Sprite Group
car_group = pygame.sprite.Group()
car_group.add(car)

# Traffic signal
signal_color = RED

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Change car color
        if event.type == CHANGE_CAR_COLOR:
            if car.color == RED:
                car.color = GREEN
            else:
                car.color = RED

            car.image.fill(car.color)

        # Change traffic signal
        if event.type == CHANGE_SIGNAL:
            if signal_color == RED:
                signal_color = GREEN
            else:
                signal_color = RED

    # Move car
    car_group.update()

    # Check road boundary
    if car.rect.right >= WIDTH:
        car.rect.right = WIDTH

        # Trigger custom events
        pygame.event.post(pygame.event.Event(CHANGE_CAR_COLOR))
        pygame.event.post(pygame.event.Event(CHANGE_SIGNAL))

        # Move car back
        car.velocity = -5

    if car.rect.left <= 0:
        car.rect.left = 0

        # Trigger custom events again
        pygame.event.post(pygame.event.Event(CHANGE_CAR_COLOR))
        pygame.event.post(pygame.event.Event(CHANGE_SIGNAL))

        car.velocity = 5

    screen.fill(WHITE)

    pygame.draw.rect(screen, GRAY, (0, 250, WIDTH, 100))

    pygame.draw.rect(screen, BLACK, (650, 50, 80, 180))

    pygame.draw.circle(
        screen,
        RED if signal_color == RED else GRAY,
        (690, 100),
        25
    )

    pygame.draw.circle(
        screen,
        GREEN if signal_color == GREEN else GRAY,
        (690, 170),
        25
    )

    car_group.draw(screen)

    pygame.display.update()

    clock.tick(60)

pygame.quit()