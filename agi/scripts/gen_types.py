import lxml.html

template_type_ref = "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html"
tree = lxml.html.parse(template_type_ref)

service_types = {}
types = tree.xpath('//div[@class="highlights"]//li/a/text()')
for svc, typ in [typ.rsplit("::", 1) for typ in types]:
    service_types.setdefault(svc, []).append(typ)

for service in sorted(service_types):
    types = sorted(service_types[service])
    service = service.split("::")[1]
    print 'AWS.%s = service(' % service
    for typ in [service] + types:
        print '    "%s",' % typ
    print ')'
