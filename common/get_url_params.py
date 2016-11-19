# -*- coding: utf-8 -*-
from data_type import ObjectDict


def to_str(obj):
    """
    Python 3 obj bytes to str.
    :param obj:
    :return:
    """
    return obj.decode('utf-8') if isinstance(obj, bytes) else obj


def get_url_params(arguments):
    """
    Get all arguments for request.
    :param arguments:
    :return:
    """
    params = ObjectDict(arguments)
    for key in params:
        if isinstance(params[key], list) and params[key]:
            params[to_str(key)] = to_str(params[key][0])
    return params


