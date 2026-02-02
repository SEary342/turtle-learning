# LEVEL 7: 2D Lists (Lists of Lists)
# Goal: Learn how to work with 2D lists - lists that contain other lists

from list_libraries.list_engine import print_list_state

print("=" * 60)
print("LEVEL 7: 2D Lists (Advanced)")
print("=" * 60)

# CHALLENGE 1: Create a 2D List
# A 2D list is like a grid or table with rows and columns
print("\nChallenge 1: Create a 2D list (grid)")
print("-" * 60)

# TODO: Create a 3x3 grid of numbers 1-9
# Hint: It should look like this:
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]
grid = []  # <-- REPLACE WITH YOUR 2D LIST


# CHALLENGE 2: Access Elements in 2D List
# Remember: grid[row][column]
print("\nChallenge 2: Access elements")
print("-" * 60)

# TODO: Get the element at row 0, column 0 (top-left)
top_left = None  # <-- REPLACE WITH grid[0][0]

# TODO: Get the element at row 1, column 1 (middle)
middle = None  # <-- REPLACE WITH grid[1][1]

# TODO: Get the element at row 2, column 2 (bottom-right)
bottom_right = None  # <-- REPLACE WITH grid[2][2]

print(f"Top-left: {top_left}")
print(f"Middle: {middle}")
print(f"Bottom-right: {bottom_right}")


# CHALLENGE 3: Loop Through 2D List
print("\nChallenge 3: Print the entire grid")
print("-" * 60)

# TODO: Use nested for loops to print each row
# Hint:
#   for row in grid:
#       print(row)
# <-- WRITE YOUR NESTED FOR LOOP HERE


# CHALLENGE 4: Modify a 2D List
print("\nChallenge 4: Modify elements in the grid")
print("-" * 60)

# TODO: Change the middle element (row 1, column 1) to 0
# Hint: grid[1][1] = 0
# <-- WRITE YOUR CODE HERE


# CHALLENGE 5: Create a Game Board
print("\nChallenge 5: Create a tic-tac-toe board")
print("-" * 60)

# TODO: Create a 3x3 board with all empty spaces " "
# This is what a tic-tac-toe board looks like before any moves
# <-- CREATE YOUR BOARD HERE


# CHALLENGE 6: Find and Count in 2D List
print("\nChallenge 6: Count specific values in 2D list")
print("-" * 60)

# Create a board with some data
data_grid = [
    [1, 2, 1],
    [1, 3, 2],
    [2, 1, 3]
]

# TODO: Count how many times the number 1 appears in the entire grid
# Hint:
#   count = 0
#   for row in data_grid:
#       for num in row:
#           if num == 1:
#               count = count + 1
# <-- WRITE YOUR CODE HERE


print("\n" + "=" * 60)
print("LEVEL 7 COMPLETE!")
print("🎉 YOU'VE MASTERED LISTS! 🎉")
print("=" * 60)
