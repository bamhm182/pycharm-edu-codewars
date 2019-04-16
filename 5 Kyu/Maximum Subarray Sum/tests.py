from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_maxSequence(self):
        try:
            self.assertEqual(task.maxSequence([]), 0)
            self.assertEqual(task.maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
