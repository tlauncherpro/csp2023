import turtle as trtl
import random as rand
import leaderboard as lb

t_color = "red"
t_size = 3
t_shape = "circle"
score = 0
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000
timer_up = False

leaderboard_file_name = "leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input ("enter your name:")

c = trtl.Turtle()
c.shape(t_shape)
c.shapesize(t_size)
c.fillcolor(t_color)

score_write = trtl.Turtle()
score_write.penup()
score_write.goto(150,-200)
score_write.hideturtle()

timer_write = trtl.Turtle()
timer_write.penup()
timer_write.goto(50,200)
timer_write.hideturtle()

def c_clicked(x,y):
  global timer
  if(timer > 0):
    update_score()
    change_pos()
  else:
    c.hideturtle()
def change_pos():
  new_x = rand.randint(-200,200)
  new_y = rand.randint(-200,200)
  c.penup()
  c.hideturtle()
  c.goto(new_x,new_y)
  c.showturtle()
  c.pendown()
  
def update_score():
  global score
  score += 1
  score_write.clear()
  score_write.write(score,font=font_setup)

def countdown():
  global timer, timer_up
  timer_write.clear()
  if timer <= 0:
    timer_write.write("time over", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    timer_write.write("timer: " + str(timer), font=font_setup)
    timer -= 1
    timer_write.getscreen().ontimer(countdown, counter_interval)
    
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global c

  
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > int(leader_scores_list[4])):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, c, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, c, score)

wn = trtl.Screen()
c.onclick(c_clicked)
countdown()
wn.mainloop()