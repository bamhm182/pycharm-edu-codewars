from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_primeFactors(self):
        try:
            self.assertEqual(task.primeFactors(7775460), "(2**2)(3**3)(5)(7)(11**2)(17)")
            self.assertEqual(task.primeFactors(86240), "(2**5)(5)(7**2)(11)")
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
