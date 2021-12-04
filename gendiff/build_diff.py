from gendiff.constants import (
    ADDED,
    CHILDREN,
    KEY,
    NESTED,
    ORIGIN,
    REMOVED,
    TYPE,
    UNCHANGED,
    UPDATED,
    VALUE
)


def build_diff(data1, data2):
    return {TYPE: ORIGIN,
            CHILDREN: create_diff(data1, data2)}


def create_list_keys(dict1, dict2):
    keys1 = list(dict1.keys())
    keys2 = list(dict2.keys())

    return keys1 if (dict1 == dict2) else set(keys1 + keys2)


def create_diff(data1, data2=None):
    if not isinstance(data1, dict):
        return data1

    if data2 is None:
        data2 = data1

    keys = create_list_keys(data1, data2)

    result_diff = []
    for key in sorted(keys):
        if key not in data1:
            result_diff.append({
                TYPE: ADDED,
                KEY: key,
                VALUE: data2[key],
            })
            continue

        if key not in data2:
            result_diff.append({
                TYPE: REMOVED,
                KEY: key,
                VALUE: data1[key],
            })
            continue

        if isinstance(data1[key], dict):
            if isinstance(data2[key], dict):
                result_diff.append({
                    TYPE: NESTED,
                    KEY: key,
                    CHILDREN: create_diff(data1[key], data2[key]),
                })
                continue

        if data1[key] != data2[key]:
            result_diff.append({
                TYPE: UPDATED,
                KEY: key,
                'old_value': data1[key],
                'new_value': data2[key],
            })
            continue

        result_diff.append({
            TYPE: UNCHANGED,
            KEY: key,
            VALUE: data1[key],
        })

    return result_diff
