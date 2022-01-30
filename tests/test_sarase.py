from sarase import __version__
import unittest
from sarase import add

def test_version():
    assert __version__ == '0.1.7'

class TestUtilities(unittest.TestCase):
    def test_add(self):
        assert add(1, 2) == 3
