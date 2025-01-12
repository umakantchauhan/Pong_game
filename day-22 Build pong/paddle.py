from turtle import Turtle

class Paddle(Turtle):#Paddle(Turtle) used to make Paddle a Turtle objects
    def __init__(self,position):
        super().__init__()#to get all the ability of the turtle
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)