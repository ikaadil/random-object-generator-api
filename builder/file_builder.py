import uuid
from builder.object_builder import *


FOLDER_PATH = "templates/static/"
MAX_FILE_SIZE = 2097152


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



def generate_link():
    """Generate a link with unique file name"""

    file_name = str(uuid.uuid4()) + ".txt"  # defined unique file name
    file_link = FOLDER_PATH + file_name

    return file_link
def generate_file(text, file_link):
    """Create the file with text in the file link with unique name"""

    with open(file_link, 'w') as file:
        file.write(text)


