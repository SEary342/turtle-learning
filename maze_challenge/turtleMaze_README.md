# 🐢 The Turtle Maze Challenge

**[⬅️ Back to Main Menu](../README.md)**

Welcome to the **Turtle Maze Challenge**!

In this challenge, you are the navigator. Your goal is to write code to guide a turtle through a series of mazes. If the turtle touches the black walls, it resets!

## 🎮 The Scenario

*   **The Turtle**: A digital turtle that follows your exact commands.
*   **The Maze**: A path with walls.
*   **The Goal**: Reach the finish line without crashing.

## 🚀 How to Play

1.  **Open the Controller**:
    Open the file `maze_level_1.py` in VS Code.

2.  **Run the Code**:
    Run the file to see what the turtle does.

3.  **Write Your Code**:
    You need to give the turtle commands to move and turn.
    ```python
    move(100)        # Move forward 100 pixels
    player.left(90)  # Turn left 90 degrees
    player.right(90) # Turn right 90 degrees
    ```

4.  **Check the Result**:
    *   **Success**: The turtle reaches the end!
    *   **Crash**: The turtle hits a wall and goes back to the start.

---

## 🏆 The Levels

Change the level number in `setup_maze(level=1)` to try harder mazes!

### Level 1: The Straight Shot
*   **Goal**: Just move forward to the end.

### Level 2: The Corner
*   **Goal**: Move, turn, and move again.

### Level 3: The Zig Zag
*   **Goal**: Navigate a winding path.

### Level 4: The Spiral
*   **Goal**: Follow the path inwards.

### Level 5: The Labyrinth
*   **Goal**: A complex maze. Good luck!

---

## 🧠 Turtle Commands

*   `move(distance)`: Moves the turtle forward.
*   `player.left(degrees)`: Turns the turtle to the left.
*   `player.right(degrees)`: Turns the turtle to the right.