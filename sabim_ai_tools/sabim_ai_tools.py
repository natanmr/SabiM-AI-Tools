
from sabim_ai_tools.rw import read_bibtex_to_dataframe

def run_llm_analysis(activity, file_path, model, api_key):
    """
    Main function for analysis

    Args:
        - activity(str): activity to perform. This argument can have the values "w" for wrinting previous analysis, "a" for 
            analising all articles in bibfile or "r" for analising the remaining files. 
        - file_path (str, optional): File with the bibdata. 
        - model(str, optional): LLM model for using in the analysis. 
        - api_key(str, optional): api key for germini ai. 

    """


    print(  "#===========================================================================#\n"+
            "# SabiM-AI-Tools  Copyright (C) 2024  Natan Moreira Regis                   #\n"+
            "# This program comes with ABSOLUTELY NO WARRANTY; for details see LICENSE.  #\n"+
            "# This is free software, and you are welcome to redistribute it             #\n"+
            "# under certain conditions; see LICENSE file for details.                   #\n"+
            "#===========================================================================#\n"
    )

    # Call the bibfile
    print("Reading the bibfile")
    if ".json" in file_path:
        raise ValueError("Not implemented yet.")
    elif ".bib" in file_path:
        bibcontent = read_bibtex_to_dataframe(file_path)
    else:
        raise ValueError("Currently the code only suport bibtex files.")

    # Create a Json with this file. 
    

    # Analyse the data with LLMs and save them


     
     