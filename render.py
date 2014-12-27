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
    S2 = Sphere((2, 2, 1), 1, (0, 100, 200))
    S3 = Sphere((3, 1, 1), 1, (100, 100, 200))
    P = HorizontalPlane(0, (200, 100, 200), (0, 20, 200))
    return [S1, S2, S3, P]

def first_intersection(scene, line):
    ans = []
    for S in scene: 
        ts =  S.intersection_value(line)
        if ts:
            p = line.point_after_t(ts[0])
            ans.append((ts[0], S, p.coords))
    if not ans:
        return []
    ans.sort()
    return [ans[0]]

def first_intersection_color(scene, line):
    ans = first_intersection(scene, line)
    if not ans:
        return (255, 255, 255)
    to_light = first_intersection(scene, Line.through_points(ans[0][2], light))
    if to_light and to_light[0][0] < 1:
        return (0, 0, 0)
    return ans[0][1].color_at_point(ans[0][2])

world = create_world()
camera = (3, -1, 3)
light = (3, -1, 5)

# Colouring each pixel
for i in range(size):
    x0 = coordinates(i)
    for k in range(size):
        y0 = coordinates(k)
        j = size - 1 - k
        l = Line.through_points(camera, (x0, 0, y0))
        rays[i, j] = first_intersection_color(world, l)
            
tmp.save(path)
