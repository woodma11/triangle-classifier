import math
from triangle import classify_triangle

def test_equilateral_triangle():
    assert classify_triangle(3, 3, 3) == "Equilateral"

def test_isosceles_triangle():
    assert classify_triangle(3, 3, 2) == "Isosceles"

def test_scalene_triangle():
    assert classify_triangle(3, 4, 6) == "Scalene"

def test_zero_side_is_invalid():
    assert classify_triangle(0, 4, 5) == "Invalid"
    
def test_degenerate_triangle_is_invalid():
    assert classify_triangle(2, 3, 1) == "Invalid"

def test_right_triangle():
    assert classify_triangle(3, 4, 5) == "Right Scalene"

def test_non_integer_right_triangle():
    assert classify_triangle(1.5, 2, 2.5) == "Right Scalene"

def test_right_isosceles_triangle():
    assert classify_triangle(1, 1, math.sqrt(2)) == "Right Isosceles"

