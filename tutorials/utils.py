import json
from typing import Dict, List, Union


def load_json(json_file: str) -> Union[List, Dict]:
    """
    Loads a JSON file and returns its content as a list or dictionary.

    Args:
        json_file (str): The path to the JSON file to be loaded.

    Returns:
        Union[List, Dict]: The content of the JSON file as a list or dictionary.

    Raises:
        FileNotFoundError: If the specified JSON file does not exist.
        json.JSONDecodeError: If the JSON file cannot be parsed.
    """
    with open(json_file, 'r') as file:
        data = json.load(file)

    return data


def export_to_json(data: Union[List, Dict], json_file: str) -> None:
    """
    Exports the given data to a JSON file.

    Args:
        data (Union[List, Dict]): The content to be exported as a list or dictionary.
        json_file (str): The path to the JSON file where the data will be written.

    Returns:
        None: This function does not return a value, but it writes the data to the specified JSON file.

    Raises:
        TypeError: If the data is not a list or dictionary.
        FileNotFoundError: If the specified JSON file does not exist.
        PermissionError: If the function does not have permission to write to the specified JSON file.
    """
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)