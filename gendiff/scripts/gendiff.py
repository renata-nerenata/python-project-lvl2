import argparse
from gendiff.gendiff import generate_diff


def get_args():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        help='set format of output',
                        default='stylish')

    args = parser.parse_args()
    return args


def main():
    args = get_args()
    answer = generate_diff(args.first_file, args.second_file, args.format)
    print(answer)
    with open('tests/fixtures/answer_r_plain.txt', 'w') as f:
        f.write(answer)


if __name__ == '__main__':
    main()
