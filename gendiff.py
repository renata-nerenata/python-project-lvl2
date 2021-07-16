import argparse
import json


def read_file(path):
    return json.load(open(path))


def get_answer(file1, file2):
    answer = {}
    for key_1, value_1 in file1.items():
        for key_2, value_2 in file2.items():
            if (key_1 == key_2) & (value_1 == value_2):
                answer[str('  ' + key_1)] = value_1
            if (key_1 == key_2) & (value_1 != value_2):
                answer[str('- ' + key_1)] = value_1
                answer[str('+ ' + key_2)] = value_2
    for key in set(file1) - set(file2):
        answer[str('- ' + key)] = file1[key]
    for key in set(file2) - set(file1):
        answer[str('+ ' + key)] = file2[key]
    return answer


def sorted_answer(answer):
    return {k: v for k, v in sorted(answer.items(), key =  lambda x: x[0][2])}


def answer_to_string(answer_sorted):
    string = '{\n'
    for k, v in answer_sorted.items():
        string = string + str(k) + ' : ' + str(v) + '\n'
    string = string + '}'
    return print(string)


def generate_diff():
    file1 = read_file('file1.json')
    file2 = read_file('file2.json')
    answer = get_answer(file1, file2)
    answer_sorted = sorted_answer(answer)
    return answer_to_string(answer_sorted)


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '-format', help='set format of output')

    args = parser.parse_args()
    print(args.accumulate(args.integers))


if __name__ == '__main__':
    main()