from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_count_smileys(self):
        try:
            self.assertEqual(task.count_smileys([':D',':~)',';~D',':)']), 4)
            self.assertEqual(task.count_smileys([':)',':(',':D',':O',':;']), 2)
            self.assertEqual(task.count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
