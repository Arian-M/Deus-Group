import turtle
PROGNAME = 'Sierpinski Carpet'

myPen = turtle.Turtle()
myPen.speed(10)
myPen.color("#000000")


# This function draws a box by drawing each side of the square and using the fill function
initial_size = 100
initial_x = 0
initial_y = 0
P_Sqrs = [[0, 0]]
N_Sqrs = [[0, 0]]

P_Size = initial_size
N_Size = initial_size
Depth = 3


def box(x, y, boxSize):
    myPen.penup()
    myPen.goto(x, y)
    myPen.pendown()
    myPen.begin_fill()
    # 0 deg.
    myPen.forward(boxSize)
    myPen.left(90)
    # 90 deg.
    myPen.forward(boxSize)
    myPen.left(90)
    # 180 deg.
    myPen.forward(boxSize)
    myPen.left(90)
    # 270 deg.
    myPen.forward(boxSize)
    myPen.end_fill()
    myPen.setheading(0)


def Frac_Draw(x, y, size):
    x1 = 4*size/3+x
    y1 = 4*size/3+y
    N_Sqrs.append([x1, y1])
    x2 = 4*size/3+x
    y2 = size/3+y
    N_Sqrs.append([x2, y2])
    x3 = 4*size/3+x
    y3 = -2*size/3+y
    N_Sqrs.append([x3, y3])

    x4 = -2*size/3+x
    y4 = 4*size/3+y
    N_Sqrs.append([x4, y4])
    x5 = -2*size/3+x
    y5 = size/3+y
    N_Sqrs.append([x5, y5])
    x6 = -2*size/3+x
    y6 = -2*size/3+y
    N_Sqrs.append([x6, y6])

    x7 = size/3+x
    y7 = 4*size/3+y
    N_Sqrs.append([x7, y7])
    x8 = size/3+x
    y8 = -2*size/3+y
    N_Sqrs.append([x8, y8])

    size = size/3
    # N_Size=size

    box(x1, y1, size)
    box(x2, y2, size)
    box(x3, y3, size)
    box(x4, y4, size)
    box(x5, y5, size)
    box(x6, y6, size)
    box(x7, y7, size)
    box(x8, y8, size)


box(initial_x, initial_y, initial_size)

# def Frac(Depth):
for i in range(Depth):
    for x, y in P_Sqrs:
        Frac_Draw(x, y, P_Size)

    P_Sqrs = []
    P_Sqrs = N_Sqrs
    N_Sqrs = []
    P_Size = P_Size/3
