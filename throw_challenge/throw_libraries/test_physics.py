import unittest
import math
import throw_challenge.throw_libraries.physics as physics
from throw_challenge.throw_libraries.game_engine import LEVELS


class TestPhysics(unittest.TestCase):
    def test_landing_distance_with_drag(self):
        """Test that drag reduces the range compared to vacuum."""
        v = 20
        angle = 45
        g = physics.GRAVITY

        # Vacuum range formula
        expected_range = (v**2 * math.sin(math.radians(2 * angle))) / g

        # Simulated range with drag
        result = physics.calculate_landing_x(v, angle)

        # Result should be less than vacuum range due to air resistance
        self.assertLess(result, expected_range)
        self.assertGreater(result, 0)

    def test_vertical_throw(self):
        """A vertical throw should land exactly where it started (drag acts vertically)."""
        result = physics.calculate_landing_x(velocity=10, angle_degrees=90, start_x=0)
        self.assertAlmostEqual(result, 0, places=1)

    def test_start_offset(self):
        """Test throwing from a different x position."""
        v = 10
        angle = 45
        # Calculate range from 0
        range_from_zero = physics.calculate_landing_x(v, angle, start_x=0)
        # Calculate range from 10
        range_from_ten = physics.calculate_landing_x(v, angle, start_x=10)

        self.assertAlmostEqual(range_from_ten, range_from_zero + 10, places=1)

    def test_target_height_landing(self):
        """Test that the ball lands at the correct distance for an elevated target."""
        v = 15
        angle = 60
        target_h = 1.0

        # Calculate landing x for target height 1
        landing_x = physics.calculate_landing_x(v, angle, target_height=target_h)

        # Ensure it lands shorter than it would on flat ground
        flat_landing = physics.calculate_landing_x(v, angle, target_height=0)
        self.assertTrue(landing_x < flat_landing)

    def test_levels_solvable(self):
        """Ensure all levels (except 4) have at least one valid solution."""
        for level_num, config in LEVELS.items():
            if level_num == 4:
                continue

            target_dist = config["target_dist"]
            target_width = config["target_width"]
            start_height = config["start_height"]
            target_height = config.get("target_height", 0)
            tolerance = config.get("tolerance", 1.0)

            solution_found = False

            if level_num == 5:
                # Level 5: Weak Robot (Fixed V=6, A=60, vary Position)
                velocity = 6
                angle = 60
                # Search range for robot position
                for pos in range(-20, int(target_dist) + 5):
                    landing_x = physics.calculate_landing_x(
                        velocity,
                        angle,
                        start_x=pos,
                        start_height=start_height,
                        target_height=target_height,
                        target_dist=target_dist,
                        target_width=target_width,
                    )
                    if abs(landing_x - target_dist) <= tolerance:
                        solution_found = True
                        break
            else:
                # Standard Levels: Fixed Position=0, vary Velocity and Angle
                for velocity in range(10, 121):
                    if solution_found:
                        break
                    for angle in range(10, 90):
                        landing_x = physics.calculate_landing_x(
                            velocity,
                            angle,
                            start_x=0,
                            start_height=start_height,
                            target_height=target_height,
                            target_dist=target_dist,
                            target_width=target_width,
                        )
                        if abs(landing_x - target_dist) <= tolerance:
                            solution_found = True
                            break

            self.assertTrue(solution_found, f"Level {level_num} should be solvable.")


if __name__ == "__main__":
    unittest.main()
