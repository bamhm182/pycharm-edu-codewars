from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task

a = "\n".join([
    "000",
    "000",
    "000"
])

b = "\n".join([
    "010",
    "010",
    "010"
])

c = "\n".join([
    "010",
    "101",
    "010"
])

d = "\n".join([
    "0707",
    "7070",
    "0707",
    "7070"
])

el = "\n".join([
    "700000",
    "077770",
    "077770",
    "077770",
    "077770",
    "000007"
])

f = "\n".join([
    "777000",
    "007000",
    "007000",
    "007000",
    "007000",
    "007777"
])

g = "\n".join([
    "000000",
    "000000",
    "000000",
    "000010",
    "000109",
    "001010"
])


class Test(unittest.TestCase):

    def test_path_finder(self):
        try:
            self.assertEqual(task.path_finder(a), 0)
            self.assertEqual(task.path_finder(b), 2)
            self.assertEqual(task.path_finder(c), 4)
            self.assertEqual(task.path_finder(d), 42)
            self.assertEqual(task.path_finder(el), 14)
            self.assertEqual(task.path_finder(f), 0)
            self.assertEqual(task.path_finder(g), 4)
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
