# sabim_ai_tools/rw.py

import os
import pandas as pd
from pybtex.database import parse_string
import json

def openfile(path_file):
    """
    Open a file and return its content as a string.

    Arguments:
        - filename (str): Name of the file to open.
    
    Returns: 
        - str: File content.
    
    Raises:
        - FileNotFoundError: If the file does not exist.
        - IOError: If there's an issue reading the file.
    """
    try:
        with open(path_file, 'r', encoding="utf-8") as f:
            return f.read()
    except IOError as e:
        raise IOError(f"Error reading file '{path_file}': {e}")

def read_bibtex_to_dataframe(path_file):
    """
    Reads a BibTeX file and converts its entries into a pandas DataFrame.

    This function uses the `openfile` function to read the BibTeX file content,
    then parses the entries and extracts their fields into a DataFrame.

    Arguments:
        - path_file (str): Path to the BibTeX file.

    Returns:
        - pd.DataFrame: A DataFrame where each row corresponds to a BibTeX entry.
          Columns are the fields (e.g., 'title', 'author', 'year').

    Raises:
        - FileNotFoundError: If the file does not exist.
        - ValueError: If the file content cannot be parsed as BibTeX.
    """
    # Read file content using the provided openfile function
    bibtex_content = openfile(path_file)
    
    try:
        # Parse the BibTeX content
        bib_database = parse_string(bibtex_content, "bibtex")
    except Exception as e:
        raise ValueError(f"Error parsing BibTeX file: {e}")
    
    # Extract BibTeX entries into a list of dictionaries
    entries = []
    for entry_key, entry in bib_database.entries.items():
        entry_data = {"id": entry_key}  # Include the entry key (e.g., citation key)
        for field, value in entry.fields.items():
            entry_data[field] = value
        # Add author/editor fields if present
        for person_role in ["author", "editor"]:
            if person_role in entry.persons:
                entry_data[person_role] = " and ".join(
                    [" ".join(person.prelast_names + person.last_names) for person in entry.persons[person_role]]
                )
        entries.append(entry_data)
    
    # Convert list of dictionaries into a pandas DataFrame
    return pd.DataFrame(entries)


class JSONUtilities:
    """
    A class to perform various operations on a JSON file using a pandas DataFrame.
    """

    def __init__(self, path="./", file="Articles.json"):
        """
        Initialize the JSONUtilities instance.

        Args:
            path (str): Directory path where the JSON file is located or will be created. Default is "./".
            file (str): Name of the JSON file. Default is "Articles.json".
        """
        self.file_path = os.path.join(path, file)

    def read(self):
        """
        Read the content of the JSON file and return it as a pandas DataFrame.

        Returns:
            pandas.DataFrame: The content of the JSON file as a DataFrame.

        Raises:
            FileNotFoundError: If the file does not exist.
        """
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"No such file: '{self.file_path}'")

        with open(self.file_path, 'r') as f:
            content = json.load(f)
        return pd.DataFrame(content)

    def write(self, data):
        """
        Write the provided DataFrame to the JSON file. Overwrites the file if it exists.

        Args:
            data (pandas.DataFrame): The DataFrame to write to the JSON file.

        Raises:
            ValueError: If the provided data is not a pandas DataFrame.
        """
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Data must be a pandas DataFrame.")

        data.to_json(self.file_path, orient='records', indent=4)

    def update(self, data):
        """
        Update existing entries in the JSON file with the provided DataFrame.

        Args:
            data (pandas.DataFrame): The DataFrame containing updates. Must include an 'id' column.

        Raises:
            ValueError: If the provided data is not a pandas DataFrame.
            FileNotFoundError: If the file does not exist.
        """
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Data must be a pandas DataFrame.")
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"No such file: '{self.file_path}'")

        with open(self.file_path, 'r') as f:
            existing_data = pd.DataFrame(json.load(f))

        # Ensure 'id' is the index for combining
        existing_data.set_index('id', inplace=True)
        data.set_index('id', inplace=True)

        # Update existing data with new data
        updated_data = existing_data.combine_first(data).reset_index()

        # Write updated data back to JSON
        updated_data.to_json(self.file_path, orient='records', indent=4)

    def append(self, data):
        """
        Append new entries from the provided DataFrame to the JSON file. If the file does not exist, it will be created.

        Args:
            data (pandas.DataFrame): The DataFrame to append to the JSON file.

        Raises:
            ValueError: If the provided data is not a pandas DataFrame.
        """
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Data must be a pandas DataFrame.")

        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                existing_data = pd.DataFrame(json.load(f))
            combined_data = pd.concat([existing_data, data], ignore_index=True)
        else:
            combined_data = data

        combined_data.to_json(self.file_path, orient='records', indent=4)