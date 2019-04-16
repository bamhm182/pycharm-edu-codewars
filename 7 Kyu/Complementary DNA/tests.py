from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_DNS_strand(self):
        try:
            self.assertEqual(task.DNS_strand("AAAA"), "TTTT")
            self.assertEqual(task.DNS_strand("ATTGC"), "TAACG")
            self.assertEqual(task.DNS_strand("GTAT"), "CATA")
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
