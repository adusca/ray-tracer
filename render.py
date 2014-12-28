from geometry import *
from PIL import Image

def coordinates(num, sz):
    """
    Take a number in range(size) and returns the proportional value between 1 and 5 
    """
    return 4.0*num/(sz - 1) + 1

def create_world():
    S1 = Sphere((1, 4, 2), 2, (20, 200, 0))
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

def first_intersection_color(scene, line, light):
    ans = first_intersection(scene, line)
    if not ans:
        return (255, 255, 255)
    l = Line.through_points(ans[0][2], light)
    to_light = first_intersection(scene, l)
    if to_light and to_light[0][0] < 1:
        return (0, 0, 0)
    a, b, c = ans[0][1].color_at_point(ans[0][2])
    vector1 = Vector(l.slope).normalize()
    vector2 = ans[0][1].normal(ans[0][2])
    cos = vector1.scalar_product(vector2)
    return (int(a*cos), int(b*cos), int(c*cos))


def render(size):
    world = create_world()
    camera = (2, -1, 3)
    light = (3, -1, 10)
    color_dict = {}
    # Colouring each pixel
    for i in range(size):
        x0 = coordinates(i, size) 
        for k in range(size):
            y0 = coordinates(k, size)
            j = size - 1 - k
            l = Line.through_points(camera, (x0, 0, y0))
            color_dict[(i, j)] = first_intersection_color(world, l, light)
    return color_dict

def create_image(size):
    path = "./rays.png"
    tmp = Image.new('RGB', (size, size), "white")
    rays = tmp.load()
    dic = render(3*size)
    for i in range(size):
        for j in range(size):
            pixels_to_sum = [dic[(3*i + di, 3*j + dj)] for di in range(0,3) for dj in range(0,3)]
            sum_r, sum_g, sum_b = reduce(lambda (x1,x2,x3), (y1,y2,y3): (x1+y1, x2+y2, x3+y3), pixels_to_sum)
            rays[i, j] = (sum_r/9, sum_g/9, sum_b/9)    
    tmp.save(path)
            
create_image(500)

