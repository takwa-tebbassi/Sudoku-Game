# still not done yet

import pygame

from random import*

grid = []

cell_width = 80
cell_height = 80

pygame.init()

screen = pygame.display.set_mode((1200, 720))
pygame.display.set_caption('Sudoku game')

running = True

screen.fill('purple')

for x in range(0,9):
    row = []
    for y in range(0,9):
        cell = randint(1, 9)
        row.append(cell)
    grid.append(row)
print(grid)

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()  # to know where the user clicked
            row = pos[1] // cell_height
            col = pos[0] // cell_width
       
            
            


pygame.display.flip()

pygame.quit()
