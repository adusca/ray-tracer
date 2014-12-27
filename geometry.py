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
    def through_points(point0, point1):
        """
        Creates a line that passes in two given points 
        """
        x1, y1, z1 = point1
        x0, y0, z0 = point0
        return Line((x1 - x0, y1 - y0, z1 - z0), (x0, y0, z0))

    def distance_to_point(self, point):
        """
        Returns the distance between a line and a point
        """
        q = Vector(point)
        v = Vector(self.slope)
        p = Vector(self.start)
        vec = q.subtract(p)
        proj = vec.project(v)
        return (proj.subtract(vec)).norm()

    def point_after_t(self, num):
        p = Vector(self.start)
        q = Vector(self.slope)
        return p.add(q.mul_by_number(num))

class HorizontalPlane():
    def __init__(self, cte, color):
        self.cte = cte
        self.color = color

    def intersect(self, line):
        return line.slope[2] != 0

    def intersection_value(self, line):
return float(self.cte -  line.start[2])/line.slope[2]

    def color_at_point(self, p):
        return (0, 200, 0) if int(p[0]) % 2 == int(p[1]) % 2 else (0, 0, 200)

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
        return line.distance_to_point(self.center) <= self.radius

    def intersection_value(self, line):
        v = Vector(line.slope)
        s = Vector(line.start)
        c = Vector(self.center)
        q = s.subtract(c)
        A = sum(x*x for x in v.coords)
        B = sum(-2*x*y for (x, y) in zip(v.coords, q.coords))
        C = sum(y*y for y in q.coords) - self.radius**2
        return solve_quadradic((A, B, C))
        
    def color_at_point(self, p):
        return self.color

class Vector():
    def __init__(self, coords):
        self.coords = coords

    def scalar_product(self, v2):
        return sum(x*y for (x, y) in zip(self.coords, v2.coords))

    def subtract(self, v2):
        return Vector([self.coords[0] - v2.coords[0], self.coords[1] - v2.coords[1], self.coords[2] - v2.coords[2]])

    def add(self, v2):
        return Vector([self.coords[0] + v2.coords[0], self.coords[1] + v2.coords[1], self.coords[2] + v2.coords[2]])

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

def solve_quadradic(coef):
    a = coef[0]
    b = coef[1]
    c = coef[2]
    delta = b**2 - 4*a*c
    ans = []
    ans.append(-b + sqrt(delta)/2.0*a)
    x = -b - sqrt(delta)/2.0*a
    if x >= 0:
        ans.append(x)
    return min(ans)
