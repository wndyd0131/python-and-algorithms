import pygame

pygame.init() #초기화

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Nado Game")

background = pygame.image.load("C:/Users/wndyd/Desktop/파이썬/pygame_basic/background.png")

character = pygame.image.load("C:/Users/wndyd/Desktop/파이썬/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = screen_width / 2 - character_width / 2# 화면 가로의 절반 크기에 위치
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 위치

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  #screen.fill((0, 255, 255)) #색깔로 배경 그리기
  screen.blit(background, (0, 0)) #이미지로 배경 그리기
  
  screen.blit(character, (character_x_pos, character_y_pos))
  
  pygame.display.update() #게임화면을 다시 그리기
  
pygame.quit()