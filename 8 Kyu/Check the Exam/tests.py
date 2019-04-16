from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_check_exam(self):
        try:
            self.assertEqual(task.check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]), 6)
            self.assertEqual(task.check_exam(["a", "a", "c", "b"], ["a", "a", "b",  ""]), 7)
            self.assertEqual(task.check_exam(["a", "a", "b", "c"], ["a", "a", "b", "c"]), 16)
            self.assertEqual(task.check_exam(["b", "c", "b", "a"], ["",  "a", "a", "c"]), 0)
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
