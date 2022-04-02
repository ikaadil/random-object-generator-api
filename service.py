import os
from utils import *

FILE_NAME = "output_file.txt"
MAX_FILE_SIZE = 2097152


def generate_file():
    open(FILE_NAME, 'w')
    file_size = os.stat(FILE_NAME).st_size

    with open(FILE_NAME, 'a') as file:
        while file_size < MAX_FILE_SIZE:
            function_list = [generate_alphanumerics,
                             generate_string, generate_integer, generate_float]
            data_type = random.choice(function_list)

            result = data_type()

            if file_size == 0:
                file.write(result)
            else:
                file.write(", " + result)

            file_size = os.stat(FILE_NAME).st_size

        file.close()


if __name__ == '__main__':
    generate_file()