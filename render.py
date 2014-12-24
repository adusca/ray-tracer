from geometry import *
from PIL import Image

path = "./rays.png"
size = 300
tmp = Image.new('RGB', (size, size), "white")
rays = tmp.load()

def coordinates(num, sz = size):
    """
    Take a number in range(size) and returns the proportional value between -2 and 2
    """
    return 4.0*num/(sz - 1) - 2.0

# Creating the world
S1 = Sphere((1, 0, 0), 0.5, (10, 220, 0))
S2 = Sphere((0.6, 0, 0), 0.5, (200, 10, 200))
camera = (0, 0, -8)
world = [S1, S2]

# Colouring each pixel
for i in range(size):
    x0 = coordinates(i)
    for j in range(size):
        y0 = coordinates(j)
        l = Line.throughPoints(camera, (x0, y0, -5))
        ans = []
        for S in world: 
            if S.intersect(l):
                ans.append((S.intersection_value(l), S))
        if not ans:
            rays[i, j] = (255, 255, 255)
        else:
            ans.sort()
            rays[i, j] = ans[0][1].color
            

tmp.save(path)
