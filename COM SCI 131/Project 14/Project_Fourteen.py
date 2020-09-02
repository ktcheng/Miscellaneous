# Regular Polygons With Turtle Graphics

import random
import turtle
from turtle import *

# Opening Statement
print("This program will draw a polygon with 3 or more sides.")

colors = ["coral", "gold", "brown", "red", "green", "blue", "yellow", 
              "purple", "orange", "cyan", "pink", "magenta", "goldenrod"]

def makePolygon(sides, length, borderColor, width, fillColor):
    color(fillColor, borderColor)
    turtle.shape("turtle")
    shape = turtle.Turtle()
    shape.pensize(width)
    
    # Polygon Construction
    for i in range(sides):
        forward(length)
        left(360 / sides)

while True:
    num_sides = int(input("Enter the number of sides, less than 3 to exit: "))
    
    if num_sides < 3:
        break
    
    l = (600 / num_sides) # Side Length
    w = ((num_sides % 20) + 1) # Side Width
    bC = colors[random.randint(0, 12)] # Border Color
    fC = colors[random.randint(0, 12)] # Fill Color
    
    begin_fill()
    makePolygon(num_sides, l, bC, w, fC)
    end_fill()
    clear()

# Closing Statement
print("Thanks for using the polygon generator program.")
