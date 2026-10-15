# Triangle Classifier

## A simple Python program that classifies triangles based on the lengths of their sides. The program can identify whether a triangle is equilateral, isosceles, scalene, or right-angled.

# How to run the tests

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -v

# Equivalence Classes and Boundaries
   ## - Negative side lengths: Invalid triangle
   ## - Failed triangle inequality: Invalid triangle
   ## - Degenerate triangle (sum of two sides equals the third): Invalid triangle
   ## - Equilateral triangle (all sides equal): Valid triangle
   ## - Isosceles triangle (two sides equal): Valid triangle
   ## - Scalene triangle (all sides different): Valid triangle
   ## - Right-angled triangle (satisfies Pythagorean theorem): Valid triangle
   ## -Equilateral triangle cannot be right-angled: Invalid triangle
   ## - Key boundaries: side lengths of 0, negative values, and values that violate the triangle inequality(such as 1, 2, 3).

# Copilot Review Log
    ## - test_equilateral_triangle: accepted copilot suggestion, it correctly expected "Equilateral" for 3 equal side lengths.

    ## - classify_triangle: rejected copilot suggestion, the draft tried to return "Right {base_classification}" before a real classification variable existed, which would have caused a runtime error. I corrected this by ensuring the base classification was determined first.

    ## - test_degenerate_triangle_is_invalid: accepted copilot suggestion, it correctly expected "Invalid" for a degenerate triangle.

    ## - test_right_isosceles_triangle: edited copilot suggestion, it incorrectly expected "Isosceles" for a right isosceles triangle, but I corrected it to expect "Right Isosceles".

    ## - test_non_integer_right_triangle: accepted copilot suggestion, it correctly expected "Right Scalene" for a right triangle with non-integer sides.

# Acceptance Criteria:
    ## - Given a customer requests for 3 side lengths with 2 lengths being equal, show a message stating it is an isosceles triangle, then enforce that the lengths provided can form a valid triangle.

    ## - Given a customer requests for 3 side lengths with 1 length being a negative number, show a message stating that the lengths cannot be negative and prompt for valid lengths instead of crashing.

    ## - Given a customer requests for 3 side lengths with 1 length establishing a right-angle triangle, show a message stating it is a right-angled triangle, then enforce that the lengths provided can form a valid triangle but need reinforced corners.

# AI Disclousure: ## This code was generated with the assistance of AI, specifically GitHub Copilot and ChatGPT. The AI provided suggestions and code snippets, which were reviewed and modified by the developer to ensure correctness and adherence to the project requirements.
