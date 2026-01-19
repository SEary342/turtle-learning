# 🐉 Dragon's Treasure: Lesson Plan

**Topic:** Conditional Logic (`if`, `else`, `elif`, `or`)  
**Target Audience:** 7th Graders (Beginner Python)  
**Time Required:** 45 - 60 Minutes

---

## 🎯 Learning Objectives
By the end of this lesson, students will be able to:
1.  Use **`if`** and **`else`** statements to make binary decisions.
2.  Use **`elif`** (else if) to handle more than two options.
3.  Use the **`or`** operator to check for multiple matching conditions.
4.  Understand the difference between assignment (`=`) and comparison (`==`).

---

## 🗣️ Introduction (5 Minutes)

1.  **The Hook**: "Congratulations! You just landed the world's most dangerous summer job: 
2.  **The Challenge: Royal Dragon Hoard Manager**. The Dragon has a mountain of loot—gold, diamonds, and... old shoes?—but is way too lazy to sort it. Your job is to write a program that checks each item instantly. If you sort it right? You get to keep your job. If you accidentally toss a diamond into the incinerator? ...Let's just say the Dragon has a *very* fiery temper."
3.  **The Concept**: Explain that computers make decisions just like we do.
    *   *Real world:* "If it is raining, take an umbrella. Else, wear sunglasses."
    *   *Python:* "If variable equals value, do X. Else, do Y."

---

## 💻 Activity: Level 1 - The Basics (10 Minutes)

*   **File**: `treasureSort_level1.py`
*   **Task**: The Dragon only wants **"gold"**. Everything else turns to **"dust"**.
*   **Key Concept**: The basic `if/else` block.
*   **Common Pitfall**: Students often type `if item = "gold":`. Remind them:
    *   `=` sets a value (Assignment).
    *   `==` checks a value (Comparison).
    *   *"One equals sets, two equals checks."*

---

## 💻 Activity: Level 2 - Advanced Sorting (15 Minutes)

*   **File**: `treasureSort_level2.py`
*   **Task**: The Dragon is organizing.
    *   Gold OR Silver -> **"vault"**
    *   Ruby OR Emerald -> **"chest"**
    *   Trash -> **"incinerator"**
*   **Key Concept**: Introducing `elif` and `or`.
*   **Teaching Moment**:
    *   Show how `or` allows us to group things: `if item == "gold" or item == "silver":`
    *   Explain that `elif` only runs if the previous `if` was False.

---

## 💻 Activity: Level 3 - The Curse Breaker (10 Minutes)

*   **File**: `treasureSort_level3.py`
*   **Task**: The Dragon wants to keep everything **UNLESS** it is cursed.
*   **Key Concept**: The Not Equal Operator (`!=`).
*   **Teaching Moment**:
    *   Explain that sometimes it is easier to say what we *don't* want.
    *   "If it is NOT cursed, keep it." -> `if status != "cursed":`

---

## 💻 Activity: Level 4 - The Appraiser (15 Minutes)

*   **File**: `treasureSort_level4.py`
*   **Task**: The Dragon cares about **Value** and **Magic**.
    *   Keep if value is **> 100**.
    *   **OR** keep if it is **magical** (even if cheap).
*   **Key Concept**: Numerical comparison (`>`) and Boolean logic.
*   **Discussion**:
    *   "What happens if we have a magical item worth 5 gold?" -> It keeps it (because of the OR).
    *   "What happens if we have a rusty sword worth 5 gold?" -> Toss it.

---

## 💻 Activity: Level 5 - The Guard Dragon (10 Minutes)

*   **File**: `treasureSort_level5.py`
*   **Task**: Decide to attack based on **who** it is and **how close** they are.
*   **Key Concept**: The `and` operator + Numerical Logic.
*   **Teaching Moment**:
    *   **"Most coding is numbers."** Explain that in games, we constantly check numbers: Is health < 0? Is ammo > 0? Is distance < 5?
    *   This level combines a string check (`intruder == "knight"`) with a number check (`distance < 10`).
    *   Both must be true for the `and` to work.

---

## 🏁 Wrap Up & Review (5 Minutes)

**Quiz Questions:**
1.  **Q:** What symbol do we use to check if two things are equal?
    *   **A:** `==`
2.  **Q:** If I have 3 different choices (Door A, Door B, Door C), what keywords do I use?
    *   **A:** `if`, `elif`, `else`.
3.  **Q:** True or False: In an `or` statement, both sides must be true.
    *   **A:** False (Only one needs to be true).

## 🧩 Extension / Homework

*   **Challenge**: Modify Level 3 to be stricter!
    *   Change the rule to: Keep it ONLY if it is magical **AND** worth more than 50.
    *   (This teaches the `and` operator).