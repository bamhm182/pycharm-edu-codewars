from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_validate_usr(self):
        try:
            self.assertEqual(task.validate_usr('asddsa'), True)
            self.assertEqual(task.validate_usr('a'), False)
            self.assertEqual(task.validate_usr('Hass'), False)
            self.assertEqual(task.validate_usr("Hasd_12assssssasasasasasaasasasasas"), False)
            self.assertEqual(task.validate_usr(""), False)
            self.assertEqual(task.validate_usr("____"), True)
            self.assertEqual(task.validate_usr(""), False)
            self.assertEqual(task.validate_usr("p1pp1"), True)
            self.assertEqual(task.validate_usr(""), False)
            self.assertEqual(task.validate_usr("asd43_34"), True)
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
