import json
import uuid
from utils import *

FOLDER_PATH = "templates/static/"
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
        "alphabetical_string": count_of_string,
        "real_numbers": count_of_float,
        "integers": count_of_integer,
        "alphanumerics": count_of_alphanumerics
    }

    return report


def generate_file(text, file_link):
    """Create the file with text in the file link with unique name"""

    with open(file_link, 'w') as file:
        file.write(text)


def generate_link():
    """Generate a link with unique file name"""

    file_name = str(uuid.uuid4()) + ".txt"  # defined unique file name
    file_link = FOLDER_PATH + file_name

    return file_link


def generate_text():
    """Here our main target is to create a text which length will be
    equal to MAX_FILE_SIZE. To keep the text size exactly equal to 
    MAX_FILE_SIZE, we add objects randomly and break the loop when text
    length is less (MAX_FILE_SIZE - MAX_STRING_LENGTH). Then we add one
    more string to make the length exactly same.
    """

    text = ""

    while len(text) < MAX_FILE_SIZE - MAX_STRING_LENGTH:
        function_list = [generate_random_alphanumerics,
                         generate_random_string, generate_random_integer, generate_random_float]

        # randomly choose the object method
        data_type = random.choice(function_list)

        data_object = data_type()

        if text == "":
            text = data_object
        else:
            text += ', ' + data_object

    file_size = len(text)
    number_of_lack_byte = MAX_FILE_SIZE - file_size
    # we subtract 2 from number_of_lack_byte, because ', ' requires 2 bytes
    text += ", " + generate_random_string(number_of_lack_byte - 2)

    return text


def generate_file_and_report():
    """ Create a text which size is equal to 2MB and contains Alphabetical 
    string, Real numbers, Integers, Alphanumerics object. After that create
    a link with unique file name so that in every api call user get unique 
    files. Then generate a file in the link with that text and create a report
    that contains the counts of differenct objects
    """

    text = generate_text()
    file_link = generate_link()
    generate_file(text, file_link)
    report = generate_report(text)

    result = {
        "link": file_link,
        "report": report
    }

    return result


if __name__ == '__main__':
    result = generate_file_and_report()
    print(json.dumps(result, ensure_ascii=False, default=str, indent=2))
