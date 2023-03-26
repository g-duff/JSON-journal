'''Functions to interact with json files'''
import json
import csv


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


# Add function for loading csv and turing it to json - example with monzo, how to do others - test - check for duplicates
def csv_to_json(file):
    '''
    Convert a CSV file to a JSON.

    Parameters
    ----------
    file : file path
        File path for the CSV.

    Returns
    -------
    json_file : dict
        Returns a JSON format for the data.
    '''
    json_file = []

    with open(file, 'r') as csvfile:
        csv_file = csv.reader(csvfile)
        next(csv_file, None)
        for record in csv_file:
            dict = {}
            date = record[1]
            description = record[4]
            amount = float(record[7])
            dict['date'] = date
            dict['description'] = description
            dict['amount'] = amount
            json_file.append(dict)
    
    return json_file

