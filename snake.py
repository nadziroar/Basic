# 1. Install Pygame = pip install pygame
# 2. Create the screen
from curses import KEY_DOWN
import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0 , 0)
 
dis= pygame.display.set_mode((800,600))
pygame.display.set_caption('Snake Game')

game_over = False

#To initialize the position of snake
x1 = 300
y1 = 300

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

#To ensure the window is not closed until the game over
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over =  True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0 
            elif event.key == pygame.K_UP:
                x1_change = 0 
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10
        
    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    
    pygame.draw.rect(dis, blue , [200,150,10,10])
    pygame.display.update()
        
pygame.quit()
quit()