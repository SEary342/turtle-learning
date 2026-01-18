# 🎓 Lesson: How Video Games "See" Walls

**Target Audience:** 7th Grade (Beginner Python)
**Time:** 20-30 Minutes
**Goal:** Understand how we use X/Y coordinates to build a maze level.

---

## 1. The Hook: Invisible Boxes 📦
**Ask the class:**
> "In games like Minecraft or Mario, how does the game know when you bump into a wall? Why don't you just walk right through it?"

**The Secret:**
To a computer, a wall isn't a picture of a brick or a stone. It is an invisible rectangle called a **Hitbox**. If your character's X and Y coordinates go inside that box, the computer says "STOP!"

Today, we are going to learn how to build these invisible boxes for our Turtle.

## 2. The Map: X and Y 🗺️
**Visual:** Draw a big `+` sign on the whiteboard.
*   **The Center (0,0)**: This is where the Turtle starts.
*   **X Axis (Left/Right)**:
    *   Moving Right is **Positive (+)**.
    *   Moving Left is **Negative (-)**.
*   **Y Axis (Up/Down)**:
    *   Moving Up is **Positive (+)**.
    *   Moving Down is **Negative (-)**.

**Quick Check:**
"If I want to put a wall far to the **left**, will the X number be positive or negative?" *(Answer: Negative)*

## 3. Building a Wall with 4 Numbers 🧱
To build a wall in Python, we don't draw it. We give the computer **4 numbers** to define the rectangle.

Think of it like defining the corners of a room:
1.  **Left Edge** (Where does the wall start?)
2.  **Bottom Edge** (How low does it go?)
3.  **Right Edge** (Where does the wall end?)
4.  **Top Edge** (How high does it go?)

**The Python Code:**
In our game file (`maze_engine.py`), a wall looks like this:
```python
# (Left, Bottom, Right, Top)
wall = (-300, 50, 300, 60)
```
*   **-300 to 300**: This wall is super wide (it goes all the way across the screen).
*   **50 to 60**: This wall is only 10 pixels tall (it's a thin line).

## 4. Activity: Be the Level Designer ✏️
**Materials:** Graph paper (or just draw a grid on paper).

1.  **Draw the Center**: Put a dot in the middle and label it `(0,0)`.
2.  **Draw a Wall**: Draw a rectangle somewhere on the grid.
3.  **Find the Coordinates**:
    *   Look at the line on the **Left** side of your box. What is the X number?
    *   Look at the line on the **Bottom**. What is the Y number?
    *   Look at the **Right** side. What is the X number?
    *   Look at the **Top**. What is the Y number?
4.  **Write the Code**: Write your 4 numbers in a list: `( __, __, __, __ )`.

## 5. Where is this in the Code? 💻
Open `maze_challenge/maze_engine.py` and look at `LEVELS`.

## 6. Wrap Up Challenge 🚀
"If you wanted to make a gap in the wall for the turtle to squeeze through, which numbers would you change?"
*(Answer: You would need to split one long wall into two smaller walls with a space in between!)*