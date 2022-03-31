import turtle

my_turtle = turtle.Turtle()
my_turtle.shape('turtle')
drawing_area = turtle.Screen()

for i in range(4):
    my_turtle.forward(200)
    my_turtle.left(90)
my_turtle.penup()
my_turtle.forward(200)
my_turtle.pendown()
for i in range(3):
    my_turtle.forward(150)
    my_turtle.left(120)
