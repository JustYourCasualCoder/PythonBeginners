import turtle
import datetime

myPen = turtle.Turtle()
myPen.shape('arrow')
myPen.speed(0)

currentMinute = datetime.datetime.now().minute
currentHour = datetime.datetime.now().hour

myPen.penup()
myPen.goto(0,-180)
myPen.pendown()
myPen.color('blue')
myPen.circle(180)

myPen.color('red')

myPen.penup()
myPen.goto(0,0)
myPen.setheading(90)#Point to the top - 12 0'clock
myPen.right(currentHour*360/12)
myPen.pendown()
myPen.forward(100)

myPen.penup()
myPen.goto(0,0)
myPen.setheading(90)#Point to the top - 0 minute 
myPen.right(currentMinute*360/12)
myPen.pendown()
myPen.forward(150)

myPen.getscreen().update()
