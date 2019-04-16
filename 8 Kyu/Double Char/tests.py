from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_double_char(self):
        try:
            self.assertEqual(task.double_char("String"), "SSttrriinngg")
            self.assertEqual(task.double_char("Hello World"), "HHeelllloo  WWoorrlldd")
            self.assertEqual(task.double_char("1234!_ "), "11223344!!__  ")
            self.assertEqual(task.double_char("racecar"), "rraacceeccaarr")
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
