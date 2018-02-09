from turtle import Turtle
from random import randint
import time

chris = Turtle()
chris.color('red')
chris.shape('turtle')
chris.penup()
chris.goto(-160, 120)
chris.pendown()
chris.write("chris",font=("Arial", 16, "normal"))

huseyin = Turtle()
huseyin.color('blue')
huseyin.shape('turtle')
huseyin.penup()
huseyin.goto(-160,80)
huseyin.pendown()
huseyin.write("huseyin",font=("Arial", 16, "normal"))

elliot = Turtle()
elliot.color('green')
elliot.shape('turtle')
elliot.penup()
elliot.goto(-160,40)
elliot.pendown()
elliot.write("elliot",font=("Arial", 16, "normal"))

sophie = Turtle()
sophie.color('pink')
sophie.shape('turtle')
sophie.penup()
sophie.goto(-160,0)
sophie.pendown()
sophie.write("sophie",font=("Arial", 16, "normal"))

for movement in range(100):
    chris.forward(randint(1,5))
    huseyin.forward(randint(1,5))
    elliot.forward(randint(1,5))
    sophie.forward(randint(1,5))

time.sleep(10)
