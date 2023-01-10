"""
It's creates a simple drawing with random color lines 
which is very interesting as each run will give different output.
"""
import turtle as t
import random

COLORMODE = 255

def random_color():
    """
    Generates a random RGB color.
    """
    r = random.randint(0, COLORMODE)
    g = random.randint(0, COLORMODE)
    b = random.randint(0, COLORMODE)
    return (r,g,b)

def walk(size, total):
    """
    Move turtle object randomly and change its colour to random color and 
    draw lines, with the given `size` and `total` number of lines.
    """
    obj = t.Turtle()
    t.colormode(COLORMODE)

    directions = [d for d in range(0, 360, 45)]
    for _ in range(total):
        obj.color(random_color())
        obj.forward(size)
        obj.setheading(random.choice(directions))

if __name__ == "__main__":
    total_lines = 100
    size = 30
    walk(size, total_lines)
