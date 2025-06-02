from turtle import Turtle

PACES = 20

class Paddle(Turtle):



    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.setpos(position)

    def move(self, delta_y):
        new_y = self.ycor() + delta_y
        if -240 <= new_y <= 240:
            self.goto(self.xcor(), new_y)

    def up(self):
        self.move(PACES)

    def down(self):
        self.move(-PACES)
