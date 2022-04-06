from detector.object_detector import is_float


def test():
    assert is_float(3.1416) == True
