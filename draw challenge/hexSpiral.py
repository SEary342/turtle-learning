import turtle


colors = ["red", "purple", "blue", "green", "orange", "yellow"]


def hexSpiral():
    colLen = len(colors)
    t = turtle.Pen()
    turtle.bgcolor("black")
    turtle.speed(1000)
    for x in range(360):
        t.pencolor(colors[x % colLen])
        t.width(x / 100 + 1)
        t.forward(x)
        t.left(59)
    turtle.done()


if __name__ == "__main__":
    hexSpiral()
