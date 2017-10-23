import unittest

import machinecv


class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(machinecv.smile(), ":)")


if __name__ == '__main__':
    unittest.main()
