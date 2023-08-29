from turtle import Turtle


class Scoring(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score}  High Score: {self.high_score}", align="center", font=('Arial', 14, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.clear()
    #     self.write(f"GAME OVER! Your Score: {self.score}", align="center", font=('Arial', 18, 'normal'))

    def gain_score(self):
        self.score += 1
        self.clear()
        self.update_score()
