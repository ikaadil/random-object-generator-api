import json
from utils import *

FILE_NAME = "output_file.txt"
MAX_FILE_SIZE = 2097152


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
        "Alphabetical string": count_of_string,
        "Real numbers": count_of_float,
        "Integers": count_of_integer,
        "Alphanumerics": count_of_alphanumerics
    }

    return report


def generate_file(text):
    """Create the file with text"""

    with open(FILE_NAME, 'w') as file:
        file.write(text)


def generate_text():
    """Here our main target is to create a text which length will
    be equal to MAX_FILE_SIZE. To keep the text size exactly equal 
    to MAX_FILE_SIZE, we add objects randomly and break the loop when
    text length is less (MAX_FILE_SIZE - MAX_STRING_LENGTH). Then we add
    one more string to make the length exactly same.
    """

    text = ""

    while len(text) < MAX_FILE_SIZE - MAX_STRING_LENGTH:
        function_list = [generate_random_alphanumerics,
                         generate_random_string, generate_random_integer, generate_random_float]

        
        data_type = random.choice(function_list)    # randomly choose the object method

        data_object = data_type()

        if text == "":
            text = data_object
        else:
            text += ', ' + data_object

    file_size = len(text)
    number_of_lack_byte = MAX_FILE_SIZE - file_size
    text += ", " + generate_random_string(number_of_lack_byte - 2)      # we subtract 2 from number_of_lack_byte, because ', ' requires 2 bytes


    return text


def generate_file_and_report():
    """ Create a text which size is equal to 2MB and contains Alphabetical 
    string, Real numbers, Integers, Alphanumerics object. Then generate a file
    with that text and a report that contains the counts of differenct objects
    """

    text = generate_text()
    generate_file(text)
    report = generate_report(text)

    result = {
        "link": "/download/output_file.txt",
        "report": report
    }

    return result


if __name__ == '__main__':
    result = generate_file_and_report()
    print(json.dumps(result, ensure_ascii=False, default=str, indent=2))
