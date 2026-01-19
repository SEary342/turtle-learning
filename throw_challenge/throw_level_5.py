"""
### Level 5: The Weak Robot
*   **Goal**: Hit the hopper located at the **20m** mark.
*   **Constraint**:
      The hopper is elevated **1m off the ground**, and your robot has a weak arm
      (it can only throw about **3m**).
*   **Challenge**:
      You cannot change the speed or angle (fixed at 60°).
      Instead, you must **move the robot** (`robot_position`) closer to the target
      so your short throw makes it in!
"""

from throw_libraries.game_engine import setup_level, throw_ball, wait

# 1. Setup the level
setup_level(5)
velocity = 10  # m/s
angle = 60  # degrees

# 2. starting robot position.
robot_position = 0  # meters from start
hit = False
tries = 0
tries_max = 100

# 3. Fire!
# add loops to modify robot position and velocity until you hit the right solution.

for tries in range(tries_max):  # this is a loop that will keep trying many times.
    robot_position = robot_position + 1  # move the robot

    hit = throw_ball(
        velocity, angle, robot_x=robot_position
    )  # throw the ball and see if it hits

    if hit:  # exit early if we hit the target as we want to stay and throw the balls from there.
        break

# Keep window open
wait()
