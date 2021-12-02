'''CS 101 Lab
Program 12
Madison Shaver
mlsy7z@umkc.edu

PROBLEM: Use classes and inheritance to output a dot, rectangle, and circle.

ALGORITHM:
    1. Start
    2. Import turtle module
    3. Create an instance of class Point with x and y coordinates and 
       color as parameters
    4. Draw a dot with function in Point class
        4a. go to given x and y coordinates
        4b. set color to given color
        4c. use draw action function to draw
            4c.1. use dot method to draw a dot
    5. Create an instance of class Box with x and y coordinates, color, 
       height, and width as parameters
    6. Draw a box with functions in Box class (Box inherits from Point)
        6a. repeat steps 4a-4c with the exception of 4c.1.
            6a.1. with pen down, move turtle forward the length of the width
            6a.2. turn turtle 90 degree to the right
            6a.3. move turtle forward the length of the height
            6a.4. turn turtle 90 degrees to the right
            6a.5. repeat steps 6a.1-6a.3
    7. Create an instance of class BoxFilled with x and y coordinates, color, 
       height, width, and fill color as parameters
    8. Fill a box with functions in BoxFilled class (BoxFilled inherits from Box)
        8a. begin fill
        8b. repeat all of 6a
        8c. set fill color
        8d. end fill
    9. Create an instance of class Circle with x and y coordinates, color, 
       and radius as parameters
    10. Draw a circle with functions in Circle (Circle inherits from Point)
        10a. repeat steps 4a-4c with the exception of 4c.1
            10a.1. with pen down, use circle method to draw a circle
    11. Create an instance of CircleFilled with x and y coordinates, color, 
        radius, and fill color as parameters
    12. Fill a circle with functions in CircleFilled class (CircleFilled 
        inherits from Circle)
        12a. begin fill
        12b. repeat all of 10a
        12c. set fill color
        12d. end fill
    13. End
'''

import turtle

class Point():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()

    def draw_action(self):
        turtle.dot()

class Box(Point):
    def __init__(self, x1, y1, height, width, color):
        Point.__init__(self, x1, y1, color)
        self.height = height
        self.width = width

    def draw_action(self):
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)

class BoxFilled(Box):
    def __init__(self, x1, y1, height, width, color, fillcolor):
        Box.__init__(self, x1, y1, height, width, color)
        self.fillcolor = fillcolor

    def draw_action(self):
        turtle.begin_fill()
        Box.draw_action(self)
        turtle.color(self.fillcolor)
        turtle.end_fill()

class Circle(Point):
    def __init__(self, x1, y1, radius, color):
        Point.__init__(self, x1, y1, color)
        self.radius = radius

    def draw_action(self):
        turtle.circle(self.radius)

class CircleFilled(Circle):
    def __init__(self, x1, y1, radius, color, fillcolor):
        Circle.__init__(self, x1, y1, radius, color)
        self.fillcolor = fillcolor

    def draw_action(self):
        turtle.begin_fill()
        turtle.circle(self.radius)
        turtle.color(self.fillcolor)
        turtle.end_fill()

if __name__ == '__main__':
    p = Point(0, 0, 'blue')
    p.draw()

    b = Box(125, 100, 200, 150, 'red')
    b.draw()

    bf = BoxFilled(125, 100, 200, 150, 'green', 'blue')
    bf.draw()

    c = Circle(-200, -75, 75, 'red')
    c.draw()

    cf = CircleFilled(-200, -75, 75, 'green', 'blue')
    cf.draw()