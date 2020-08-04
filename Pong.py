import turtle  # basic module that comes pre-installed for games

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)  # stops window from updating. Helps speed up games

# Score
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()  # T = class name

paddle_a.speed(0)  # speed of animation. Sets speed to max possible speed

paddle_a.shape("square")

paddle_a.color("white")

# 1 keeps at default, 5 imples 5 times
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()

paddle_a.goto(-350, 0)  # 0,0 is in the middle


# Paddle B
paddle_b = turtle.Turtle()  # T = class name

paddle_b.speed(0)  # speed of animation. Sets speed to max possible speed

paddle_b.shape("square")

paddle_b.color("white")

# 1 keeps at default, 5 imples 5 times
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()

paddle_b.goto(350, 0)  # 0,0 is in the middle


# Ball

ball = turtle.Turtle()  # T = class name

ball.speed(0)  # speed of animation. Sets speed to max possible speed
ball.shape("square")

ball.color("white")

# 1 keeps at default, 5 imples 5 times
ball.penup()

ball.goto(0, 0)  # 0,0 is in the middle

# Ball Movement
ball.dx = 0.1
ball.dy = 0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)  # animation speed
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center",
          font=("Courier", 24, "normal"))


# Functions for gameplay


def paddle_a_up():
    y = paddle_a.ycor()  # holds current y coordinate of paddle_a
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()  # holds current y coordinate of paddle_a
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()  # holds current y coordinate of paddle_a
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()  # holds current y coordinate of paddle_a
    y -= 20
    paddle_b.sety(y)

# Keyboard binding


wn.listen()  # listen for keyboard inputs
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main game loop


while True:
    wn.update()  # updates screen every time loop runs

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # reverses direction (dy = -0.25)

    if ball.ycor() < -290:
        ball.sety(290)
        ball.dy *= -1

    if ball.xcor() > 390:  # 400 left, 400 right, 800 total
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1  # when ball goes off right side of the screen
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))

    if ball.xcor() < -390:  # 400 left, 400 right, 800 total
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1  # when ball goes off the left side
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))

    # Paddle and ball collision

    if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball_dx = ball_dx * -1

    if(ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball_dx = ball_dx * -1
