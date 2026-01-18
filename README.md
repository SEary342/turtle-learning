#  Welcome to Python Learning!

Welcome! This project is a collection of fun challenges designed to help you learn Python programming. You will control turtles, throw balls with physics, and create art using code.

**👀 Look out for new challenges added weekly!**

**[🚀 Skip Setup and Jump to Challenges](#challenges)**

## 📥 How to Download (For Beginners)

If this is your first time downloading code from GitHub, don't worry! We use a method called **"cloning"**, which simply means making a copy of the code on your own computer so you can work on it.

### Prerequisites
1.  **Git**: You need Git installed to download the code. 
    * Check if you have Git Installed:  Terminal -> New Terminal -> Type "git". 
        * If no errors it's there!
    * [Download Git here](https://git-scm.com/downloads).
2.  **Python**: Make sure you have Python installed to run the code. 
    * Check if you have Python installed: Terminal -> New Termainal -> Type "python" 
        * If you dont get errors, it's there!
    * [Download Python here](https://www.python.org/downloads/).

### Step-by-Step Download Guide

1.  **Copy the Link**:
    *   Look for the green **Code** button at the top of THIS GitHub page.
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
        * Note: This will create a folder called turtle-learning" on your computer with all the files. 
    *   When a popup asks "Would you like to open the cloned repository?", click **Open**.

🚧 **Heads up** You may get a popup asking to open a new workspace or add. Choose New Workspace.  

🎉 **Success!** You are now ready to start coding.

## 🔄 How to Update (Get New Challenges)

If we add new levels or fix bugs, you can update your code without deleting everything!

1.  **Open VS Code** to your `turtle-learning` project.
2.  **Open the Command Palette**:
    *   **Mac**: Press `Command + Shift + P`.
    *   **Windows**: Press `Ctrl + Shift + P`.
3.  **Type**: `Git: Pull` and press Enter.
    *   This downloads the latest changes from GitHub to your computer.

### ⚠️ What if "Git: Pull" Fails? (Saving Your Solutions)

If you get an error saying you have "local changes", it means Git doesn't want to overwrite the code you wrote. Since you cannot push to this repository, follow these steps to save your solutions and get the update:

1.  **Backup Your Code**:
    *   In the file explorer, **Copy and Paste** the file you worked on (e.g., `maze_level_1.py`).
    *   **Rename** the copy to something like `maze_level_1_MY_SOLUTION.py`.
2.  **Discard Changes**:
    *   Go to the **Source Control** tab (icon looks like a branch graph).
    *   Hover over the original file (e.g., `maze_level_1.py`) and click the **Discard Changes** arrow (↩).
    *   *This resets the file to the original version, but your solution is safe in the copy you made!*
3.  **Update Again**:
    *   Run `Git: Pull` again. It should work now!

## <a id="challenges"></a>🚀 Choose Your Challenge

---

### Challenge 1: 🐢 The Turtle Maze
> **Goal:** Program a turtle to navigate through different maze levels without hitting the walls.

👉 **[Click here for the Turtle Maze Instructions](turtleMaze_README.md)**

---

### Challenge 2: 🤖 Robot Ball Thrower
> **Goal:** Use physics and variables to throw a ball into a target.

👉 **[Click here for the Robot Ball Thrower Instructions](throw_challenge/ROBOT_THROWER_README.md)**

---

### Challenge 3: 🎨 Loop Art
> **Goal:** Use loops to draw cool shapes and spirals.

👉 **[Click here for the Loop Challenge Instructions](loop_challenge/Loop_README.md)**

---

## 🛠️ Advanced Setup (Optional)

If you want to run the automated tests included in the project:
    ```bash
    pip install pytest
    ```
    ```bash
    pytest
    ```

## 💡 Pro Tip: Viewing Instructions

You are reading this file in "Code Mode". To see it formatted nicely (with pictures and bold text):
1.  Open any `.md` file (like this one).
2.  Press `Ctrl + Shift + V` (Windows) / `Cmd + Shift + V` (Mac).