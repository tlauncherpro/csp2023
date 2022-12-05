import turtle as trtl
import random as rand

apple_image = "apple.gif"
ground_height = -200
apple_letter_x_offset = -25
apple_letter_y_offset = -50
screen_width = 400
screen_height = 400
number_of_apples = 26
apple_letters = []
apple_list = []
current_letter = "."
letter_list = ["A","B","C","D","F","E","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)

wn.bgpic("background.gif")
wn.tracer(False)

def reset_apple(active_apple):
  global current_letter
  length_of_list = len(letter_list)
  if (length_of_list != 0):
    index = rand.randint(0,length_of_list-1)
    active_apple.goto(rand.randint(-(screen_width)/2, (screen_width)/2), rand.randint(-(screen_height)/2, (screen_height)/2))
    current_letter = letter_list.pop(index)
    draw_apple(active_apple, current_letter)
    apple_letters.append(current_letter)

def write_letter(active_apple, letter):
  active_apple.color("white")
  remember_position = active_apple.position()
  active_apple.setpos(active_apple.xcor() + apple_letter_x_offset,active_apple.ycor() + apple_letter_y_offset)
  active_apple.write(letter, font=("Arial", 52, "bold"))
  active_apple.setpos(remember_position)

def draw_apple(active_apple, letter):
  active_apple.shape(apple_image)
  active_apple.showturtle()
  write_letter(active_apple, letter)
  wn.update()

for i in range(0, number_of_apples):
  active_apple = trtl.Turtle(shape = apple_image)
  active_apple.penup()
  reset_apple(active_apple)
  apple_list.append(active_apple)

def fall(letter):
  wn.tracer(True)
  index = apple_letters.index(letter)
  apple_letters.pop(index)
  active_apple = apple_list.pop(index)
  active_apple.goto(active_apple.xcor(), ground_height)
  active_apple.clear()
  active_apple.hideturtle()
  wn.tracer(False)
  reset_apple(active_apple)
  apple_list.append(active_apple)

def check_apple_a():
  if ("A" in apple_letters):
    fall("A")

def check_apple_b():
  if ("B" in apple_letters):
    fall("B")

def check_apple_c():
  if ("C" in apple_letters):
    fall("C")

def check_apple_d():
  if ("D" in apple_letters):
    fall("D")

def check_apple_e():
  if ("E" in apple_letters):
    fall("E")

def check_apple_f():
  if ("F" in apple_letters):
    fall("F")

def check_apple_g():
  if ("G" in apple_letters):
    fall("G")

def check_apple_h():
  if ("H" in apple_letters):
    fall("H")

def check_apple_i():
  if ("I" in apple_letters):
    fall("I")

def check_apple_j():
  if ("J" in apple_letters):
    fall("J")

def check_apple_k():
  if ("K" in apple_letters):
    fall("K")

def check_apple_l():
  if ("L" in apple_letters):
    fall("L")

def check_apple_m():
  if ("M" in apple_letters):
    fall("M")

def check_apple_n():
  if ("N" in apple_letters):
    fall("N")

def check_apple_o():
  if ("O" in apple_letters):
    fall("O")

def check_apple_p():
  if ("P" in apple_letters):
    fall("P")

def check_apple_q():
  if ("Q" in apple_letters):
    fall("Q")

def check_apple_r():
  if ("R" in apple_letters):
    fall("R")

def check_apple_s():
  if ("S" in apple_letters):
    fall("S")

def check_apple_t():
  if ("T" in apple_letters):
    fall("T")

def check_apple_u():
  if ("U" in apple_letters):
    fall("U")

def check_apple_v():
  if ("V" in apple_letters):
    fall("V")

def check_apple_w():
  if ("W" in apple_letters):
    fall("W")

def check_apple_x():
  if ("X" in apple_letters):
    fall("X")

def check_apple_y():
  if ("Y" in apple_letters):
    fall("Y")

def check_apple_z():
  if ("Z" in apple_letters):
    fall("Z")

wn.onkeypress(check_apple_a, "a")
wn.onkeypress(check_apple_b, "b")
wn.onkeypress(check_apple_c, "c")
wn.onkeypress(check_apple_d, "d")
wn.onkeypress(check_apple_e, "e")
wn.onkeypress(check_apple_f, "f")
wn.onkeypress(check_apple_g, "g")
wn.onkeypress(check_apple_h, "h")
wn.onkeypress(check_apple_i, "i")
wn.onkeypress(check_apple_j, "j")
wn.onkeypress(check_apple_k, "k")
wn.onkeypress(check_apple_l, "l")
wn.onkeypress(check_apple_m, "m")
wn.onkeypress(check_apple_n, "n")
wn.onkeypress(check_apple_o, "o")
wn.onkeypress(check_apple_p, "p")
wn.onkeypress(check_apple_q, "q")
wn.onkeypress(check_apple_r, "r")
wn.onkeypress(check_apple_s, "s")
wn.onkeypress(check_apple_t, "t")
wn.onkeypress(check_apple_u, "u")
wn.onkeypress(check_apple_v, "v")
wn.onkeypress(check_apple_w, "w")
wn.onkeypress(check_apple_x, "x")
wn.onkeypress(check_apple_y, "y")
wn.onkeypress(check_apple_z, "z")

wn.listen()
trtl.mainloop()