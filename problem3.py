from turtle import Turtle
from random import choice
color_list = ('red', 'magenta', 'blue', 'cyan', 'green', 'black', 'yellow')
t = Turtle()
for angle in range(3, 11):
    t.color(choice(color_list))
    # for i in range(100):
    #     t.right(360 / angle)
    #     t.forward(i)

    for i in range(angle):
        t.right(360 / angle)
        t.forward(100)

t.screen.mainloop()
