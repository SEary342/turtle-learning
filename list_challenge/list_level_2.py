# LEVEL 2: Modify Lists
# Goal: Learn how to add and remove items from lists

from list_libraries.list_engine import print_list_state, check_answer

print("=" * 60)
print("LEVEL 2: Modify Lists")
print("=" * 60)

# Start with a list
my_list = ["pencil", "eraser"]


# CHALLENGE 1: Add Items Using .append()
# .append() adds an item to the END of the list
# TODO: Add 'notebook' to the list
# <-- WRITE YOUR CODE HERE (use my_list.append(...))

# TODO: Add 'ruler' to the list
# <-- WRITE YOUR CODE HERE (use my_list.append(...))


# CHALLENGE 2: Change Items
# You can change an item by using its position: list[position] = new_value
# TODO: Change position 0 from 'pencil' to 'pen'
# <-- WRITE YOUR CODE HERE (use my_list[0] = ...)


# CHALLENGE 3: Remove Items Using .pop()
# .pop() removes the LAST item from the list
# TODO: Remove the last item from your list
# <-- WRITE YOUR CODE HERE (use my_list.pop())


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
print("Ready for Level 3? Open: list_level_3.py")
print("=" * 60)
