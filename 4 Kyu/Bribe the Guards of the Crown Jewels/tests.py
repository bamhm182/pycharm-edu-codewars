from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_least_bribes(self):
        try:
            self.assertEqual(task.least_bribes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 26)
            self.assertEqual(task.least_bribes([1, 2, 3, 4, 5]), 9)
            self.assertEqual(task.least_bribes([5, 1, 2, 4, 3]), 8)
            self.assertEqual(task.least_bribes([3, 2, 5, 4, 1]), 10)
            self.assertEqual(task.least_bribes([r * 53 + q for m in range(1, 51) for q, r in (divmod(m, 7),)]), 663) # 50 Rooms
            self.assertEqual(task.least_bribes([r * 53 + q for m in range(1, 101) for q, r in (divmod(m, 7),)]), 702) # 100 Rooms
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
