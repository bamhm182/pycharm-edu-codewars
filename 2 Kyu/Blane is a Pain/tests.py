from test_helper import run_common_tests, passed
from exception_helper import handle_exception
import unittest
import task

TRACK_EX = """\
                                /------------\\
/-------------\\                /             |
|             |               /              S
|             |              /               |
|        /----+--------------+------\\        |   
\\       /     |              |      |        |     
 \\      |     \\              |      |        |                    
 |      |      \\-------------+------+--------+---\\
 |      |                    |      |        |   |
 \\------+--------------------+------/        /   |
        |                    |              /    | 
        \\------S-------------+-------------/     |
                             |                   |
/-------------\\              |                   |
|             |              |             /-----+----\\
|             |              |             |     |     \\
\\-------------+--------------+-----S-------+-----/      \\
              |              |             |             \\
              |              |             |             |
              |              \\-------------+-------------/
              |                            |               
              \\----------------------------/ 
"""


class Test(unittest.TestCase):
    def test_train_crash(self):
        try:
            self.assertEqual(task.train_crash(TRACK_EX, "Aaaa", 147, "Bbbbbbbbbbb", 288, 1000), 516)
        except Exception as e:
            handle_exception(e)
        passed()


if __name__ == '__main__':
    run_common_tests()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
