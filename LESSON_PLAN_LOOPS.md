# 🎓 Lesson: The Power of Repetition (Loops)

**Target Audience:** 7th Grade (Beginner Python)
**Time:** 30-40 Minutes
**Goal:** Understand the difference between counting loops (**For**) and conditional loops (**While**).

---

## 1. The Hook: The Minecraft Builder ⛏️
**Ask the class:**
> "Imagine you are building a giant castle wall in Minecraft. You need to place 100 stone blocks in a straight line. How annoying is it to click the mouse 100 times?"

**The Solution:**
Programmers are lazy (in a smart way)! We follow the **DRY** rule: **D**on't **R**epeat **Y**ourself.
Instead of clicking 100 times, we write a loop to say "Place Block, Move Forward" and tell the computer to "Repeat 100 times".

## 2. The "For" Loop: The Counter 🔢
**Concept:** Use a `for` loop when you know **exactly how many times** you want to do something.

**Real World Analogy:** A Microwave.
*   You type in "2:00".
*   It runs for exactly 2 minutes, then stops.

**Visual:**
*   "Do 5 Jumping Jacks." (1, 2, 3, 4, 5. Stop.)

**The Code:**
```python
# Repeat 4 times
for i in range(4):
    turtle.forward(100)
    turtle.right(90)
```

### 🎮 Activity 1: The Shape Maker
1.  Open `loop_challenge/loop_art.py`.
2.  Run the code. It draws a square (4 sides).
3.  **Challenge:** Change the variable `sides` to `6`, `8`, or `12`.
4.  **Question:** Why didn't we have to write `forward` and `right` 12 times?
    *   *Answer: The loop did the repeating for us!*

## 3. The "While" Loop: The Sensor 🚦
**Concept:** Use a `while` loop when you want to keep going **until something happens**. You don't know how many times it will run.

**Real World Analogy:** Filling a Water Bottle.
*   You don't count "1 second, 2 seconds..."
*   You watch the water level.
*   "Keep filling **WHILE** the bottle is not full."

**Visual:**
*   "Keep running **WHILE** the coach is blowing the whistle."

**The Code:**
```python
# Keep drawing WHILE the line is short
length = 0
while length < 200:
    turtle.forward(length)
    length = length + 5
```

### 🎮 Activity 2: The Infinite Spiral
1.  Open `loop_challenge/spiral_maker.py`.
2.  Run the code. It draws a spiral that gets bigger and bigger.
3.  **Challenge:**
    *   Change the angle from `89` to `91`. What happens?
    *   Change the condition `while length < 300` to `while length < 100`. Does it stop sooner or later?

## 4. Discussion: Which Loop? 🧠
**Quiz the class:**
1.  **Scenario:** You want to eat 5 cookies.
    *   *Answer: For Loop (You know the number).*
2.  **Scenario:** You want to eat cookies until you are full.
    *   *Answer: While Loop (Depends on a condition).*
3.  **Scenario:** A game character walks until they hit a wall.
    *   *Answer: While Loop.*

## 5. Wrap Up 🚀
Loops allow us to create complex patterns and behaviors with very little code. In the next lesson, we will combine Loops with **If Statements** to make decisions!