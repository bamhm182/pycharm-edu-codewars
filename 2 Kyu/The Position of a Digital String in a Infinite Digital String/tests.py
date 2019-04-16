from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_find_position(self):
        try:
            self.assertEqual(task.find_position("456"), 3)
            self.assertEqual(task.find_position("454"), 79)
            self.assertEqual(task.find_position("455"), 98)
            self.assertEqual(task.find_position("910"), 8)
            self.assertEqual(task.find_position("9100"), 188)
            self.assertEqual(task.find_position("99100"), 187)
            self.assertEqual(task.find_position("00101"), 190)
            self.assertEqual(task.find_position("001"), 190)
            self.assertEqual(task.find_position("00"), 190)
            self.assertEqual(task.find_position("123456789"), 0)
            self.assertEqual(task.find_position("1234567891"), 0)
            self.assertEqual(task.find_position("123456798"), 1000000071)
            self.assertEqual(task.find_position("10"), 9)
            self.assertEqual(task.find_position("53635"), 13034)
            self.assertEqual(task.find_position("040"), 1091)
            self.assertEqual(task.find_position("11"), 11)
            self.assertEqual(task.find_position("99"), 168)
            self.assertEqual(task.find_position("667"), 122)
            self.assertEqual(task.find_position("0404"), 15050)
            self.assertEqual(task.find_position("949225100"), 382689688)
            self.assertEqual(task.find_position("58257860625"), 24674951477)
            self.assertEqual(task.find_position("3999589058124"), 6957586376885)
            self.assertEqual(task.find_position("555899959741198"), 1686722738828503)
            self.assertEqual(task.find_position("01"), 10)
            self.assertEqual(task.find_position("091"), 170)
            self.assertEqual(task.find_position("0910"), 2927)
            self.assertEqual(task.find_position("0991"), 2617)
            self.assertEqual(task.find_position("09910"), 2617)
            self.assertEqual(task.find_position("09991"), 35286)
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
