from turtle import Turtle
from random import choice, randrange, random

t = Turtle()
while True:
    color_list = ('red', 'magenta', 'blue', 'cyan', 'green', 'black', 'yellow')
    t.color(choice(color_list))
    coin = int(random() * 2)
    # coin = random.randrange(0, 2)
    if coin == 0:
        t.left(90)
    else:
        t.right(90)

    t.forward(50)
