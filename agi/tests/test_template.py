import unittest

from agi.template import *

class TestTemplate(unittest.TestCase):

    def setUp(self):
        super(TestTemplate, self).setUp()
        self.template = Template(
            AWSTemplateFormatVersion = "version",
            Description = "description",
            Parameters = "parameters",
            Outputs = "outputs",
            Mappings = "mappings",
            Resources = dict(
                Foo = "foo",
            ),
            # More Resources.
            Bar = "bar",
            Baz = "baz",
        )

    def test_version(self):
        self.assertEqual("version", self.template["AWSTemplateFormatVersion"])

    def test_description(self):
        self.assertEqual("description", self.template["Description"])

    def test_parameters(self):
        self.assertEqual("parameters", self.template["Parameters"])

    def test_mappings(self):
        self.assertEqual("mappings", self.template["Mappings"])

    def test_outputs(self):
        self.assertEqual("outputs", self.template["Outputs"])

    def test_resources_len(self):
        self.assertEqual(3, len(self.template["Resources"]))

    def test_resource(self):
        self.assertEqual("foo", self.template["Resources"]["Foo"])


class TestTemplateDefaults(unittest.TestCase):

    def setUp(self):
        super(TestTemplateDefaults, self).setUp()
        self.template = Template(Foo = "foo")

    def test_no_resources(self):
        self.assertRaises(TypeError, Template)
        
    def test_skip_unset(self):
        self.assertEqual(1, len(self.template))

    def test_resource_len(self):
        self.assertEqual(1, len(self.template))

class TestResource(unittest.TestCase):

    def setUp(self):
        super(TestResource, self).setUp()
        self.resource = Resource("type",
            DependsOn = "dependson",
            DeletionPolicy = "deletionpolicy",
            UpdatePolicy = "updatepolicy",
            Metadata = "metadata",
            Properties = dict(
                Foo = "foo",
            ),
            Bar = "bar",
            Baz = "baz",
            )

    def test_depends_on(self):
        self.assertEqual("dependson", self.resource["DependsOn"])

    def test_deletion_policy(self):
        self.assertEqual("deletionpolicy", self.resource["DeletionPolicy"])

    def test_update_policy(self):
        self.assertEqual("updatepolicy", self.resource["UpdatePolicy"])

    def test_metadata(self):
        self.assertEqual("metadata", self.resource["Metadata"])

    def test_properties_len(self):
        self.assertEqual(3, len(self.resource["Properties"]))

    def test_property(self):
        self.assertEqual("foo", self.resource["Properties"]["Foo"])

class TestResourceDefaults(unittest.TestCase):

    def setUp(self):
        super(TestResourceDefaults, self).setUp()    
        self.resource = Resource(Type = "type")

    def test_nothing(self):
        self.assertEqual(1, len(self.resource))

    def test_type(self):
        self.assertEqual("type", self.resource["Type"])

    def test_no_type(self):
        self.assertRaises(TypeError, Resource)


class TestParameter(unittest.TestCase):

    def setUp(self):
        super(TestParameter, self).setUp()
        self.parameter = Parameter("type",
            Default="default",
            AllowedValues="allowedvalues",
            AllowedPattern="allowedpattern",
            MaxLength="maxlength",
            MinLength="minlength",
            MaxValue="maxvalue",
            MinValue="minvalue",
            Description="description",
            ConstraintDescription="constraintdescription",
        )


    def test_type(self):
        self.assertEqual("type", self.parameter["Type"])
        
    def test_default(self):
        self.assertEqual("default", self.parameter["Default"])

    def test_allowedvalues(self):
        self.assertEqual("allowedvalues", self.parameter["AllowedValues"])
        
    def test_allowedpattern(self):
        self.assertEqual("allowedpattern", self.parameter["AllowedPattern"])
        
    def test_maxlength(self):
        self.assertEqual("maxlength", self.parameter["MaxLength"])

    def test_minlength(self):
        self.assertEqual("minlength", self.parameter["MinLength"])
        
    def test_maxvalue(self):
        self.assertEqual("maxvalue", self.parameter["MaxValue"])
        
    def test_minvalue(self):
        self.assertEqual("minvalue", self.parameter["MinValue"])
        
    def test_description(self):
        self.assertEqual("description", self.parameter["Description"])
        
    def test_constraintdescription(self):
        self.assertEqual("constraintdescription", self.parameter["ConstraintDescription"])

class TestParameterDefaults(unittest.TestCase):

    def setUp(self):
        super(TestParameterDefaults, self).setUp()
        self.parameter = Parameter("type")

    def test_nothing(self):
        self.assertEqual(1, len(self.parameter))

    def test_type(self):
        self.assertEqual("type", self.parameter["Type"])

    def test_no_type(self):
        self.assertRaises(TypeError, Parameter)
        
if __name__ == "__main__":
    unittest.main()
