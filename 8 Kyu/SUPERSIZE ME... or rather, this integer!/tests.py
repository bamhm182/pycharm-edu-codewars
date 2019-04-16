from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_super_size(self):
        try:
            self.assertEqual(task.super_size(69), 96)
            self.assertEqual(task.super_size(513), 531)
            self.assertEqual(task.super_size(2017), 7210)
            self.assertEqual(task.super_size(414), 441)
            self.assertEqual(task.super_size(608719), 987610)
            self.assertEqual(task.super_size(123456789), 987654321)
            self.assertEqual(task.super_size(700000000001), 710000000000)
            self.assertEqual(task.super_size(666666), 666666)
            self.assertEqual(task.super_size(2), 2)
            self.assertEqual(task.super_size(0), 0)
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
