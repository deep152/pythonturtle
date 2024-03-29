import turtle as trtl

wn = trtl.Screen()
#wn.trtl.bgpic('isc.jpg')
#wn.update()

#  screen size does the show the full car, drag to make the window bigger

#  list of colors 
colors = ['pink', '#ee0113', '#656565', '#040309', '#DC143C,', '#cf4944', '#008c45', '#F3E0BE', '#0c193c']
#                   red     dark grey   black    livery colors (w,r,g)               bg color    uc color


livery_g = trtl.Turtle()
livery_w = trtl.Turtle()
livery_r = trtl.Turtle()
wn.bgcolor('white')


#  settings for turtle
trtl.speed('fastest')
trtl.pensize(5)
trtl.pencolor(colors[3])
trtl.fillcolor(colors[1])
trtl.begin_fill()
trtl.turtlesize(1)

#  setting function to make a tire
def print_tire():
  trtl.pensize(45)
  trtl.pencolor(colors[3])
  trtl.circle(20)
  trtl.pencolor('#2d2d2d')
  trtl.pensize(30)
  trtl.circle(20)

#   starting point
trtl.penup()
trtl.goto(0,0)
trtl.pendown()

#   undercarriage
trtl.right(180)
trtl.pencolor('#0c193c')
trtl.forward(550)

#   go to right wheel
trtl.penup()
trtl.goto(-428.0,29.0)
trtl.pendown()

#   calling print_tire function to make wheel
print_tire()

#   go to left wheel
trtl.penup()
trtl.goto(19,29.0)
trtl.pendown()

#   calling print_tire function to make wheel
print_tire()

#  these numbers are steps of the back part of the car, listed in my notes check steps.jpg to see

#   3
trtl.pensize(5)
trtl.pencolor(colors[3])
trtl.penup()
trtl.goto(50.0,30.0)
trtl.pendown()
trtl.right(180)
trtl.forward(55)
trtl.fillcolor(colors[1])

#   4
trtl.left(60)
trtl.forward(55)
trtl.right(-300)

#   5
trtl.pencolor(colors[3])
trtl.backward(10)

#   6
trtl.right(90)
trtl.backward(45)

#   7
trtl.right(90)
trtl.backward(10)

#   8
trtl.right(90)
trtl.forward(25)

trtl.left(90)

#  back part of the car leading to roof
''''
i = 1
while i < 34:
  trtl.forward(2.5)
  trtl.right(0.4)
  i-=1
'''
for rear in range(35):
  trtl.forward(2.5)
  trtl.right(0.4)

trtl.forward(150)

#   go to start of bumper
trtl.penup()
trtl.goto(0,0)

trtl.right(346)
trtl.forward(550)
trtl.pendown()

#  Car Front Bumper
trtl.left(180)

trtl.pencolor(colors[3])
trtl.penup()
trtl.pendown()
trtl.pensize(5)

trtl.right(180)
trtl.right(135)
trtl.forward(30)
trtl.left(90)
trtl.forward(20)
trtl.right(90)

#  car front
#  car first curve on hood
for hood in range(40):
  trtl.forward(3.2)
  trtl.right(0.6)

#  car second curve on hood

'''''
i = 5
while i < 4:
  trtl.forward(4)
  trtl.right(4)
  trtl.right(3)
  i-=1
'''''

for hood in range(5):
  trtl.forward(4)
  trtl.right(4)
  trtl.forward(3)

trtl.forward(15)

trtl.right(155)
trtl.backward(180)
trtl.right(205)
trtl.forward(135)

trtl.end_fill()

#  blank error encountered while fill
trtl.penup()
trtl.settiltangle(90)
trtl.goto(-33.0,41.0)
trtl.left(125)
trtl.pendown()
trtl.pencolor(colors[1])
trtl.pensize(27.3)
trtl.goto(-100.0,181.0)

#  border
trtl.penup()
trtl.pensize(5)
trtl.goto(-131.0,192.0)
trtl.pendown()
trtl.pencolor('black')
trtl.goto(-96.0,192.0)
trtl.hideturtle()

#   car livery

#   green 
livery_g.goto(119.0,56.0)
livery_g.pencolor(colors[6])
livery_g.pensize(5)
livery_g.left(180)
livery_g.forward(530)
for x in range (25):
    livery_g.forward(5)
    livery_g.left(2.2)

#   white
livery_w.penup()
livery_w.goto(119.0,62.0)
livery_w.pendown()
livery_w.pencolor('white')
livery_w.pensize(7.3)
livery_w.settiltangle(-180)
livery_w.backward(530)
for x in range (25):
    livery_w.backward(5)
    livery_w.left(2.2)

#   red
livery_r.penup()
livery_r.goto(119.0,68.0)
livery_r.pendown()
livery_r.pencolor('#cf4944')
livery_r.pensize(5)
livery_r.settiltangle(-180)
livery_r.backward(530)
for x in range (25):
    livery_r.backward(5)
    livery_r.left(2.2)

# hide turtles
livery_r.hideturtle()
livery_w.hideturtle()
livery_g.hideturtle()
trtl.hideturtle()

wn.screensize(10000,10000)
wn.setup(width=1.0, height = 1.0)



wn.setup(width=1.0, height=1.0)
wn.mainloop()
