from test_helper import failed
import traceback
import re
import unittest


def handle_exception(e):
    if "AssertionError" in type(e).__name__:
        finds = re.findall(r"\s*self\.assertEqual\(task\.(.*\)).*\)(\s*#\s*(.*))?", traceback.format_exc())[0]
        command = finds[0]
        hint = "(" + finds[2] + ")" if len(finds) > 2 and finds[2] != "" else ""
        error = str(e).split("\n")[0]
        failed('Failed: {} for {} {}'.format(error, command, hint))
    else:
        failed('Error Occurred: {}'.format(str(e).replace("\n", "")))


class Test(unittest.TestCase):
    def test(self):
        try:
            self.assertEqual(1, 5)
        except AssertionError as e:
            handle_exception(e)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
