import pygame

# 초기화: 반드시 필요
pygame.init()

# 화면 크기 설정
screen_width = 1100
screen_height = 640
pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Injin Game")

# 이벤트 루프
running = True
while running:
    for event in pygame.event.get(): # 어떤 이벤트?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생
            running = False


# pygame 종료
pygame.quit()








