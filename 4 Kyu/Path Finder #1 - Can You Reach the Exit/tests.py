from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task

a = "\n".join([
  ".W.",
  ".W.",
  "..."
])

b = "\n".join([
  ".W.",
  ".W.",
  "W.."
])

c = "\n".join([
  "......",
  "......",
  "......",
  "......",
  "......",
  "......"
])

d = "\n".join([
  "......",
  "......",
  "......",
  "......",
  ".....W",
  "....W."
])


class Test(unittest.TestCase):
    def test_path_finder(self):
        try:
            self.assertEqual(task.path_finder(a), True)
            self.assertEqual(task.path_finder(b), False)
            self.assertEqual(task.path_finder(c), True)
            self.assertEqual(task.path_finder(d), False)
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
