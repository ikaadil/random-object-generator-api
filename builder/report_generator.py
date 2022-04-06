from detector.object_detector import *


def get_counts_of_objects(text):
    """ Calculate the count of each object in the text"""

    count_of_alphanumerics = 0
    count_of_string = 0
    count_of_integer = 0
    count_of_float = 0

    for value in text.split(','):
        if is_int(value):
            count_of_integer += 1
        elif is_float(value):
            count_of_float += 1
        elif is_alphanumerics(value):
            count_of_alphanumerics += 1
        else:
            count_of_string += 1

    return count_of_alphanumerics, count_of_string, count_of_integer, count_of_float


def generate_report(text):
    """Generate the report that contains the counts of each object"""

    count_of_alphanumerics, count_of_string, count_of_integer, count_of_float = get_counts_of_objects(
        text)

    report = {
        "alphabetical_string": count_of_string,
        "real_numbers": count_of_float,
        "integers": count_of_integer,
        "alphanumerics": count_of_alphanumerics
    }

    return report
