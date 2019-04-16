from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_four_pass(self):
        try:
            self.assertEqual(task.four_pass([1,69,95,70]), [1,2,3,4,5,6,7,8,9,19,29,39,49,59,69,79,78,77,76,75,85,95,94,93,92,91,81,71,70])
            self.assertEqual(task.four_pass([0,49,40,99]), [0,1,2,3,4,5,6,7,8,9,19,29,39,49,48,47,46,45,44,43,42,41,40,50,51,52,53,54,55,56,57,58,59,69,79,89,99])
            self.assertEqual(task.four_pass([37,61,92,36]), [37,27,26,25,24,23,22,21,31,41,51,61,71,81,91,92,93,94,95,96,86,76,66,56,46,36])
            self.assertEqual(task.four_pass([51,24,75,57]), [51,41,42,43,44,34,24,25,35,45,55,65,75,76,77,67,57])
            self.assertEqual(task.four_pass([92,59,88,11]), [92,93,94,95,96,97,98,99,89,79,69,59,58,68,78,88,87,77,67,57,47,37,27,17,16,15,14,13,12,11])
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
