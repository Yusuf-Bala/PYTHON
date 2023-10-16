
import turtle

t = turtle.Turtle()
t.speed(0)
t.left(90)

def branch(lenght, t):
    if lenght <= 5:
        return
    t.forward(lenght)
    t.right(20)
    branch(lenght - 15, t)
    t.left(40)
    branch(lenght - 15, t)
    t.right(20)
    t.backward(lenght)

branch(100, t)
turtle.mainloop()