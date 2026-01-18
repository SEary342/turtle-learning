import sys
from unittest.mock import MagicMock, patch
import pytest

# 1. Mock turtle BEFORE importing maze_engine to prevent window creation
sys.modules["turtle"] = MagicMock()

# 2. Import the module to be tested
from maze_challenge.maze_libraries import maze_engine  # noqa: E402


class TestMazeEngine:
    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        """Resets globals and mocks before each test."""
        # Reset global variables in maze_engine
        maze_engine.walls = []
        maze_engine.goal_pos = (0, 0)
        maze_engine.has_said_yay = False

        # Reset the player mock configuration
        maze_engine.player.reset_mock()
        # Configure return values for math calculations
        maze_engine.player.heading.return_value = 0.0
        maze_engine.player.pos.return_value = (0.0, 0.0)
        maze_engine.player.xcor.return_value = 0.0
        maze_engine.player.ycor.return_value = 0.0
        maze_engine.player.distance.return_value = 100.0  # Default: not at goal

        yield

    def test_get_collision_point_none(self):
        """Test that moving in open space returns None."""
        # Wall is far away
        maze_engine.walls = [(100, 100, 200, 200)]
        start_x, start_y = 0, 0
        end_x, end_y = 50, 0

        collision = maze_engine.get_collision_point(start_x, start_y, end_x, end_y)
        assert collision is None

    def test_get_collision_point_hit(self):
        """Test that moving through a wall returns a collision point."""
        # Wall blocking the x-axis at x=50
        # Format: x1, y1, x2, y2
        maze_engine.walls = [(50, -100, 60, 100)]

        start_x, start_y = 0, 0
        end_x, end_y = 100, 0

        collision = maze_engine.get_collision_point(start_x, start_y, end_x, end_y)

        assert collision is not None
        cx, cy = collision
        # Buffer is 8, so collision should be detected around x=50 +/- buffer
        assert 40 <= cx <= 70
        assert cy == 0

    def test_move_success(self):
        """Test moving without collision."""
        maze_engine.walls = []
        maze_engine.goal_pos = (200, 0)

        maze_engine.move(100)

        # Should move to (100, 0)
        maze_engine.player.goto.assert_called_with(100.0, 0.0)
        # Should not write OUCH
        maze_engine.player.write.assert_not_called()

    def test_move_collision(self):
        """Test moving into a wall."""
        # Wall at x=50
        maze_engine.walls = [(50, -100, 60, 100)]

        maze_engine.move(100)

        # Should NOT go to (100, 0), but to collision point
        args, _ = maze_engine.player.goto.call_args
        dest_x, dest_y = args
        assert dest_x < 100
        assert dest_x > 40  # Hit the wall

        # Should write OUCH
        maze_engine.player.write.assert_called()
        assert "OUCH" in maze_engine.player.write.call_args[0][0]

    def test_move_reach_goal(self):
        """Test reaching the goal triggers the 'yay' message."""
        maze_engine.walls = []
        maze_engine.goal_pos = (100, 0)

        # Mock distance to return small value (reached goal)
        maze_engine.player.distance.return_value = 10.0

        maze_engine.move(100)

        maze_engine.player.goto.assert_called_with(100.0, 0.0)
        maze_engine.player.write.assert_called()
        assert "yay" in maze_engine.player.write.call_args[0][0]

    def test_setup_maze(self):
        """Test that setup_maze loads level data correctly."""
        with patch("os.system"):  # Prevent OS commands
            maze_engine.setup_maze(1)

        assert maze_engine.walls == maze_engine.LEVELS[1]["walls"]
        assert maze_engine.goal_pos == maze_engine.LEVELS[1]["goal"]
        maze_engine.player.showturtle.assert_called()
