from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task

a = [
    [1,1],
    [1,1]
]

b = [
    [0,1],
    [1,1]
]

c = [
    [1,1,1],
    [1,1,1],
    [1,1,1]
]

d = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
]

el = [
    [0,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [0,1,1,0,1],
    [1,1,1,1,1]
]


class Test(unittest.TestCase):
    def test_count(self):
        try:
            self.assertEqual(task.count(a), {2: 1})
            self.assertEqual(task.count(b), {})
            self.assertEqual(task.count(c), {2: 4, 3: 1})
            self.assertEqual(task.count(d), {})
            self.assertEqual(task.count(el), {3: 2, 2: 9})
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
