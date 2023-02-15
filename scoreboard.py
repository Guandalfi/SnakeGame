from turtle import Turtle

FONT = ('Arial', 20, 'normal')
ALIGN = "center"

class Scoreboard(Turtle):
    def __init__(self,):
        super().__init__()
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.penup()

        self.goto(x=0, y=270)
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGN, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        current_score = f"Scoreboard: {self.score}"
        self.write(current_score, move=False, align=ALIGN, font=FONT)