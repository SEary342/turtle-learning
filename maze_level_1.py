from maze_challenge.maze_engine import move, player, setup_maze, screen

# 1. Choose your level (1-5)
setup_maze(level=1)

# 2. Write your commands below!
# Use move(distance) instead of player.forward()
# Use player.right(angle) and player.left(angle)

move(100)
player.left(90)
player.forward(80)

# Keep the window open
screen.mainloop()