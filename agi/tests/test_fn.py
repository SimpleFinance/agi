import unittest

from agi.fn import *

class TestFn(unittest.TestCase):


    def test_fn(self):
        class FnTest(Fn): pass
        self.assertTrue("Fn::Test" in FnTest("arg"))
        self.assertEqual(
            "arg",
            FnTest("arg")["Fn::Test"])

    def test_fn_base64(self):
        self.assertEqual(
            "arg",
            FnBase64("arg")["Fn::Base64"])

    def test_fn_find_in_map(self):
        self.assertEqual(
            ["map", "key", "label"],
            FnFindInMap("map", "key", "label")["Fn::FindInMap"])

    def test_fn_get_att(self):
        self.assertEqual(
            ["resource", "attr"],
            FnGetAtt("resource", "attr")["Fn::GetAtt"])

    def test_get_azs(self):
        self.assertEqual(
            "region",
            FnGetAZs("region")["Fn::GetAZs"])

    def test_fn_join(self):
        self.assertEqual(
            ["delimiter", "val1", "val2"],
            FnJoin("delimiter", "val1", "val2")["Fn::Join"])

    def test_fn_select(self):
        self.assertEqual(
            ["1", ["val1", "val2"]],
            FnSelect(1, "val1", "val2")["Fn::Select"])

    def test_ref(self):
        self.assertEqual(
            {"Ref": "name"},
            Ref("name"))

if __name__ == "__main__":
    unittest.main()
