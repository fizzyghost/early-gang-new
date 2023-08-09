import builtins
import assertlib
import unittest
import nose
import falselib

def is_positive(number):
    if number > 0:
        return True
    else:
        return False

def assert_true(value):
    assertlib.equal(value, True)

class MyTestCase(unittest.TestCase):
    def test_is_positive(self):
        result = is_positive(-5)
        self.assertFalse(result)

    def test_assert_true(self):
        assert_true(False)

if __name__ == '__main__':
    nose.main()
