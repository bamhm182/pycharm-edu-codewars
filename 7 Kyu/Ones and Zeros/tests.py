from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_binary_array_to_number(self):
        try:
            self.assertEqual(task.binary_array_to_number([0, 0, 0, 1]), 1)
            self.assertEqual(task.binary_array_to_number([0, 0, 1, 0]), 2)
            self.assertEqual(task.binary_array_to_number([1, 1, 1, 1]), 15)
            self.assertEqual(task.binary_array_to_number([0, 1, 1, 0]), 6)
            self.assertEqual(task.binary_array_to_number([1, 1, 0, 0, 1, 0, 1, 1, 0] ), 406)
            self.assertEqual(task.binary_array_to_number([1, 1, 1, 0, 1, 1]), 59)
            self.assertEqual(task.binary_array_to_number([1, 0, 0, 0, 0, 0, 1, 1, 1, 1]), 527)
            self.assertEqual(task.binary_array_to_number([1, 1, 0, 0, 1, 0, 0, 1, 1]), 403)
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
