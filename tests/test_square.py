
import unittest
from square import area, perimeter

class TestSquare(unittest.TestCase):
    def test_area(self):
        # Arrange
        side = 3
        expected_area = 9

        # Act
        result = area(side)

        # Assert
        self.assertEqual(result, expected_area)

    def test_perimeter(self):
        # Arrange
        side = 3
        expected_perimeter = 12

        # Act
        result = perimeter(side)

        # Assert
        self.assertEqual(result, expected_perimeter)

    def test_area_negative(self):
        # Arrange
        side = -3

        # Act & Assert
        with self.assertRaises(ValueError):
            area(side)

    def test_perimeter_negative(self):
        # Arrange
        side = -3

        # Act & Assert
        with self.assertRaises(ValueError):
            perimeter(side)

if __name__ == '__main__':
    unittest.main()
