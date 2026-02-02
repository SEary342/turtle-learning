# LEVEL 1: Create and Access Lists - SOLUTION
# Goal: Learn how to create a list and access items by position

from list_libraries.list_engine import print_list_state, check_answer

print("=" * 60)
print("LEVEL 1: Create and Access Lists - SOLUTION")
print("=" * 60)

# CHALLENGE 1: Create Your First List
fruits = ["apple", "banana", "orange", "grape"]

# Display the list
print("\nYour Fruits List:")
print_list_state("fruits", fruits)

# CHALLENGE 2: Access Items by Position
print("\nAccessing Items:")
print("=" * 60)

first_fruit = fruits[0]
print(f"First fruit: {first_fruit}")

second_fruit = fruits[1]
print(f"Second fruit: {second_fruit}")

last_fruit = fruits[3]
print(f"Last fruit: {last_fruit}")

# CHALLENGE 3: Check Your Answers
print("\n" + "=" * 60)
print("Checking Your Answers...")
print("=" * 60)

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
print("=" * 60)
