import random
import string


MIN_STRING_LENGTH = 2
MAX_STRING_LENGTH = 30
MIN_INT = 0
MAX_INT = 10000
MIN_FLOAT = 0.0
MAX_FLOAT = 10000.0


def generate_alphanumeric():
    length = random.randint(MIN_STRING_LENGTH, MAX_STRING_LENGTH)  
    result = ""

    for i in range(length):
        result += random.choice(string.ascii_lowercase + string.digits)
    
    return result


def generate_string():
    length = random.randint(MIN_STRING_LENGTH, MAX_STRING_LENGTH) 
    result = ""

    for i in range(length):
        result +=random.choice(string.ascii_lowercase) 
    
    return result


def generate_integer():
    result = random.randint(MIN_INT, MAX_INT)
    result = str(result)
    
    return result

def generate_float():
    length = random.randint(1, 6) 
    print(length)
    result = round(random.uniform(MIN_FLOAT, MAX_FLOAT), length)
    result = str(result)
    
    return result

if __name__ == '__main__':
    # function_list = [generate_alphanumeric, generate_string, generate_integer, generate_float]
    # dataType = random.choice(function_list)

    # result = dataType()

    # print(dataType, result)
    print(generate_string())