from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_format_money(self):
        try:
            self.assertEqual(task.format_money(3), "$3.00")
            self.assertEqual(task.format_money(5.99), "$5.99")
            self.assertEqual(task.format_money(3.1), "$3.10")
            self.assertEqual(task.format_money(410.63), "$410.63")
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
