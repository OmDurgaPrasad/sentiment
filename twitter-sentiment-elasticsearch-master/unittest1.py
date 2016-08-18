import unittest


class ObviousTest(unittest.TestCase):
    def setUp(self):
        self.num = 1

    def test_math(self):
        self.assertEqual(self.num, 1)

    def test_divides_by_zero(self):
        self.assertRaises(ZeroDivisionError, lambda: 1 / 0)


if __name__ == '__main__':
    unittest.main()
