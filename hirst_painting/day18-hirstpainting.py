#Script for extracting colors

# import colorgram

# colors = colorgram.extract('day 18/hirst_painting/image.jpg', 30)

# rgb_list = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     result = (r, g, b)
#     rgb_list.append(result)

color_list = [ (211, 154, 98), (241, 248, 246), 
                (236, 241, 245), (53, 107, 131), (177, 78, 34), (199, 142, 34), 
                (116, 156, 171), (123, 80, 98), (124, 175, 157), (226, 197, 130), 
                (190, 88, 110), (55, 38, 19), (12, 49, 63), (43, 168, 128), 
                (51, 126, 121), (197, 124, 143), (166, 21, 31), (222, 93, 79), 
                (243, 163, 160), (38, 32, 35), (4, 25, 24), (80, 147, 168), 
                (161, 26, 23), (19, 79, 92), (233, 167, 172), (175, 207, 187), 
                (101, 127, 158), (165, 203, 210) ]

from turtle import Turtle, Screen
import turtle
import random

turtle.colormode(255)
hirst = Turtle()
hirst.hideturtle()
hirst.penup()
hirst.goto(-200, -270)
hirst.pendown()


def get_y(position):
    new_position = list(position)
    y = new_position[1]
    return y

def returner():
    x = -200
    y_new = get_y(hirst.position()) + 50
    hirst.penup()
    hirst.goto(x, y_new)
    hirst.pendown()

def draw():
    for i in range(10):
        hirst_color = random.choice(color_list)
        hirst.color(hirst_color)
        hirst.speed('fastest')
        hirst.begin_fill()
        hirst.circle(10)
        hirst.end_fill()
        hirst.penup()
        hirst.forward(50)
        hirst.pendown()

for i in range(10):
    draw()
    returner()


screen = Screen()
screen.exitonclick()