from direction import Direction
from position import Position
from random import randint

INITIAL_SNAKE = [
    Position(1,2),
    Position(2,2),
    Position(3,2)
]
INITIAL_DIRECTION = Direction.RIGHT


class GameState:
    def __init__(self, snake, direction, food, field_size, score):
        self.snake = snake
        self.direction = direction
        self.food = food
        self.field_size = field_size
        self.score = score
    def set_initial_position(self):
        self.snake = INITIAL_SNAKE[:]
        self.direction = INITIAL_DIRECTION
        self.set_random_food_position()
    def next_head(self, direction):
        pos = self.snake[-1]
        if direction == Direction.UP:
            return Position(pos.x, (pos.y -1) % self.field_size
            )
        elif direction == Direction.DOWN:
            return Position(pos.x, (pos.y + 1) % self.field_size
            )
        elif direction == Direction.LEFT:
            return Position(
                (pos.x - 1) % self.field_size, pos.y
            )
        elif direction == Direction.RIGHT:
            return Position(
                (pos.x + 1) % self.field_size, pos.y
            )
    def set_random_food_position(self):
        self.food = Position(
            randint(0, self.field_size -1),
            randint(0, self.field_size - 1)
        )
        if self.food in self.snake:
            self.set_random_food_position()
    def step(self):
        new_head =self.next_head(self.direction)
        collision = new_head in self.snake
        if collision:
            self.set_initial_position()
            self.score = 1
            return
        self.snake.append(new_head)
        if new_head == self.food:
            self.score = self.score << 1
            self.set_random_food_position()
        else:
            self.snake = self.snake[1:]
    def can_turn(self,direction):
        new_head =self.next_head(direction)
        return new_head != self.snake[-2]

    def turn(self, direction):
        if self.can_turn(direction):
            self.direction = direction


