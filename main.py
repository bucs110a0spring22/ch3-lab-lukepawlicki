import turtle               #1. import modules
import random
#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here
rand_num = random.randrange(0,100)
leonardo.forward(rand_num)
rand_num = random.randrange(0,100)
michelangelo.forward(rand_num)
leonardo.goto(-100,-20)
michelangelo.goto(-100,20)

for i in range(0,10):
  rand_num2 = random.randrange(0,10)
  leonardo.forward(rand_num2)
  rand_num2 = random.randrange(0,10)
  michelangelo.forward(rand_num2)


# Part B - complete part B here

leonardo.right(90)
leonardo.forward(40)
leonardo.down()
side_length = 20
num_sides=[3,4,6,9,12]
for i in num_sides:
  for _ in range(i):
    leonardo.forward(side_length)
    leonardo.left(360/i)
  leonardo.clear()



  

window.exitonclick()
