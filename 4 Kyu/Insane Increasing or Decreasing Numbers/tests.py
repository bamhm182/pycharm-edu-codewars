from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_insane_inc_or_dec(self):
        try:
            self.assertEqual(task.insane_inc_or_dec(1), 9)
            self.assertEqual(task.insane_inc_or_dec(2), 99)
            self.assertEqual(task.insane_inc_or_dec(3), 474)
            self.assertEqual(task.insane_inc_or_dec(4), 1674)
            self.assertEqual(task.insane_inc_or_dec(5), 4953)
            self.assertEqual(task.insane_inc_or_dec(6), 12951)
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
