"""Templates and their main components.
"""

from .base import Object
from .fn import Ref
from .util import *

__all__ = [
    "Template",
    "Parameters", "Parameter",
    "Mappings", "Mapping",
    "Outputs", "Output",
    "Resource", "Property", "Attribute", "Options",
]

class ListObject(list):

    def __init__(self, *items):
        super(ListObject, self).__init__(list(items))

class Template(Object):

    def __init__(self, 
                 AWSTemplateFormatVersion=None,
                 Description=None,
                 Parameters=None,
                 Mappings=None,
                 Outputs=None,
                 Resources=None,
                 **resources):
        Resources = merge([Resources or {}, resources])

        if not Resources:
            raise TypeError("Template must have resources")

        template = filter_pairs(
            AWSTemplateFormatVersion=AWSTemplateFormatVersion,
            Description=Description,
            Parameters=Parameters,
            Mappings=Mappings,
            Outputs=Outputs,
            Resources=Resources)

        super(Template, self).__init__(template)


class Resource(Object):

    def __init__(self, Type,
                 Name=None,
                 DependsOn=None,
                 DeletionPolicy=None,
                 UpdatePolicy=None,
                 Metadata=None,
                 Properties=None,
                 **properties):
        self.Type = Type
        self.Name = Name
        Properties = merge([Properties or {}, properties]) or None

        resource = filter_pairs(
            Type=Type,
            DependsOn=DependsOn,
            DeletionPolicy=DeletionPolicy,
            UpdatePolicy=UpdatePolicy,
            Metadata=Metadata,
            Properties=Properties)

        super(Resource, self).__init__(resource)

    def id(self):
        path = "::".join(filter(None, (self.Type, self.Name)))
        return "".join(atom.capitalize() for atom in path.split("::"))

    def ref(self):
        return Ref(self.id())

class Property(Object): pass
class Options(Object): pass
class Attribute(Object): pass

class Parameters(Object): pass
class Parameter(Object):

    def __init__(self, Type,
                 Name=None,
                 Default=None,
                 NoEcho=None,
                 AllowedValues=None,
                 AllowedPattern=None,
                 MaxLength=None,
                 MinLength=None,
                 MaxValue=None,
                 MinValue=None,
                 Description=None,
                 ConstraintDescription=None):
        self.Name = Name
        parameter = filter_pairs(
            Type=Type,
            Default=Default,
            AllowedValues=AllowedValues,
            AllowedPattern=AllowedPattern,
            MaxLength=MaxLength,
            MinLength=MinLength,
            MaxValue=MaxValue,
            MinValue=MinValue,
            Description=Description,
            ConstraintDescription=ConstraintDescription,
            )            
        super(Parameter, self).__init__(parameter)

    def id(self):
        return self.Name

    def ref(self):
        return Ref(self.id())

class Mappings(Object): pass
class Mapping(Object): pass

class Outputs(Object): pass
class Output(Object):

    def __init__(self, value, description=None):
        output = {"Value": value}
        if description is not None:
            output["Description"] = description
        super(Output, self).__init__(output)
