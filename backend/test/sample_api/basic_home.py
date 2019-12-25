from flask import Flask
from logging import getLogger
import os
from backend.app.library.csv_library.csv_library import generate_from_csv_data


logger = getLogger("simpleExample")

travel_commrade = Flask('__name__')

# Root Page
@travel_commrade.route('/')
def index():
    logger.info("Well the application has started....")
    return "Hello, Travellers"

# Sample API to get list of all countries
# TODO: to implment query format and graphql version
@travel_commrade.route('/_travel_commrade/basic/utilities/countries', methods=['GET'])
def get_country_details():
    logger.info("Fetching country details for you...")
    project_root = os.path.dirname(os.path.dirname(__file__))
    data_folder = os.path.join("testdata", "csv_files", "worldcities.csv")
    csv_path = os.path.join(project_root, data_folder)
    print(csv_path)
    return generate_from_csv_data(csv_path)


if __name__ == '__main__':
    travel_commrade.run(debug=True)