import json
import logging


def load_json_data(file_path):
    logging.info(f"Loading JSON data from: {file_path}")

    with open(file_path, "r") as file:
        data = json.load(file)

    logging.info(f"Successfully loaded data from: {file_path}")
    return data