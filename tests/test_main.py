from context import machinecv
import unittest


class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(machinecv.smile(), ":)")


if __name__ == '__main__':
    unittest.main()
