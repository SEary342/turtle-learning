# 🐢 Turtle Maze Challenge

Welcome to the Turtle Maze Challenge! This project is designed to help you learn Python by programming a turtle to navigate through different maze levels without hitting the walls.

## 📥 How to Download (For Beginners)

If this is your first time downloading code from GitHub, don't worry! We use a method called **"cloning"**, which simply means making a copy of the code on your own computer so you can work on it.

### Prerequisites
1.  **Git**: You need Git installed to download the code. (Note: If you have VS Code installed, you likely already have Git). [Download Git here](https://git-scm.com/downloads).
2.  **Python**: Make sure you have Python installed to run the code. [Download Python here](https://www.python.org/downloads/).

### Step-by-Step Download Guide

1.  **Copy the Link**:
    *   Look for the green **Code** button at the top of this GitHub page.
    *   Click it and copy the HTTPS URL (it looks like `https://github.com/.../turtle-learning.git`).

2.  **Open VS Code**.

3.  **Open the Command Palette**:
    *   **Mac**: Press `Command + Shift + P`.
    *   **Windows**: Press `Ctrl + Shift + P`.

4.  **Start Cloning**:
    *   Type `Git: Clone` and press Enter.
    *   Paste the URL you copied in Step 1 and press Enter.

5.  **Save and Open**:
    *   Select a folder on your computer where you want to save the project.
    *   When a popup asks "Would you like to open the cloned repository?", click **Open**.

🎉 **Success!** You are now ready to start coding.

## 🏃‍♂️ How to Run

To play with the maze, you will write Python scripts to control the turtle.

1.  **Install Testing Tools** (Optional):
    If you want to run the automated tests included in the project:
    ```bash
    pip install pytest
    ```

2.  **Run Tests**:
    To check if the game engine is working correctly:
    ```bash
    pytest
    ```

3.  **Start Coding**:
    Open the file `maze_level_1.py` in VS Code. It's already set up for you:

    ```python
    from maze_challenge.maze_engine import move, player, setup_maze, screen

    # Setup Level 1 (Levels 1-5 available)
    setup_maze(level=1)

    # Write your code to move the turtle!
    move(100)

    # Keep the window open
    screen.mainloop()
    ```
