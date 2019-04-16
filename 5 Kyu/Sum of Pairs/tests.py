from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_sum_pairs(self):
        try:
            self.assertEqual(task.sum_pairs([1, 4, 8, 7, 3, 15], 8), [1, 7])
            self.assertEqual(task.sum_pairs([1, -2, 3, 0, -6, 1], -6), [0, -6])
            self.assertEqual(task.sum_pairs([20, -13, 40], -7), None)
            self.assertEqual(task.sum_pairs([1, 2, 3, 4, 1, 0], 2), [1, 1])
            self.assertEqual(task.sum_pairs([10, 5, 2, 3, 7, 5], 10), [3, 7])
            self.assertEqual(task.sum_pairs([4, -2, 3, 3, 4], 8), [4, 4])
            self.assertEqual(task.sum_pairs([0, 2, 0], 0), [0, 0])
            self.assertEqual(task.sum_pairs([5, 9, 13, -3], 10), [13, -3])
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)

