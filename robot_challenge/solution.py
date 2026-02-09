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

# Dictionary used for Challenge 3
shooter_dict = {x.distance: x.rpm for x in shooter_table}

# --- 2. SOLUTIONS ---


def check_intake():
    """SOLUTION 1: Basic distance check."""
    global has_ball
    if robot.distance(ball) < 20:
        has_ball = True


def shooter_table_lookup(current_dist) -> int:
    """SOLUTION 2: Finding the closest value in a list."""
    closest_param = shooter_table[0]
    smallest_diff = abs(current_dist - closest_param.distance)

    for param in shooter_table:
        diff = abs(current_dist - param.distance)
        if diff < smallest_diff:
            smallest_diff = diff
            closest_param = param

    return closest_param.rpm


def shooter_dict_lookup(current_dist) -> int:
    """SOLUTION 3: Checking for exact matches in a dictionary."""
    # We round distance to see if it matches a key exactly
    rounded_dist = round(current_dist)
    if rounded_dist in shooter_dict:
        return shooter_dict[rounded_dist]
    return None  # Return None to let calculate_rpm try another method


def shooter_calculation(current_dist) -> int:
    """SOLUTION 4: Linear Interpolation."""
    # 1. Sort the table to ensure we can find neighbors
    table = sorted(shooter_table, key=lambda x: x.distance)

    # 2. Handle out-of-bounds (Floor and Ceiling)
    if current_dist <= table[0].distance:
        return table[0].rpm
    if current_dist >= table[-1].distance:
        return table[-1].rpm

    # 3. Find the two surrounding points
    for i in range(len(table) - 1):
        low_p = table[i]
        high_p = table[i + 1]

        if low_p.distance <= current_dist <= high_p.distance:
            # Calculate progress between low and high (0.0 to 1.0)
            progress = (current_dist - low_p.distance) / (
                high_p.distance - low_p.distance
            )

            # Calculate RPM based on that progress
            rpm_range = high_p.rpm - low_p.rpm
            return int(low_p.rpm + (rpm_range * progress))
    return 0


def calculate_rpm(current_dist):
    # This priority list checks the Interpolation first (Challenge 4),
    # then the Dictionary (Challenge 3), then the List (Challenge 2).
    rpm_values = [
        shooter_calculation(current_dist),
        shooter_dict_lookup(current_dist),
        shooter_table_lookup(current_dist),
    ]
    valid_values = [x for x in rpm_values if x is not None]
    return valid_values[0] if valid_values else 0


# --- 3. SETUP ---
screen = turtle.Screen()
screen.setup(800, 600)
screen.title("FRC Simulator: TEACHER SOLUTION")

# Field Elements
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

# Robot (Turtle shape is great because it has a clear 'front')
robot = turtle.Turtle()
robot.shape("turtle")
robot.color("blue")
robot.penup()

# --- 4. THE SYSTEM LOOP ---


def update_systems():
    global has_ball
    check_intake()  # Challenge 1

    dist = robot.distance(goal)
    target_rpm = calculate_rpm(dist)

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
    dist = robot.distance(goal)
    rpm = calculate_rpm(dist)

    if has_ball:
        if rpm > 0:
            ball.goto(goal.pos())
            print(f">>> SHOT FIRED AT {rpm} RPM! <<<")
            has_ball = False
        else:
            print("Error: RPM not set! Cannot shoot.")
    else:
        print("Error: No ball in intake!")


screen.listen()
screen.onkey(left_fwd, "w")
screen.onkey(left_rev, "s")
screen.onkey(right_fwd, "i")
screen.onkey(right_rev, "k")
screen.onkey(shoot, "space")

print("TEACHER MODE: Intake and Interpolation Active.")
screen.mainloop()
