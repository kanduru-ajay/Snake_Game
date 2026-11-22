import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH = 600
HEIGHT = 400
BLOCK_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Font
font = pygame.font.SysFont(None, 35)

# Snake settings
snake = [(100, 100), (80, 100), (60, 100)]
direction = (BLOCK_SIZE, 0)

# Food position
food = (
    random.randrange(0, WIDTH, BLOCK_SIZE),
    random.randrange(0, HEIGHT, BLOCK_SIZE)
)

score = 0
game_over = False

def display_score():
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

def show_game_over():
    text = font.render("GAME OVER!", True, RED)
    screen.blit(text, (WIDTH // 2 - 90, HEIGHT // 2))
    pygame.display.update()
    pygame.time.wait(2000)

# Main game loop
while True:

    # Handle keyboard input and window events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, BLOCK_SIZE):
                direction = (0, -BLOCK_SIZE)

            elif event.key == pygame.K_DOWN and direction != (0, -BLOCK_SIZE):
                direction = (0, BLOCK_SIZE)

            elif event.key == pygame.K_LEFT and direction != (BLOCK_SIZE, 0):
                direction = (-BLOCK_SIZE, 0)

            elif event.key == pygame.K_RIGHT and direction != (-BLOCK_SIZE, 0):
                direction = (BLOCK_SIZE, 0)

   # Update snake position
new_head = (
    snake[0][0] + direction[0],
    snake[0][1] + direction[1]
)

snake.insert(0, new_head)

# Check whether food is eaten
ate_food = new_head == food

if not ate_food:
    snake.pop()

# Check wall collision
if (
    new_head[0] < 0 or new_head[0] >= WIDTH or
    new_head[1] < 0 or new_head[1] >= HEIGHT
):
    game_over = True

# Check self collision
if new_head in snake[1:]:
    game_over = True

# Increase score and generate new food
if ate_food and not game_over:
    score += 1

    while True:
        food = (
            random.randrange(0, WIDTH, BLOCK_SIZE),
            random.randrange(0, HEIGHT, BLOCK_SIZE)
        )

        if food not in snake:
            break
    else:
        snake.pop()

    # Check wall collision
    if (
        new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT
    ):
        game_over = True

    # Check self collision
    if new_head in snake[1:]:
        game_over = True

    if game_over:
        show_game_over()
        break

    # Draw screen
    screen.fill(BLACK)

    # Draw snake
    for segment in snake:
        pygame.draw.rect(
            screen, GREEN,
            (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE)
        )

    # Draw food
    pygame.draw.rect(
        screen, RED,
        (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE)
    )

    display_score()

    pygame.display.update()

    # Control game speed
    clock.tick(10)

pygame.quit()
sys.exit()
