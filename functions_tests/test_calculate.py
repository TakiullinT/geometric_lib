import unittest
import math
from calculate import calc

class testing_calculate_function(unittest.TestCase):
    
    def testing_the_square_area(self):

        fig = 'square'
        func = 'area'
        size = [1]

        result_of_the_actions = calc(fig, func, size)

        self.assertEqual(result_of_the_actions, 1)

    def testing_the_circle_area(self):

        fig = 'circle'
        func = 'area'
        size = [1]

        result_of_the_actions = calc(fig, func, size)

        self.assertEqual(result_of_the_actions, 3.141592653589793)
    
    def testing_the_triangle_area(self):

        fig = 'triangle'
        func = 'area'
        size = [4, 5, 7]

        result_of_the_actions = calc(fig, func, size)

        self.assertEqual(result_of_the_actions, 8)

    def testing_the_negative_size(self):

        fig = 'circle'
        func = 'area'
        size = [-1]

        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def testing_the_wrong_triangle_side_sizes(self):

        fig = 'triangle'
        func = 'area'
        size = [1, 2, 15]

        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def testing_the_square_perimeter(self):

        fig = 'square'
        func = 'perimeter'
        size = [1]

        result_of_the_actions = calc(fig, func, size)

        self.assertEqual(result_of_the_actions, 4)

    def testing_the_triangle_perimeter(self):
    
        fig = 'triangle'
        func = 'perimeter'
        size = [4, 6, 7]

        result_of_the_actions = calc(fig, func, size)

        self.assertEqual(result_of_the_actions, 17)

    def testing_the_circle_perimeter(self):

        fig = 'circle'
        func = 'perimeter'
        size = [1]

        result_of_the_actions = calc(fig, func, size)

        self.assertEqual(result_of_the_actions, 6.283185307179586)

    def testing_the_wrong_function(self):

        fig = 'circle'
        func = 'multiply'
        size = [1]

        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def testing_the_wrong_figure(self):

        fig = 'oval'
        func = 'area'
        size = [1]

        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def testing_the_wrong_size(self):

        fig = 'circle'
        func = 'area'
        size = [1, 3]

        with self.assertRaises(AssertionError):
            calc(fig, func, size)

if __name__ == '__main__':
    unittest.main()
