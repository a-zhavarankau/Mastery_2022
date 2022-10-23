import unittest

from main import custom_sum, custom_sort, dict_factory, lambda_message_factory

class TestCustomSum(unittest.TestCase):

    def test_case_1(self):
        result = custom_sum([1, 2, 3, 4])
        self.assertIsInstance(result, int)
        self.assertEqual(result, 10)

    def test_case_2(self):
        result = custom_sum([1, 2, 3.4])
        self.assertIsInstance(result, float)
        self.assertEqual(result, 6.4)

    def test_case_3(self):
        result = custom_sum([-1, 2, -3, 4])
        self.assertIsInstance(result, int)
        self.assertEqual(result, 2)

    def test_case_4(self):
        result = custom_sum([-1, 2, -3.4])
        self.assertIsInstance(result, float)
        self.assertEqual(result, -2.4)

    def test_case_5(self):
        result = custom_sum(list(range(-100, 101)))
        self.assertIsInstance(result, int)
        self.assertEqual(result, 0)


class TestCustomSort(unittest.TestCase):

    def test_case_1(self):
        result = custom_sort([3, 2, 5, 1, 4], reverse=False)
        self.assertListEqual(result, [1, 2, 3, 4, 5])

    def test_case_2(self):
        result = custom_sort([3, 2, 5, 1, 4], reverse=True)
        self.assertListEqual(result, [5, 4, 3, 2, 1])

    def test_case_3(self):
        result = custom_sort([3, 2, 5, 1, 4])
        self.assertListEqual(result, [1, 2, 3, 4, 5])

    def test_case_4(self):
        expected = list(range(1, 10000))
        result = custom_sort(expected)
        self.assertListEqual(result, expected)

    def test_case_5(self):
        expected = list(range(-10000, 0))
        result = custom_sort(expected, reverse=True)
        self.assertListEqual(result, expected[::-1])


class TestDictFactory(unittest.TestCase):

    def test_case_1(self):
        result = dict_factory('k1', 'k2', k3='v3', k4='v4', default_='def')
        self.assertDictEqual(result, {
            'k1': 'def',
            'k2': 'def',
            'k3': 'v3',
            'k4': 'v4',
        })

    def test_case_2(self):
        result = dict_factory('k1', 'k2', k3='v3', k4='v4')
        self.assertDictEqual(result, {
            'k1': None,
            'k2': None,
            'k3': 'v3',
            'k4': 'v4',
        })

    def test_case_3(self):
        result = dict_factory(1, 2, k3='v3', k4='v4')
        self.assertDictEqual(result, {
            1: None,
            2: None,
            'k3': 'v3',
            'k4': 'v4',
        })

    def test_case_4(self):
        result = dict_factory((1, 2), (3, 4), k3='v3', k4='v4')
        self.assertDictEqual(result, {
            (1, 2): None,
            (3, 4): None,
            'k3': 'v3',
            'k4': 'v4',
        })


class TestLambdaMessageFactory(unittest.TestCase):

    def test_case_1(self):
        result = lambda_message_factory('Wow! Such {such}. So {}')
        self.assertTrue(callable(result))
        self.assertEqual(
            result('agile', such='python'),
            'Wow! Such python. So agile',
        )
        self.assertEqual(
            result('x', such='y'),
            'Wow! Such y. So x',
        )

    def test_case_2(self):
        result = lambda_message_factory('{}')
        self.assertTrue(callable(result))
        self.assertEqual(result(list(range(1, 100))), str(list(range(1, 100))))

    def test_case_3(self):
        result_1 = lambda_message_factory('{} {y} {x}')
        result_2 = lambda_message_factory('_{}_{z}_{b}_')
        self.assertTrue(callable(result_1))
        self.assertTrue(callable(result_2))
        self.assertEqual(result_1(0, x=2, y=1), '0 1 2')
        self.assertEqual(result_2(0, z=1, b=2), '_0_1_2_')


if __name__ == '__main__':
    unittest.main()
