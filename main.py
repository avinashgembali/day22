from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

s = Screen()
s.setup(width=800, height=600)
s.bgcolor("black")
s.title("PONG GAME")
s.tracer(0)

paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
score = Score()
s.listen()


s.onkey(paddle1.go_up, "w")
s.onkey(paddle1.go_down, "s")

s.onkey(paddle2.go_up, "Up")
s.onkey(paddle2.go_down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    s.update()
    ball.move()
    # collision on top or bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # collision with right paddle
    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # if ball goes out of bounds in left or right
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

s.exitonclick()
