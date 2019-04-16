from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_special_primes(self):
        try:
            self.assertEqual(task.special_primes(101), [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
            self.assertEqual(task.special_primes(200), [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
            self.assertEqual(task.special_primes(457),[[251, 439, 2], [349, 457, 4], [431, 431, 1]])
            self.assertEqual(task.special_primes(500),[[251, 439, 2], [349, 479, 5], [431, 431, 1]])
            self.assertEqual(task.special_primes(1000),[[251, 947, 11], [349, 479, 5], [431, 983, 4]])
            self.assertEqual(task.special_primes(5000),[[251, 4987, 58], [349, 4789, 13], [431, 983, 4]])
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
