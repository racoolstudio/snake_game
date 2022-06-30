from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('green')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed('fastest')
        self.y_cord = 0
        self.x_cord = 0
        self.score = 0
        self.random()

    def random(self):
        self.y_cord = random.uniform(-250, 240)
        self.x_cord = random.uniform(-260, 270)
        self.goto(self.x_cord, self.y_cord)
