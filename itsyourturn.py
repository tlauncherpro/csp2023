import turtle as trtl

painter = trtl.Turtle()

painter.pensize(5)

for i in range(90):
    painter.forward(4)
    painter.left(4)

painter.penup()
painter.goto(0, 20)
painter.pendown()

for i in range(10):
    painter.forward(4)
    painter.left(4)
painter.right(40)

painter.penup()
painter.goto(0, 20)
painter.pendown()

painter.right(180)
for i in range(10):
    painter.forward(4)
    painter.right(4)
painter.left(40)

painter.penup()
painter.goto(-25, 60)
painter.pendown()

painter.dot()

painter.penup()
painter.goto(25, 60)
painter.pendown()

painter.dot()

painter.penup()
painter.goto(-25, 5)
painter.pendown()

painter.left(70)
for i in range(10):
    painter.forward(8)
    painter.left(4)

painter.left(50)
for i in range(8):
    painter.forward(8)
    painter.left(4)

painter.left(50)
for i in range(12):
    painter.forward(8)
    painter.left(4)

painter.right(140)
painter.forward(80)

painter.penup()
painter.goto(-25, 5)
painter.pendown()

painter.right(90)
painter.forward(80)

painter.penup()
painter.goto(-30, -70)
painter.pendown()

painter.left(10)
painter.forward(80)

painter.penup()
painter.goto(35, -80)
painter.pendown()

painter.left(30)
painter.forward(80)

wn = trtl.Screen()
wn.mainloop()