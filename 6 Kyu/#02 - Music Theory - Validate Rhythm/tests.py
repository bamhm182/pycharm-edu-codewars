from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_validate_rhythm(self):
        try:
            self.assertEqual(task.validate_rhythm([4,4], '4444|88888888|22|2488|1'), 'Valid rhythm')
            self.assertEqual(task.validate_rhythm([5,2], '22222|2244244|8888244888844|112'), 'Valid rhythm')
            self.assertEqual(task.validate_rhythm([3,8], '888|48|84'), 'Valid rhythm')
            self.assertEqual(task.validate_rhythm([4, 4], '4444'), 'Valid rhythm')
            self.assertEqual(task.validate_rhythm([5, 2], '22222'), 'Valid rhythm')
            self.assertEqual(task.validate_rhythm([1, 4], '4'), 'Valid rhythm')
            self.assertEqual(task.validate_rhythm([3, 8], '888'), 'Valid rhythm')
            self.assertEqual(task.validate_rhythm([4, 4], '44|4444|884884|22|1|44'), 'Valid rhythm with anacrusis')
            self.assertEqual(task.validate_rhythm([5, 2], '222|1144|41188|22'), 'Valid rhythm with anacrusis')
            self.assertEqual(task.validate_rhythm([3, 8], '88|48|84|8'), 'Valid rhythm with anacrusis')
            self.assertEqual(task.validate_rhythm([4, 4], '44|11|224|44'), 'Invalid rhythm')
            self.assertEqual(task.validate_rhythm([5, 2], '222|111|222222|22'), 'Invalid rhythm')
            self.assertEqual(task.validate_rhythm([3, 8], '8|8888|448|88'), 'Invalid rhythm')
            self.assertEqual(task.validate_rhythm([4, 4], '|11|224|4444'), 'Invalid rhythm')
            self.assertEqual(task.validate_rhythm([5, 2], '2288888244|111|222222|'), 'Invalid rhythm')
            self.assertEqual(task.validate_rhythm([3, 8], '|884|888|'), 'Invalid rhythm')
            self.assertEqual(task.validate_rhythm([4, 4], '444|22|1|244'), 'Invalid rhythm')
            self.assertEqual(task.validate_rhythm([5, 2], '111|222222|888'), 'Invalid rhythm')
            self.assertEqual(task.validate_rhythm([3, 8], '444|888|1'), 'Invalid rhythm')
            self.assertEqual(task.validate_rhythm([7, 3], '222|111|2222222|1112|2222'), 'Invalid rhythm')
            self.assertEqual(task.validate_rhythm([1, 3], '2|44|22'), 'Invalid rhythm')
            self.assertEqual(task.validate_rhythm([9, 9], '444448|2288'), 'Invalid rhythm')
            self.assertEqual(task.validate_rhythm([3, 3], '333|333|333'), 'Invalid rhythm')
            self.assertEqual(task.validate_rhythm([5, 7], '777|77777|77'), 'Invalid rhythm')
            self.assertEqual(task.validate_rhythm([2, 6], '66|66|66|66|66'), 'Invalid rhythm')
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
