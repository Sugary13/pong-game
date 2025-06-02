from turtle import Turtle

STARTING_SPEED = 0.05

class Ball(Turtle):



    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.move_speed = STARTING_SPEED
        self.x_move = 5
        self.y_move = 5


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_ball(self):
        self.goto(0, 0)
        self.move_speed = STARTING_SPEED
        self.x_move *= 1

