
import unittest
from circle import area, perimeter

class TestCircle(unittest.TestCase):
    def test_area(self):
        # Arrange
        radius = 3
        expected_area = 28.27433

        # Act
        result = area(radius)

        # Assert
        self.assertAlmostEqual(result, expected_area, places=5)

    def test_perimeter(self):
        # Arrange
        radius = 3
        expected_perimeter = 18.84956

        # Act
        result = perimeter(radius)

        # Assert
        self.assertAlmostEqual(result, expected_perimeter, places=5)

    def test_area_negative(self):
        # Arrange
        radius = -3

        # Act & Assert
        with self.assertRaises(ValueError):
            area(radius)

    def test_perimeter_negative(self):
        # Arrange
        radius = -3

        # Act & Assert
        with self.assertRaises(ValueError):
            perimeter(radius)

if __name__ == '__main__':
    unittest.main()
