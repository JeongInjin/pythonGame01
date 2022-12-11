import pygame

# 초기화: 반드시 필요
pygame.init()

# 화면 크기 설정
screen_width = 1100
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Injin Game")

# 배경이미지 불러오기
background = pygame.image.load("/Users/injinjeong/jeong_workspace/python_workspace/game01/무제.skt/Layer~0.png")

# 이벤트 루프
running = True
while running:
    for event in pygame.event.get(): # 어떤 이벤트?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생
            running = False

    # screen.fill((0, 0, 255)) 이미지 없이 백그라운드 채우기
    screen.blit(background, (0, 0)) # 배경 그리기
    pygame.display.update() # 게임화면 다시 그리기(필수)

# pygame 종료
pygame.quit()








