'''Functions to interact with json files'''
import json


def load_json_file(file_path):
    '''
    Load json file from given file path.

    Parameters
    ----------
    File_path : file path
        Location of the json file to be loaded.

    Returns
    -------
    Data : dict
        Data from the loaded json file
    '''
    with open(file_path, 'r', encoding="utf-8") as file:
        data = json.load(file)
    return data


def save_json_file(all_data, file_path):
    '''
    Save data to a json file for a given file path.

    Parameters
    ----------
    All_data : dict
        Contains the full account name and corresponding balance.
    File_path : file path
        Location for the json file to be saved.

    Returns
    -------
    Creates and saves data to specified json file in the provided location.
    '''
    json_string = json.dumps(all_data, indent=4)
    with open(file_path, 'w+', encoding="utf-8") as file:
        file.write(json_string)
