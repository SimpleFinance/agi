import unittest

from agi.aws import *

class TestService(unittest.TestCase):

    def setUp(self):
        self.cls = service("the::name")
        self.obj = self.cls(Name="Name")

    def test_class_name(self):
        self.assertEqual("name", self.cls.__name__)

    def test_type(self):
        self.assertEqual("the::name", self.obj.Type)

    def test_name(self):
        self.assertEqual("Name", self.obj.Name)

    def test_services(self):
        s = service("name", "a", "b", "c")
        self.assertEqual("c", s.c.__name__)
        self.assertEqual("name::c", s.c().Type)

if __name__ == "__main__":
    unittest.main()
