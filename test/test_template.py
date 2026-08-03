"""
# To run tests, enter:
$ python -m unittest .\test\test_template.py

# To get coverage:
$ python -m coverage run -m unittest .\test\test_template.py
$ python -m coverage report
$ python -m coverage html (then open index.html in file explorer)
"""
import unittest

class TestFunctionName1(unittest.TestCase):
    """
    Unit tests for function_1 which will test...
    """
    def test_name_of_test_1(self):
        pass

    def test_name_of_test_2(self):
        pass

    def test_name_of_test_3(self):
        pass

class TestFunctionName2(unittest.TestCase):
    """
    Unit tests for function_2 which will test...
    """
    def test_name_of_test_1(self):
        pass

    def test_name_of_test_2(self):
        pass

    def test_name_of_test_3(self):
        pass

if __name__ == "__main__": # pragma: no cover
    unittest.main()
