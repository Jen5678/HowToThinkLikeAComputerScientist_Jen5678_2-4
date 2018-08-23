import turtle
w = turtle.Screen()
w.bgcolor("Black")
w.title("Chap4 - ex1")
t = turtle.Turtle()

def makeSquare (t, colr, sz, w):
    """ 
        Set up a turtle with the given color and pensize,
        that draws a square of length w, with a seperationspace of m.
    """
    t.color(colr)
    t.pensize(sz)    
    
    for i in range(4):
        t.forward(w)
        t.right(90)
    t.penup()    
    t.forward(2*w)
    t.pendown()

for i in range (4):
    makeSquare(t, "green", 3, 20)
w.mainloop()