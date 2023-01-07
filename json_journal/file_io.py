import json

def load_json_file(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    return data