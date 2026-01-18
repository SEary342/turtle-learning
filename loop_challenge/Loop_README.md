# 🎨 Loop Art Challenge
**[⬅️ Back to Main Menu](../README.md)**

**Goal:** Let the computer do the hard work!

---

## 1. Why Loops? 😫
Imagine drawing a shape with 100 sides. You would have to type `forward` and `turn` 100 times!
**Loops** let you type it once, and the computer repeats it for you.

## 2. The "For" Loop 🔢
**Use this when:** You know **how many times** to repeat.
*   *Example:* "Clap your hands 3 times."

**In Python:**
```python
# This runs 4 times
for i in range(4):
    forward(100)
    right(90)
```

## 3. The "While" Loop ⏳
A **While Loop** is like a game of "Red Light, Green Light". It keeps running **while** a condition is true.

**Visual:** Eating cereal.
*   "Keep eating **while** there is milk in the bowl."

**Code:**
```python
milk_level = 10
while milk_level > 0:
    eat_spoonful()
    milk_level = milk_level - 1
```

---

## 🚀 Activities

### Activity 1: The Shape Maker (`loop_art.py`)
Open `loop_art.py`. We use a `for` loop to draw cool geometric patterns.
*   **Challenge:** Can you change the number of sides to make a Hexagon (6 sides) or a Decagon (10 sides)?

### Activity 2: The Infinite Spiral (`spiral_maker.py`)
Open `spiral_maker.py`. We use a `while` loop to keep drawing until the turtle goes off-screen.
*   **Challenge:** Change the colors or the angle to make different spiral art!
> **Goal:** Use loops to draw cool shapes and spirals.