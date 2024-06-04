# https://www.codewars.com/kata/520446778469526ec0000001/

def same_structure_as(original: list, other: list) -> bool:
    if not isinstance(original, type(other)):
        return False

    if len(original) != len(other):
        return False

    for key, value in enumerate(original):
        allowed = (type(other[key]),)
        if isinstance(other[key], int):
            allowed += (str,)
        if isinstance(other[key], str):
            allowed += (int,)
        if not isinstance(value, allowed):
            return False

        if isinstance(value, list):
            if len(value) != len(other[key]):
                return False

            if len(value) != 0:
                if not isinstance(value[0], type(other[key][0])):
                    return False

    return True
