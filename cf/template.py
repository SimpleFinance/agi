"""Templates and their main components.
"""

from .util import *

__all__ = [
    "Template",
    "Parameters", "Parameter",
    "Mappings", "Mapping",
    "Outputs", "Output",
    "Resource",
]

class Object(dict): pass
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
                 DependsOn=None,
                 DeletionPolicy=None,
                 UpdatePolicy=None,
                 Metadata=None,
                 Properties=None,
                 **properties):
        Properties = merge([Properties or {}, properties]) or None

        resource = filter_pairs(
            Type=Type,
            DependsOn=DependsOn,
            DeletionPolicy=DeletionPolicy,
            UpdatePolicy=UpdatePolicy,
            Metadata=Metadata,
            Properties=Properties)

        super(Resource, self).__init__(resource)


class Parameters(Object): pass
class Parameter(Object):

    def __init__(self, Type,
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

class Mappings(Object): pass
class Mapping(Object): pass

class Outputs(Object): pass
class Output(Object):

    def __init__(self, value, description=None):
        output = {"Value": value}
        if description is not None:
            output["Description"] = description
        super(Output, self).__init__(output)
