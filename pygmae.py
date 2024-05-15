import pygame

pygame.init()

#스크린 설정
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("OSS 팀플 벽돌 깨기")

# 색 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

#패들 크기, 속도
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
bricks = [ ]

paddle = pygame.Rect(400, 750, paddle_width, paddle_height) # 좌표 400, 750에 paddle_width, brick_height크기 사각형 생성

ball = pygame.Rect(500, 700, ball_radius * 2, ball_radius * 2) # 좌표 500, 700에 가로길이 세로길이 ball_radius * 2인 사각형 생성

for i in range(9): # 9 X 9 벽돌 생성
    for j in range(9):
        brick = pygame.Rect(j * (brick_width + 4) + 40, i * (brick_height + 4) + 25, brick_width, brick_height) #벽돌간 간격 4픽셀
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
    if keys[pygame.K_RIGHT] and paddle.right < screen_width:
        paddle.x += paddle_speed

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, paddle)
    pygame.draw.ellipse(screen, RED, ball)
    for brick in bricks:
        pygame.draw.rect(screen, GREEN, brick)
    pygame.display.flip()

    pygame.time.Clock().tick(60)
pygame.quit()
