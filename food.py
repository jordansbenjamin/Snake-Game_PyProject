from turtle import Turtle
import random as rand
class Food(Turtle): # Inherting the Turtle class, which is the superclass

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        self.new_location()
        
    def new_location(self):
        random_x = rand.randint(-280,280)
        random_y = rand.randint(-280,280)
        self.goto(random_x, random_y)