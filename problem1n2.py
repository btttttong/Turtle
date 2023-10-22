from turtle import Turtle

t = Turtle()
t.fillcolor('pink')
t.color('pink')
t.penup()
# for line in range:
#     draw_line

for i in range(4):
    t.speed(0)
    t.left(90)
    for j in range(5):
        t.dot(5, "medium orchid")
        t.fd(20)


t.screen.mainloop()

