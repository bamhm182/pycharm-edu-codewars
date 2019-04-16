* How to make tests.py

    I recommend making a live template as follows:

    from test_helper import run_common_tests, passed
    from exception_helper import handle_exception
    import unittest
    import task


    class Test(unittest.TestCase):
        def test_$function$(self):
            try:
                self.assertEqual(task.$function$($in1$), $out1$)
                self.assertEqual(task.$function$($in2$), $out2$)
                self.assertEqual(task.$function$($in3$), $out3$)
                self.assertEqual(task.$function$($in4$), $out4$)
            except Exception as e:
                handle_exception(e)
            passed()


    if __name__ == '__main__':
        run_common_tests()
        suite = unittest.TestLoader().loadTestsFromTestCase(Test)
        unittest.TextTestRunner(verbosity=2).run(suite)

    This will allow you to easily create the tests.py files. Just open tests.py and delete everything, then insert your
    live template. Fill in the blanks with the name of the function from CodeWars and insert the tests into the
    assertEqual statements. This takes a small amount of manual work since the CodeWars tests take a different format.
    Here, $in#$ represents the args going into the function and $out#$ represents the expected outcome.

* How to make task.html

    Make task.html match the following:

    <html>
    From <a href="">CodeWars</a>
    </html>

    Paste the URL to the CodeWars problem in the href. Right click on the instructions and click inspect. Click the tag:

    <div class="markdown" id="description">

    and copy it. This will copy all its children. Paste it just below the `From CodeWars` line.

* How to make task.py

    I've just been making sure that I have the function name the same as in CodeWars and giving it an empty return
    statement to keep PyCharm happy.

    I've also been adding a # ----... line to separate the code from a few tests so students can see their current
    output and whether or not it passes.
