import unittest
import math
from circle import area, perimeter


class TestingCircleFunction(unittest.TestCase):

    def test_the_zero_area(self):
        the_radius = 0
        result_of_the_actions = area(the_radius)
        self.assertEqual(result_of_the_actions, 0)

    def test_the_zero_perimeter(self):
        the_radius = 0
        result_of_the_actions = perimeter(the_radius)
        self.assertEqual(result_of_the_actions, 0)

    def test_the_perimeter_actions(self):
        the_radius = 1
        result_of_the_actions = perimeter(the_radius)
        self.assertEqual(result_of_the_actions, 2 * math.pi)

    def test_the_area_actions(self):
        the_radius = 1
        result_of_the_actions = area(the_radius)
        self.assertEqual(result_of_the_actions, math.pi)


if __name__ == '__main__':
    unittest.main()
