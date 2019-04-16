from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_lowercase_count(self):
        try:
            self.assertEqual(task.lowercase_count("abc"), 3)
            self.assertEqual(task.lowercase_count("abcABC123"), 3)
            self.assertEqual(task.lowercase_count("abcABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~"), 3)
            self.assertEqual(task.lowercase_count(""), 0)
            self.assertEqual(task.lowercase_count("abcABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~"), 0)
            self.assertEqual(task.lowercase_count("abcdefghijklmnopqrstuvwxyz"), 26)
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
