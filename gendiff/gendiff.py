import json
import yaml
from gendiff.build_diff import build_diff
from gendiff.formaters.format_diff import format_diff


def read_file(file_name):
    try:
        if file_name.endswith(".json"):
            return json.load(open(file_name))
        elif file_name.endswith(".yml") or file_name.endswith(".yaml"):
            return yaml.safe_load(open(file_name))
    except ValueError:
        raise ValueError("ValueError: wrong file extension")


def generate_diff(first_file, second_file, format_name='stylish'):
    file1 = read_file(first_file)
    file2 = read_file(second_file)
    diff = build_diff(file1, file2)
    answer = format_diff(diff, format_name)
    return answer
