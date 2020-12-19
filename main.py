import turtle
import winsound

win = turtle.Screen()
canvas = win.getcanvas()
root = canvas.winfo_toplevel()
win.title('Pong by')
win.bgcolor('darkblue')
win.setup(width=800, height=600)
win.tracer(0)

score_a = 0
score_b = 0

a = turtle.Turtle()
a.speed(0)
a.shape('square')
a.color('red')
a.shapesize(stretch_wid=5, stretch_len=1)
a.penup()
a.goto(-350, 0)

b = turtle.Turtle()
b.speed(0)
b.shape('square')
b.color('white')
b.shapesize(stretch_wid=5, stretch_len=1)
b.penup()
b.goto(350, 0)

ball = turtle.Turtle()
ball.speed()
ball.shape('circle')
ball.color('orange')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.8
ball.dy = -0.8

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Player A: 0  AI: 0', align="center", font=("Courier", 24, "italic"))


def a_up():
    y = a.ycor()
    y += 20
    a.sety(y)


def a_down():
    y = a.ycor()
    y -= 20
    a.sety(y)


def b_up():
    y = b.ycor()
    y += 20
    b.sety(y)


def b_down():
    y = b.ycor()
    y -= 20
    b.sety(y)
def close():
    global Continue
    Continue = False

win.listen()
win.onkeypress(a_up, "w")
win.onkeypress(a_down, "s")
win.onkeypress(b_up, "Up")
win.onkeypress(b_down, "Down")
root.protocol("WM_DELETE_WINDOW", close)
Continue = True

while Continue:
    win.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f'Player A: {score_a} AI: {score_b}', align="center", font=("Courier", 24, "italic"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f'Player A:{score_a} AI: {score_b}', align="center", font=("Courier", 24, "italic"))

    if a.ycor() > 260:
        a.goto(-350, 260)

    if a.ycor() < -240:
        a.goto(-350, -240)

    if b.ycor() > 260:
        b.goto(350, 260)

    if b.ycor() < -240:
        b.goto(350, -240)

    if ball.xcor() > 330 and ball.xcor() < 340 and (ball.ycor() < b.ycor() + 40 and ball.ycor() > b.ycor() - 40):
        ball.setx(330)
        ball.dx *= -1
        winsound.PlaySound("pongbounce.wav", winsound.SND_ASYNC)

    if ball.xcor() < -330 and ball.xcor() > -340 and (ball.ycor() < a.ycor() + 40 and ball.ycor() > a.ycor() - 40):
        ball.setx(-330)
        ball.dx *= -1
        winsound.PlaySound("pongbounce.wav", winsound.SND_ASYNC)

    if b.ycor() < ball.ycor() and abs(b.ycor() - ball.ycor()) > 10:
        b_up()

    elif b.ycor() > ball.ycor() and abs(b.ycor() - ball.ycor()) > 10:
        b_down()
