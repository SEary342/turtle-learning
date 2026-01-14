import os
import platform
import turtle
import math

# Challenging Maze Data
LEVELS = {
    1: {"walls": [(-300, 50, 300, 60), (-300, -60, 300, -50)], "goal": (280, 0)},
    2: {
        "walls": [(-300, 100, 300, 110), (-300, -110, 300, -100), (0, -100, 20, 40)],
        "goal": (260, 70),
    },
    3: {  # The "S" Bend
        "walls": [
            (-310, 160, 310, 170),
            (-310, -170, 310, -160),
            (-100, -160, -80, 40),
            (100, -40, 120, 160),
        ],
        "goal": (280, 100),
    },
    4: {  # Narrow Corridor
        "walls": [
            (-300, 60, 100, 70),
            (-100, -70, 300, -60),
            (100, 60, 110, 250),
            (-100, -250, -90, -70),
        ],
        "goal": (250, -130),
    },
    5: {  # The Spiral
        "walls": [
            (-200, -200, 200, -190),
            (200, -200, 210, 200),
            (-200, 190, 200, 200),
            (-210, -100, -200, 200),
            (-100, -100, 100, -90),
            (100, -100, 110, 100),
            (-100, 90, 100, 100),
        ],
        "goal": (0, 0),
    },
}

screen = turtle.Screen()
screen.setup(700, 700)
player = turtle.Turtle(shape="turtle")
player.penup()
player.color("blue")

painter = turtle.Turtle()
painter.hideturtle()

walls = []
goal_pos = (0, 0)
has_said_yay = False


def draw_maze():
    screen.tracer(0)
    painter.clear()
    painter.fillcolor("black")
    for x1, y1, x2, y2 in walls:
        painter.penup()
        painter.goto(x1, y1)
        painter.pendown()
        painter.begin_fill()
        for _ in range(2):
            painter.forward(x2 - x1)
            painter.left(90)
            painter.forward(y2 - y1)
            painter.left(90)
        painter.end_fill()

    # Visual Goal
    painter.penup()
    painter.goto(goal_pos[0], goal_pos[1] - 10)
    painter.color("gold")
    painter.begin_fill()
    painter.circle(10)
    painter.end_fill()
    screen.update()
    screen.tracer(1)


def get_collision_point(start_x, start_y, end_x, end_y):
    """Finds the point of impact if a collision occurs."""
    buffer = 8
    steps = 15  # Check 15 points along the path for precision
    for i in range(steps + 1):
        check_x = start_x + (end_x - start_x) * (i / steps)
        check_y = start_y + (end_y - start_y) * (i / steps)
        for x1, y1, x2, y2 in walls:
            if (x1 - buffer) <= check_x <= (x2 + buffer) and (
                y1 - buffer
            ) <= check_y <= (y2 + buffer):
                return check_x, check_y
    return None


def move(distance):
    global has_said_yay
    angle = player.heading()
    dx = distance * math.cos(math.radians(angle))
    dy = distance * math.sin(math.radians(angle))

    start_x, start_y = player.pos()
    end_x, end_y = start_x + dx, start_y + dy

    impact = get_collision_point(start_x, start_y, end_x, end_y)

    if impact:
        player.goto(*impact)
        player.color("red")
        player.write("   OUCH!", font=("Arial", 12, "bold"))
    else:
        player.goto(end_x, end_y)
        dist = player.distance(goal_pos)
        if dist < 50:
            player.color("green")
            if not has_said_yay:
                player.write("   yay!", font=("Arial", 14, "bold"))
                has_said_yay = True
        else:
            player.color("blue")
            has_said_yay = False


def setup_maze(level=1):
    global walls, goal_pos, has_said_yay
    has_said_yay = False
    player.hideturtle()

    # --- MAC & WINDOWS FOREGROUND FIX ---
    root = screen.getcanvas().winfo_toplevel()
    root.lift()
    root.attributes("-topmost", True)
    if platform.system() == "Darwin":
        os.system(
            """/usr/bin/osascript -e 'tell app "System Events" to set frontmost of every process whose name is "Python" to true' """
        )
    # ------------------------------------

    player.penup()
    player.clear()
    data = LEVELS.get(level, LEVELS[1])
    walls, goal_pos = data["walls"], data["goal"]
    draw_maze()
    player.goto(-250, 0)
    player.setheading(0)
    player.showturtle()
    player.pendown()


player.forward = move
