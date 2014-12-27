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

def create_world():
    S1 = Sphere((0, 0, 0), 0.5, (100, 220, 0))
    S2 = Sphere((0, 0, 0), 1, (200, 10, 200))
    S3 = Sphere((1, 1, -3), 0.4, (100, 100, 200))
    P = HorizontalPlane(0, (200, 200, 200))
    return [S1, S2, S3, P]

world = create_world()
camera = (0, 0, -8)
light = (0, 10, 0)

# Colouring each pixel
for i in range(size):
    x0 = coordinates(i)
    for j in range(size):
        y0 = coordinates(j)
        l = Line.through_points(camera, (x0, y0, -5))
        ans = []
        for S in world: 
            if S.intersect(l):
                t = S.intersection_value(l)
                p = l.point_after_t(t)
                ans.append((t, S, p.coords))
        if not ans:
            rays[i, j] = (255, 255, 255)
        else:
            ans.sort()
            rays[i, j] = ans[0][1].color_at_point(ans[0][2])
            
tmp.save(path)
