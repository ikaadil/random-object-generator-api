def is_int(value):
    """ If the value can be convert into interger, then return true
    otherwise retrun false.
    """

    try:
        int(value)
        return True
    except ValueError:
        return False


def is_float(value):
    """ If the value can be convert into float, then return true
    otherwise retrun false.
    """

    try:
        float(value)
        return True
    except ValueError:
        return False


def is_alphanumerics(value):
    """ If we find any digit in the value, then return true
    otherwise retrun false.
    """

    for character in value:
        if character.isnumeric():
            return True

    return False


if __name__ == '__main__':
    print(is_alphanumerics("ad123"))
