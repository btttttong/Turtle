from turtle import Turtle
from random import random

tt = Turtle()
for i in range(6):
    for color in ('red', 'magenta', 'blue',
                  'cyan', 'green', 'pink',
                  'yellow'):
        tt.color(color)
        tt.circle(100)
        tt.left(10)
    tt.hideturtle()

tt.screen.mainloop()