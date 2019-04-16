from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_xo(self):
        try:
            self.assertEqual(task.xo('xo'), True)
            self.assertEqual(task.xo('xo0'), True)
            self.assertEqual(task.xo('xxxoo'), False)
            self.assertEqual(task.xo('xxoooooooooooooo'), False)
            self.assertEqual(task.xo(''), True)
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
