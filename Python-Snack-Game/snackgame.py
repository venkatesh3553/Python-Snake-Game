import pygame
import random

pygame.init()

# screen set
width, height = 500, 500
game_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("VSP Snake Game")

# snake set
snake_x, snake_y = width // 2, height // 2
snake_move_x, snake_move_y = 0, 0
snake_body = [(snake_x, snake_y)]

# food set
food_x, food_y = random.randrange(0, width, 10), random.randrange(0, height, 10)

#  game values
clock = pygame.time.Clock()
score = 0
speed = 8  
font = pygame.font.SysFont(None, 36)

def game_over():
    font_large = pygame.font.SysFont(None, 48)
    text = font_large.render("Game Over!", True, (255, 0, 0))
    game_screen.blit(text, (width // 2 - 100, height // 2 - 20))
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    quit()

def display_snake_and_food():
    global snake_x, snake_y, food_x, food_y, score, speed

    # snake movement 
    snake_x = (snake_x + snake_move_x) % width
    snake_y = (snake_y + snake_move_y) % height

    if (snake_x, snake_y) in snake_body[1:]:
        game_over()

    snake_body.append((snake_x, snake_y))

    # snake eats food
    if food_x == snake_x and food_y == snake_y:
        score += 1
        food_x, food_y = random.randrange(0, width, 10), random.randrange(0, height, 10)

        # increase speed every 3 points
        if score % 3 == 0:
            speed += 1
    else:
        del snake_body[0]

    game_screen.fill((0, 0, 0))
    pygame.draw.rect(game_screen, (0, 255, 0), [food_x, food_y, 10, 10])
    for index, (x, y) in enumerate(snake_body):
        pygame.draw.rect(game_screen, (50, 50, 50), [x+2, y+2, 10, 10])  # shadow
        pygame.draw.rect(game_screen, (0, 255, 255), [x, y, 10, 10])     # body

    score_text = font.render(f"Score: {score}  Speed: {speed}", True, (255, 255, 0))
    game_screen.blit(score_text, (10, 10))
    pygame.display.update()

# game loop
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            quit()

        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT and snake_move_x == 0:
                snake_move_x = -10
                snake_move_y = 0
            elif i.key == pygame.K_RIGHT and snake_move_x == 0:
                snake_move_x = 10
                snake_move_y = 0
            elif i.key == pygame.K_UP and snake_move_y == 0:
                snake_move_x = 0
                snake_move_y = -10
            elif i.key == pygame.K_DOWN and snake_move_y == 0:
                snake_move_x = 0
                snake_move_y = 10

    display_snake_and_food()
    clock.tick(speed)
