"""
SoftDes in-class exercise: Geometry classes
"""
import math


class Line:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
    def __str__(self):
        """Python's `print` function calls this method. It should return a string.

        Examples:
        >>> line = Line(10, 20, 100, 200)
        >>> print(line)
        Line(10, 20, 100, 200)
        """
        return 'Line(%.d, %.d, %.d, %.d)' % (self.x0, self.y0, self.x1, self.y1)

    def top(self):
        """Return the smallest y value.

        This is the *opposite* of the convention in math. It's the standard convention in many computer window
        systems and 2D computer graphics systems -- probably because Western writing systems, except boustrophedon
        Greek and Irish runes, are written from left to right (x increases to the right) and top to bottom (y
        increases towards the ground).

        Examples:
        >>> Line(10, 20, 100, 200).top()
        20
        >>> Line(100, 200, 10, 20).top()
        20
        """
        if self.y0 <= self.y1:
            return self.y0
        else:
            return self.y1

    def left(self):
        """Returns the smallest x value.
        Examples:
        >>> Line(10, 20, 100, 200).left()
        10
        >>> Line(100, 200, 10, 20).left()
        10
        """
        if self.x0 <= self.x1:
            return self.x0
        else:
            return self.x1

    def bottom(self):
        """Returns the biggest y value
        >>> Line(10, 20, 100, 200).bottom()
        200
        >>> Line(100, 200, 10, 20).bottom()
        200
        """
        if self.y0 >= self.y1:
            return self.y0
        else:
            return self.y1

    def right(self):
        """Returns the biggest x value
        >>> Line(10, 20, 100, 200).right()
        100
        >>> Line(100, 200, 10, 20).right()
        100
        """
        if self.x0 >= self.x1:
            return self.x0
        else:
            return self.x1

    def length(self):
        """Examples:
        >>> Line(10, 20, 10 + 30, 20 + 40).length()
        50.0
        """
        return math.sqrt((self.x1-self.x0)**2+(self.y1-self.y0)**2)

    def is_horizontal(self):
        """Examples:
        >>> Line(10, 20, 100, 20).is_horizontal()
        True
        >>> Line(10, 20, 10, 200).is_horizontal()
        False
        """
        if self.y0 == self.y1:
            return True
        else:
            return False

    def is_vertical(self):
        """Examples:
        >>> Line(10, 20, 10, 200).is_vertical()
        True
        >>> Line(10, 20, 100, 20).is_vertical()
        False
        """
        if self.x0 == self.x1:
            return True
        else:
            return False

    def intersection(self, other):
        """Going Beyond: Returns the intersection of two lines.

        For this assignment, this only need work if `self` and `other` are
        both horizontal. This is already surprisingly difficult.

        Examples:
        # >>> Line(10, 20, 100, 20).intersection(Line(5, 20, 105, 20))
        # Line(10, 20, 100, 20)
        # >>> Line(10, 20, 100, 20).intersection(Line(5, 20, 15, 20))
        # Line(10, 20, 15, 20)
        # >>> Line(10, 20, 100, 20).intersection(Line(15, 20, 105, 20))
        # Line(15, 20, 100, 20)
        # >>> Line(10, 20, 100, 20).intersection(Line(15, 20, 95, 20))
        # Line(15, 20, 95, 20)
        # >>> Line(15, 20, 95, 20).intersection(Line(10, 20, 100, 20))
        # Line(15, 20, 95, 20)
        """
        pass


class Rect:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
    def __str__(self):
        """Examples:
        >>> rect = Rect(10, 20, 100, 200)
        >>> print(rect)
        Rect(10, 20, 100, 200)
        """
        return 'Rect(%.d, %.d, %.d, %.d)' % (self.x0, self.y0, self.x1, self.y1)

    def width(self):
        """Examples:
        >>> Rect(10, 20, 100, 200).width()
        90
        >>> Rect(100, 200, 10, 20).width()
        90
        """
        return abs(self.x1-self.x0)

    def height(self):
        """Examples:
        >>> Rect(10, 20, 100, 200).height()
        180
        >>> Rect(100, 200, 10, 20).height()
        180
        """
        return abs(self.y1-self.y0)

    def area(self):
        """Examples:
        >>> Rect(10, 20, 100, 200).area()
        16200
        """
        return (abs(self.y1-self.y0) * abs(self.x1-self.x0))

    def bbox(self):
        """Return this shape's bounding box. This is the smallest practically-computable rectangle that contains all
        the points in this shape's interior. For a rectangle, its bounding box is itself. The bounding box is a
        fundamental graphics concept."""
        return self

    def contains_pt(self, x0, y0):
        """Examples:
        >>> Rect(10, 20, 100, 200).contains_pt(5, 5)
        False
        >>> Rect(10, 20, 100, 200).contains_pt(50, 50)
        True
        >>> Rect(10, 20, 100, 200).contains_pt(5, 50)
        False
        >>> Rect(10, 20, 100, 200).contains_pt(50, 5)
        False
        >>> Rect(10, 20, 100, 200).contains_pt(50, 300)
        False
        >>> Rect(100, 200, 10, 20).contains_pt(50, 50)
        True
        """
        if x0 > self.x0 and x0 < self.x1:
            if y0 > self.y0 and y0 < self.y1:
                return True
            elif y0 < self.y0 and y0 > self.y1:
                return True
            else:
                return False
        elif x0 < self.x0 and x0 > self.x1:
            if y0 > self.y0 and y0 < self.y1:
                return True
            elif y0 < self.y0 and y0 > self.y1:
                return True
            else:
                return False
        else:
            return False

    def intersection(self):
        """Going Beyond: intersection. `self` is another instance of `Rect`.

        Examples:
        # >>> Rect(10, 20, 100, 200).intersection(Rect(15, 25, 90, 180))
        # Rect(15, 25, 90, 180)
        """
        pass

print(Line(0,1,2,3))

# Run this code when called from the command line
if __name__ == "__main__":
    import doctest

    # Run all doctests in this file
    doctest.testmod()

    # Run the doctests for a single function or method (e.g. Line.left)
    # doctest.run_docstring_examples(Line.left, globals())
