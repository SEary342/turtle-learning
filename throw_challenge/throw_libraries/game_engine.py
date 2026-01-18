import turtle
from . import visuals
from . import physics

# Define levels with increasing complexity
MAX_VELOCITY = 120 # m/s (Increased for volleyball physics)

LEVELS = {
    1: {
        "target_dist": 40,
        "target_width": 2,
        "start_height": 0,
        "target_height": 0,
        "description": "Level 1: Hit the target at 40m."
    },
    2: {
        "target_dist": 65,
        "target_width": 2,
        "start_height": 0,
        "target_height": 0,
        "description": "Level 2: Further away! Hit the target at 65m."
    },
    3: {
        "target_dist": 57,
        "target_width": 2,
        "start_height": 0,
        "target_height": 20,
        "tolerance": 0.5,
        "description": "Level 3: Target is on a 20m platform! Hit the target at 57m."
    },
    4: {
        "target_dist": 60,
        "target_width": 2,
        "start_height": 0,
        "target_height": 20,
        "tolerance": 0.5,
        "description": "Level 4: Target is on a 20m platform! Hit the target at 60m."
    },
    5: {
        "target_dist": 20,
        "target_width": 1,
        "start_height": 0,
        "target_height": 1,
        "description": "Level 5: Hopper is at 20m! Robot on ground."
    },
}

result_pen = None

current_level_config = None

def setup_level(level_number) -> bool:
    """Sets up the simulation environment for a specific level."""
    global current_level_config
    
    if level_number not in LEVELS:
        print(f"Level {level_number} not found. Defaulting to Level 1.")
        level_number = 1
        
    current_level_config = LEVELS[level_number]
    
    # Calculate dynamic view based on target
    target_dist = current_level_config["target_dist"]
    # Ensure we see a bit past the target (1.4x), but keep a minimum width of 20m
    view_width = max(target_dist * 1.4, 20)
    view_height = max(current_level_config["start_height"] + 30, current_level_config.get("target_height", 0) + 30, 40)
    
    screen = visuals.setup_screen(x_max=view_width, y_max=view_height)
    visuals.draw_environment(x_max=view_width)
    
    # Draw specific level elements
    if current_level_config["start_height"] > 0:
        visuals.draw_hill(current_level_config["start_height"])
        
    visuals.draw_target(current_level_config["target_dist"], current_level_config["target_width"], current_level_config.get("target_height", 0))
    
    # Write instructions
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(-5, 50)
    pen.write(current_level_config["description"], font=("Arial", 14, "bold"))
    
    return screen

def throw_ball(velocity, angle, robot_x=0):
    """Simulates the throw and checks if the user passed the level."""
    global result_pen
    if not current_level_config:
        print("Error: Level not set up. Call setup_level() first.")
        return

    if velocity > MAX_VELOCITY:
        visuals.draw_error(f"⚠️ TOO FAST! Max: {MAX_VELOCITY} m/s")
        print(f"Error: {velocity} m/s is too fast! Please keep it under {MAX_VELOCITY} m/s.")
        return

    start_h = current_level_config["start_height"]
    target_x = current_level_config["target_dist"]
    target_w = current_level_config["target_width"]
    target_h = current_level_config.get("target_height", 0)
    
    # Run visualization
    visuals.simulate_throw(velocity, angle, start_x=robot_x, start_height=start_h, target_height=target_h, target_dist=target_x, target_width=target_w)
    
    # Calculate result
    flight_path = physics.simulate_flight(velocity, angle, start_x=robot_x, start_height=start_h, target_height=target_h, target_dist=target_x, target_width=target_w)
    if flight_path:
        landing_x, landing_y = flight_path[-1]
    else:
        landing_x, landing_y = robot_x, start_h
    
    # Check win condition
    dist_error = abs(landing_x - target_x)
    tolerance = current_level_config.get("tolerance", 1.0)
    hit = dist_error <= tolerance
    
    # Ensure we landed ON the target, not below it (hitting the side of the platform)
    if hit and target_h > 0 and landing_y < (target_h - 0.05):
        hit = False
        print(f"Too low! You hit the side of the platform at {landing_y:.2f}m height.")

    if result_pen is None:
        result_pen = turtle.Turtle()
        result_pen.hideturtle()
        result_pen.penup()
    
    result_pen.clear()
    result_pen.goto(landing_x, landing_y + 20)
    
    if hit:
        visuals.draw_fireworks(landing_x, 20)
        result_pen.color("green")
        result_pen.write("HIT!", align="center", font=("Arial", 40, "bold"))
        print(f"SUCCESS! You hit the target at {landing_x:.2f}m.")
    else:
        result_pen.color("red")
        result_pen.write("MISS", align="center", font=("Arial", 16, "bold"))
        print(f"Missed. Landed at {landing_x:.2f}m. Target was {target_x}m.")

    return hit

def wait():
    """Keeps the window open."""
    turtle.done()