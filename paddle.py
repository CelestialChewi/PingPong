from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setpos(position)

    def move_up(self):
        if self.ycor() < 330:
            up_ycor = self.ycor() + 40
            self.setpos(self.xcor(), up_ycor)

    def move_down(self):
        if self.ycor() > -330:
            down_ycor = self.ycor() - 40
            self.setpos(self.xcor(), down_ycor)
