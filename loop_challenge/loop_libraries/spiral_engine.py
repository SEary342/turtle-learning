import turtle


def setup():
    # Setup the screen
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Activity 2: The Spiral Maker (While Loops)")

    # Setup the turtle
    artist = turtle.Turtle()
    artist.shape("circle")
    artist.speed(0)  # Fastest speed
    artist.pensize(2)

    return artist, screen
