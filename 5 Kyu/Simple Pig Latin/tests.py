from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_pig_it(self):
        try:
            self.assertEqual(task.pig_it('Pig latin is cool'),'igPay atinlay siay oolcay')
            self.assertEqual(task.pig_it('This is my string'),'hisTay siay ymay tringsay')
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
