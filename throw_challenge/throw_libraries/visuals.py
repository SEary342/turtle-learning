import turtle
import random
from .physics import get_trajectory

CURRENT_Y_MAX = 60
stats_pen = None

def setup_screen(x_max=100, y_max=60):
    """Initializes the turtle screen with a coordinate system suitable for simulation."""
    global CURRENT_Y_MAX
    CURRENT_Y_MAX = y_max
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("Projectile Motion Simulation")
    # Set coordinates: Bottom-Left (-10, -10) to Top-Right (x_max, y_max)
    # This zooms the view to fit the level
    screen.setworldcoordinates(-10, -10, x_max, y_max)
    screen.tracer(0) # Turn off auto-update for faster drawing setup
    return screen

def draw_environment(x_max=100):
    """Draws the ground and axes."""
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.width(2)
    
    # Draw Ground
    pen.penup()
    pen.goto(-10, 0)
    pen.pendown()
    pen.goto(x_max, 0)
    pen.penup()

def draw_target(x, width, height=0):
    """Draws a red target strip on the ground or elevated."""
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    
    pen.penup()
    
    # Draw pole if height > 0
    if height > 0:
        # Draw platform rectangle
        pen.color("gray")
        pen.begin_fill()
        platform_width = max(width, 4)
        pen.goto(x - platform_width/2, 0)
        pen.pendown()
        pen.goto(x + platform_width/2, 0)
        pen.goto(x + platform_width/2, height)
        pen.goto(x - platform_width/2, height)
        pen.goto(x - platform_width/2, 0)
        pen.end_fill()
        pen.penup()

    # Draw Target
    pen.color("red")
    pen.width(5) # Thicker target
    pen.goto(x - width/2, height)
    pen.pendown()
    pen.forward(width)
    pen.penup()
    
    # Draw Flag
    pen.goto(x, height)
    pen.color("black")
    pen.width(2)
    pen.pendown()
    pen.goto(x, height + 4)
    pen.penup()
    
    pen.color("red")
    pen.begin_fill()
    pen.goto(x, height + 4)
    pen.goto(x + 2, height + 3)
    pen.goto(x, height + 2)
    pen.goto(x, height + 4)
    pen.end_fill()
    
    pen.goto(x, -5)
    pen.write(f"{x}m", align="center", font=("Arial", 10, "bold"))

def draw_hill(height):
    """Draws a grey cliff/hill at the starting position."""
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.color("gray")
    pen.begin_fill()
    
    pen.penup()
    pen.goto(-10, 0)
    pen.pendown()
    pen.goto(0, 0)
    pen.goto(0, height)
    pen.goto(-10, height)
    pen.goto(-10, 0)
    
    pen.end_fill()

def simulate_throw(velocity, angle, start_x=0, start_height=0, target_height=0, target_dist=None, target_width=None, color="blue"):
    """Animates a ball throw."""
    ball = turtle.Turtle()
    ball.hideturtle()
    ball.color(color)
    ball.shape("circle")
    ball.shapesize(0.5)
    ball.width(3) # Thicker trail
    
    points = get_trajectory(velocity, angle, start_x=start_x, start_height=start_height, target_height=target_height, target_dist=target_dist, target_width=target_width)
    
    # Draw Stats
    global stats_pen
    if stats_pen is None:
        stats_pen = turtle.Turtle()
        stats_pen.hideturtle()
        stats_pen.speed(0)
        stats_pen.penup()
    
    stats_pen.clear()
    stats_pen.goto(-8, CURRENT_Y_MAX - 5)
    stats_pen.write(f"Velocity: {velocity} m/s   Angle: {angle}°   Distance: {points[-1][0]:.1f}m", font=("Arial", 12, "bold"))
    
    ball.penup()
    ball.goto(points[0])
    ball.showturtle()
    ball.pendown()
    
    screen = turtle.Screen()
    screen.tracer(1) # Enable animation
    
    for x, y in points[1:]:
        ball.goto(x, y)
        
    # Label the landing distance
    ball.penup()
    ball.goto(points[-1][0], -3)
    ball.write(f"{points[-1][0]:.1f}m", align="center", font=("Arial", 10, "bold"))
    ball.hideturtle()

def draw_error(message):
    """Displays an error message on the screen."""
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.color("red")
    pen.penup()
    pen.goto(45, 30) # Center of the sky
    pen.write(message, align="center", font=("Arial", 20, "bold"))

def draw_fireworks(x, y):
    """Draws a fireworks celebration."""
    fw = turtle.Turtle()
    fw.hideturtle()
    fw.speed(0)
    fw.width(2)
    
    colors = ["red", "gold", "orange", "yellow", "purple", "cyan", "lime"]
    
    # Draw multiple bursts
    for _ in range(5):
        bx = x + random.randint(-10, 10)
        by = y + random.randint(0, 20)
        for _ in range(20):
            fw.penup()
            fw.goto(bx, by)
            fw.color(random.choice(colors))
            fw.setheading(random.randint(0, 360))
            fw.pendown()
            fw.forward(random.randint(5, 15))