import unittest

from agi import util


class TestTemplateUtil(unittest.TestCase):

    def test_merge(self):
        self.assertEqual({1: 3}, util.merge([{1: 2}, {1: 3}]))

    def test_filter_pairs(self):
        self.assertEqual([("a", 3)],
                         list(util.filter_pairs(a=3, b=None)))

if __name__ == "__main__":
    unittest.main()
