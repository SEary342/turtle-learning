# 🤖 Robot Hopper Challenge

Welcome to the **Robot Hopper Challenge**! 

In this scenario, we have a robot that needs to throw a ball into a hopper (the target). Your job is to calculate the correct **angle**, **velocity** (power), or **position** to get the ball in and score!

This exercise helps us understand how angles and launch speeds relate to distance, so we can later code a real robot to hit targets autonomously.

## 🎮 The Scenario

*   **The Robot**: Your code controls the launcher.
*   **The Hopper**: A red target on the ground that you must hit.
*   **The Physics**: You control the `velocity` (speed) and `angle` of the throw.

## 🚀 How to Play

1.  **Open the Controller**:
    Open the file `throw_level_1.py` in VS Code.

2.  **Run the Simulation**:
    Run the code to see the robot's current attempt. Watch the ball fly!

3.  **Modify the Code**:
    You need to change the variables to hit the target.
    ```python
    # Configure your throw
    velocity = 20  # Power of the throw (m/s)
    angle = 45     # Angle of the throw (degrees)
    ```

4.  **Check the Result**:
    *   **Green "HIT!"**: You scored!
    *   **Red "MISS"**: Adjust your numbers and try again.

---

## 🏆 The Levels

To switch levels, change the number in `setup_level(1)` inside your code.

### Level 1: The Practice Range
*   **Goal**: The hopper is **40 meters** away.
*   **Challenge**: Find a balance between speed and angle.
*   **Tip**: A 45-degree angle usually gives the longest distance for the same speed.

### Level 2: Long Shot
*   **Goal**: The hopper is moved back to **65 meters**.
*   **Challenge**: You need more power! Increase your velocity.

### Level 3: The High Tower
*   **Goal**: The robot is on the ground, but the hopper is on a **20m platform** 57m away.
*   **Challenge**: You need to throw high enough to reach the platform!

### Level 4: The Further Tower
*   **Goal**: The robot is on the ground, but the hopper is on a **20m platform** 60m away.
*   **Challenge**: Adjust your throw to reach the extra distance!

### Level 5: The Weak Robot
*   **Goal**: Hit the hopper located at the **20m** mark.
*   **Constraint**: The hopper is elevated **1m off the ground**, and your robot has a weak arm (it can only throw about **3m**).
*   **Challenge**: You cannot change the speed or angle (fixed at 60°). Instead, you must **move the robot** (`robot_position`) closer to the target so your short throw makes it in!

---

## 🧠 Physics Concepts

*   **Velocity (m/s)**: How fast the ball leaves the robot. Higher velocity = further distance.
*   **Angle (degrees)**: The direction of the throw.
    *   **45°**: Maximum distance.
    *   **90°**: Straight up (0 distance).
    *   **0°**: Straight forward (hits the ground immediately).
*   **Gravity**: The simulation uses standard gravity ($9.81 m/s^2$).