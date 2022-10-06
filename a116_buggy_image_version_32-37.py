#   a116_ladybug.py
import turtle as trtl

# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)

# legs
ladybug.pensize(10)
legs = 6
rotation = 360/legs
for i in range(legs):
  ladybug.setheading(rotation*i)
  ladybug.goto(0,-37)
  ladybug.forward(70)

# and body
ladybug.setheading(0)
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 2
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots

for i in range(num_dots):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)
    # position next dots
  xpos = xpos + 5
  ypos = ypos + 25





ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()