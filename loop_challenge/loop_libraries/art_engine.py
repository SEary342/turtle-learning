import turtle

def setup():
    # Setup the screen
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Activity 1: The Shape Maker (For Loops)")

    # Setup the turtle
    blueTurtle = turtle.Turtle()
    blueTurtle.shape("turtle")
    blueTurtle.color("cyan") # changes the color
    blueTurtle.speed(5) # changes how fast it draws
    blueTurtle.pensize(3) # changes the size of the line
    
    return blueTurtle, screen