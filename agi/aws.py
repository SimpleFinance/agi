from .template import Resource

__all__ = ["service", "AWS"]

def service(name, *services):
    sep = "::"
    class Service(Resource):

        def __init__(self, Name=None, **params):
            super(Service, self).__init__(name, Name=Name, **params)
    Service.__name__ = name.split(sep)[-1]

    for svc in services:
        service_name = "::".join((name, svc))
        setattr(Service, svc, service(service_name))
    return Service

AWS = service("AWS")
AWS.AutoScaling = service("AWS::AutoScaling",
    "AutoScalingGroup",                          
    "LaunchConfiguration",
)
AWS.EC2 = service("AWS::EC2",
    "EIPAssociation",
    "Instance",
    "SecurityGroup",
)
