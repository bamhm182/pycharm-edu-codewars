from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_uni_total(self):
        try:
            self.assertEqual(task.uni_total("a"), 97)
            self.assertEqual(task.uni_total("b"), 98)
            self.assertEqual(task.uni_total("c"), 99)
            self.assertEqual(task.uni_total(""), 0)
            self.assertEqual(task.uni_total("aaa"), 291)
            self.assertEqual(task.uni_total("abc"), 294)
            self.assertEqual(task.uni_total("Mary Had A Little Lamb"), 1873)
            self.assertEqual(task.uni_total("Mary had a little lamb"), 2001)
            self.assertEqual(task.uni_total("CodeWars rocks"), 1370)
            self.assertEqual(task.uni_total("And so does Strive"), 1661)
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
