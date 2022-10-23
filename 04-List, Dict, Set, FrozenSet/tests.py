import os
import unittest

if os.path.exists('./main_sln.py'):
    import main_sln as main
else:
    import main


class TestDictMerge(unittest.TestCase):

    def test_case_1(self):
        result = main.dict_merge(
            {'Ten': 10, 'Twenty': 20, 'Thirty': 30},
            {'Thirty': 30, 'Forty': 40, 'Fifty': 50},
        )
        self.assertDictEqual(result, {
            'Ten': 10, 'Twenty': 20, 'Thirty': 30,
            'Forty': 40, 'Fifty': 50
        })

    def test_case_2(self):
        result = main.dict_merge({}, {})
        self.assertDictEqual(result, {})

    def test_case_3(self):
        result = main.dict_merge(
            {'one': 1, 'three': 3, 'five': 5},
            {'two': 2, 'four': 4, 'six': 6},
        )
        self.assertDictEqual(result, {
            'one': 1, 'three': 3, 'five': 5,
            'two': 2, 'four': 4, 'six': 6,
        })

    def test_case_4(self):
        result = main.dict_merge({}, {'one': 1})
        self.assertDictEqual(result, {'one': 1})


    def test_case_5(self):
        dict1, dict2 = {}, {}
        result = main.dict_merge(dict1, dict2)
        self.assertNotEqual(id(result), id(dict1))
        self.assertNotEqual(id(result), id(dict2))


class TestListConcatenation(unittest.TestCase):

    def test_case_1(self):
        result = main.list_concatenation([2, 2, 1], [10, 11])
        self.assertListEqual(result, [2, 2, 1, 10, 11])

    def test_case_2(self):
        result = main.list_concatenation([2, 4, 2, 34, 5], [])
        self.assertListEqual(result, [2, 4, 2, 34, 5])

    def test_case_3(self):
        result = main.list_concatenation([], [5, 3, -2, 0])
        self.assertListEqual(result, [5, 3, -2, 0])

    def test_case_4(self):
        result = main.list_concatenation([2, 4, 56, 7, 34, 2, 4, 6, 0], [6, 3, 5, 23, 2, 4, 6, 67, 9])
        self.assertListEqual(result, [2, 4, 56, 7, 34, 2, 4, 6, 0, 6, 3, 5, 23, 2, 4, 6, 67, 9])

    def test_case_5(self):
        result = main.list_concatenation([2, 6, 3, 5], [1])
        self.assertListEqual(result, [2, 6, 3, 5, 1])


class TestTwoTeams(unittest.TestCase):

    def test_case_1(self):
        result = main.two_teams([1, 11, 13, 6, 14])
        self.assertEqual(result, 11)

    def test_case_2(self):
        result = main.two_teams([3, 4])
        self.assertEqual(result, -1)

    def test_case_3(self):
        result = main.two_teams([16, 14, 79, 8, 71, 72, 71, 10, 80, 76, 83, 70, 57, 29, 31])
        self.assertEqual(result, 209)

    def test_case_4(self):
        result = main.two_teams([23, 72, 54, 4, 88, 91, 8, 44])
        self.assertEqual(result, -38)

    def test_case_5(self):
        result = main.two_teams([23, 74, 57, 33, 61, 99, 19, 12, 19, 38, 77, 70, 20])
        self.assertEqual(result, -50)


class TestRemoveTasks(unittest.TestCase):

    def test_case_1(self):
        result = main.remove_tasks(3, [1237, 2847, 27485, 2947, 1, 247, 374827, 22])
        self.assertListEqual(result, [1237, 2847, 2947, 1, 374827, 22])

    def test_case_2(self):
        result = main.remove_tasks(1, [1237, 2847, 27485, 2947, 1, 247, 374827, 22])
        self.assertListEqual(result, [])

    def test_case_3(self):
        result = main.remove_tasks(10, [1237])
        self.assertListEqual(result, [1237])

    def test_case_4(self):
        result = main.remove_tasks(
            3,
            [552, 987, 422, 309, 222, 949, 448, 524, 542, 562, 105, 210, 887,
             762, 750, 239, 738, 920, 764],
        )
        self.assertListEqual(
            result,
            [552, 987, 309, 222, 448, 524, 562, 105,887, 762, 239, 738, 764],
        )

    def test_case_5(self):
        result = main.remove_tasks(
            2,
            [82614, 34200, 25887, 53226, 32161, 9495, 49341, 81259, 83693,
             30921, 46944, 8450, 63590, 97745],
        )
        self.assertListEqual(result, [82614, 25887, 32161, 49341, 83693, 46944, 63590])


if __name__ == '__main__':
    unittest.main()
