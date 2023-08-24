from turtle import Turtle
import random as r


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.new_position()

    def new_position(self):
        self.color("blue")
        self.speed("fastest")
        self.goto(r.randint(-280, 280), r.randint(-280, 280))