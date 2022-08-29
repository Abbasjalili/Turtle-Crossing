from turtle import Turtle
FONT = ("Courier", 14, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.color("black")
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-240, 260)
        self.write(f"Level: {self.level}", align= 'center', font= FONT)
        

    def increase_score(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()  

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over! A car hits you.", align= "center", font=("arial", 14, "normal"))
