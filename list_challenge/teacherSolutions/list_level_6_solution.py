# LEVEL 6: Advanced - Sort and Combine Lists - SOLUTION
# Goal: Learn to sort lists and combine multiple lists

from list_libraries.list_engine import print_list_state

print("=" * 60)
print("LEVEL 6: Advanced - Sort and Combine Lists - SOLUTION")
print("=" * 60)

# CHALLENGE 1: Sort a List
scores = [87, 92, 76, 95, 88]
print("\nChallenge 1: Sort lists")
print("Original scores:", scores)

scores.sort()
print("Scores after sorting:", scores)

# CHALLENGE 2: Sort Strings
names = ["Zoe", "Alice", "Charlie", "Bob", "Diana"]
print("\nChallenge 2: Sort a list of names")
print("Original names:", names)

names.sort()
print("Names after sorting:", names)

# CHALLENGE 3: Reverse Sort
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print("\nChallenge 3: Sort in reverse order")
print("Original numbers:", numbers)

numbers.sort(reverse=True)
print("Numbers after reverse sorting:", numbers)

# CHALLENGE 4: Combine Lists
shopping_list_1 = ["apples", "milk", "bread"]
shopping_list_2 = ["eggs", "butter", "cheese"]
print("\nChallenge 4: Combine two lists")

combined = shopping_list_1 + shopping_list_2
print("Combined list:", combined)

# CHALLENGE 5: Combine Using Loop
backpack = ["pencil", "eraser"]
items_to_add = ["ruler", "notebook", "pen"]
print("\nChallenge 5: Add items from one list to another")
print("Starting backpack:", backpack)

for item in items_to_add:
    backpack.append(item)

print("Backpack after adding items:", backpack)

# CHALLENGE 6: Filter and Create New List
all_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nChallenge 6: Filter a list")
print("All numbers:", all_numbers)

even_numbers = []
for num in all_numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print("Even numbers:", even_numbers)

print("\n" + "=" * 60)
print("LEVEL 6 COMPLETE!")
print("🎉 YOU MASTERED LISTS! 🎉")
print("=" * 60)
