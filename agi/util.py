from itertools import chain, ifilter


def filter_pairs(**pairs):
    return ifilter(lambda (k, v): v is not None, pairs.items())
