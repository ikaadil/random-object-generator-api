from detector.object_detector import is_alphanumerics
from detector.object_detector import is_alphanumerics


def test():
    assert is_alphanumerics("adng123565") == True
