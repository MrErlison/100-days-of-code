"""
The draw function creates a turtle object and draws total number of 
shapes, each with sides number of sides and each side of length size. 
Each shape is a polygon, it starts with 3 sides, and each shape the 
number of sides increase by 1 up to total shapes.
"""

import turtle as t

DEGRESS = 360

def draw(total, sides, size):
    """
    Draws `total` number of shapes, each with `sides` number of sides and each side of length `size`.
    """
    obj = t.Turtle()
    for _ in range(total):
        for _ in range(sides):
            obj.forward(size)
            obj.right(DEGRESS / sides)
        sides += 1

if __name__ == "__main__":
    total_drawings = 5
    sides = 3
    size = 30
    draw(total_drawings, sides, size)
