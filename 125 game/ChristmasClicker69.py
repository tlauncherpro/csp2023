
import turtle as trtl

#ben set up the code and found the images

click_shape = "circle.gif"

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(click_shape)
score = 0

wn.bgpic("map.gif")
wn.tracer(False)

#troy used a list to store the values that can be used as key inputs

keys = ["g","h","b"]

trtl.goto(200,200)
trtl.shape(click_shape)

#troy defined where the circle goes when clicked

def draw_circle():
    trtl.shape(click_shape)
    trtl.showturtle()
    wn.update()
    
def click(key):
    wn.tracer(True)
    trtl.goto(100,100)
    trtl.goto(200,200)
    update_score()
    wn.tracer(False)

#ben wrote the code for the score writer that is used to track your score

score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-400,-400)
score_writer.pendown()

def update_score():
  global score
  score = score + 1
  score_writer.clear()
  score_writer.write(score, font=("Arial", 200, "bold"))

#troy wrote the code that checks for key inputs

def check_g():
  if ("g" in keys):
    click("g")

def check_h():
  if ("h" in keys):
    click("h")

def check_b():
  if ("b" in keys):
    click("b")

wn.onkeypress(check_g, "g")

wn.onkeypress(check_h, "h")

wn.onkeypress(check_h, "b")

wn.listen()






trtl.mainloop()
