
import unittest
from triangle import semi_perimeter, area

class TestTriangle(unittest.TestCase):
    def test_semi_perimeter(self):
        # Arrange
        a, b, c = 3, 4, 5
        expected_semi_perimeter = 6.0

        # Act
        result = semi_perimeter(a, b, c)

        # Assert
        self.assertEqual(result, expected_semi_perimeter)

    def test_area(self):
        # Arrange
        a, b, c = 3, 4, 5
        expected_area = 6.0

        # Act
        result = area(a, b, c)

        # Assert
        self.assertAlmostEqual(result, expected_area, places=5)

    def test_invalid_triangle(self):
        # Arrange
        a, b, c = 1, 2, 10

        # Act & Assert
        with self.assertRaises(ValueError):
            area(a, b, c)

    def test_negative_side(self):
        # Arrange
        a, b, c = -3, 4, 5

        # Act & Assert
        with self.assertRaises(ValueError):
            area(a, b, c)

if __name__ == '__main__':
    unittest.main()
