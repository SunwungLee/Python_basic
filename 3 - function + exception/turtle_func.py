import turtle

t = turtle.Turtle()
t.shape("turtle")

# --------------------- #
def move_pen_origin():
    t.penup()
    t.goto(0,0)
    t.pendown()

def r_upper_square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)


def l_lower_tri(length):
    for i in range(3):
        t.forward(-length)
        t.right(-360 / 3)

# --------------------- #
for i in range(50, 210, 50):
    r_upper_square(i)

move_pen_origin()

for i in range(50, 210, 50):
    l_lower_tri(i)
