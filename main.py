from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreBoard import ScoreBoard

import time

my_screen = Screen()
border = Turtle()
border.color('brown')
border.hideturtle()
my_screen.title('Snake Game')
my_screen.bgcolor('black')
my_screen.setup(600, 600)
my_screen.tracer(0)
mr_white = Snake()
border.pensize(10)
border.penup()
border.goto(x=-300, y=260)
border.pendown()

for i in range(2):
    border.forward(590)
    border.right(90)
    border.forward(550)
    border.right(90)
score_board = ScoreBoard()
food = Food()
my_screen.listen()
SPEED = 0.1
my_screen.onkey(key='Up', fun=mr_white.move_up)
my_screen.onkey(key='Down', fun=mr_white.move_down)
my_screen.onkey(key='Right', fun=mr_white.move_right)
my_screen.onkey(key='Left', fun=mr_white.move_left)
my_screen.onkey(key='w', fun=mr_white.move_up)
my_screen.onkey(key='s', fun=mr_white.move_down)
my_screen.onkey(key='d', fun=mr_white.move_right)
my_screen.onkey(key='a', fun=mr_white.move_left)
my_screen.onkey(key='W', fun=mr_white.move_up)
my_screen.onkey(key='S', fun=mr_white.move_down)
my_screen.onkey(key='D', fun=mr_white.move_right)
my_screen.onkey(key='A', fun=mr_white.move_left)

def check():
    for i in mr_white.snake[1:]:
        if i.distance(mr_white.head)<10:
            return True
    return False
game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(SPEED)
    mr_white.move()
    if mr_white.head.distance(food) < 20:
        score_board.update_score()
        mr_white.grow()
        food.random()
    if mr_white.head.xcor() > 290 or mr_white.head.ycor() < -280 or mr_white.head.xcor() < -300 or mr_white.head.ycor() > 250or check() :
        score_board.game_over()
        game_is_on = False



my_screen.exitonclick()
