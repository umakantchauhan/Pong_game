from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from turtle import Screen
import time

screen=Screen()
screen.title("Pong game")
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.tracer(0)#turning off the animation

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))

ball=Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update() #turning on the animation
    ball.move()

    #detect collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #detect collision with wall
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:#ball.distance(r_paddle) distance between ball and right paddle;;ball.xcor()>340 distance from right wall
        ball.bounce_x()

    #detect R paddle misses
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()

    #detect L paddle misses
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()