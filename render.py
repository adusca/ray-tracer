from geometry import *
from PIL import Image

path = "./rays.png"

tmp = Image.new('RGB', (200, 200), "white")
rays = tmp.load()

def coordinates(num):
    """
    Take a number between 0 and 199 and returns the proportional value between -2 and 2
    """
    return 8.0*num/199.0 - 2.0


S = Sphere((0, 0, 0), 0.5, (0, 0, 0))
origin = (-10, 0, 0)


for i in range(200):
    x0 = coordinates(i)
    for j in range(200):
        y0 = coordinates(j)
        l = Line.throughPoints(origin, (x0, y0, -5))
        rays[i, j] = S.intersect(l)

tmp.save(path)
