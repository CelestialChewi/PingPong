from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time

screen = Screen()

screen.setup(width = 1000, height= 800)
screen.bgcolor("black")
screen.title("Welcome to Pong!")
screen.tracer(0)

paddle1 = Paddle((-450, 0))
paddle2 = Paddle((450, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle1.move_up, "w")
screen.onkey(paddle1.move_down, "s")
screen.onkey(paddle2.move_up, "Up")
screen.onkey(paddle2.move_down, "Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move_ball()

    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_ball()

    if ball.distance(paddle1) <= 22 and paddle1.xcor() < -300 or ball.distance(paddle2) <= 23 and paddle2.xcor() > 300:
        ball.hit_paddle()
        scoreboard.update_scoreboard()

    if ball.xcor() > 490:
        ball.reset_position()
        scoreboard.add_player1_score()

    if ball.xcor() < -490:
        ball.reset_position()
        scoreboard.add_player2_score()

screen.exitonclick()