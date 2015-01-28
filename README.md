Ray-tracer
==========

This project uses PIL to render images from a dictionary of pixel colors, the rest is straight Python.
Currently it generates this image:
![Ray-tracer](https://raw.githubusercontent.com/adusca/adusca.github.io/master/images/rays15.png)

To generate different pictures, just change the [create_word](https://github.com/adusca/ray-tracer/blob/master/render.py#L10-L17) function in render.py. For exemple, to generate a picture of a single red sphere:
```python
def create_world():
    S1 = Sphere((5, 3, 2), 1, (255, 0, 0), 0)
    return [S1]
```
