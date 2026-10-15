# Triangle Classifier

A simple Python program that classifies triangles from their side lengths. It identifies valid equilateral, isosceles, scalene, and right-angled triangles.

## Run the tests

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -v
```

## Equivalence classes and boundaries

| Class or boundary | Expected result |
| --- | --- |
| Negative side length | Invalid triangle |
| Failed triangle inequality | Invalid triangle |
| Degenerate triangle: the sum of two sides equals the third | Invalid triangle |
| Equilateral: all sides equal | Valid equilateral triangle |
| Isosceles: exactly two sides equal | Valid isosceles triangle |
| Scalene: all sides different | Valid scalene triangle |
| Right-angled: satisfies the Pythagorean theorem | Valid triangle prefixed with `Right` |

The key boundaries are side lengths of zero, negative values, and equality in the triangle inequality—for example, `1, 2, 3`.

### Why an equilateral triangle cannot be right-angled

An equilateral triangle has three 60-degree angles. A right triangle must have one 90-degree angle, so a triangle cannot be both equilateral and right-angled.

## Copilot Review Log

| Test or suggestion | Copilot-suggested? | Decision | Review result |
| --- | --- | --- | --- |
| `test_equilateral_triangle` | Yes | Accepted | It correctly expected `"Equilateral"` for three equal side lengths. |
| `classify_triangle` right-triangle draft | Yes | Rejected | The draft tried to return `"Right {base_classification}"` before a classification variable existed, which would have caused a runtime error. The base classification is determined first. |
| `test_degenerate_triangle_is_invalid` | Yes | Accepted | It correctly expected `"Invalid"` for a degenerate triangle. |
| `test_right_isosceles_triangle` | Yes | Edited | It incorrectly expected `"Isosceles"`; the expected result was changed to `"Right Isosceles"`. |
| `test_non_integer_right_triangle` | Yes | Accepted | It correctly expected `"Right Scalene"` for a right triangle with non-integer sides. |

## Acceptance criteria

1. Given three valid side lengths with exactly two equal values, the classifier returns `"Isosceles"`.
2. Given any side length less than or equal to zero, the classifier returns `"Invalid"` without crashing.
3. Given valid side lengths that form a right triangle, the classifier returns a result beginning with `"Right "` so reinforced corners can be identified.

## AI-use disclosure

This code was generated with assistance from GitHub Copilot and ChatGPT. The tools provided suggestions and code snippets, which were reviewed and modified by the developer for correctness and adherence to the project requirements.
