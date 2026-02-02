"""
LIST CHALLENGE LIBRARY
Provides visual feedback for list operations
"""


def print_list_state(list_name, the_list):
    """Print a list in a nice format"""
    print(f"\n{'=' * 50}")
    print(f"List: {list_name}")
    print(f"{'=' * 50}")
    for i, item in enumerate(the_list):
        print(f"  Position {i}: {item}")
    print(f"Total items: {len(the_list)}")
    print(f"{'=' * 50}\n")


def check_answer(student_answer, correct_answer):
    """Check if student got the answer right"""
    if student_answer == correct_answer:
        print("✓ CORRECT! Great job!")
        return True
    else:
        print(f"✗ Not quite. Got: {student_answer}, Expected: {correct_answer}")
        return False
