from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')

xpos = 0

for snake_body in range(3):
    snake_body = Turtle('square')
    snake_body.color('white')
    snake_body.goto(x=xpos, y=0)
    xpos += -20


screen.exitonclick()