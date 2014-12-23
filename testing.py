from geometry import *

S = Sphere((0, 0, 0), 1, (10, 200, 20))
S2 = Sphere((0, 0, 0), 0.5, (10, 200, 20))
l = Line.throughPoints((-10, 0, 0), (1, 1, 1))
print S.intersect(l)
print S2.intersect(l)
