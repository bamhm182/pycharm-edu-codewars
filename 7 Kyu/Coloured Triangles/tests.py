from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_triangle(self):
        try:
            self.assertEqual(task.triangle('GB'), 'R')
            self.assertEqual(task.triangle('RRR'), 'R')
            self.assertEqual(task.triangle('RGBG'), 'B')
            self.assertEqual(task.triangle('RBRGBRB'), 'G')
            self.assertEqual(task.triangle('RBRGBRBGGRRRBGBBBGG'), 'G')
            self.assertEqual(task.triangle('B'), 'B')
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
