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
    def __init__(self, cte, color1, color2):
        self.cte = cte
        self.color1 = color1
        self.color2 = color2

    def intersection_value(self, line):
        a = line.slope[2]
        if a == 0:
            return []
	t =  float(self.cte -  line.start[2])/line.slope[2]
        if t > 0.01:
            return [t]
        else:
            return []

    def color_at_point(self, p):
        if int(p[0]) % 2 == int(p[1]) % 2:
            return self.color1 
        else:
            return self.color2

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

    def intersection_value(self, line):
        v = Vector(line.slope)
        s = Vector(line.start)
        c = Vector(self.center)
        q = s.subtract(c)
        A = v.squared_norm()
        B = 2*v.scalar_product(q)
        C = q.squared_norm() - self.radius**2
        return solve_quadradic(A, B, C)
        
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

    def squared_norm(self):
        return sum(x**2 for x in self.coords)

    def norm(self):
        return sqrt(self.squared_norm())

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

def solve_quadradic(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return []
    ans = []
    ans.append((-b - sqrt(delta))/(2.0*a))
    ans.append((-b + sqrt(delta))/(2.0*a))
    return filter(lambda x: x > 0.01, ans)
