import turtle as t
import colorgram

colors = colorgram.extract('spots.jpg', 25)

t.colormode(255)
tim = t.Turtle()
tim.hideturtle()
tim.penup()
INIT_POS = (-150,300)
tim.goto(INIT_POS)

for i in range(len(colors)):
    print(i)
    if i % 5 == 0:
        tim.goto(INIT_POS[0] , tim.ycor()-100)
    else:
        tim.fd(100)
    tim.dot(50, (int(colors[i].rgb.r), int(colors[i].rgb.g), int(colors[i].rgb.b)))

tim.screen.mainloop()