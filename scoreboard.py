from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
         super().__init__()
         self.player1_score = 0
         self.player2_score = 0
         self.color("white")
         self.hideturtle()
         self.penup()
         self.goto(0, 350)
         self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 300)
        self.write(self.player1_score, align="center", font=("Arial", 20, "normal"))
        self.goto(100, 300)
        self.write(self.player2_score, align="center", font=("Arial", 20, "normal"))

    def add_player1_score(self):
        self.player1_score += 1
        self.update_scoreboard()

    def add_player2_score(self):
        self.player2_score += 1
        self.update_scoreboard()

    def final_score(self):
        self.clear()
        self.goto(0, 100)
        self.write(f"Game Over! Your Final score: {self.score}", align="center", font=("Arial", 20, "normal"))