# LEVEL 1: Create and Access Lists
# Goal: Learn how to create a list and access items by position

from list_libraries.list_engine import print_list_state, check_answer

print("=" * 60)
print("LEVEL 1: Create and Access Lists")
print("=" * 60)

# CHALLENGE 1: Create Your First List
# TODO: Create a list of 4 fruits
# Hint: Use square brackets [ ] and separate items with commas
fruits = []  # <-- DELETE THIS AND WRITE YOUR LIST


# Display the list
print("\nYour Fruits List:")
print_list_state("fruits", fruits)


# CHALLENGE 2: Access Items by Position
# Remember: Positions start at 0!
#   Position 0 = First item
#   Position 1 = Second item
#   Position 2 = Third item
#   Position 3 = Fourth item

print("\nAccessing Items:")
print("=" * 60)

# TODO: Get the FIRST fruit
first_fruit = None  # <- Update Here with your code
print(f"First fruit: {first_fruit}")

# TODO: Get the SECOND fruit
second_fruit = None  # <- Update Here with your code
print(f"Second fruit: {second_fruit}")

# TODO: Get the LAST fruit
last_fruit = None  # <- Update Here with your code
print(f"Last fruit: {last_fruit}")


# CHALLENGE 3: Check Your Answers
print("\n" + "=" * 60)
print("Checking Your Answers...")
print("=" * 60)

# These checks will verify your code
if len(fruits) >= 4:
    print("✓ You created a list with 4 items!")
else:
    print(f"✗ Your list needs 4 items. You have {len(fruits)}")

if first_fruit is not None and first_fruit == fruits[0]:
    print(f"✓ First fruit is correct: {first_fruit}")
else:
    print(f"✗ First fruit didn't match")

if second_fruit is not None and second_fruit == fruits[1]:
    print(f"✓ Second fruit is correct: {second_fruit}")
else:
    print(f"✗ Second fruit didn't match")

if last_fruit is not None and last_fruit == fruits[3]:
    print(f"✓ Last fruit is correct: {last_fruit}")
else:
    print(f"✗ Last fruit didn't match")

print("\n" + "=" * 60)
print("LEVEL 1 COMPLETE!")
print("Ready for Level 2? Open: list_level_2.py")
print("=" * 60)
