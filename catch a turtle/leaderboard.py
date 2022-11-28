bronze_score = 15
silver_score = 20
gold_score = 25

def load_leaderboard(file_name, leader_names, leader_scores):

  leaderboard_file = open(file_name, "r")  

  for line in leaderboard_file:
    leader_name = ""
    leader_score = ""    
    index = 0
    
    while (line[index] != ","):
      leader_name = leader_name + line[index] 
      index = index + 1
    
    leader_names.append(leader_name)
    
    index = index + 1
    while (line[index] != "\n"):
      leader_score = leader_score + line[index] 

      index = index + 1

    leader_scores.append(leader_score)

  leaderboard_file.close()

def update_leaderboard(file_name, leader_names, leader_scores, player_name, player_score):

  leader_index = 0
  
  while (leader_index < len(leader_scores)):
    
    if (player_score >= int(leader_scores[leader_index])):
      break
    else:
      leader_index = leader_index + 1
  
  leader_scores.insert(leader_index, player_score)
  leader_names.insert(leader_index, player_name)
  
  if (len(leader_names) == 6):
      leader_names.pop(5)
  if (len(leader_scores) == 6):
      leader_scores.pop(5)
  
  leaderboard_file = open(file_name, "w") 
  leader_index = 0
  
  while (leader_index < len(leader_names)):
    leaderboard_file.write(leader_names[leader_index] + "," + str(leader_scores[leader_index]) + "\n")
    leader_index = leader_index + 1
  
  leaderboard_file.close()
  
def draw_leaderboard(leader_names, leader_scores, high_scorer, turtle_object, player_score):
  
  font_setup = ("Arial", 20, "normal")
  turtle_object.clear()
  turtle_object.penup()
  turtle_object.goto(-200,100)
  turtle_object.hideturtle()
  turtle_object.down()
  leader_index = 0

  while leader_index < len(leader_names):
    turtle_object.write(str(leader_index + 1) + "\t" + leader_names[leader_index] + "\t" + str(leader_scores[leader_index]), font=font_setup)
    turtle_object.penup()
    turtle_object.goto(-200,int(turtle_object.ycor())-50)
    turtle_object.down()
    leader_index = leader_index + 1

  if (high_scorer):
    turtle_object.write("you made the leaderboard", font=font_setup)
  else:
    turtle_object.write("L", font=font_setup)

  turtle_object.penup()
  turtle_object.goto(-200,int(turtle_object.ycor())-50)
  turtle_object.pendown()
  
  if (player_score >= bronze_score and player_score < silver_score):
    turtle_object.write("... bronze", font=font_setup)
  elif (player_score >= silver_score and player_score < gold_score):
    turtle_object.write("... silver", font=font_setup)
  elif (player_score >= gold_score):
    turtle_object.write("... gold", font=font_setup)
  