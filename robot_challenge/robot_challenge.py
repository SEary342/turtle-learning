import turtle


# --- 1. SHOOTER DATA ---
class ShotParameter:
    def __init__(self, distance, rpm):
        self.distance = distance  # in pixels
        self.rpm = rpm


shooter_table = [
    ShotParameter(100, 2000),
    ShotParameter(200, 3500),
    ShotParameter(400, 5500),
]

shooter_dict = {x.distance: x.rpm for x in shooter_table}

# --- 2. STUDENT CHALLENGE FUNCTIONS ---


def check_intake():
    """
    TODO: CHALLENGE 1
    Check if the robot is close enough to the 'ball' (e.g., distance < 20).
    If it is, set 'has_ball' to True.
    """
    global has_ball
    # Your logic here
    pass


def shooter_table_lookup(current_dist) -> int:
    """
    TODO: CHALLENGE 2
    Use the shooter_table to return the correct RPM based on distance.
    """
    pass


def shooter_dict_lookup(current_dist) -> int:
    """
    TODO: CHALLENGE 3
    Use the shooter_dict to return the correct RPM based on distance.
    """
    pass


def shooter_calculation(current_dist) -> int:
    """
    TODO: CHALLENGE 4
    What if the distance isn't a whole number? Could we get a closer to exact value?
    """
    pass


def calculate_rpm(current_dist):
    rpm_values = [
        shooter_calculation(current_dist),
        shooter_table_lookup(current_dist),
        shooter_dict_lookup(current_dist),
    ]
    valid_values = [x for x in rpm_values if x]
    return valid_values[0] if valid_values else 0


# --- 3. SETUP ---
screen = turtle.Screen()
screen.setup(800, 600)
screen.title("FRC Simulator: Tank Drive, Intake, & Shooter")

goal = turtle.Turtle()
goal.shape("circle")
goal.color("red")
goal.penup()
goal.goto(0, 250)

ball = turtle.Turtle()
ball.shape("circle")
ball.color("orange")
ball.penup()
ball.goto(100, -100)
has_ball = False

robot = turtle.Turtle()
robot.shape("turtle")
robot.color("blue")
robot.penup()

# --- 4. THE SYSTEM LOOP ---


def update_systems():
    global has_ball

    # ---------------------------------------------------------
    # CALL CHALLENGE 1 HERE:
    # We need to check if we've picked up the ball every time the robot moves.
    check_intake()
    # ---------------------------------------------------------

    # Calculate distance for the shooter
    dist = robot.distance(goal)
    target_rpm = calculate_rpm(dist)

    # If the student successfully sets has_ball to True, the ball follows the robot
    if has_ball:
        ball.goto(robot.pos())

    print(
        f"Dist: {dist:.1f}px | Target: {target_rpm} RPM | Ball: {'Held' if has_ball else 'Field'}"
    )


# --- 5. TANK DRIVE CONTROLS ---
MOVE_SPEED = 10
TURN_SPEED = 7


def left_fwd():
    robot.right(TURN_SPEED)
    robot.forward(MOVE_SPEED)
    update_systems()


def left_rev():
    robot.left(TURN_SPEED)
    robot.backward(MOVE_SPEED)
    update_systems()


def right_fwd():
    robot.left(TURN_SPEED)
    robot.forward(MOVE_SPEED)
    update_systems()


def right_rev():
    robot.right(TURN_SPEED)
    robot.backward(MOVE_SPEED)
    update_systems()


def shoot():
    global has_ball
    if has_ball:
        ball.goto(goal.pos())
        print(">>> SHOT FIRED! <<<")
        has_ball = False
    else:
        print("Error: No ball in intake!")


screen.listen()
screen.onkey(left_fwd, "w")
screen.onkey(left_rev, "s")
screen.onkey(right_fwd, "i")
screen.onkey(right_rev, "k")
screen.onkey(shoot, "space")

print("MISSION: Write the logic for check_intake and calculate_rpm!")
screen.mainloop()
