from turtle import *
import colorsys
title("NIIN KM")
tracer(10)
bgcolor('black')
pensize(2)
h=0.8
for i in range (200):
    c = colorsys.hsv_to_rgb(h,1,1)
    h+=0.002
    color(c)
    up()
    forward(i)
    down()
    circle(i,-200)
    forward(i)
    circle(i,-200)
    hideturtle()
done()
