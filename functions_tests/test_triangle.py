import unittest
import math
from triangle import area, perimeter

class testing_the_triangle_function(unittest.TestCase):

    def testing_the_area_actions(self):

        a, b, c = 4, 5, 7

        result_of_the_actions = area(a, b, c)

        self.assertEqual(result_of_the_actions, 8)

    def testing_the_perimeter_actions(self):

        a, b, c = 4, 5, 7

        result_of_the_actions = perimeter(a, b, c)

        self.assertEqual(result_of_the_actions, 16)

    def testing_the_zero_perimeter(self):

        a, b, c = 0, 0, 0

        result_of_the_actions = perimeter(a, b, c)

        self.assertEqual(result_of_the_actions, 0)

    def testing_the_zero_area(self):

        a, b, c = 0, 0, 0

        result_of_the_actions = area(a, b, c)

        self.assertEqual(result_of_the_actions, 0)
        
if __name__ == '__main__':
    unittest.main()
