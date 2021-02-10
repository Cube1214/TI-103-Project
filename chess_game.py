import pygame #module
import sys



pygame.init() #initialise
screen = pygame.display.set_mode((800, 600))# screen size
pygame.display.set_caption("CHESS GAME")# name of the tb

board = pygame.Surface((480, 480)) # size of board game
board.fill((175, 141,120)) #filll the board game with the color


for x in range(0, 8, 2):
    for y in range(0, 8, 2):
        pygame.draw.rect(board, (255, 240, 230), (x*60, y*60, 60, 60))

for x in range(1, 9, 2):
    for y in range(1,9,2):
        pygame.draw.rect(board, (255, 240, 230), (x * 60, y * 60, 60, 60))






while True:
    for event in pygame.event.get(): # capture every events
        if event.type == pygame.QUIT: # if use click on x tab used as quit
            print("Bye Bye")

            sys.exit(1111111111111)# the mark of end

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                print(x, y)

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                x, y = event.pos
                print(x, y)



    screen.fill((0, 200, 0))#color of the tab
    screen.blit(board,board.get_rect())
    pygame.display.update()






#to end the task