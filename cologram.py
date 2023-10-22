import colorgram
from turtle import Turtle

t = Turtle()

colors = colorgram.extract('spots.jpg', 25)

print(colors)
# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.
first_color = colors[0]
rgb = first_color.rgb  # e.g. (255, 151, 210)
hsl = first_color.hsl  # e.g. (230, 255, 203)
proportion = first_color.proportion  # e.g. 0.34

for i in range(len(colors)):
    print(f'{colors[i].rgb.r},{colors[i].rgb.g},{colors[i].rgb.b}')
    tupi = (float(colors[i].rgb.r), float(colors[i].rgb.g), float(colors[i].rgb.b))
    print(tupi)
    print(len(colors))
    if i % 5 != 0:
        t.color()
        t.dot(20, tupi)
        t.fd(100)
    else:
        t.right(90)


t.screen.mainloop()
# RGB and HSL are named tuples, so values can be accessed as properties.
# These all work just as well:
# red = rgb[0]
# red = rgb.r
# saturation = hsl[1]
# saturation = hsl.s
