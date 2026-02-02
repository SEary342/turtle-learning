# LEVEL 7: 2D Lists (Lists of Lists) - SOLUTION
# Goal: Learn how to work with 2D lists - lists that contain other lists

from list_libraries.list_engine import print_list_state

print("=" * 60)
print("LEVEL 7: 2D Lists (Advanced) - SOLUTION")
print("=" * 60)

# CHALLENGE 1: Create a 2D List
print("\nChallenge 1: Create a 2D list (grid)")
print("-" * 60)

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Grid created:")
for row in grid:
    print(row)

# CHALLENGE 2: Access Elements in 2D List
print("\nChallenge 2: Access elements")
print("-" * 60)

top_left = grid[0][0]
middle = grid[1][1]
bottom_right = grid[2][2]

print(f"Top-left: {top_left}")
print(f"Middle: {middle}")
print(f"Bottom-right: {bottom_right}")

# CHALLENGE 3: Loop Through 2D List
print("\nChallenge 3: Print the entire grid")
print("-" * 60)

for row in grid:
    print(row)

# CHALLENGE 4: Modify a 2D List
print("\nChallenge 4: Modify elements in the grid")
print("-" * 60)

grid[1][1] = 0
print("Grid after changing middle to 0:")
for row in grid:
    print(row)

# CHALLENGE 5: Create a Game Board
print("\nChallenge 5: Create a tic-tac-toe board")
print("-" * 60)

tic_tac_toe = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

print("Empty tic-tac-toe board:")
for row in tic_tac_toe:
    print(f"| {row[0]} | {row[1]} | {row[2]} |")

# CHALLENGE 6: Find and Count in 2D List
print("\nChallenge 6: Count specific values in 2D list")
print("-" * 60)

data_grid = [
    [1, 2, 1],
    [1, 3, 2],
    [2, 1, 3]
]

count = 0
for row in data_grid:
    for num in row:
        if num == 1:
            count = count + 1

print(f"The number 1 appears {count} times in the grid")

print("\n" + "=" * 60)
print("LEVEL 7 COMPLETE!")
print("🎉 YOU'VE MASTERED LISTS! 🎉")
print("=" * 60)
