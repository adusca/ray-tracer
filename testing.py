from geometry import *

def test_intersect_True():
    S = Sphere((0, 0, 0), 1, (10, 200, 20))
    l = Line.throughPoints((0, 1, 0), (0, 1, 1))
    assert S.intersect(l) 

def test_intersect_False():
    S = Sphere((100, 100, 100), 0.1, (10, 200, 20))
    l = Line.throughPoints((0, 0, 1), (0, 0, 2))
    assert S.intersect(l) == False

def test_subtract():
    v = Vector([1, 0, 0])
    w = Vector([1, 1, 0])
    r = Vector([0, 1, 0])
    assert w.subtract(v).equals(r)

def test_norm():
    v = Vector([1, 0, 0])
    w = Vector([0, 2, 0])
    assert v.norm() == 1.0
    assert w.norm() == 2.0

def test_cross_product():
    v = Vector([1, 2, 3])
    w = Vector([4, 5, 6])
    r = Vector([-3, 6, -3])
    assert v.cross_product(w).equals(r)

def test_mul_by_number():
    v = Vector([1, 1, 1])
    r = Vector([2, 2, 2])
    assert v.mul_by_number(2).equals(r)


# Calling tests

test_intersect_True()
test_intersect_False()
test_subtract()
test_norm()
test_cross_product()
test_mul_by_number()
