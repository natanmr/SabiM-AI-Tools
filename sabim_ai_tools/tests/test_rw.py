# tests/test_rw.py

"""
Module for test the rw module
Author: Natan Moreira Regis
E-mail: natan.moreira.regis12@gmail.com
Licence: GPLv3 
"""

def test_rw_openfile() -> None:
    """
    Test openfile function from rw module
    """
    from rw import openfile

    try:
        openfile("./data/refs.bib")
    except:
        raise Exception("The function openfile from rw module return an error.")


    return None


if __name__=="__main__":

    print("Testing rw.openfile")
    test_rw_openfile()