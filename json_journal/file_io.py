# pylint: disable = import-error, missing-class-docstring, missing-function-docstring, missing-module-docstring
import json


def load_json_file(file_path):
    '''documentation'''
    with open(file_path, 'r', encoding="utf-8") as file:
        data = json.load(file)
    return data


def save_json_file(all_data, file_path):
    json_string = json.dumps(all_data, indent=4)
    with open(file_path, 'w+', encoding="utf-8") as file:
        file.write(json_string)
