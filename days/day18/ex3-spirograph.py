
import turtle as t
import random

DEGRESS = 360
COLORMODE = 255

def random_color():
    """
    Generates a random RGB color.
    """
    r = random.randint(0, COLORMODE)
    g = random.randint(0, COLORMODE)
    b = random.randint(0, COLORMODE)
    return (r, g, b)

def draw(displacement, radius):
    """
    Draws circles in different colors and with a 
    `displacement` angle between them, with a given `radius`
    """
    obj = t.Turtle()
    t.colormode(COLORMODE)

    amount_of_circles = int(DEGRESS / displacement)
    for _ in range(amount_of_circles):
        obj.color(random_color())
        obj.circle(radius)
        obj.setheading(obj.heading() + displacement)

if __name__ == "__main__":
    displacement = 10
    radius = 50
    draw(displacement, radius)
