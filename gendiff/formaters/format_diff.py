from gendiff.formaters.stylish import render_stylish
from gendiff.formaters.plain import render_plain
from gendiff.formaters.json import render_json


def format_diff(diff, format_name):
    if format_name == 'stylish':
        return render_stylish(diff)
    if format_name == 'plain':
        return render_plain(diff)
    if format_name == 'json':
        return render_json(diff)
