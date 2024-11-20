mport turtle as t
leo = t.Turtle()
s = t.Screen()
def front():
    leo.fd(10)
def back():
    leo.bk(10)
def clockwise():
    leo.right(10)
def anticlockwise():
    leo.left(10)

s.listen()
s.onkey(fun = front, key = "w")
s.onkey(fun= back, key= "s")
s.onkey(fun= clockwise, key= "a")
s.onkey(fun= anticlockwise, key= "d")


s.exitonclick()