from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_duplicate_encode(self):
        try:
            self.assertEqual(task.duplicate_encode("din"), "(((")
            self.assertEqual(task.duplicate_encode("recede"), "()()()")
            self.assertEqual(task.duplicate_encode("Success"), ")())())")  # Should not be case sensitive
            self.assertEqual(task.duplicate_encode("(( @"), "))((")
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
