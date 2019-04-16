from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_high_and_low(self):
        try:
            self.assertEqual(task.high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214")
            self.assertEqual(task.high_and_low("17 52 81 5 32 -64"), "81 -64")
            self.assertEqual(task.high_and_low("12 17 4"), "4 17")
            self.assertEqual(task.high_and_low("0 1 2 3 4 5 6 7 8 9"), "9 0")
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
