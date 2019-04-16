from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_Descending_Order(self):
        try:
            self.assertEqual(task.Descending_Order(0), 0)
            self.assertEqual(task.Descending_Order(15), 51)
            self.assertEqual(task.Descending_Order(123456789), 987654321)
            self.assertEqual(task.Descending_Order(6483), 8643)
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
