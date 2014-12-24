from math import sqrt

class Line():
    def __init__(self, slope, start):
        """
        Slope is a 3-element tuple representing the line slope
        Start is a 3-element tuple representing one point in the line
        """
        self.slope = slope
        self.start = start

    @staticmethod
    def throughPoints(point0, point1):
        """
        Creates a line that passes in two given points 
        """
        x1, y1, z1 = point1
        x0, y0, z0 = point0
        return Line((x1 - x0, y1 - y0, z1 - z0), (x0, y0, z0))

    def distanceToPoint(self, point):
        """
        Returns the distance between a line and a point
        """
        q = Vector(point)
        v = Vector(self.slope)
        p = Vector(self.start)
        vec = q.subtract(p)
        proj = vec.project(v)
        return (proj.subtract(vec)).norm()

class Sphere():
    def __init__(self, center, radius, color):
        """
        Center is a 3-element tuple representing a spacial position
        Radius is a positive number
        Color is 3-element tuple representing RGB values of the sphere's color
        """
        self.center = center
        self.radius = radius
        self.color = color

    def intersect(self, line):
        if line.distanceToPoint(self.center) <= self.radius:
            return self.color
        else:
            return (255, 255, 255)

class Vector():
    def __init__(self, coords):
        self.coords = coords

    def scalar_product(self, v2):
        return sum(x*y for (x, y) in zip(self.coords, v2.coords))

    def subtract(self, v2):
        return Vector([self.coords[0] - v2.coords[0], self.coords[1] - v2.coords[1], self.coords[2] - v2.coords[2]])

    def norm(self):
        return sqrt(sum(x**2 for x in self.coords))

    def cross_product(self, v2):
        a0, a1, a2 = self.coords
        b0, b1, b2 = v2.coords
        return Vector([a1*b2 - a2*b1, a2*b0 - a0*b2, a0*b1 - a1*b0])

    def equals(self, v2):
        eps = 0.0001
        for i in range(len(self.coords)):
            if abs(self.coords[i] - v2.coords[i]) > eps:
                return False
        return True

    def mul_by_number(self, num):
        return Vector([x*num for x in self.coords])

    def project(self, v2):
        n = float(self.scalar_product(v2))/v2.scalar_product(v2)
        return v2.mul_by_number(n)
