from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.pencolor('#94d2bd')
        self.hideturtle()
        self.score = 0
        self.setpos(350, 250)
        self.level = 1
        self.lives = 10
        self.update_score()

    def update_score(self):
        self.clear()
        self.setpos(350, 260)
        self.write(f"Level {self.level}", align='center', font=('Courier', 16, 'bold'))
        self.setpos(350, 230)
        self.write(f"Score: {self.score}", align='center', font=('Courier', 20, 'bold'))
        self.setpos(-350, 245)
        self.pencolor('red3')
        self.write(f"{self.lives}❤️", align='center', font=('Courier', 24, 'bold'))
        self.pencolor('#94d2bd')

    def increase_score(self, amount):
        self.score += amount
        self.update_score()

    def increase_level(self):
        self.level += 1
        self.update_score()

    def game_over_screen(self):
        self.clear()
        self.setpos(0, 0)
        self.pencolor("#f94144")
        self.write(f"GAME OVER", align='center', font=('Courier', 24, 'bold'))
        self.setpos(0, -30)
        self.write(f"Your final score is {self.score}", align='center', font=('Courier', 24, 'bold'))



