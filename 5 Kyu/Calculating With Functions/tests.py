from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_math(self):
        try:
            self.assertEqual(task.seven(task.times(task.five())), 35)
            self.assertEqual(task.four(task.plus(task.nine())), 13)
            self.assertEqual(task.eight(task.minus(task.three())), 5)
            self.assertEqual(task.six(task.divided_by(task.two())), 3)
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
