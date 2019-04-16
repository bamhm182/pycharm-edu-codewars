from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_even_or_odd(self):
        try:
            self.assertEqual(task.even_or_odd(2), "Even")
            self.assertEqual(task.even_or_odd(42), "Even")
            self.assertEqual(task.even_or_odd(7), "Odd")
            self.assertEqual(task.even_or_odd(863), "Odd")
            self.assertEqual(task.even_or_odd(-1), "Odd")
            self.assertEqual(task.even_or_odd(0), "Even")
            self.assertEqual(task.even_or_odd(-22), "Even")
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
