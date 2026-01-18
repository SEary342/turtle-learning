# 🔄 Loop-de-Loop Challenge

**Target Audience:** 7th Grade (Beginner Python)
**Goal:** Learn how to make the computer repeat tasks using **Loops**.

---

## 1. The Concept: Don't Repeat Yourself (DRY) 🦜
Imagine you want to draw a square. You could write:
```python
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
```
That's boring! What if you want to draw a shape with 100 sides?

## 2. The "For" Loop 🔢
A **For Loop** is like a counter. You tell it exactly how many times to run.

**Visual:** Walking around a block.
*   "Walk forward, Turn Right." (Repeat 4 times).

**Code:**
```python
for side in range(4):
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