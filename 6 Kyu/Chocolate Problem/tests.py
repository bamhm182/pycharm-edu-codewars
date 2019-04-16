from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_chocolate(self):
        try:
            self.assertEqual(task.chocolate(5, [4, 3, 2, 5, 1], [1, 2, 5, 3, 4]), 3)
            self.assertEqual(task.chocolate(2, [1, 2], [2, 1]), 1)
            self.assertEqual(task.chocolate(3, [3, 1, 2], [2, 3, 1]), 1)
            self.assertEqual(task.chocolate(3, [1, 3, 2], [1, 2, 3]), 2)
            self.assertEqual(task.chocolate(3, [1, 2, 3], [3, 2, 1]), 2)
            self.assertEqual(task.chocolate(4, [4, 3, 2, 1], [2, 1, 4, 3]), 1)
            self.assertEqual(task.chocolate(5, [3, 5, 2, 1, 4], [4, 5, 2, 1, 3]), 2)
            self.assertEqual(task.chocolate(6, [3, 6, 1, 5, 4, 2], [1, 5, 4, 2, 3, 6]), 1)
            self.assertEqual(task.chocolate(6, [3, 6, 1, 5, 4, 2], [1, 4, 5, 3, 2, 6]), 5)
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
