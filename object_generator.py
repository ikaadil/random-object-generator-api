import random
import string


MIN_STRING_LENGTH = 2
MAX_STRING_LENGTH = 30
MIN_INT = 0
MAX_INT = 10000
MIN_FLOAT = 0.0
MAX_FLOAT = 10000.0


def generate_random_alphanumerics():
    """First defined the length of the object between predefined MIN_STRING_LENGTH
    and MAX_STRING_LENGTH with default random function. Then randomly 
    added each character of the objects from ansci lowercase and digits.
    """

    length = random.randint(MIN_STRING_LENGTH, MAX_STRING_LENGTH)
    result = ""

    for i in range(length):
        result += random.choice(string.ascii_lowercase + string.digits)

    return result


def generate_random_string(length=None):
    """First checked the length is given or not. If the length is not given 
    then defined the length of the object between predefined MIN_STRING_LENGTH 
    and MAX_STRING_LENGTH with default random function. Then randomly added each 
    character of the objects from ansci lowercase.
    """

    if not length:
        length = random.randint(MIN_STRING_LENGTH, MAX_STRING_LENGTH)

    result = ""

    for i in range(length):
        result += random.choice(string.ascii_lowercase)

    return result


def generate_random_integer():
    """Generate integer with default random function between predefined MIN_INT 
    and MAX_INT
    """

    result = random.randint(MIN_INT, MAX_INT)
    result = str(result)

    return result


def generate_random_float():
    """ first we defined the number of positions after decimal point with random
    function between 1 and 6. Then we randomly findout the float number between
    MIN_FLOAT and MAX_FLOAT
    """

    length = random.randint(1, 6)

    result = round(random.uniform(MIN_FLOAT, MAX_FLOAT), length)
    result = str(result)

    return result
