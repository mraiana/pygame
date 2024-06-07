import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
red = (213, 50, 80)
purple = (138,43,226)
blue = (50, 153, 213)
 
dis_width = 600
dis_height = 400
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Демо')
 
clock = pygame.time.Clock()
 
block = 10
speed = 15

 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
 
def Your_score(score):
    value = score_font.render("Балл: " + str(score), True, red)
    dis.blit(value, [0, 0])
 
 
 
def our_snake(block, block_list):
    for x in block_list:
        pygame.draw.rect(dis, red, [x[0], x[1], block, block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    block_List = []
    Length_of_block = 1
 
    foodx = round(random.randrange(0, dis_width - block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(blue)
            message("проигрыш!нажмите C-играть заново или Q-выйти", red)
            Your_score(Length_of_block - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, purple, [foodx, foody, block, block])
        block_Head = []
        block_Head.append(x1)
        block_Head.append(y1)
        block_List.append(block_Head)
        if len(block_List) > Length_of_block:
            del block_List[0]
 
        for x in block_List[:-1]:
            if x == block_Head:
                game_close = True
 
        our_snake(block, block_List)
        Your_score(Length_of_block - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - block) / 10.0) * 10.0
            Length_of_block += 1
        clock.tick(speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()