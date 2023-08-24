from turtle import Turtle


class Scoring(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score : {self.score}", align="center", font=('Arial', 14, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write(f"GAME OVER! Your Score: {self.score}", align="center", font=('Arial', 18, 'normal'))

    def gain_score(self):
        self.score += 1
        self.clear()
        self.update_score()
