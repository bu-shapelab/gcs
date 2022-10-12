import unittest
import tests

def test_all():
    """Runs all unit tests in the `tests/` directory.
    """
    suite = unittest.defaultTestLoader.loadTestsFromModule(tests)
    unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    test_all()
