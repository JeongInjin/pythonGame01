import pygame

# 초기화: 반드시 필요
pygame.init()

# 화면 크기 설정
screen_width = 1100
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Injin Game")

# FPS
clock = pygame.time.Clock()

# 배경이미지 불러오기
background = pygame.image.load("/Users/injinjeong/jeong_workspace/python_workspace/game01/pygame_basic/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("/Users/injinjeong/jeong_workspace/python_workspace/game01/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0] #캐릭터 가로 크기
character_height = character_size[1] #캐릭터 세로 크기
character_x_pos = screen_width / 2 - (character_width / 2) # 화면 가로의 절반 크기에 해당 하는 곳에 위치함.
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당 하는 곳에 위치함

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 적 캐릭터
enemy = pygame.image.load("/Users/injinjeong/jeong_workspace/python_workspace/game01/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0] #캐릭터 가로 크기
enemy_height = enemy_size[1] #캐릭터 세로 크기
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) # 화면 가로의 절반 크기에 해당 하는 곳에 위치함.
enemy_y_pos = (screen_height / 2) - (enemy_height / 2) # 화면 세로 크기 가장 아래에 해당 하는 곳에 위치함

# 이벤트 루프
running = True
while running:
    dt = clock.tick(60) # fps 설정
    # print("fps: " + str(clock.get_fps()))

    for event in pygame.event.get(): # 어떤 이벤트?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP: # 방향키 때면 멈춤.
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경게값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경게값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌 함")
        running = False

    # screen.fill((0, 0, 255)) 이미지 없이 백그라운드 채우기
    screen.blit(background, (0, 0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기

    pygame.display.update() # 게임화면 다시 그리기(필수)

# pygame 종료
pygame.quit()








