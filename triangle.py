import math

def classify_triangle(a, b, c):
    if not is_valid_triangle(a, b, c):
        return "Invalid"

    if a == b == c:
        classification = "Equilateral"
    elif a == b or a == c or b == c:
        classification = "Isosceles"
    else:
        classification = "Scalene"

    x, y, z = sorted((a, b, c))
    if math.isclose(x**2 + y**2, z**2, rel_tol=1e-9, abs_tol=1e-9):
        return f"Right {classification}"
    return classification

def is_valid_triangle(a, b, c):
    return a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a)