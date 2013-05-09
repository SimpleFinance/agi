from itertools import chain

__all__ = ["filter_pairs", "merge"]

def filter_pairs(**pairs):        
    return filter(lambda (k, v): v is not None, pairs.items())

def merge(dicts):
    return dict(chain(*[d.items() for d in dicts]))
