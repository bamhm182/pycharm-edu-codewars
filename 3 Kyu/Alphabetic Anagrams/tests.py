from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_listPosition(self):
        try:
            self.assertEqual(task.listPosition('A'), 1)
            self.assertEqual(task.listPosition('ABAB'), 2)
            self.assertEqual(task.listPosition('AAAB'), 1)
            self.assertEqual(task.listPosition('BAAA'), 4)
            self.assertEqual(task.listPosition('QUESTION'), 24572)
            self.assertEqual(task.listPosition('BOOKKEEPER'), 10743)
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
