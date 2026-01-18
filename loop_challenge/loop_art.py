from loop_libraries.art_engine import setup

# Setup the drawing environment
blueTurtle, screen = setup()

# --- LESSON: FOR LOOPS ---
# A for loop repeats code a specific number of times.
# range(4) means: 0, 1, 2, 3 (4 times total)

sides = 4
angle = 360 / sides  # 360 / 4 = 90 degrees

for i in range(sides):
    blueTurtle.forward(100)
    blueTurtle.right(angle)

# Challenge:
# 1. Change 'sides' to 6 (Hexagon)
# 2. Change 'sides' to 36 (Circle-ish)
# 3. Change the color inside the loop!

blueTurtle.hideturtle()
screen.mainloop()