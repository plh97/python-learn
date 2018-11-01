import turtle
colors=[
    'red','purple', 'blue', 'green', 'yellow','orange'
]
t=turtle.Pen()
turtle.bgcolor('black')
# t.pencolor("red")
name = input('name >>>')
sides = 6
for x in range(200):
    t.pencolor(colors[x%sides])
    t.penup()
    t.forward(x*sides)
    t.pendown()
    t.write(name, font=("Arial", int((x+4)/2), 'bold'))
    t.left(360/sides + 5)