import random
import time


# ANSI colors for fun output
class Colors:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"


def print_slow(text):
    print(text)
    time.sleep(0.5)


def check_answer(item, student_decision, correct_decision):
    print(f"Dragon presents: {Colors.BOLD}{item}{Colors.ENDC}")
    print(f"You decided to: {Colors.BLUE}{student_decision}{Colors.ENDC}")

    if student_decision == correct_decision:
        print(f"{Colors.GREEN}Correct! The dragon is pleased.{Colors.ENDC}")
        return True
    else:
        print(
            f"{Colors.FAIL}Wrong! The dragon growls. (Expected: {correct_decision}){Colors.ENDC}"
        )
        return False


# --- LEVEL 1 LOGIC ---
def start_level_1(student_function):
    print(f"{Colors.HEADER}--- LEVEL 1: The Pile of Gold ---{Colors.ENDC}")
    print("Instructions: If it is 'gold', return 'keep'. Otherwise, return 'dust'.\n")

    score = 0
    items = ["gold", "rock", "gold", "shoe", "gold", "bone", "gold"]

    for item in items:
        try:
            decision = student_function(item)
        except Exception as e:
            print(f"{Colors.FAIL}Error in your code: {e}{Colors.ENDC}")
            return

        correct = "keep" if item == "gold" else "dust"

        if check_answer(item, decision, correct):
            score += 1
        print("-" * 20)
        time.sleep(1)

    print(f"Level 1 Score: {score}/{len(items)}")
    if score == len(items):
        print(f"{Colors.HEADER}PERFECT! You move to Level 2.{Colors.ENDC}")


# --- LEVEL 2 LOGIC ---
def start_level_2(student_function):
    print(f"\n{Colors.HEADER}--- LEVEL 2: Gems and Rubbish ---{Colors.ENDC}")
    print(
        "Instructions: 'gold' -> 'vault', 'gem' -> 'chest', everything else -> 'incinerator'.\n"
    )

    score = 0
    items = [
        {"type": "gold", "name": "Gold Coin"},
        {"type": "trash", "name": "Old Boot"},
        {"type": "gem", "name": "Ruby"},
        {"type": "gem", "name": "Emerald"},
        {"type": "trash", "name": "Fish Bone"},
        {"type": "gold", "name": "Gold Bar"},
    ]

    for item in items:
        try:
            decision = student_function(item["type"])
        except Exception as e:
            print(f"{Colors.FAIL}Error in your code: {e}{Colors.ENDC}")
            return

        if item["type"] == "gold":
            correct = "vault"
        elif item["type"] == "gem":
            correct = "chest"
        else:
            correct = "incinerator"

        if check_answer(item["name"], decision, correct):
            score += 1
        print("-" * 20)
        time.sleep(1)

    print(f"Level 2 Score: {score}/{len(items)}")


# --- LEVEL 3 LOGIC ---
def start_level_3(student_function):
    print(f"\n{Colors.HEADER}--- LEVEL 3: The Appraiser ---{Colors.ENDC}")
    print(
        "Instructions: Value > 100 -> 'keep'. Value <= 100 -> 'toss'. BUT if it is 'magical', always 'keep'.\n"
    )

    score = 0
    items = [
        {"name": "Rusty Sword", "value": 5, "magical": False},
        {"name": "Diamond", "value": 500, "magical": False},
        {"name": "Magic Bean", "value": 1, "magical": True},
        {"name": "Golden Crown", "value": 200, "magical": False},
        {"name": "Cursed Ring", "value": 50, "magical": True},
    ]

    for item in items:
        try:
            decision = student_function(item["value"], item["magical"])
        except Exception as e:
            print(f"{Colors.FAIL}Error in your code: {e}{Colors.ENDC}")
            return

        if item["magical"] or item["value"] > 100:
            correct = "keep"
        else:
            correct = "toss"

        if check_answer(item["name"], decision, correct):
            score += 1
        print("-" * 20)
        time.sleep(1)

    print(f"Level 3 Score: {score}/{len(items)}")
