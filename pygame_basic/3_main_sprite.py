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
background = pygame.image.load("/Users/injinjeong/jeong_workspace/python_workspace/game01/pygame_basic/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("/Users/injinjeong/jeong_workspace/python_workspace/game01/pygame_basic/character.png")
character = pygame.image.load("/Users/injinjeong/jeong_workspace/python_workspace/game01/pygame_basic/character.png")
# character_size = character.get_rect().size # 이미지 크기
character_size = character.get_rect().size
character_width = character_size[0] #캐릭터 가로 크기
character_height = character_size[1] #캐릭터 세로 크기
character_x_pos = screen_width / 2 - (character_width / 2) # 화면 가로의 절반 크기에 해당 하는 곳에 위치함.
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당 하는 곳에 위치함


# 이벤트 루프
running = True
while running:
    for event in pygame.event.get(): # 어떤 이벤트?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생
            running = False

    # screen.fill((0, 0, 255)) 이미지 없이 백그라운드 채우기
    screen.blit(background, (0, 0)) # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기

    pygame.display.update() # 게임화면 다시 그리기(필수)

# pygame 종료
pygame.quit()








