from turtle import RawTurtle, TurtleScreen


class Paddle(RawTurtle):
    def __init__(self, screen):
        super().__init__(screen)
        self.shape("square")
        self.color("#091353")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()

    def move_right(self):
        if self.xcor() < 340:
            new_x = self.xcor() + 20
            self.goto(new_x, self.ycor())

    def move_left(self):
        if self.xcor() > -340:
            new_x = self.xcor() - 20
            self.goto(new_x, self.ycor())

    def dragging(self, x, y):
        y = - 240
        if -340 < x < 340:
            self.goto(x, y)


class Brick(RawTurtle):

    def __init__(self, screen, color, brick_x, brick_y):
        super().__init__(screen)
        self.shape("square")
        self.fillcolor(color)
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.goto(brick_x, brick_y)


class Ball(RawTurtle):

    def __init__(self, screen):
        super().__init__(screen)
        self.shape("circle")
        self.color("#091353")
        self.penup()
        self.step_y = 4
        self.step_x = 4

    def move(self):
        new_x = self.xcor() + self.step_x
        new_y = self.ycor() + self.step_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.step_y *= -1

    def bounce_x(self):
        self.step_x *= -1


class Scoreboard(RawTurtle):

    def __init__(self, screen):
        super().__init__(screen)
        self.color("#091353")
        self.penup()
        self.hideturtle()
        self.turns = 3
        self.score = 0
        self.game_over = ""
        self.update_score()

    def update_score(self):
        self.goto(320, 250)
        self.write(f"points {self.score}", align="center", font=("Arial", 20, "normal"))
        self.goto(-270, 250)
        self.write(f"turns {self.turns}", align="center", font=("Arial", 20, "normal"))
        self.goto(0, -20)
        self.write(self.game_over, align="center", font=("Arial", 40, "normal"))

    def add_points(self, point):
        self.clear()
        self.score += point
        self.update_score()

    def lose_turn(self):
        self.clear()
        self.turns -= 1
        self.update_score()
