from triangle import classify_triangle

def test_glass_stained_customer_requirements():
    assert classify_triangle(5, 5, 8) == "Isosceles"
    
    assert classify_triangle(-3, 4, 5) == "Invalid"
    
    assert classify_triangle(3, 4, 5) == "Right Scalene"