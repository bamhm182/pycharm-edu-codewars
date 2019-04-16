from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_the_var(self):
        try:
            self.assertEqual(task.the_var('j*p'), 8)
            self.assertEqual(task.the_var('o*l'), 2)
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)

