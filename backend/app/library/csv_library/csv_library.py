import csv
from logging import getLogger
logger = getLogger("simpleExample")

def generate_from_csv_data(file_path):
    logger.info("we are in")
    ret_string = ""
    
    with open(file_path) as csvfile:
        country_reader = csv.reader(csvfile, delimiter=',')
        for row in country_reader:
            print (" ".join(row))
            ret_string += " ".join(row) + '<br>'
    return ret_string

