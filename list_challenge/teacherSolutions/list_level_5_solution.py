# LEVEL 5: Transform Lists - SOLUTION
# Goal: Learn how to modify every item in a list using loops

from list_libraries.list_engine import print_list_state

print("=" * 60)
print("LEVEL 5: Transform Lists - SOLUTION")
print("=" * 60)

# CHALLENGE 1: Convert Numbers
prices = [10, 20, 15, 30, 25]
print("\nChallenge 1: Transform all items in a list")
print("Original prices:", prices)

for i in range(len(prices)):
    prices[i] = prices[i] * 0.9

print("Prices after discount:", prices)

# CHALLENGE 2: Convert Text
names = ["alice", "bob", "charlie", "diana"]
print("\nChallenge 2: Transform text in a list")
print("Original names:", names)

for i in range(len(names)):
    names[i] = names[i].upper()

print("Names after transformation:", names)

# CHALLENGE 3: Filter and Rebuild
numbers = [1, 2, 3, 4, 5]
print("\nChallenge 3: Create a new list with transformed items")
print("Original numbers:", numbers)

new_numbers = []
for num in numbers:
    double = num * 2
    new_numbers.append(double)

print("New list with doubled numbers:", new_numbers)

# CHALLENGE 4: Complex Transformation
temperatures_fahrenheit = [32, 50, 68, 86, 104]
print("\nChallenge 4: Complex data transformation")
print("Temperatures in Fahrenheit:", temperatures_fahrenheit)

temperatures_celsius = []
for temp_f in temperatures_fahrenheit:
    temp_c = (temp_f - 32) * 5 / 9
    temperatures_celsius.append(temp_c)

print("Temperatures in Celsius:", temperatures_celsius)

print("\n" + "=" * 60)
print("LEVEL 5 COMPLETE!")
print("=" * 60)
