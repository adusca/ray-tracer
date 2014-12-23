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
        currently broken
        """
        return 1

class Sphere():
    def __init__(self, center, radius):
        """
        Center is an 3-element tuple
        Radius is a positive number
        """
        self.center = center
        self.radius = radius

    @staticmethod
    def new_sphere(center, radius):
        return Sphere(center, radius)

def intersect(line, sphere):
    return line.distanceToPoint(sphere.center) <= sphere.radius

S = Sphere.new_sphere((0, 0, 0), 1)
S2 = Sphere.new_sphere((0, 0, 0), 0.5)
l = Line.throughPoints((-10, 0, 0), (1, 1, 1))
print intersect(l, S)
print intersect(l, S2)
