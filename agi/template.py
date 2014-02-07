"""Templates and their main components.
"""

from itertools import ifilter

from .fn import Ref, FnGetAtt


def filter_pairs(**pairs):
    return ifilter(lambda (k, v): v, pairs.iteritems())


class Listdict(list):

    def __init__(self, *items):
        self += list(items)


class Template(dict):

    def __init__(self,
                 AWSTemplateFormatVersion=None,
                 Description=None,
                 Parameters=None,
                 Mappings=None,
                 Outputs=None,
                 Resources=None,
                 **resources):
        if not Resources:
            Resources = {}
        Resources.update(resources)

        if not len(Resources):
            raise TypeError("Template must have resources")

        self.update(
            filter_pairs(
                AWSTemplateFormatVersion=AWSTemplateFormatVersion,
                Description=Description,
                Parameters=Parameters,
                Mappings=Mappings,
                Outputs=Outputs,
                Resources=Resources
            )
        )


class Resource(dict):

    def __init__(self, Type,
                 Name=None,
                 DependsOn=None,
                 DeletionPolicy=None,
                 UpdatePolicy=None,
                 Metadata=None,
                 Properties=None,
                 **properties):
        self.Type = Type

        if Name and not Name.isalnum():
            raise ValueError("Resource Name must be alpha-numeric (%s)" % Name)
        if properties:
            if not Properties:
                Properties = {}
            Properties.update(properties)

        self.Name = Name

        self.update(
            filter_pairs(
                Type=Type,
                DependsOn=DependsOn,
                DeletionPolicy=DeletionPolicy,
                UpdatePolicy=UpdatePolicy,
                Metadata=Metadata,
                Properties=Properties
            )
        )

    def id(self):
        name = self.Name
        if name is not None:
            name = name.capitalize()

        path = "::".join(filter(None, (self.Type, name)))
        return "".join(path.split("::"))

    def ref(self):
        return Ref(self.id())

    def get_att(self, attribute):
        return FnGetAtt(self.id(), attribute)

    # deprecated
    def get(self, attribute):
        return self.get_att(attribute)


class Property(dict):
    pass


class Options(dict):
    pass


class Attribute(dict):
    pass


class Parameters(dict):
    pass


class Parameter(dict):

    def __init__(self, Type,
                 Name=None,
                 Default=None,
                 AllowedValues=None,
                 AllowedPattern=None,
                 MaxLength=None,
                 MinLength=None,
                 MaxValue=None,
                 MinValue=None,
                 NoEcho=None,
                 Description=None,
                 ConstraintDescription=None):
        self.Name = Name

        self.update(
            filter_pairs(
                Type=Type,
                Default=Default,
                AllowedValues=AllowedValues,
                AllowedPattern=AllowedPattern,
                MaxLength=MaxLength,
                MinLength=MinLength,
                MaxValue=MaxValue,
                MinValue=MinValue,
                NoEcho=NoEcho,
                Description=Description,
                ConstraintDescription=ConstraintDescription
            )
        )

    def id(self):
        return self.Name

    def ref(self):
        return Ref(self.id())


class Mappings(dict):
    pass


class Mapping(dict):
    pass


class Outputs(dict):
    pass


class Output(dict):

    def __init__(self, value, description=None):
        output = {"Value": value}
        if description is not None:
            output["Description"] = description
        self.update(output)
