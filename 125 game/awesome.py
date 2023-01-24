import turtle as trtl
import random as rand

circle_image = "circle.gif"
ground_height = 0
circle_letter_x_offset = -25
circle_letter_y_offset = -50
screen_width = 400
screen_height = 400
number_of_circles = 26
circle_letters = []
circle_list = []
current_letter = "."
letter_list = ["A","B","C","D","F","E","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(circle_image)

wn.bgpic("map.gif")
wn.tracer(False)

def reset_circle(active_circle):
  global current_letter
  length_of_list = len(letter_list)
  if (length_of_list != 0):
    index = rand.randint(0,length_of_list-1)
    active_circle.goto(rand.randint(-(screen_width)/2, (screen_width)/2), rand.randint(-(screen_height)/2, (screen_height)/2))
    current_letter = letter_list.pop(index)
    draw_circle(active_circle, current_letter)
    circle_letters.append(current_letter)

def draw_circle(active_circle, letter):
  active_circle.shape(circle_image)
  active_circle.showturtle()

  wn.update()

for i in range(0, number_of_circles):
  active_circle = trtl.Turtle(shape = circle_image)
  active_circle.penup()
  reset_circle(active_circle)
  circle_list.append(active_circle)

def fall(letter):
  wn.tracer(True)
  index = circle_letters.index(letter)
  circle_letters.pop(index)
  active_circle = circle_list.pop(index)
  active_circle.clear()
  active_circle.hideturtle()
  wn.tracer(False)
  reset_circle(active_circle)
  circle_list.append(active_circle)

def check_circle_a():
  if ("A" in circle_letters):
    fall("A")

def check_circle_b():
  if ("B" in circle_letters):
    fall("B")

def check_circle_c():
  if ("C" in circle_letters):
    fall("C")

def check_circle_d():
  if ("D" in circle_letters):
    fall("D")

def check_circle_e():
  if ("E" in circle_letters):
    fall("E")

def check_circle_f():
  if ("F" in circle_letters):
    fall("F")

def check_circle_g():
  if ("G" in circle_letters):
    fall("G")

def check_circle_h():
  if ("H" in circle_letters):
    fall("H")

def check_circle_i():
  if ("I" in circle_letters):
    fall("I")

def check_circle_j():
  if ("J" in circle_letters):
    fall("J")

def check_circle_k():
  if ("K" in circle_letters):
    fall("K")

def check_circle_l():
  if ("L" in circle_letters):
    fall("L")

def check_circle_m():
  if ("M" in circle_letters):
    fall("M")

def check_circle_n():
  if ("N" in circle_letters):
    fall("N")

def check_circle_o():
  if ("O" in circle_letters):
    fall("O")

def check_circle_p():
  if ("P" in circle_letters):
    fall("P")

def check_circle_q():
  if ("Q" in circle_letters):
    fall("Q")

def check_circle_r():
  if ("R" in circle_letters):
    fall("R")

def check_circle_s():
  if ("S" in circle_letters):
    fall("S")

def check_circle_t():
  if ("T" in circle_letters):
    fall("T")

def check_circle_u():
  if ("U" in circle_letters):
    fall("U")

def check_circle_v():
  if ("V" in circle_letters):
    fall("V")

def check_circle_w():
  if ("W" in circle_letters):
    fall("W")

def check_circle_x():
  if ("X" in circle_letters):
    fall("X")

def check_circle_y():
  if ("Y" in circle_letters):
    fall("Y")

def check_circle_z():
  if ("Z" in circle_letters):
    fall("Z")

wn.onkeypress(check_circle_a, "a")
wn.onkeypress(check_circle_b, "b")
wn.onkeypress(check_circle_c, "c")
wn.onkeypress(check_circle_d, "d")
wn.onkeypress(check_circle_e, "e")
wn.onkeypress(check_circle_f, "f")
wn.onkeypress(check_circle_g, "g")
wn.onkeypress(check_circle_h, "h")
wn.onkeypress(check_circle_i, "i")
wn.onkeypress(check_circle_j, "j")
wn.onkeypress(check_circle_k, "k")
wn.onkeypress(check_circle_l, "l")
wn.onkeypress(check_circle_m, "m")
wn.onkeypress(check_circle_n, "n")
wn.onkeypress(check_circle_o, "o")
wn.onkeypress(check_circle_p, "p")
wn.onkeypress(check_circle_q, "q")
wn.onkeypress(check_circle_r, "r")
wn.onkeypress(check_circle_s, "s")
wn.onkeypress(check_circle_t, "t")
wn.onkeypress(check_circle_u, "u")
wn.onkeypress(check_circle_v, "v")
wn.onkeypress(check_circle_w, "w")
wn.onkeypress(check_circle_x, "x")
wn.onkeypress(check_circle_y, "y")
wn.onkeypress(check_circle_z, "z")

wn.listen()
trtl.mainloop()