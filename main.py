import turtle
import winsound

window = turtle.Screen()
canvas = window.getcanvas()
root = canvas.winfo_toplevel()
window.title("PinPong")
window.bgcolor("orange")
window.setup(width=800, height=600)
window.tracer(0)

racket_a = turtle.Turtle()
racket_a.speed(0)
racket_a.shape('square')
racket_a.color('black')
racket_a.penup()
racket_a.goto(-350, 0)
racket_a.shapesize(5, 1)

racket_b = turtle.Turtle()
racket_b.speed(0)
racket_b.shape('square')
racket_b.color('white')
racket_b.penup()
racket_b.goto(350, 0)
racket_b.shapesize(5, 1)

ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('red')
ball.penup()
ball.dx = 0.15
ball.dy = 0.15

write = turtle.Turtle()
write.speed(0)
write.color('white')
write.penup()
write.goto(0, 260)
write.write("Player A:0   Player B:0",
            align='center', font=('Courier', 24, 'bold'))
write.hideturtle()
point_a = 0
point_b = 0


def racket_a_up():
    y = racket_a.ycor()
    y = y + 20
    racket_a.sety(y)


def racket_a_down():
    y = racket_a.ycor()
    y = y - 20
    racket_a.sety(y)


def racket_b_up():
    y = racket_b.ycor()
    y = y + 20
    racket_b.sety(y)


def racket_b_down():
    y = racket_b.ycor()
    y = y - 20
    racket_b.sety(y)


def close():
    global Continue
    Continue = False

window.listen()
window.onkeypress(racket_a_up, 'w')
window.onkeypress(racket_a_down, 's')
window.onkeypress(racket_b_up, 'Up')
window.onkeypress(racket_b_down, 'Down')

root.protocol("WM_DELETE_WINDOW", close)
Continue = True

while Continue:
    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy = ball.dy * -1

    if ball.xcor() > 390:
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx = ball.dx * -1
        point_a = point_a + 1
        write.clear()
        write.write("Player A:{}   Player B:{}".format(point_a, point_b),
                    align='center', font=('Courier', 24, 'bold'))
    if ball.xcor() < -390:
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx = ball.dx * -1
        point_b = point_b + 1
        write.clear()
        write.write("Player A:{}   Player B:{}".format(point_a, point_b),
                    align='center', font=('Courier', 24, 'bold'))

    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < racket_b.ycor() + 60 and
            ball.ycor() > racket_b.ycor() - 60):
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        ball.setx(340)
        ball.dx = ball.dx * -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < racket_a.ycor() + 60 and
            ball.ycor() > racket_a.ycor() - 60):
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        ball.setx(-340)
        ball.dx = ball.dx * -1
