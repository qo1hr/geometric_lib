
import unittest
from calculate import calc

class TestCalculate(unittest.TestCase):
    def test_calc_circle_area(self):
        # Arrange
        fig, func, size = "circle", "area", [3]
        expected_result = 28.27433

        # Act
        result = calc(fig, func, size)

        # Assert
        self.assertAlmostEqual(result, expected_result, places=5)

    def test_calc_square_perimeter(self):
        # Arrange
        fig, func, size = "square", "perimeter", [3]
        expected_result = 12

        # Act
        result = calc(fig, func, size)

        # Assert
        self.assertEqual(result, expected_result)

    def test_invalid_figure(self):
        # Arrange
        fig, func, size = "triangle", "area", [3, 4, 5]

        # Act & Assert
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_invalid_function(self):
        # Arrange
        fig, func, size = "circle", "volume", [3]

        # Act & Assert
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

if __name__ == '__main__':
    unittest.main()
