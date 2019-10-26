import pygame
pygame.init()
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
BLOCK_SIZE = 50

gameWindow = pygame.display.set_mode((10*BLOCK_SIZE,10*BLOCK_SIZE))
pygame.display.set_caption("Snake 1")


exit_game = False
game_over = False
snake_x = 50
snake_y = 50
snake_size = 10

while not exit_game:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            exit_game = False
    
    
    
    gameWindow.fill(white)
    pygame.draw.rect(gameWindow, red, [snake_x, snake_y,snake_size])
    pygame.display.update()  
    
        






pygame.quit()
quit()


