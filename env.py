import pygame

from snake import *
from food import *

class environment:
    bounds = None
    block_size = None
    snake = None
    Food = None
    window = None

    def __init__(self, bounds, block_size):
        pygame.init()
        self.window = pygame.display.set_mode(bounds)
        pygame.display.set_caption("SnakeAI")
        self.snake = Snake(block_size, bounds)
        self.food = Food(block_size, bounds)

    def update_score(self):
        font = pygame.font.SysFont('comicsans', 12, True)
        text = font.render("Score: {}".format(self.snake.score), True, (255, 255, 255))
        self.window.blit(text, (0, 0))
        pygame.display.update()

    def game_over(self):
        font = pygame.font.SysFont('comicsans', 60, True)
        text = font.render('Game Over', True, (255, 255, 255))
        self.window.blit(text, (100, 150))
        pygame.display.update()
        pygame.time.delay(1000)
        self.snake.respawn()
        self.food.respawn()

    def game_step(self):
        self.update_score()
        pygame.time.delay(75)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
        # handles user input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.snake.steer(Direction.LEFT)
        elif keys[pygame.K_RIGHT]:
            self.snake.steer(Direction.RIGHT)
        elif keys[pygame.K_UP]:
            self.snake.steer(Direction.UP)
        elif keys[pygame.K_DOWN]:
            self.snake.steer(Direction.DOWN)

        self.snake.move()
        self.snake.check_if_eat_food(self.food, self.window)

        # game over condition
        if self.snake.check_collision() == True:
            self.game_over()

        self.window.fill((0,0,0))
        self.snake.draw(pygame, self.window)
        self.food.draw(pygame, self.window)
        pygame.display.flip()