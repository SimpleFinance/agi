import re
from itertools import chain, ifilter


ALPHA_RE = re.compile("^[a-zA-Z0-9]+$")


def filter_pairs(**pairs):
    return ifilter(lambda (k, v): v is not None, pairs.items())


def merge(dicts):
    return dict(chain(*[d.items() for d in dicts]))


def is_alpha(string):
    return True if ALPHA_RE.match(string) else False
