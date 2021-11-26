import json
import yaml
from gendiff.build_diff import build_diff
from gendiff.formaters.stylish import render_stylish
from gendiff.formaters.plain import render_plain
from gendiff.formaters.json import render_json


def read_file(file_name):
    if file_name.endswith(".json"):
        return json.load(open(file_name))
    elif file_name.endswith(".yml") or file_name.endswith(".yaml"):
        return yaml.safe_load(open(file_name))
    else:
        print('Wrong file extension')


def format_diff(diff, format_name):
    if format_name == 'stylish':
        return render_stylish(diff)
    if format_name == 'plain':
        return render_plain(diff)
    if format_name == 'json':
        return render_json(diff)


def generate_diff(first_file, second_file, format_name='stylish'):
    file1 = read_file(first_file)
    file2 = read_file(second_file)
    answer_raw = build_diff(file1, file2)
    answer = format_diff(answer_raw, format_name)
    print(answer)
    return answer
