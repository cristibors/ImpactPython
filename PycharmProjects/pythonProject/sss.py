import turtle
turtle.setup(900,400)
wn = turtle.Screen()
wn.title("Turtle writing my name: IDAN")
wn.bgcolor("lightgreen")
turtle.width(30)
# turtle.pensize(30)

t = turtle.Turtle()
t.up()
t.backward(360)
t.left(90)
t.backward(80)
t.down()
t.forward(250)
t.right(90)
t.forward(62.5)
t.backward(62.5 * 2)
t.forward(62.5)
t.right(90)
t.forward(250)
t.right(90)
t.forward(62.5)
t.backward(62.5 * 2)
t.up()
t.backward(100)
t.right(90)
t.down()
t.forward(250)
t.right(90)
for x in range(180):
    .t.forward(2.2)  # adjust HERE to get different size of circle
    t.right(1)
    t.up()
    t.right(90)
    t.forward(230)
    t.right(90)
    t.forward(4 * 62.5)
    t.right(65)
    t.down()
    t.forward(250)
    t.right(180)
    t.forward(275)
    t.left(135)
    t.forward(250)
    t.right(180)
    t.forward(120)
    t.right(70)
    t.forward(110)
    t.right(90)
    t.up()
    t.forward(115)
    t.left(90)
    t.forward(1.5 * 62.5)
    t.left(90)
    t.down()
    t.forward(250)
    t.right(145)
    t.forward(320)
    t.left(145)
    t.forward(250)

    wn.mainloop()
