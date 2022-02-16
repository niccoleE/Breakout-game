import time
from turtle import TurtleScreen
from objects import Brick, Ball, Scoreboard, Paddle
from tkinter import Tk, Canvas, Button


def play():
    root = Tk()
    root.title("Breakout Game")
    root.config(bg="white")

    canvas = Canvas(root, width=780, height=600)
    canvas.config(width=780, height=600)
    canvas.grid(column=0, row=0)

    screen = TurtleScreen(canvas)
    screen.tracer(0)

    # # create rows of bricks
    bricks_list = []
    start_x = -360
    for _ in range(13):
        red_brick = Brick(screen, "red", start_x, 220)
        red_down_brick = Brick(screen, "red", start_x, 200)
        orange_brick = Brick(screen, "orange", start_x, 180)
        orange_down_brick = Brick(screen, "orange", start_x, 160)
        yellow_brick = Brick(screen, "yellow", start_x, 140)
        yellow_down_brick = Brick(screen, "yellow", start_x, 120)
        green_brick = Brick(screen, "green", start_x, 100)
        green_down_brick = Brick(screen, "green", start_x, 80)
        start_x += 60
        bricks_list.append(red_brick)
        bricks_list.append(red_down_brick)
        bricks_list.append(orange_brick)
        bricks_list.append(orange_down_brick)
        bricks_list.append(yellow_brick)
        bricks_list.append(yellow_down_brick)
        bricks_list.append(green_brick)
        bricks_list.append(green_down_brick)

    scoreboard = Scoreboard(screen)
    scoreboard.update_score()
    paddle = Paddle(screen)
    paddle.goto(0, -240)

    ball = Ball(screen)

    screen.listen()
    screen.onkeypress(paddle.move_right, "Right")
    screen.onkeypress(paddle.move_left, "Left")

    paddle.ondrag(paddle.dragging)

    is_on = True

    while is_on:
        screen.update()
        ball.move()
        if ball.xcor() > 375 or ball.xcor() < -375:
            ball.bounce_x()
        if ball.ycor() > 280:
            ball.bounce_y()

        if ball.distance(paddle) < 63 and -220 > ball.ycor() > -240:
            ball.bounce_y()
        elif ball.ycor() < -320:
            time.sleep(1)
            paddle.color("#091353")
            paddle.goto(-0, -240)
            ball.goto(-0, -220)
            scoreboard.lose_turn()

        for brick in bricks_list:
            if ball.distance(brick) < 30:
                ball.bounce_y()
                if brick.fillcolor() != "LightGray" and brick.ycor() >= 160:
                    scoreboard.add_points(5)
                    brick.fillcolor("LightGray")
                else:
                    scoreboard.add_points(1)
                    bricks_list.remove(brick)
                    brick.goto(1000, 0)

        if scoreboard.turns == 0:
            scoreboard.game_over = "GAME OVER"
            scoreboard.update_score()
            canvas.config(height=570)
            ball.goto(800, 0)
            paddle.goto(800, 0)
            play_button = Button(root, text="PLAY", height=2, width=10, command=lambda: [root.destroy(), play()])
            play_button.grid(row=1, column=0, padx=30)
            is_on = False

    root.mainloop()


play()
