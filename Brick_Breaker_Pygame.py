import pygame

pygame.init()

# 스크린 설정
display_width = 1000
display_height = 800
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("벽돌 깨기")
score_font = pygame.font.SysFont("comicsans", 40)

# 색
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 패들 크기, 속도
paddle_width = 150
paddle_height = 15
paddle_speed = 10

# 공 크기, 속도
ball_radius = 10
ball_speed_x = 5
ball_speed_y = 5

# 벽돌 크기
brick_width = 100
brick_height = 20
bricks = []

#점수
score = 0
life = 3

paddle = pygame.Rect(400, 750, paddle_width, paddle_height)
ball = pygame.Rect(500, 700, ball_radius * 2, ball_radius * 2)

for i in range(9):
    for j in range(9):
        brick = pygame.Rect(j * (brick_width + 4) + 40, i * (brick_height + 4) + 25, brick_width, brick_height)
        bricks.append(brick)

ball_dx = ball_speed_x
ball_dy = ball_speed_y

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < display_width:
        paddle.x += paddle_speed

    ball.x += ball_dx
    ball.y += ball_dy

    if ball.top <= 0:
        ball_dy *= -1
    if ball.left <= 0 or ball.right >= display_width:
        ball_dx *= -1

    if ball.colliderect(paddle) and ball_dy > 0:
        ball_dy *= -1

    for brick in bricks:  
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_dy *= -1
            score += 1
    
    if ball.top >= display_height:
        life -= 1
        ball.x = 500
        ball.y = 500

    score_text = score_font.render("Score: " + str(score), 1, "black")
    display.fill(WHITE)
    pygame.draw.rect(display, BLACK, paddle)
    pygame.draw.ellipse(display, RED, ball)
    for brick in bricks:
        pygame.draw.rect(display, GREEN, brick)
    
    display.blit(score_text, (0, 0))
    pygame.display.flip()

    if len(bricks) == 0 or life == 0:
        running = False

    pygame.time.Clock().tick(60)

pygame.quit()
