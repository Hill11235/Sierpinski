#Code which draws Sierpinski triangle fractal (05-04-20)

import turtle
import math as M

window = turtle.Screen()
window.bgcolor("white")
window.title("Sierpinski")

T = turtle.Turtle()
T.shape("classic")
T.turtlesize(0.5,0.5,0.5)
T.pensize(2)
T.speed(1000)

#creates more space for the pattern
T.color("white")
T.left(90)
T.forward(250)
T.right(90)
T.color("black")

#triangle side length variable
y=15

#code that draws triangle layers, draws base of row first left to right then _
#completes triangles right to left. Colour change is based on calculating _
#binomial coefficent modulo 2

for j in range(1,33):
    p=0
    q=0
    for i in range(1,3*j+2):
        if i<j:
            if (M.factorial(j-1)/(M.factorial(i-1)*M.factorial(j-i)))%2 == 0:
                T.color("white")
                T.forward(y)
            else:
                T.color("black")
                T.forward(y)
        elif i==j:
            T.color("black")
            T.forward(y)
            T.left(120)
        elif i>j and i<(3*j+1):
            if i>j+1:
                p=p+1
            if p%2 == 0 and p>1:
                q=q+1
            if (M.factorial(j-1)/(M.factorial(max((i-j-1-(p%2)-q),0))*M.factorial(max((2*j-i+(p%2)+q),0))))%2 == 0:
                T.color("white")
                T.forward(y)
                T.left(120+((i+(j+1)%2)%2)*120)
            else:
                T.color("black")
                T.forward(y)
                T.left(120+((i+(j+1)%2)%2)*120)
        elif i==(3*j+1) and j!=32:
            T.color("black")
            T.left(120)
            T.forward(y)
            T.left(120)

window.mainloop()

