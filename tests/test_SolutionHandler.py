import unittest
from solution.handlers.SolutionHandler import SolutionHandler


class SolutionHandlerTest(unittest.TestCase):

    # Test expected functionality of get_sortest_list method
    def test_get_sortest_list(self):
        start = 'head'
        target = 'tail'
        dictionary = ['head', 'heal', 'heil', 'hail', 'tail',
                      'rail', 'fail', 'mail', 'nail']
        expected = ['head', 'heal', 'heil', 'hail', 'tail']
        solution = SolutionHandler(start, target, dictionary)
        result = solution.get_sortest_list()
        self.assertEqual(result, expected)

    # If same input provided then it should exit with zero (0) code
    def test_gsl_with_same_input(self):
        start = 'head'
        target = 'head'
        dictionary = ['head', 'heal', 'heil', 'hail', 'tail',
                      'rail', 'fail', 'mail', 'nail']
        solution = SolutionHandler(start, target, dictionary)
        with self.assertRaises(SystemExit) as cm:
            solution.get_sortest_list()
        self.assertEqual(cm.exception.code, 0)

    # If end word not in dictionary then it should exit with zero (0) code
    def test_gsl_with_different_endword(self):
        start = 'head'
        target = 'jail'
        dictionary = ['head', 'heal', 'heil', 'hail', 'tail',
                      'rail', 'fail', 'mail', 'nail']
        solution = SolutionHandler(start, target, dictionary)
        with self.assertRaises(SystemExit) as cm:
            solution.get_sortest_list()
        self.assertEqual(cm.exception.code, 0)

    # Test case with three letter word
    def test_get_sortest_list_tlw(self):
        start = 'hea'
        target = 'tia'
        dictionary = ['hea', 'mea', 'lea', 'lia', 'zia',
                      'tia']
        expected = ['hea', 'lea', 'lia', 'tia']
        solution = SolutionHandler(start, target, dictionary)
        result = solution.get_sortest_list()
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
