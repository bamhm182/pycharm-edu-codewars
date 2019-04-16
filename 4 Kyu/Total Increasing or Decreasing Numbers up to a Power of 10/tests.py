from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_total_inc_dec(self):
        try:
            self.assertEqual(task.total_inc_dec(0), 1)
            self.assertEqual(task.total_inc_dec(1), 10)
            self.assertEqual(task.total_inc_dec(2), 100)
            self.assertEqual(task.total_inc_dec(3), 475)
            self.assertEqual(task.total_inc_dec(4), 1675)
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
