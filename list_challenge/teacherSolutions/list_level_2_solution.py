# LEVEL 2: Modify Lists - SOLUTION
# Goal: Learn how to add and remove items from lists

from list_libraries.list_engine import print_list_state, check_answer

print("=" * 60)
print("LEVEL 2: Modify Lists - SOLUTION")
print("=" * 60)

# Start with a list
my_list = ["pencil", "eraser"]

# CHALLENGE 1: Add Items Using .append()
my_list.append("notebook")
my_list.append("ruler")

# CHALLENGE 2: Change Items
my_list[0] = "pen"

# CHALLENGE 3: Remove Items Using .pop()
my_list.pop()

# CHALLENGE 4: Check Your Work
print("\n" + "=" * 60)
print("FINAL RESULTS:")
print("=" * 60)
print("\nYour list:")
print_list_state("my_list", my_list)

expected_length = 3

if len(my_list) == expected_length:
    print(f"✓ Your list has {expected_length} items!")
else:
    print(f"✗ Your list has {len(my_list)} items. Expected {expected_length}")

if "pen" in my_list:
    print("✓ 'pen' is in your list (you changed pencil correctly!)")
else:
    print("✗ 'pen' is not in your list")

if "notebook" in my_list:
    print("✓ 'notebook' is in your list")
else:
    print("✗ 'notebook' is not in your list")

print("\n" + "=" * 60)
print("LEVEL 2 COMPLETE!")
print("=" * 60)
