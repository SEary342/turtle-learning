# LEVEL 3: Loop Through Lists - SOLUTION
# Goal: Learn how to use a for loop to process every item in a list

from list_libraries.list_engine import print_list_state

print("=" * 60)
print("LEVEL 3: Loop Through Lists - SOLUTION")
print("=" * 60)

# CHALLENGE 1: Print Each Item
students = ["Alice", "Bob", "Charlie", "Diana"]
print("\nChallenge 1: Print each student's name")
for student in students:
    print(student)

# CHALLENGE 2: Add a Greeting
print("\nChallenge 2: Add a greeting to each name")
for student in students:
    print(f"Hello, {student}!")

# CHALLENGE 3: Process Numbers
scores = [95, 87, 92, 88, 91]
print("\nChallenge 3: Print each score")
for score in scores:
    print(score)

# CHALLENGE 4: Calculate Average Score
print("\nChallenge 4: Calculate average score")
total = 0
for score in scores:
    total = total + score

average = total / len(scores)
print(f"Average score: {average}")

print("\n" + "=" * 60)
print("LEVEL 3 COMPLETE!")
print("=" * 60)
