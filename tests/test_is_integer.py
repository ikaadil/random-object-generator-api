from detector.object_detector import is_integer


def test():
    assert is_integer(167) == True
