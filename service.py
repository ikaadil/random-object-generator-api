import os
import json
from utils import *

FILE_NAME = "output_file.txt"
MAX_FILE_SIZE = 2097152


def generate_report(count_of_alphanumerics,
                    count_of_string, count_of_float, count_of_integer):
    report = {
        "Alphabetical string": count_of_string,
        "Real numbers": count_of_float,
        "Integers": count_of_integer,
        "Alphanumerics": count_of_alphanumerics
    }

    return report


def generate_file():
    open(FILE_NAME, 'w')
    file_size = os.stat(FILE_NAME).st_size
    count_of_alphanumerics = 0
    count_of_string = 0
    count_of_integer = 0
    count_of_float = 0

    with open(FILE_NAME, 'a') as file:
        while file_size < MAX_FILE_SIZE:
            function_list = [generate_alphanumerics,
                             generate_string, generate_integer, generate_float]
            data_type = random.choice(function_list)

            data_object = data_type()

            if file_size == 0:
                file.write(data_object)
            else:
                file.write(", " + data_object)

            file_size = os.stat(FILE_NAME).st_size

            if data_type == generate_alphanumerics:
                count_of_alphanumerics += 1
            elif data_type == generate_string:
                count_of_string += 1
            elif data_type == generate_float:
                count_of_float += 1
            else:
                count_of_integer += 1
                
        file.close()


    report = generate_report(count_of_alphanumerics,
                             count_of_string, count_of_float, count_of_integer)

    result = {
        "link": "/download/output_file.txt",
        "report": report
    }

    return result


if __name__ == '__main__':
    result = generate_file()
    print(json.dumps(result, ensure_ascii=False, default=str, indent=2))