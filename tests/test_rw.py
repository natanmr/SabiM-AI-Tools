# tests/test_rw.py

"""
Module for test the rw module
Author: Natan Moreira Regis
E-mail: natan.moreira.regis12@gmail.com
Licence: GPLv3 
"""

import os
from sabim_ai_tools.rw import openfile

def test_rw_openfile():
    """
    Test the `openfile` function from the `rw` module.
    """
    # Caminho relativo para o arquivo de teste
    test_file_path = "./tests/data/refs.bib"

    # Verifica se o arquivo existe antes do teste
    assert os.path.exists(test_file_path), f"Test file {test_file_path} does not exist."

    # Testa a função `openfile`
    content = openfile(test_file_path)
    assert content is not None, "The function `openfile` returned None."
    assert isinstance(content, str), "The function `openfile` should return a string."


if __name__=="__main__":

    print("Testing rw.openfile")
    test_rw_openfile()