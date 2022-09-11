import turtle



bob = turtle.Turtle()


bob.color("red", "blue")

bob.begin_fill()
bob.forward(100)
bob.left(45)
bob.right(135)
bob.forward(100)
bob.right(90)
bob.forward(100)
bob.right(90)
bob.forward(100)
bob.end_fill()

bob.penup()
bob.forward(150)
bob.penup()

bob.begin_fill()
bob.forward(100)
bob.left(45)
bob.right(135)
bob.forward(100)
bob.right(90)
bob.forward(100)
bob.right(90)
bob.forward(100)
bob.end_fill()


turtle.done()
