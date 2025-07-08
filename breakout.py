import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Breakout Game')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Paddle settings
paddle_width = 100
paddle_height = 15
paddle_speed = 7
paddle = pygame.Rect((WIDTH - paddle_width) // 2, HEIGHT - 40, paddle_width, paddle_height)

# Ball settings
ball_radius = 10
ball_speed_x = 4
ball_speed_y = -4
ball = pygame.Rect(WIDTH // 2 - ball_radius, HEIGHT // 2, ball_radius * 2, ball_radius * 2)

# Brick settings
brick_rows = 5
brick_cols = 8
brick_width = 75
brick_height = 20
bricks = []
for row in range(brick_rows):
    for col in range(brick_cols):
        bricks.append(pygame.Rect(60 + col * (brick_width + 10), 60 + row * (brick_height + 10), brick_width, brick_height))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += paddle_speed

    # Move ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with walls
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x *= -1
    if ball.top <= 0:
        ball_speed_y *= -1
    if ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Ball collision with paddle
    if ball.colliderect(paddle):
        ball_speed_y *= -1

    # Ball collision with bricks
    for brick in bricks[:]:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_speed_y *= -1
            break

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    for brick in bricks:
        pygame.draw.rect(screen, RED, brick)

    pygame.display.flip()
    clock.tick(60)
