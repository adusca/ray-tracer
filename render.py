from geometry import *
from PIL import Image

path = "./rays.png"
size = 300
tmp = Image.new('RGB', (size, size), "white")
rays = tmp.load()

def coordinates(num, sz = size):
    """
    Take a number in range(size) and returns the proportional value between 1 and 5 
    """
    return 4.0*num/(sz - 1) + 1

def create_world():
    S1 = Sphere((4, 4, 2), 2, (100, 220, 0))
    S2 = Sphere((7, 7, 1), 1, (200, 10, 200))
    S3 = Sphere((3, 1, 1), 1, (100, 100, 200))
    P = HorizontalPlane(0, (200, 100, 200), (10, 200, 10))
    return [S1, S2, S3, P]

world = create_world()
camera = (3, -1, 3)
light = (0, 10, 0)

# Colouring each pixel
for i in range(size):
    x0 = coordinates(i)
    for j in range(size):
        y0 = coordinates(j)
        l = Line.through_points(camera, (x0, 0, y0))
        ans = []
        for S in world: 
            ts =  S.intersection_value(l)
            if ts:
                p = l.point_after_t(ts[0])
                ans.append((ts[0], S, p.coords))
        if not ans:
            rays[i, size - 1 - j] = (255, 255, 255)
        else:
            ans.sort()
            rays[i, size - 1 -j] = ans[0][1].color_at_point(ans[0][2])
            
tmp.save(path)
