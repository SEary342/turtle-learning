from maze_libraries.maze_engine import move, player, setup_maze, screen

# 1. Choose your level (1-5)
setup_maze(level=5)

# 2. Write your commands below!
# Use move(distance) instead of player.forward()
# Use player.right(angle) and player.left(angle)

move(100)
player.right(90)
player.forward(260)
player.left(90)
player.forward(200)
player.right(90)
player.forward(200)
player.left(90)
player.forward(200)
player.left(90)
player.forward(300)

# Keep the window open
screen.mainloop()