# 🎓 Lesson: Programming a Robot Arm (The Throw Challenge)

**Target Audience:** 7th Grade (Beginner Python)
**Time:** 30-40 Minutes
**Goal:** Understand how **Variables** control a simulation and how **Loops** can solve problems automatically.

---

## 1. The Hook: Angry Birds Physics 🐦
**Ask the class:**
> "Who has played Angry Birds? When you pull back on the slingshot, what two things are you controlling?"

**The Answer:**
1.  **Power** (How far you pull back).
2.  **Angle** (Where you aim).

In Physics and Engineering, we call these:
*   **Velocity** (Speed/Power)
*   **Angle** (Direction)

Today, you aren't just flinging birds; you are programming a **Robot Arm** to hit a target using Python code!

## 2. The Variables: Speaking to the Robot 🗣️
A robot doesn't know "throw it hard." It needs a number.
In Python, we use **Variables** to save these numbers.

**Write on board:**
```python
velocity = 20   # m/s (Meters per second)
angle = 45      # degrees
```

*   **Experiment:**
    *   If `angle = 90` (Straight up), where does the ball go? *(On the robot's head!)*
    *   If `angle = 0` (Straight forward), where does it go? *(Hits the ground immediately)*
    *   **Pro Tip:** `45` degrees usually makes the ball go the furthest!

## 3. Activity: The Human Robot 🤖
**Materials:** A trash can (Target), a crumpled paper ball, and a **Blindfold**.
**Volunteers:** 1 "Robot" (Thrower), 1 "Coder" (Commander).

1.  **Blindfold the Coder**: The Coder cannot see the target or the throw!
2.  Place the trash can far away.
3.  **The Coder** gives commands using only numbers (e.g., "Velocity 50, Angle 45").
4.  **The Robot** tries to follow the instructions exactly.
5.  **The Class** acts as the computer's feedback system. They shout: "Too short!", "Too far!", or "HIT!"
6.  The Coder must adjust their numbers based *only* on what the class says.

**The Lesson:** Just like the blindfolded Coder relies on the Class, a programmer relies on **Function Feedback** (Return Values or Print Statements) to know if the code worked!

**The Code (For Loop):**
```python
# Try every position from 0 meters to 20 meters
for position in range(0, 21):
    print("Moving robot to", position)
    throw_ball(velocity=6, angle=60, robot_x=position)
```
*   The computer will try: 0m, 1m, 2m, 3m... all in a split second!
*   When it hits, we stop!

## 5. Discussion Questions 🧠
1.  Why is `45` degrees usually the best angle for distance?
2.  In Level 3, the target is up on a tower. Do you need more velocity or a higher angle?
3.  Why do we use a Loop in Level 5 instead of typing the code over and over? *(Answer: Computers are faster at boring repetitive tasks than humans!)*

## 6. Wrap Up 🚀
Open `throw_level_1.py` and start your engines! See who can hit the Level 2 target (65m away) first!
