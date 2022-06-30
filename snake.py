from turtle import Turtle


class Snake:
    START = [(0, 0), (-20, 0), (-40, 0)]
    X_CORD = -30
    MOVE_DISTANCE = 20
    UP = 90
    LEFT = 180
    RIGHT = 0
    DOWN = 270

    def __init__(self):
        self.snake = []
        self.snake_color = 'white'
        self.create()
        self.head = self.snake[0]
        self.rest_body = self.snake[1:]

    def create(self):
        for i in Snake.START:
            self.add(i)

    def move_right(self):
        if self.head.heading() != Snake.LEFT:
            self.head.seth(Snake.RIGHT)

    def move_left(self):
        if self.head.heading() != Snake.RIGHT:
            self.head.seth(Snake.LEFT)

    def move_up(self):
        if self.head.heading() != Snake.DOWN:
            self.head.seth(Snake.UP)

    def move_down(self):
        if self.head.heading() != Snake.UP:
            self.head.seth(Snake.DOWN)

    def move(self):
        for snake_num in range(len(self.snake) - 1, 0, -1):
            new_pos = self.snake[snake_num - 1].pos()
            self.snake[snake_num].goto(new_pos)
        self.head.forward(Snake.MOVE_DISTANCE)

    def add(self,position):
        new_snake = Turtle()
        new_snake.shape('square')
        new_snake.penup()
        new_snake.color(self.snake_color)
        new_snake.goto(position)
        self.snake.append(new_snake)
    def grow(self):
        self.add(self.snake[-1].pos())
