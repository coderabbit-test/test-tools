import unittest
from main import nth_fibonacci

class TestFibonacci(unittest.TestCase):
    def test_base_cases(self):
        self.assertEqual(nth_fibonacci(0), 0)
        self.assertEqual(nth_fibonacci(1), 1)

    def test_positive_values(self):
        self.assertEqual(nth_fibonacci(2), 1)
        self.assertEqual(nth_fibonacci(5), 5)
        self.assertEqual(nth_fibonacci(10), 55)

    def test_input_validation(self):
        with self.assertRaises(TypeError):
            nth_fibonacci('5')
        with self.assertRaises(ValueError):
            nth_fibonacci(-1)

if __name__ == '__main__':
    unittest.main()
