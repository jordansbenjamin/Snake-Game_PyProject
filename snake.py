from turtle import Turtle

# XPOS = 0
MOVE_DISTANCE = 10

class Snake:

    def __init__(self):
        self.xpos = 0
        self.bodies = []
        self.create_snake()
        self.head = self.bodies[0]

    def create_snake(self):
        '''Create 3 snake body objects'''
        for snake_body in range(3):
            snake_body = Turtle('square')
            snake_body.color('white')
            snake_body.penup()
            snake_body.goto(x=self.xpos, y=0)
            self.xpos += -20
            self.bodies.append(snake_body)

    def move(self):
        for snake_bod in range(len(self.bodies) - 1, 0, -1):
            new_x = self.bodies[snake_bod - 1].xcor()
            new_y = self.bodies[snake_bod - 1].ycor()
            self.bodies[snake_bod].goto(new_x, new_y)
        self.bodies[0].forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)