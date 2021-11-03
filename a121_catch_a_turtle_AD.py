# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
spot = trtl.Turtle()
import random as rand
#-----game configuration----
spot_color = "red"
spot_size = 2
spot_shape = "circle"
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)
def spot_clicked(x, y):
  print("Spot was clicked!")
def change_position():
  rand.randint(a,b)
#-----initialize turtle-----
score = 0 

# circular turtle will not use a global variable
spot = trtl.Turtle()
spot.goto(-100, 0)
spot.shape("circle")
spot.shapesize(3)

# square shaped turtle will use a global variable
box = trtl.Turtle()
box.goto(100,0)
box.shape("square")
box.shapesize(3)

# attempts to update the score for spot, but will not work because this function
# does not have access to the score that was created above
def update_score_for_spot(x,y):
  score += 1
  print(score)

# update_score_for_box will update the score for spot
def update_score_for_box(x,y):
  global score # gives this function access to the score that was created above
  score += 1
  print(score)

#-----countdown variables-----
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----countdown writer-----
counter =  trtl.Turtle()

#-----game functions-----
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
    
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()
#---------events----------
spot.onclick(update_score_for_spot)
box.onclick(update_score_for_box)
#---------events---------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.mainloop()