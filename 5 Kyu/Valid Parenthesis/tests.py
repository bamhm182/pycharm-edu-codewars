from test_helper import run_common_tests, failed, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_valid_parentheses(self):
        try:
            self.assertEqual(task.valid_parentheses(")test"), False)
            self.assertEqual(task.valid_parentheses(""), True)
            self.assertEqual(task.valid_parentheses("  ("), False)
            self.assertEqual(task.valid_parentheses("hi())("), False)
            self.assertEqual(task.valid_parentheses("hi(hi)()"), True)
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
