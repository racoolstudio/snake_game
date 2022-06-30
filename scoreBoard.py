from turtle import Turtle

STYLE = ('Verdana', 20, 'normal')
ALIGNMENT = 'center'
X_CORD = 0
Y_CORD = 270


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.score = 0
        self.goto(X_CORD, Y_CORD)
        self.write(f'Scores : {self.score}', align=ALIGNMENT, font=STYLE)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f'Scores : {self.score}', align='center', font=STYLE)
    def game_over(self):
        self.background()
        self.color('white')
        self.goto(0,0)
        self.write('Game_Over 🥲!',False,align=ALIGNMENT,font=STYLE)
    def background(self):
    
        self.goto(x=-50,y=50)
        self.color('black')
        self.pensize(20)
        self.forward(50)
