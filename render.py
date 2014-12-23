from geometry import *
from PIL import Image

path = "./rays.png"

tmp = Image.new('RGB', (100, 100), "white")
rays = tmp.load()



tmp.save(path)
