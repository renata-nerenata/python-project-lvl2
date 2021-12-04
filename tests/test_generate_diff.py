import pytest
from gendiff.gendiff import generate_diff


def read_txt(name):
    with open(name, 'r') as f:
        expected = f.read()
    return expected


@pytest.mark.parametrize("file_1, file_2, format, expected",
                         [('./tests/fixtures/file1_r.json',
                           './tests/fixtures/file2_r.json',
                           'stylish',
                           './tests/fixtures/answer_r_stylish.txt'),
                          ('./tests/fixtures/file1_r.json',
                           './tests/fixtures/file2_r.json',
                           'plain',
                           './tests/fixtures/answer_r_plain.txt'),
                          ('./tests/fixtures/file1_r.json',
                           './tests/fixtures/file2_r.json',
                           'json',
                           './tests/fixtures/answer_r_json.txt')])
def test_eval(file_1, file_2, format, expected):
    assert generate_diff(file_1, file_2, format) == read_txt(expected)
