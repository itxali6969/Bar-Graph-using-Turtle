import turtle as t

data = [50, 120, 80, 150, 200]
screen = t.Screen()
screen.bgcolor("white")
graph_turtle = t.Turtle()
graph_turtle.speed(1)

def draw_bar(height):
    graph_turtle.begin_fill()
    graph_turtle.left(90)
    graph_turtle.forward(height)
    graph_turtle.write(str(height))
    graph_turtle.right(90)
    graph_turtle.forward(40)
    graph_turtle.right(90)
    graph_turtle.forward(height)
    graph_turtle.left(90)
    graph_turtle.end_fill()

graph_turtle.penup()
graph_turtle.goto(-200, -150)
graph_turtle.pendown()

for value in data:
    draw_bar(value)
    graph_turtle.forward(50)  
graph_turtle.hideturtle()
t.done()