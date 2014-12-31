from geometry import *
from PIL import Image

def coordinates(num, sz):
    """
    Take a number in range(size) and returns the proportional value between 0 and 4 
    """
    return 4.0*num/(sz - 1)

def create_world():
    S1 = Sphere((5, 3, 2), 2, (20, 200, 0), 0.6) 
    S2 = Sphere((2, 2, 1), 1, (0, 100, 200), 0.5)
    S3 = Sphere((8, 1, 2), 1, (100, 100, 200))
    S4 = Sphere((1, 4, 2), 1, (20, 200, 0))
    S5 = Sphere((7, 4, 2), 1, (200, 0, 0))
    P = HorizontalPlane(0, (200, 100, 200), (0, 20, 200))
    return [S1, S2, S3, S4, S5, P]

def first_intersection(scene, line):
    ans = []
    for S in scene: 
        ts =  S.intersection_value(line)
        if ts:
            p = line.point_after_t(ts[0])
            ans.append((ts[0], S, p.coords))
    if not ans:
        return None
    ans.sort()
    return ans[0]

def first_intersection_color(scene, line, light, num_iterations=0):
    if num_iterations >= 2:
        return (0, 0, 0)
    ans = first_intersection(scene, line)
    if ans == None:
        return (255, 255, 255)
    r = ans[1].reflectivity
    normal = ans[1].normal(ans[2])
    shadow_ray = Line.through_points(ans[2], light)
    to_light = first_intersection(scene, shadow_ray)
    if to_light != None and to_light[0] < 1:
        value_diffuse =  (0, 0, 0)
    else:
        a, b, c = ans[1].color_at_point(ans[2])
        vector1 = Vector(shadow_ray.slope).normalize()
        cos = max(0, vector1.scalar_product(normal))
        value_diffuse = (int(a*cos*(1-r)), int(b*cos*(1-r)), int(c*cos*(1-r)))
    if r == 0:
        return value_diffuse
    v = Vector(line.slope).normalize().mul_by_number(-1)
    reflex = v.project(normal).mul_by_number(2).subtract(v)
    new_line = Line(reflex.coords, ans[2])
    value_reflection =  first_intersection_color(scene, new_line, light, num_iterations + 1)
    value_reflection = tuple_times_num(value_reflection, r)
    return (value_diffuse[0] + value_reflection[0], value_diffuse[1] + value_reflection[1], value_diffuse[2] + value_reflection[2])

def render(size):
    world = create_world()
    camera = (1, -2, 3)
    light = (2, -1, 6)
    color_dict = {}
    # Colouring each pixel
    for i in range(size):
        x0 = coordinates(i, size) 
        for k in range(size):
            y0 = coordinates(k, size)
            j = size - 1 - k
            l = Line.through_points(camera, (x0, -1, y0))
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
            rays[i, j] = tuple_average(pixels_to_sum)
    tmp.save(path)
            
create_image(300)

