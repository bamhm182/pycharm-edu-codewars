from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_solve(self):
        try:
            self.assertEqual(task.solve("tft","^&"), 2)
            self.assertEqual(task.solve("ttftff","|&^&&"), 16)
            self.assertEqual(task.solve("ttftfftf","|&^&&||"), 339)
            self.assertEqual(task.solve("ttftfftft","|&^&&||^"), 851)
            self.assertEqual(task.solve("ttftfftftf","|&^&&||^&"), 2434)
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)


Test.it("Basic tests")
Test.assert_equals(solve(),2)
Test.assert_equals(solve(),16)
Test.assert_equals(solve(),339)
Test.assert_equals(solve(),851)
Test.assert_equals(solve(),2434)
