import unittest
from circle import area, perimeter
from square import area, perimeter
from triangle import area, perimeter
from calculate import calc


class TestingCalculateFunction(unittest.TestCase):

    def test_the_square_area(self):
        fig = 'square'
        func = 'area'
        size = [1]

        result_of_the_actions = calc(fig, func, size)

        self.assertEqual(result_of_the_actions, 1)

    def test_the_circle_area(self):
        fig = 'circle'
        func = 'area'
        size = [1]

        result_of_the_actions = calc(fig, func, size)

        self.assertEqual(result_of_the_actions, 3.141592653589793)

    def test_the_triangle_area(self):
        fig = 'triangle'
        func = 'area'
        size = [4, 5, 7]

        result_of_the_actions = calc(fig, func, size)

        self.assertEqual(result_of_the_actions, 9.797958971132712)

    def test_the_negative_size(self):
        fig = 'circle'
        func = 'area'
        size = [-1]

        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_the_wrong_triangle_side_sizes(self):
        fig = 'triangle'
        func = 'area'
        size = [1, 2, 15]

        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_the_square_perimeter(self):
        fig = 'square'
        func = 'perimeter'
        size = [1]

        result_of_the_actions = calc(fig, func, size)

        self.assertEqual(result_of_the_actions, 4)

    def test_the_triangle_perimeter(self):
        fig = 'triangle'
        func = 'perimeter'
        size = [4, 6, 7]

        result_of_the_actions = calc(fig, func, size)

        self.assertEqual(result_of_the_actions, 17)

    def test_the_circle_perimeter(self):
        fig = 'circle'
        func = 'perimeter'
        size = [1]

        result_of_the_actions = calc(fig, func, size)

        self.assertEqual(result_of_the_actions, 6.283185307179586)

    def test_the_wrong_function(self):
        fig = 'circle'
        func = 'multiply'
        size = [1]

        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_the_wrong_figure(self):
        fig = 'oval'
        func = 'area'
        size = [1]

        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_the_wrong_size(self):
        fig = 'circle'
        func = 'area'
        size = [1, 3]

        with self.assertRaises(AssertionError):
            calc(fig, func, size)


if __name__ == '__main__':
    unittest.main()
