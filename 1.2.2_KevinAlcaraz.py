# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random
import turtle as score_writer
import leaderboard as lb 

#-----game configuration----
shape ="turtle"
size = 10
color = "orange"
score = 0

font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#leaderboard variables

leaderboard_file_name="a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("please enter name")

#-----initialize turtle-----
juan = trtl.Turtle(shape=shape)
juan.color(color) 
juan.shapesize(size)

score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(-450,350)

font = ("arial", 30, "bold")
score_writer.write("score", font=font)

score_writer.ht()

counter =  trtl.Turtle()

#-----game functions--------
def turtle_clicked(x,y):
    print("juan get clicked")
    change_postion()
    score_counter()
    juan.speed(0)
    change_size()



def change_postion():
    juan.penup()
    juan.ht()
    new_xpos = random.randint(-400,400)
    new_ypos = random.randint(-400,400)
    juan.goto(new_xpos, new_ypos)
    juan.st()

def score_counter():
    global score
    score += 1
    print(score)
    score_writer.clear()
    score_writer.write(score, font = font )

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0: 
    counter.penup()
    counter.goto(-50,300)
    counter.pendown()
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    
    
    game_over()
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
    counter.ht()
    counter.penup()
    counter.goto(350,370)
    counter.pendown()

def game_over():
    juan.ht()
    juan.goto(500,500)
    wn.bgcolor("red")


def change_size(): #another change
    global size
    if size >= 1:
      size -=  1
      juan.shapesize(size)

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global juan

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, juan, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, juan, score)

#-----events----------------
juan.onclick(turtle_clicked)
wn = trtl.Screen()
wn.bgcolor("blue") # one of my changes to the game
wn.ontimer(countdown, counter_interval) 
wn.mainloop()
