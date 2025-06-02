from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

LOCATIONS = [(350, 0), (-350, 0)]
DISTANCE = 50
Y_LIMIT = 290

def check_winner():
    return scoreboard.l_score >= 10 or scoreboard.r_score >= 10


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(LOCATIONS[0])
left_paddle = Paddle(LOCATIONS[1])
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True


while game_is_on:
    screen.update()
    ball.move()
    #Detect collision with walls
    if ball.ycor() > Y_LIMIT or ball.ycor() < -Y_LIMIT:
        ball.wall_bounce()

    #Detect collision with paddles
    if ball.xcor() > 320 and ball.distance(right_paddle) < DISTANCE or ball.xcor() < -320 and ball.distance(left_paddle) < DISTANCE:
        ball.paddle_bounce()

    #Detect if right paddle missed the ball
    if ball.xcor() > 420:
        ball.reset_ball()
        scoreboard.l_point()

    #Detect if left paddle missed the ball
    if ball.xcor() < -420:
        ball.reset_ball()
        scoreboard.r_point()

    if check_winner():
        game_is_on = False
        scoreboard.declare_winner()

    time.sleep(ball.move_speed)



screen.exitonclick()
