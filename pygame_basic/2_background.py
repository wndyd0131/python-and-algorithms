import pygame

pygame.init() #초기화

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Nado Game")

background = pygame.image.load("C:/Users/wndyd/Desktop/파이썬/pygame_basic/background.png")

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  #screen.fill((0, 255, 255))
  #screen.blit(background, (0, 0)) #배경 그리기
  
  pygame.display.update() #게임화면을 다시 그리기
pygame.quit()