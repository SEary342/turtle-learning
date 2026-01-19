# 🐉 Dragon's Treasure Challenge

**[⬅️ Back to Main Menu](../README.md)**

Welcome to the **Dragon's Treasure Challenge**!

In this challenge, you have been hired by a wealthy (and slightly grumpy) Dragon to organize their hoard. The Dragon is very particular about what they keep and what they throw away.

Your job is to write Python code to inspect items and make the correct decision. If you make a mistake, the Dragon might growl at you!

## 🎮 The Scenario

*   **The Dragon**: Presents you with an item (like "gold", "rock", or a "rusty sword").
*   **The Decision**: You must tell the Dragon what to do with it (e.g., "keep", "dust", "vault").
*   **The Code**: You will use `if` statements to make these decisions automatically.

## 🚀 How to Play

1.  **Open the Level**:
    Open the file `treasureSort_level1.py` in VS Code.

2.  **Run the Code**:
    Run the file. You will see the Dragon presenting items, but your code currently does nothing!

3.  **Write Your Logic**:
    You need to write `if` and `else` statements to return the correct answer.
    ```python
    if item == "gold":
        return "keep"
    else:
        return "dust"
    ```

4.  **Check the Result**:
    *   **Green "Correct!"**: The Dragon is pleased.
    *   **Red "Wrong!"**: Check your logic and try again.

---

## 🏆 The Levels

### Level 1: The Basics
*   **File**: `treasureSort_level1.py`
*   **Goal**: The Dragon only wants **"gold"**.
*   **Logic**: If it is "gold", return `"keep"`. For everything else, return `"dust"`.

### Level 2: Advanced Sorting
*   **File**: `treasureSort_level2.py`
*   **Goal**: The Dragon is getting organized.
*   **Logic**:
    *   If it is **"gold"** or **"silver"** -> return `"vault"`
    *   If it is **"ruby"** or **"emerald"** -> return `"chest"`
    *   Everything else -> return `"incinerator"`

    **💡 Hint:** You can check for multiple things using `or`:
    ```python
    if color == "red" or color == "blue":
        return "primary color"
    ```

### Level 3: The Master Appraiser
*   **File**: `treasureSort_level3.py`
*   **Goal**: The Dragon cares about **Value** and **Magic**.
*   **Logic**:
    *   Keep the item if the value is **greater than 100**.
    *   **OR** keep the item if it is **magical** (even if it's cheap!).
    *   Otherwise, toss it.

---

## 🧠 Python Concepts

*   **`if` / `else`**: Making a choice between two things.
*   **`elif`**: "Else If" - checking a second option if the first one was false.
*   **`==`**: Checks if two things are equal.
*   **`>` / `<`**: Checks if a number is greater or smaller.
*   **`or`**: Checks if *either* condition is true.