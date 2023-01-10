"""
It's creates a simple drawing with random color lines 
which is very interesting as each run will give different output.
"""
import turtle as t
import random

def random_color():
    """
    Generates a random RGB color.
    """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

def walk(size, total):
    """
    Move turtle object randomly and change its colour to random color and 
    draw lines, with the given `size` and `total` number of lines.
    """
    obj = t.Turtle()
    t.colormode(255)

    directions = [d for d in range(0, 360, 45)]
    for _ in range(total):
        obj.color(random_color())
        obj.forward(size)
        obj.setheading(random.choice(directions))

if __name__ == "__main__":
    total_lines = 100
    size = 30
    walk(size, total_lines)
