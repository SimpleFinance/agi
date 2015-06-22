from .template import Resource


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
# Generate the following with:
#   ./bin/pip install lxml
#   ./bin/python -m agi.scripts.gen_types
AWS.AutoScaling = service(
    "AWS::AutoScaling",
    "AutoScalingGroup",
    "LaunchConfiguration",
    "ScalingPolicy",
    "Trigger",
)
AWS.CloudFormation = service(
    "AWS::CloudFormation",
    "Authentication",
    "CustomResource",
    "Init",
    "Stack",
    "WaitCondition",
    "WaitConditionHandle",
)
AWS.CloudFront = service(
    "AWS::CloudFront",
    "Distribution",
)
AWS.CloudWatch = service(
    "AWS::CloudWatch",
    "Alarm",
)
AWS.DynamoDB = service(
    "AWS::DynamoDB",
    "Table",
)
AWS.EC2 = service(
    "AWS::EC2",
    "CustomerGateway",
    "DHCPOptions",
    "EIP",
    "EIPAssociation",
    "Instance",
    "InternetGateway",
    "NetworkAcl",
    "NetworkAclEntry",
    "NetworkInterface",
    "NetworkInterfaceAttachment",
    "Route",
    "RouteTable",
    "SecurityGroup",
    "SecurityGroupEgress",
    "SecurityGroupIngress",
    "Subnet",
    "SubnetNetworkAclAssociation",
    "SubnetRouteTableAssociation",
    "VPC",
    "VPCDHCPOptionsAssociation",
    "VPCGatewayAttachment",
    "VPNConnection",
    "VPNConnectionRoute",
    "VPNGateway",
    "Volume",
    "VolumeAttachment",
)
AWS.ElastiCache = service(
    "AWS::ElastiCache",
    "CacheCluster",
    "ParameterGroup",
    "ReplicationGroup",
    "SecurityGroup",
    "SecurityGroupIngress",
    "SubnetGroup",
)
AWS.ElasticBeanstalk = service(
    "AWS::ElasticBeanstalk",
    "Application",
    "Environment",
)
AWS.ElasticLoadBalancing = service(
    "AWS::ElasticLoadBalancing",
    "LoadBalancer",
)
AWS.IAM = service(
    "AWS::IAM",
    "AccessKey",
    "Group",
    "InstanceProfile",
    "Policy",
    "Role",
    "User",
    "UserToGroupAddition",
)
AWS.RDS = service(
    "AWS::RDS",
    "DBInstance",
    "DBParameterGroup",
    "DBSecurityGroup",
    "DBSecurityGroupIngress",
    "DBSubnetGroup",
)
AWS.Route53 = service(
    "AWS::Route53",
    "HealthCheck",
    "HostedZone",
    "RecordSet",
    "RecordSetGroup",
)
AWS.S3 = service(
    "AWS::S3",
    "Bucket",
    "BucketPolicy",
)
AWS.SDB = service(
    "AWS::SDB",
    "Domain",
)
AWS.SNS = service(
    "AWS::SNS",
    "Topic",
    "TopicPolicy",
)
AWS.SQS = service(
    "AWS::SQS",
    "Queue",
    "QueuePolicy",
)
