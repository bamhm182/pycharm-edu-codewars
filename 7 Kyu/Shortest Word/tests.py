from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_find_short(self):
        try:
            self.assertEqual(task.find_short("bitcoin take over the world maybe who knows perhaps"), 3)
            self.assertEqual(task.find_short("turns out random test cases are easier than writing out basic ones"), 3)
            self.assertEqual(task.find_short("lets talk about javascript the best language"), 3)
            self.assertEqual(task.find_short("i want to travel the world writing code one day"), 1)
            self.assertEqual(task.find_short("Lets all go on holiday somewhere very cold"), 2)
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
