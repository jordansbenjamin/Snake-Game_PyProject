from turtle import Turtle

class Snake:

    XPOS = 0
    MOVE_DISTANCE = 10

    def __init__(self):
        self.bodies = []
        self.create_snake()

    def create_snake(self):
        '''Create 3 snake body objects'''
        for snake_body in range(3):
            snake_body = Turtle('square')
            snake_body.speed(1)
            snake_body.color('white')
            snake_body.penup()
            snake_body.goto(x=Snake.XPOS, y=0)
            Snake.XPOS += -20
            self.bodies.append(snake_body)

    def move(self):
        for snake_bod in range(len(self.bodies) - 1, 0, -1):
            new_x = self.bodies[snake_bod - 1].xcor()
            new_y = self.bodies[snake_bod - 1].ycor()
            self.bodies[snake_bod].goto(new_x, new_y)
        self.bodies[0].forward(Snake.MOVE_DISTANCE)