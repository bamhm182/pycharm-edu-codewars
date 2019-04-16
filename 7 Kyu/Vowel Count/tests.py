from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_getCount(self):
        try:
            self.assertEqual(task.getCount("abracadabra"), 5)
            self.assertEqual(task.getCount("aeiou"), 5)
            self.assertEqual(task.getCount("a"), 1)
            self.assertEqual(task.getCount(""), 0)
            self.assertEqual(task.getCount("hkjlm"), 0)
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
