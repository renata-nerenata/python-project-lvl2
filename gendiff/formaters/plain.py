from gendiff.constants import (
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


def to_string(value_to_str):  # как отобразить python формат в строке
    if isinstance(value_to_str, dict):  # если
        return '[complex value]'

    if isinstance(value_to_str, str):  # строка в кавычках
        return "'{0}'".format(value_to_str)

    if value_to_str is None:
        return 'null'

    return str(value_to_str).lower()  # если булевое значение


def to_list(items):
    items_list = []

    if not isinstance(items, list):
        return [items]
    for item in items:
        items_list.extend(to_list(item))

    return items_list


def render_plain(diff):
    diff_type = diff[TYPE]
    key = diff.get(KEY)
    children = diff.get(CHILDREN)

    if diff_type == ORIGIN:
        rows = [render_plain(child) for child in children]
        return '\n'.join(to_list(rows))

    if diff_type == NESTED:
        rows = []
        for child in children:
            child[KEY] = '{0}.{1}'.format(key, child[KEY])
            rows.append(render_plain(child))
        return rows

    if diff_type == ADDED:
        value = to_string(diff['value'])
        return "Property '{0}' was added with value: {1}".format(key, value)

    if diff_type == REMOVED:
        return "Property '{0}' was removed".format(key)

    if diff_type == UPDATED:
        value = to_string(diff['old_value'])
        new_value = to_string(diff['new_value'])
        return "Property '{0}' was updated. From {1} to {2}".format(
            key,
            value,
            new_value,
        )

    if diff_type == UNCHANGED:
        return []
