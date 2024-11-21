import unittest
import math
from circle import area, perimeter

class testing_circle_function(unittest.TestCase):

    def testing_the_zero_area(self):
        the_radius = 0

        result_of_the_actions = area(the_radius)
        
        self.assertEqual(result_of_the_actions, 0)

    def testing_the_zero_perimeter(self):
        the_radius = 0

        result_of_the_actions = perimeter(the_radius)

        self.assertEqual(result_of_the_actions, 0)

    def testing_the_preimeter_actions(self):
        the_radius = 1

        result_of_the_actions = perimeter(the_radius)

        self.assertEqual(result_of_the_actions, 2 * math.pi)
    
    def testing_the_area_actions(self):
        the_radius = 1

        result_of_the_actions = area(the_radius)

        self.assertEqual(result_of_the_actions, math.pi)

if __name__ == '__main__':
    unittest.main()





