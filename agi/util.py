import re
from itertools import chain

__all__ = ["filter_pairs", "merge", "is_alpha"]

def filter_pairs(**pairs):        
    return filter(lambda (k, v): v is not None, pairs.items())

def merge(dicts):
    return dict(chain(*[d.items() for d in dicts]))

alpha_re = re.compile("^[a-zA-Z0-9]+$")
def is_alpha(string):
    return True if alpha_re.match(string) else False
