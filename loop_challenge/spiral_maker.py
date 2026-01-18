import random
from loop_libraries.spiral_engine import setup

# Setup the drawing environment
artist, screen = setup()

# --- LESSON: WHILE LOOPS ---
# A while loop runs AS LONG AS a condition is True.

countTurns = 10
colors = ["red", "orange", "yellow", "green", "blue", "purple"] # you can add more. Google how! 

# Keep drawing WHILE the line length is less than 300 pixels
while countTurns < 300:
    # Pick a random color
    artist.color(random.choice(colors))
    
    # Move forward by the current length
    artist.forward(countTurns)
    
    # Turn right
    artist.right(89) # 90 makes a square, 89 makes a spiral!
    
    # Make the line a little longer for next time
    countTurns = countTurns + 5

screen.mainloop()