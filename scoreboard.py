from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.current_high_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"SCORE: {self.score} High Score: {self.current_high_score}", align = ALIGNMENT, font = FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.current_high_score:
            self.current_high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.score))


        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align = ALIGNMENT, font = FONT)

