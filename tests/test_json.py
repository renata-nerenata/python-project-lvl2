from gen_diff.gendiff import generate_diff


def read_txt(name):
    with open(name, 'r') as f:
        expected = f.readline()
    return expected


def test_simple_string_1():
    actual = generate_diff('./tests/fixtures/file1.json',
                           './tests/fixtures/file2.json',
                           'stylish')
    assert actual == read_txt('./tests/fixtures/answer_stylish.txt')

