from throw_libraries.game_engine import setup_level, throw_ball, wait

# 1. Setup the level (Try levels 1, 2, 3, 4, or 5)
setup_level(1)

# 2. Configure your throw
# Can you calculate the right values to hit the target?
velocity = 20  # m/s
angle = 45  # degrees

# Advanced: Move the robot
robot_position = 0  # meters from start

# 3. Fire!
throw_ball(velocity, angle, robot_x=robot_position)

# Keep window open
wait()
