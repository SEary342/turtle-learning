# LEVEL 4: Search and Find in Lists - SOLUTION
# Goal: Learn how to find items in lists and use 'in' operator

from list_libraries.list_engine import print_list_state

print("=" * 60)
print("LEVEL 4: Search and Find in Lists - SOLUTION")
print("=" * 60)

# CHALLENGE 1: Check if item is in list
favorite_games = ["Minecraft", "Fortnite", "Roblox", "Pokemon", "Mario Kart"]
print("\nChallenge 1: Check if items are in list")

if "Minecraft" in favorite_games:
    print("✓ 'Minecraft' is in the list")

if "Chess" in favorite_games:
    print("✓ 'Chess' is in the list")
else:
    print("✗ 'Chess' is NOT in the list")

# CHALLENGE 2: Find Position of Item
fruits = ["apple", "banana", "orange", "grape", "banana"]
print("\nChallenge 2: Find the position of an item")

position = fruits.index("orange")
print(f"Position of orange: {position}")

# CHALLENGE 3: Count Items in List
print("\nChallenge 3: Count how many times an item appears")

count = fruits.count("banana")
print(f"'banana' appears {count} times")

# CHALLENGE 4: Search and React
print("\nChallenge 4: Search and do something based on result")

inventory = ["sword", "shield", "potion", "gold", "key"]

for item in inventory:
    if item == "sword":
        print(f"{item}: You have a weapon!")
    elif item == "potion":
        print(f"{item}: Health item found!")
    elif item == "key":
        print(f"{item}: Quest item found!")
    else:
        print(f"{item}")

print("\n" + "=" * 60)
print("LEVEL 4 COMPLETE!")
print("=" * 60)
