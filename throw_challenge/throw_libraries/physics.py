import math

GRAVITY = 9.81 # m/s^2

# Volleyball Physics Constants
MASS = 0.27         # kg (Standard volleyball: 0.26-0.28 kg)
RADIUS = 0.105      # m (Standard radius: ~10.5 cm)
AREA = math.pi * RADIUS**2
DRAG_COEFF = 0.47   # Approximate Cd for a sphere
AIR_DENSITY = 1.225 # kg/m^3 (Sea level)

# Calculate Drag Factor: k = 0.5 * rho * Cd * A / m
DRAG_FACTOR = (0.5 * AIR_DENSITY * DRAG_COEFF * AREA) / MASS

def calculate_landing_x(velocity, angle_degrees, start_x=0, start_height=0, target_height=0, target_dist=None, target_width=None):
    """Calculates the x-coordinate where the ball lands or hits target height using simulation."""
    # Get the final point from the simulation
    points = simulate_flight(velocity, angle_degrees, start_x, start_height, target_height, target_dist, target_width)
    if not points:
        return start_x
    return points[-1][0]

def get_trajectory(velocity, angle_degrees, start_x=0, start_height=0, target_height=0, steps=50, target_dist=None, target_width=None):
    """Generates a list of (x, y) tuples representing the flight path."""
    raw_points = simulate_flight(velocity, angle_degrees, start_x, start_height, target_height, target_dist, target_width)
    
    # Downsample for plotting
    if len(raw_points) <= steps:
        return raw_points
    
    step_size = len(raw_points) / steps
    return [raw_points[int(i * step_size)] for i in range(steps)] + [raw_points[-1]]

def simulate_flight(velocity, angle_degrees, start_x, start_height, target_height, target_dist=None, target_width=None):
    """Simulates the flight physics step-by-step with air resistance."""
    angle_rad = math.radians(angle_degrees)
    v_x = velocity * math.cos(angle_rad)
    v_y = velocity * math.sin(angle_rad)
    
    x = start_x
    y = start_height
    dt = 0.01 # 10ms time step
    
    points = [(x, y)]
    
    while True:
        # Calculate velocity magnitude
        v = math.sqrt(v_x**2 + v_y**2)
        
        # Drag acceleration: a = -k * v * v_vector
        # This models air resistance proportional to v^2
        ax = -(DRAG_FACTOR * v * v_x)
        ay = -GRAVITY - (DRAG_FACTOR * v * v_y)
        
        # Update velocity
        v_x += ax * dt
        v_y += ay * dt
        
        # Update position
        x += v_x * dt
        y += v_y * dt
        
        points.append((x, y))
        
        # Stop conditions
        if y < 0: # Hit ground
            break
            
        # Platform Collision Logic
        if target_height > 0:
            if target_dist is not None and target_width is not None:
                # Visuals draws platform with min width of 4
                effective_width = max(target_width, 4)
                plat_left = target_dist - effective_width/2
                plat_right = target_dist + effective_width/2
                
                # Check if inside platform box (x bounds and y bounds)
                if 0 <= y <= target_height and (plat_left <= x <= plat_right):
                    # We are inside. Correct the point to be on the surface.
                    points.pop() # Remove the point inside the box
                    
                    prev_x, prev_y = points[-1]
                    
                    if prev_y > target_height:
                        # Hit top
                        points.append((x, target_height))
                    elif prev_x < plat_left:
                        # Hit left side
                        points.append((plat_left, y))
                    elif prev_x > plat_right:
                        # Hit right side
                        points.append((plat_right, y))
                    else:
                        # Fallback
                        points.append((x, target_height))
                    break
            elif y <= target_height and v_y < 0: 
                # Fallback for infinite floor if no width provided
                break
            
        # Safety break
        if x > 300 or len(points) > 5000:
            break
            
    return points