'''Functions to interact with json files'''
import json


def load_json_file(file_path):
    '''file_path -> file path for the json file that needs to be loaded.
    Returns dictionary of loaded data from json file'''
    with open(file_path, 'r', encoding="utf-8") as file:
        data = json.load(file)
    return data


def save_json_file(all_data, file_path):
    '''all_data -> dictionary with the full account name and corresponding balance,
    file_path -> file path for the json file that needs to be loaded.
    Returns nothing, creates and saves data to specified json file'''
    json_string = json.dumps(all_data, indent=4)
    with open(file_path, 'w+', encoding="utf-8") as file:
        file.write(json_string)
