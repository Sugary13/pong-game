from turtle import Turtle


FONT = ("Courier", 80, "normal")
WINNER_FONT = ("Courier", 24, "bold")
L_POSITION = (-100, 200)
R_POSITION = (100, 200)

class Scoreboard(Turtle):



    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(L_POSITION)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(R_POSITION)
        self.write(self.r_score, align="center", font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def declare_winner(self):
        self.goto(0, 0)
        winner = "RIGHT" if self.r_score > self.l_score else "LEFT"
        self.write(f"The {winner} player wins!", align="center", font=("Courier", 24, "bold"))
