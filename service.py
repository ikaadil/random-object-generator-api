import json
from builder.file_builder import*
from builder.report_generator import generate_report


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
