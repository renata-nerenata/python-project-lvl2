from gen_diff.gendiff import generate_diff


def read_txt(name):
    with open(name, 'r') as f:
        expected = f.read()
    return expected


def test_simple_stylish():
    actual = generate_diff('./tests/fixtures/file1.json',
                           './tests/fixtures/file2.json',
                           'stylish')
    assert actual == read_txt('./tests/fixtures/answer_stylish.txt')


def test_simple_plain():
    actual = generate_diff('./tests/fixtures/file1.json',
                           './tests/fixtures/file2.json',
                           'plain')
    assert actual == read_txt('./tests/fixtures/answer_plain.txt')


def test_simple_json():
    actual = generate_diff('./tests/fixtures/file1.json',
                           './tests/fixtures/file2.json',
                           'json')
    assert actual == read_txt('./tests/fixtures/answer_json.txt')


def test_tree_stylish():
    actual = generate_diff('./tests/fixtures/file1_r.json',
                           './tests/fixtures/file2_r.json',
                           'stylish')
    assert actual == read_txt('./tests/fixtures/answer_r_stylish.txt')


def test_tree_plain():
    actual = generate_diff('./tests/fixtures/file1_r.json',
                           './tests/fixtures/file2_r.json',
                           'plain')
    assert actual == read_txt('./tests/fixtures/answer_r_plain.txt')


def test_tree_json():
    actual = generate_diff('./tests/fixtures/file1_r.json',
                           './tests/fixtures/file2_r.json',
                           'json')
    assert actual == read_txt('./tests/fixtures/answer_r_json.txt')
