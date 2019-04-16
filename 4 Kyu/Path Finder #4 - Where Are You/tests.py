from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_i_am_here(self):
        try:
            self.assertEqual(task.i_am_here(''), [0, 0])
            self.assertEqual(task.i_am_here('RLrl'), [0, 0])
            self.assertEqual(task.i_am_here('r5L2l4'), [4, 3])
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
