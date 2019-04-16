from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task


class Test(unittest.TestCase):
    def test_sort_by_length(self):
        try:
            self.assertEqual(task.sort_by_length(["beg", "life", "i", "to"]), ["i", "to", "beg", "life"])
            self.assertEqual(task.sort_by_length(["", "moderately", "brains", "pizza"]), ["", "pizza", "brains", "moderately"])
            self.assertEqual(task.sort_by_length(["longer", "longest", "short"]), ["short", "longer", "longest"])
            self.assertEqual(task.sort_by_length(["dog", "food", "a", "of"]), ["a", "of", "dog", "food"])
            self.assertEqual(task.sort_by_length(["", "dictionary", "eloquent", "bees"]), ["", "bees", "eloquent", "dictionary"])
            self.assertEqual(task.sort_by_length(["a longer sentence", "the longest sentence", "a short sentence"]), ["a short sentence", "a longer sentence", "the longest sentence"])
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
