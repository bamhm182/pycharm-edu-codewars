from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_get_middle(self):
        try:
            self.assertEqual(task.get_middle("test"), "es")
            self.assertEqual(task.get_middle("testing"), "t")
            self.assertEqual(task.get_middle("middle"), "dd")
            self.assertEqual(task.get_middle("A"), "A")
            self.assertEqual(task.get_middle("of"), "of")
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
