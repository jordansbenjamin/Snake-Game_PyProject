from turtle import Turtle

data_file = "data.txt"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_file()
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f'Score: {self.score} High Score: {self.high_score}', align='center', font=('New Courier', 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg='GAME OVER', align='center', font=('New Courier', 20, 'normal'))

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_file(self.high_score)
        self.score = 0
        self.update_scoreboard()

    def read_file(self):
        with open(data_file, 'r') as data:
            content = data.read()
            return int(content)
        
    def write_file(self, high_score):
        with open(data_file, 'w') as data:
            content = data.write(str(high_score))