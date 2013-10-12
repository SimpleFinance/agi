"""Templates and their main components.
"""

from . import util
from .base import Object
from .fn import Ref, FnGetAtt


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
        Resources = util.merge([Resources or {}, resources])

        if not Resources:
            raise TypeError("Template must have resources")

        template = util.filter_pairs(
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

        if Name is not None and not util.is_alpha(Name):
            raise TypeError("Resource Name must be alpha-numeric (%s)" % Name)

        self.Name = Name
        Properties = util.merge([Properties or {}, properties]) or None

        resource = util.filter_pairs(
            Type=Type,
            DependsOn=DependsOn,
            DeletionPolicy=DeletionPolicy,
            UpdatePolicy=UpdatePolicy,
            Metadata=Metadata,
            Properties=Properties)

        super(Resource, self).__init__(resource)

    def id(self):
        name = self.Name
        if name is not None:
            name = name.capitalize()

        path = "::".join(filter(None, (self.Type, name)))
        return "".join(path.split("::"))

    def ref(self):
        return Ref(self.id())

    def get(self, attribute):
        return FnGetAtt(self.id(), attribute)


class Property(Object):
    pass


class Options(Object):
    pass


class Attribute(Object):
    pass


class Parameters(Object):
    pass


class Parameter(Object):

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
        parameter = util.filter_pairs(
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
            ConstraintDescription=ConstraintDescription,
            )
        super(Parameter, self).__init__(parameter)

    def id(self):
        return self.Name

    def ref(self):
        return Ref(self.id())


class Mappings(Object):
    pass


class Mapping(Object):
    pass


class Outputs(Object):
    pass


class Output(Object):

    def __init__(self, value, description=None):
        output = {"Value": value}
        if description is not None:
            output["Description"] = description
        super(Output, self).__init__(output)
