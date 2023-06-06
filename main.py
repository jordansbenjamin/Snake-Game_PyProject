from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

xpos = 0

bodies = []

# Create 3 snake body objects
for snake_body in range(3):
    snake_body = Turtle('square')
    snake_body.speed(1)
    snake_body.color('white')
    snake_body.penup()
    snake_body.goto(x=xpos, y=0)
    xpos += -20
    bodies.append(snake_body)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    for snake_bod in range(len(bodies) - 1, 0, -1):
        new_x = bodies[snake_bod - 1].xcor()
        new_y = bodies[snake_bod - 1].ycor()
        bodies[snake_bod].goto(new_x, new_y)
    bodies[0].forward(10)

screen.exitonclick()