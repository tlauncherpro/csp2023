#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
painter = trtl.Turtle()

# create body
painter.pensize(40)
painter.circle(20)

# configure legs
legs = 8
length = 70
rotation_increment = 360 / legs
painter.pensize(5)
n = 0

# draw legs
while (n < legs/2):
  painter.goto(0,20)
  painter.setheading(rotation_increment*n/2-45)
  painter.forward(length)
  n = n + 1

while (n < legs):
  painter.goto(0,20)
  painter.setheading(rotation_increment*n/2+45)
  painter.forward(length)
  n = n + 1

painter.color("red")
painter.penup()

painter.goto(-10,20)
painter.pendown()
painter.circle(3)
painter.penup()

painter.goto(10,20)
painter.pendown()
painter.circle(3)
painter.penup()


painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()