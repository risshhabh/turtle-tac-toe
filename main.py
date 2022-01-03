import turtle


board = ["~"] * 10
global master_coords
master_coords = {
    1: (-180, 180),
    2: (0, 180),
    3: (180, 180),
    4: (-180, 0),
    5: (0, 0),
    6: (180, 0),
    7: (-180, -180),
    8: (0, -180),
    9: (180, -180),
}

# Unnecessary unpacking but my code-format messes everything up.
wins = (
    *((1, 2, 3), (4, 5, 6), (7, 8, 9)),  # Horizontal
    *((1, 4, 7), (2, 5, 8), (3, 6, 9)),  # Vertical
    *((1, 5, 9), (3, 5, 7)),  # Diagonal
)


wn = turtle.Screen()  # Window
wn.title("Tic-Tac-Toe")
wn.bgcolor("black")
wn.setup(width=600, height=600)  # (0, 0) is at the center of the screen.
wn.tracer(0)  # Max possible speed.

w = 27  # Width
l = 0.25  # Height

# Borders
def border(side: bool, dr: bool, w=27, l=0.25, coord=90):
    """
    If `side` is true   :  Left or Top.
    If `side` is false  :  Right or Bottom.
    If `dr`   is true   :  The direction is vertical.
    If `dr`   is false  :  The direction is horizontal.
    """

    side, dr = map(bool, (side, dr))

    out = turtle.Turtle()
    out.speed(0)
    out.shape("square")
    out.color("white")
    out.shapesize(stretch_wid=w, stretch_len=l) if dr else out.shapesize(stretch_wid=l, stretch_len=w)
    out.penup()
    mult = 1 if side else -1
    out.goto(*((coord * mult, 0) if dr else (0, coord * mult)))

    return out


# Draw 4 border lines.
[border(*(paras)) for paras in ((0, 0), (0, 1), (1, 0), (1, 1))]


# Functions
def draw_piece(coords: tuple, who: bool, ln: int):
    """Draw X if who == True else Draw O"""

    if who:

        def draw_x_line(in_coords: tuple, in_ln: int):

            out = turtle.Turtle()
            out.speed(0)
            out.shape("square")
            out.color("red")
            out.shapesize(stretch_wid=1, stretch_len=(ln / 20))
            out.penup()
            out.goto(*coords)

            return out

        draw_x_line(coords, ln).right(45)
        draw_x_line(coords, ln).left(45)

    else:

        def draw_o_part(in_coords: tuple, in_r: int, colour: bool):  # `in_r` is radius.
            """blue if colour == True else black"""

            out = turtle.Turtle()
            out.speed(0)
            out.shape("circle")
            out.color("blue") if colour else out.color("black")
            out.shapesize(stretch_wid=(in_r / 20), stretch_len=(in_r / 20))
            out.penup()
            out.goto(*coords)

            return out

        draw_o_part(coords, ln, True)
        draw_o_part(coords, ln * 0.75, False)


# draw_piece((0,0), False, 160)
# draw_piece((0,0), True, 160)

# Keyboard bindings
wn.listen()  # Listen for keyboard input.
wn.onkeypress(turtle.bye, "q")
wn.onkeypress(turtle, "1")
# Using functools.partial
### wn.onkeypress(partial(func_with_args, arg1, arg2), "q")


wn.onkeypress(lambda: draw_piece(master_coords[1], True, 160), "1")
wn.onkeypress(lambda: draw_piece(master_coords[2], False, 160), "2")
wn.onkeypress(lambda: draw_piece(master_coords[3], True, 160), "3")
wn.onkeypress(lambda: draw_piece(master_coords[4], False, 160), "4")
wn.onkeypress(lambda: draw_piece(master_coords[5], True, 160), "5")
wn.onkeypress(lambda: draw_piece(master_coords[6], False, 160), "6")
wn.onkeypress(lambda: draw_piece(master_coords[7], True, 160), "7")
wn.onkeypress(lambda: draw_piece(master_coords[8], False, 160), "8")
wn.onkeypress(lambda: draw_piece(master_coords[9], True, 160), "9")


"""
r t y & 1 2 3
f g h & 4 5 6
v b n & 7 8 9
"""


# wn.onkeypress(turtle.reset, "r") --> Does not work.

# Main game loop
while True:
    wn.update()  # Update the screen every time the loop starts.
