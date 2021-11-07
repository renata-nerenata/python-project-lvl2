from constants import (
    ADDED,
    CHILDREN,
    KEY,
    NESTED,
    ORIGIN,
    REMOVED,
    TYPE,
    UNCHANGED,
    UPDATED
)

INDENT_TYPE = ' '
INDENT_SIZE = 4


def to_string(value_to_str, depth):
    if value_to_str is None:
        return 'null'

    if isinstance(value_to_str, bool):
        return str(value_to_str).lower()

    if isinstance(value_to_str, dict):
        result = []
        indent = make_indent(depth + 1)
        for key, value_to_str in value_to_str.items():
            str_value = to_string(value_to_str, depth + 1)
            result.append(
                '{0}    {1}: {2}\n'.format(indent, key, str_value),
            )
        return '{{\n{0}{1}}}'.format(''.join(result), indent)

    return value_to_str


def make_indent(depth, indent_size=INDENT_SIZE, indent_type=INDENT_TYPE):
    return indent_type * indent_size * depth


def render_stylish(diff, depth=0):
    diff_type = diff[TYPE] #получаем статус дерева - ORIGIN - нулевой уровень дерева
    key = diff.get(KEY)
    indent = make_indent(depth) #управление отступом
    children = diff.get(CHILDREN) #пройтись по детям

    if diff_type == ORIGIN: #
        rows = ['{0}{1}\n'.format(
            indent,
            render_stylish(child, depth),
        ) for child in children]
        return '{{\n{0}}}'.format(''.join(rows))

    if diff_type == NESTED:
        rows = ['{0}\n'.format(
            render_stylish(child, depth + 1),
        ) for child in children]
        return '{0}    {1}: {{\n{2}{3}}}'.format(
            indent,
            key,
            ''.join(rows),
            make_indent(depth + 1),
        )

    if diff_type == ADDED:
        return '{0}  + {1}: {2}'.format(
            indent,
            key,
            to_string(diff['value'], depth),
        )

    if diff_type == REMOVED:
        return '{0}  - {1}: {2}'.format(
            indent,
            key,
            to_string(diff['value'], depth),
        )

    if diff_type == UPDATED:
        str1 = '{0}  - {1}: {2}'.format(
            indent,
            key,
            to_string(diff['old_value'], depth),
        )
        str2 = '{0}  + {1}: {2}'.format(
            indent,
            key,
            to_string(diff['new_value'], depth),
        )
        return '\n'.join([str1, str2])

    if diff_type == UNCHANGED:
        return '{0}    {1}: {2}'.format(
            indent,
            key,
            to_string(diff['value'], depth),
        )