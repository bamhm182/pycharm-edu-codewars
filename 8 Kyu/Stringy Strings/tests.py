from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_stringy(self):
        try:
            self.assertEqual(type(task.stringy(5)), str) # It should be a string
            self.assertEqual(task.stringy(10)[0], "1")  # It should start with 1
            self.assertEqual(task.stringy(4), '1010')
            self.assertEqual(task.stringy(5), '10101')
            self.assertEqual(task.stringy(12), '101010101010')
            self.assertEqual(task.stringy(3), '101')
            self.assertEqual(task.stringy(26), '10101010101010101010101010')
            self.assertEqual(task.stringy(28), '1010101010101010101010101010')
            self.assertEqual(task.stringy(27), '101010101010101010101010101')
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
