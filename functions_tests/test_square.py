import unittest
import math
from square import perimeter, area

class testing_square_function(unittest.TestCase):

    def testing_the_zero_area(self):
        the_side = 0

        result_of_the_actions = area(the_side)

        self.assertEqual(result_of_the_actions, 0)
    
    def testing_the_zero_perimeter(self):
        the_side = 0

        result_of_the_actions = perimeter(the_side)

        self.assertEqual(result_of_the_actions, 0)

    def testing_the_area_actions(self):
        the_side = 1

        result_of_the_actions = area(the_side)

        self.assertEqual(result_of_the_actions, 1)

    def testing_the_perimeter_actions(self):
        the_side = 1

        result_of_the_actions = perimeter(the_side)

        self.assertEqual(result_of_the_actions, 4)

if __name__ == '__main__':
    unittest.main()





