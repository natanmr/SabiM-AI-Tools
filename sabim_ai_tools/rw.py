import os
import pandas as pd
from pybtex.database import parse_string


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
    if not os.path.exists(path_file):
        raise FileNotFoundError(f"File '{path_file}' not found.")
    
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


