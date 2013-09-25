from .base import Object


class Fn(Object):

    def __init__(self, arg):
        name = self.__class__.__name__.replace("Fn", "Fn::")
        super(Fn, self).__init__({name: arg})


class FnBase64(Fn):
    pass


class FnFindInMap(Fn):

    def __init__(self, map_, key, label):
        super(FnFindInMap, self).__init__([map_, key, label])


class FnGetAtt(Fn):

    def __init__(self, resource, attr):
        super(FnGetAtt, self).__init__([resource, attr])


class FnGetAZs(Fn):

    def __init__(self, region=""):
        super(FnGetAZs, self).__init__(region)


class FnJoin(Fn):

    def __init__(self, delimiter, *values):
        super(FnJoin, self).__init__([delimiter] + list(values))


class FnSelect(Fn):

    def __init__(self, index, *values):
        super(FnSelect, self).__init__([str(index), list(values)])


class Ref(Object):

    def __init__(self, name):
        super(Ref, self).__init__(Ref=name)
