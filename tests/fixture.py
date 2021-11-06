from gendiff import generate_diff


def test_plain(file1, file2):
    answer = ''
    if generate_diff(file1, file2) != answer:
        raise Exception('Функция работает неверно!')