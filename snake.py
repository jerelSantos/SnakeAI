from enum import Enum

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

# handles snake movement, drawing, respawn, and direction changes
# RLA will directly affect this class' methods
class Snake:
    length = None
    direction = None
    body = None
    block_size = None
    body_color = (0, 255, 0)
    head_color = (0, 0, 255)
    bounds = None
    score = 0

    def __init__(self, block_size, bounds):
        self.block_size = block_size
        self.bounds = bounds
        self.respawn()

    def respawn(self):
        self.score = 0
        self.length = 3
        self.body = [(20, 20), (20, 40), (20, 60)]
        self.direction = Direction.DOWN

    def draw(self, game, window):
        for segment in self.body:
            game.draw.rect(window, self.body_color, (segment[0], segment[1], self.block_size, self.block_size))
        head = self.body[-1]
        game.draw.rect(window, self.head_color, (head[0], head[1], self.block_size, self.block_size))

    def move(self):
        curr_head = self.body[-1]
        if self.direction == Direction.DOWN:
            next_head = (curr_head[0], curr_head[1] + self.block_size)
        elif self.direction == Direction.UP:
            next_head = (curr_head[0], curr_head[1] - self.block_size)
        elif self.direction == Direction.RIGHT:
            next_head = (curr_head[0] + self.block_size, curr_head[1])
        elif self.direction == Direction.LEFT:
            next_head = (curr_head[0] - self.block_size, curr_head[1])
        self.body.append(next_head)

        if self.length < len(self.body):
            self.body.pop(0)

    def steer(self, newDirection):
        if self.direction == Direction.DOWN and newDirection != Direction.UP:
            self.direction = newDirection
        elif self.direction == Direction.UP and newDirection != Direction.DOWN:
            self.direction = newDirection
        elif self.direction == Direction.LEFT and newDirection != Direction.RIGHT:
            self.direction = newDirection
        elif self.direction == Direction.RIGHT and newDirection != Direction.LEFT:
            self.direction = newDirection

    def eat(self):
        self.length += 1

    def check_if_eat_food(self, food, window):
        head = self.body[-1]
        # if head collides with food
        if head[0] == food.x and head[1] == food.y:
            self.score += 1
            self.eat()
            food.respawn()

    def check_collision(self):
        head = self.body[-1]
        death = False

        # check for collision with body
        for i in range(len(self.body) - 1):
            segment = self.body[i]
            if head[0] == segment[0] and head[1] == segment[1]:
                death = True

        # check for collision with wall
        if head[0] >= self.bounds[0]:
            death = True
        if head[1] >= self.bounds[1]:
            death = True
        
        if head[0] < 0:
            death = True
        if head[1] < 0:
            death = True

        return death