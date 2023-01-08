import json


def load_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def save_json_file(all_data, file_path):
    json_string = json.dumps(all_data, indent=4)
    with open(file_path, 'w+') as file:
        file.write(json_string)
