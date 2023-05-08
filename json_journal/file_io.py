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


# Date format - test - check for duplicates

def csv_to_json(file, bank):
    '''
    Convert a CSV file to a JSON.

    Parameters
    ----------
    file : file path
        File path for the CSV.
    bank : dict
        Dictionary with the date, description and amount columns for the bank CSV.

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
            date = record[bank['date']]
            description = record[bank['description']]
            amount = float(record[bank['amount']])
            dict['date'] = date
            dict['description'] = description
            dict['amount'] = amount
            json_file.append(dict)

    
    return json_file

def convert_date(date):
    try date_split = date.split("/"):
        new_date = date_split[2] + "/" + date_split[1] + "/" + date_split [0]
    else:
        
