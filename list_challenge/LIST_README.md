# 📚 List Challenge - Learn Lists in Python
**[⬅️ Back to Main Menu](../README.md)**
Welcome to the List Challenge! This is a progressive series of lessons designed to teach you how to work with lists in Python.

## 🎯 What You'll Learn

- **Level 1**: Create lists and access items by position
- **Level 2**: Add and remove items from lists
- **Level 3**: Loop through lists with `for` loops
- **Level 4**: Search for items and check if they exist
- **Level 5**: Transform all items in a list
- **Level 6**: Sort and combine lists

## 🚀 How to Use This Challenge

1. **Start with Level 1**: Open `list_level_1.py`
2. **Read the instructions** carefully - each level has TODO comments
3. **Modify the code** to complete each challenge
4. **Run the code** to see if it works
5. **Move to the next level** when complete

## 📁 Files

```
list_challenge/
├── LESSON_PLAN_LISTS.md      ← Read this first for teacher notes
├── LIST_README.md            ← You are here!
├── list_level_1.py           ← Start here
├── list_level_2.py           ← Add/remove items
├── list_level_3.py           ← Loops through lists
├── list_level_4.py           ← Search and find
├── list_level_5.py           ← Transform items
├── list_level_6.py           ← Sort and combine
└── list_libraries/
    └── list_engine.py        ← Helper functions
```

## 💡 Quick Tips

### Creating a List
```python
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
```

### Accessing Items (Remember: starts at 0!)
```python
fruits = ["apple", "banana", "orange"]
print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[-1])  # orange (last item)
```

### Adding Items
```python
fruits.append("grape")  # Add to the end
```

### Removing Items
```python
fruits.pop()  # Remove the last item
```

### Looping Through
```python
for fruit in fruits:
    print(fruit)
```

### Checking if Item Exists
```python
if "apple" in fruits:
    print("Yes!")
```

## 🎮 Example Challenges

### Level 1
```python
# Create a list of 4 fruits
fruits = ["apple", "banana", "orange", "grape"]

# Access the first fruit
first = fruits[0]  # "apple"
```

### Level 3
```python
# Print each item in a list
for fruit in fruits:
    print(f"I like {fruit}")
```

### Level 5
```python
# Double each number
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
# Result: [2, 4, 6, 8, 10]
```

## 📝 Common Mistakes to Avoid

1. **Forget that indexing starts at 0!**
   - ❌ `fruits[1]` is the SECOND item, not the first
   - ✓ `fruits[0]` is the first item

2. **Using wrong syntax for accessing**
   - ❌ `fruits(0)` - Wrong! Use square brackets
   - ✓ `fruits[0]` - Correct!

3. **Forgetting to update position in loops**
   - ❌ `for item in list: item = "new"` - This doesn't work!
   - ✓ `for i in range(len(list)): list[i] = "new"` - Use index!

4. **Trying to access non-existent position**
   - ❌ `fruits[10]` when list only has 3 items
   - ✓ Check length first: `if 10 < len(fruits):`

## 🧪 Testing Your Code

Each level will print out checks to verify your code is correct. Look for:
- ✓ Green checkmarks = Correct!
- ✗ Red X marks = Try again

## 🚀 Extensions & Challenges

Once you master all 6 levels, try these:

1. **Game Inventory**: Create a game inventory system with items and quantities
2. **Leaderboard**: Sort player scores and display top 10
3. **Shopping Cart**: Add/remove items and calculate total price
4. **Data Analysis**: Calculate average, min, max of a list of numbers
5. **Turtle Graphics**: Use lists to store coordinates and draw shapes

## 🤔 For Teachers

See [LESSON_PLAN_LISTS.md](LESSON_PLAN_LISTS.md) for:
- Teaching strategies
- Real-world analogies
- Discussion questions
- Extension ideas
- Timing guidelines

## 📚 Related Topics

After mastering lists, explore:
- Dictionaries (storing key-value pairs)
- 2D Lists (lists of lists)
- List Comprehensions (advanced)
- Sorting algorithms
- Working with libraries

---

**Happy Learning! 🐍✨**
