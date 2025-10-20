import turtle
import tkinter as tk
from threading import Thread

def start_game():
    def game_loop():
        # setup window ======================
        window = turtle.Screen()
        window.title("Ping Pong Game By Mohamed")
        window.setup(width=800, height=600)
        window.tracer(0)  # set delay for update drawings
        window.bgcolor(.1, .1, .1)

        # setup game objects =================
        # ball
        ball = turtle.Turtle()
        ball.speed(0)  # drawing speed(fastest)
        ball.shape("circle")
        ball.color("white")
        ball.shapesize(stretch_len=1, stretch_wid=1)
        ball.goto(0, 0)  # start position
        ball.penup()
        ball_dx, ball_dy = 1, 1
        ball_speed = .5

        # center line
        center_line = turtle.Turtle()
        center_line.speed(0)
        center_line.shape("square")
        center_line.color("white")
        center_line.shapesize(stretch_len=.1, stretch_wid=25)
        center_line.penup()
        center_line.goto(0, 0)

        # player1
        player1 = turtle.Turtle()
        player1.speed(0)
        player1.shape("square")
        player1.shapesize(stretch_len=1, stretch_wid=5)
        player1.color("yellow")
        player1.penup()
        player1.goto(-350, 0)

        # player2
        player2 = turtle.Turtle()
        player2.speed(0)
        player2.shape("square")
        player2.shapesize(stretch_len=1, stretch_wid=5)
        player2.color("red")
        player2.penup()
        player2.goto(350, 0)

        # score text
        score = turtle.Turtle()
        score.speed(0)
        score.color("white")
        score.penup()
        score.goto(0, 260)
        score.write("Player1: 0 Player2: 0", align="center", font=("Courier", 14, "normal"))
        score.hideturtle()
        p1_score, p2_score = 0, 0

        # Players Movement ====================
        players_speed = 20

        def p1_move_up():
            player1.sety(player1.ycor() + players_speed)

        def p1_move_down():
            player1.sety(player1.ycor() - players_speed)

        def p2_move_up():
            player2.sety(player2.ycor() + players_speed)

        def p2_move_down():
            player2.sety(player2.ycor() - players_speed)

        window.listen()
        window.onkeypress(p1_move_up, "w")
        window.onkeypress(p1_move_down, "s")
        window.onkeypress(p2_move_up, "e")
        window.onkeypress(p2_move_down, "f")

        # game loop ==========================
        while True:
            window.update()

            # ball movement
            ball.setx(ball.xcor() + (ball_dx * ball_speed))
            ball.sety(ball.ycor() + (ball_dy * ball_speed))

            # ball & borders collisions
            if ball.ycor() > 290:
                ball.sety(290)
                ball_dy *= -1

            if ball.ycor() < -290:
                ball.sety(-290)
                ball_dy *= -1

            # ball & players collisions
            if ball.xcor() < -340 and ball.xcor() > -350 and player1.ycor()-60 < ball.ycor() < player1.ycor()+60:
                ball.setx(-340)
                ball_dx *= -1

            if ball.xcor() > 340 and ball.xcor() < 350 and player2.ycor()-60 < ball.ycor() < player2.ycor()+60:
                ball.setx(340)
                ball_dx *= -1

            # score handling
            if ball.xcor() > 390:
                ball.goto(0, 0)
                ball_dx *= -1
                score.clear()
                p1_score += 1
                score.write(f"Player1: {p1_score} Player2: {p2_score}", align="center", font=("Courier", 14, "normal"))

            if ball.xcor() < -390:
                ball.goto(0, 0)
                ball_dx *= -1
                score.clear()
                p2_score += 1
                score.write(f"Player1: {p1_score} Player2: {p2_score}", align="center", font=("Courier", 14, "normal"))

    # Run game in a separate thread to keep GUI responsive
    Thread(target=game_loop).start()

# Create GUI window
root = tk.Tk()
root.title("Ping Pong Game Launcher")
root.geometry("300x200")
root.resizable(False, False)

start_button = tk.Button(root, text="Start Game", font=("Arial", 12), command=start_game)
start_button.pack(pady=50)

root.mainloop()
