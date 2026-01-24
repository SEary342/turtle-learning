import unittest
from unittest.mock import patch
import dragon_hoard

class TestDragonTreasure(unittest.TestCase):
    """
    Unit tests to verify the logic of the Dragon Treasure game engine.
    These tests ensure that the 'correct' solutions defined in the lesson plan
    actually result in a perfect score in the game engine.
    """

    def setUp(self):
        # Patch print and sleep to keep test output clean and fast
        self.patcher_print = patch('builtins.print')
        self.patcher_sleep = patch('dragon_hoard.time.sleep')
        self.mock_print = self.patcher_print.start()
        self.mock_sleep = self.patcher_sleep.start()

    def tearDown(self):
        self.patcher_print.stop()
        self.patcher_sleep.stop()

    def run_level_and_verify(self, level_function, student_solution):
        """
        Helper to run a level with a student solution and verify correctness.
        We mock check_answer to ensure every decision matches the expected outcome.
        """
        with patch('dragon_hoard.check_answer') as mock_check:
            # side_effect to return True if student matches correct, mimicking game logic
            mock_check.side_effect = lambda item, student, correct: student == correct
            
            # Run the level
            level_function(student_solution)
            
            # Verify check_answer was called at least once
            self.assertTrue(mock_check.called, "Game engine did not process any items.")
            
            # Verify every call was correct
            for call in mock_check.call_args_list:
                args = call.args
                # args structure: (item_display_name, student_decision, correct_decision)
                item_display = args[0]
                student_decision = args[1]
                correct_decision = args[2]
                
                self.assertEqual(
                    student_decision, 
                    correct_decision, 
                    f"Failed for item '{item_display}'. Student: '{student_decision}', Expected: '{correct_decision}'"
                )

    def test_level_1_logic(self):
        # Level 1: Gold -> keep, else -> dust
        def solution(item):
            if item == "gold":
                return "keep"
            return "dust"
        
        self.run_level_and_verify(dragon_hoard.start_level_1, solution)

    def test_level_2_logic(self):
        # Level 2: Gold/Silver -> vault, Ruby/Emerald -> chest, else -> incinerator
        def solution(item_type):
            if item_type == "gold" or item_type == "silver":
                return "vault"
            elif item_type == "ruby" or item_type == "emerald":
                return "chest"
            else:
                return "incinerator"
                
        self.run_level_and_verify(dragon_hoard.start_level_2, solution)

    def test_level_3_logic(self):
        # Level 3: NOT cursed -> keep, else -> banish
        def solution(status):
            if status != "cursed":
                return "keep"
            return "banish"
            
        self.run_level_and_verify(dragon_hoard.start_level_3, solution)

    def test_level_4_logic(self):
        # Level 4: NOT broken -> keep, else -> toss
        def solution(is_broken):
            if not is_broken:
                return "keep"
            return "toss"
            
        self.run_level_and_verify(dragon_hoard.start_level_4, solution)

    def test_level_5_logic(self):
        # Level 5: Value > 100 OR Magical -> keep, else -> toss
        def solution(value, is_magical):
            if value > 100 or is_magical:
                return "keep"
            return "toss"
            
        self.run_level_and_verify(dragon_hoard.start_level_5, solution)

    def test_level_6_logic(self):
        # Level 6: Knight & <10 -> fire, Thief & <5 -> bite, else -> watch
        def solution(intruder, distance):
            if intruder == "knight" and distance < 10:
                return "fire"
            elif intruder == "thief" and distance < 5:
                return "bite"
            return "watch"
            
        self.run_level_and_verify(dragon_hoard.start_level_6, solution)

if __name__ == '__main__':
    unittest.main()
