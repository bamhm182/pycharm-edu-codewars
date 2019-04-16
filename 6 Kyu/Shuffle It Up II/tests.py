from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_fixed_points_perms(self):
        try:
            self.assertEqual(task.fixed_points_perms(4, 1), 8)
            self.assertEqual(task.fixed_points_perms(4, 2), 6)
            self.assertEqual(task.fixed_points_perms(4, 3), 0)
            self.assertEqual(task.fixed_points_perms(10, 3), 222480)
            self.assertEqual(task.fixed_points_perms(10, 4), 55650)
            self.assertEqual(task.fixed_points_perms(20, 2), 447507315596451070)
            self.assertEqual(task.fixed_points_perms(4, 0), 9)
            self.assertEqual(task.fixed_points_perms(4, 4), 1)
            self.assertEqual(task.fixed_points_perms(4, 5), 0)
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
