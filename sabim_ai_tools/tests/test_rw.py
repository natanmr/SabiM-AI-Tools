# tests/test_rw.py

"""
Module for test the rw module
Author: Natan Moreira Regis
E-mail: natan.moreira.regis12@gmail.com
Licence: GPLv3 
"""

import os
import pandas as pd

from sabim_ai_tools.rw import openfile
from sabim_ai_tools.rw import JSONUtilities
from sabim_ai_tools.rw import DBUtilities
from sabim_ai_tools.rw import read_bibtex_to_dataframe

def test_rw_openfile() -> None:
    """
    Test the `openfile` function from the `rw` module.
    """
    # Caminho relativo para o arquivo de teste
    test_file_path = "sabim_ai_tools/tests/data/refs.bib"

    # Verifica se o arquivo existe antes do teste
    assert os.path.exists(test_file_path), f"Test file {test_file_path} does not exist."

    # Testa a função `openfile`
    content = openfile(test_file_path)
    assert content is not None, "The function `openfile` returned None."
    assert isinstance(content, str), "The function `openfile` should return a string."

    return None

def test_rw_read_bibtex_to_dataframe() -> None:
    """ Test the `read_bibtex_to_dataframe` function from the `rw` module. """

    # Caminho relativo para o arquivo de teste
    test_file_path = "sabim_ai_tools/tests/data/refs.bib"

    # Verifica se o arquivo existe antes do teste
    assert os.path.exists(test_file_path), f"Test file {test_file_path} does not exist."

    content = read_bibtex_to_dataframe(test_file_path)

    assert content is not None, "The function `read_bibtex_to_dataframe` returned None."

    assert isinstance(content, pd.DataFrame), "The function `read_bibtex_to_dataframe` should return a pandas dataframe." 

    return None

def test_JSONUtilities():
    """
    Test the JSONUtilities class methods.
    """
    # Test file path
    test_file_path = "sabim_ai_tools/tests/data/test_refs.json"

    test_file_path_bib = "sabim_ai_tools/tests/data/refs.bib"

    # Ensure the test file doesn't affect the original
    if os.path.exists(test_file_path):
        os.remove(test_file_path)

    # Create an instance of the JSONUtilities class
    json_util = JSONUtilities(file=test_file_path)

    initial_data = read_bibtex_to_dataframe(test_file_path_bib)

    # Test write_json
    json_util.write(initial_data)
    assert os.path.exists(test_file_path), "File was not created."

    # Test read_json
    read_data = json_util.read()
    # pd.testing.assert_frame_equal(read_data, initial_data, check_dtype=False)

    # Test update_json
    updated_data = pd.DataFrame({
        "id": [2, 3],
        "Abstract": [25.0, 35.0]
    })
    json_util.update(updated_data)

    expected_updated_data = pd.DataFrame({
        "id": [1, 2, 3],
        "Title": ["Alice", "Bob", "Charlie"],
        "Abstract": [10.5, 25.0, 35.0]
    })
    read_data = json_util.read()
    pd.testing.assert_frame_equal(read_data.sort_values(by="id"), expected_updated_data.sort_values(by="id"), check_dtype=False)

    # Test append_json
    new_data = pd.DataFrame({
        "id": [4, 5],
        "Title": ["Dave", "Eve"],
        "Abstract": [40.0, 50.0]
    })
    json_util.append(new_data)

    expected_appended_data = pd.concat([expected_updated_data, new_data], ignore_index=True)
    read_data = json_util.read()
    # pd.testing.assert_frame_equal(read_data.sort_values(by="id"), expected_appended_data.sort_values(by="id"), check_dtype=False)

    # Clean up test file
    if os.path.exists(test_file_path):
        os.remove(test_file_path)

def test_DBUtilities():

    # Initiate the instance:
    db = DBUtilities()

    # Create a database for testing using the example bibtex
    


    return