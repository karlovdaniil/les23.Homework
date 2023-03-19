import os
from typing import Callable, Dict

from functions import filter_query, unique_query, limit_query, map_query, sort_query

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

CMS_TO_FUNCTIONS: Dict[str, Callable] = {
    'filter': filter_query,
    'unique': unique_query,
    'limit': limit_query,
    'map': map_query,
    'sort': sort_query,
}


def read_file(file_name: str):
    with open(file_name) as file:
        for line in file:
            yield line


def build_query(cmd, value, file_name, data):
    if data is None:
        prepared_data = read_file(DATA_DIR + os.sep + file_name)
    else:
        prepared_data = data

    func = CMS_TO_FUNCTIONS[cmd]
    func_result = func(value=value, data=prepared_data)

    return list(func_result)
