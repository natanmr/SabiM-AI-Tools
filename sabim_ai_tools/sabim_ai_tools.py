# sabim_ai_tools.py

# Call required modules
from sabim_ai_tools.rw import read_bibtex_to_dataframe, JSONUtilities
from sabim_ai_tools.llms_ultilities import LLMAnalysis
import os

def run_llm_analysis(activity, file_path, model="llama3.2:1b", api_key=None):
    """
    Main function for LLM analysis on bibliographic data.

    Args:
        activity (str): The activity to perform:
            - "w": Write previous analysis data to JSON.
            - "a": Analyze all articles in the bibliographic file.
            - "r": Analyze only the remaining (unanalyzed) files.
        file_path (str): Path to the bibliographic file (.bib format).
        model (str, optional): LLM model to use for analysis. Defaults to "llama3.2:1b".
        api_key (str, optional): API key for models requiring authentication. Defaults to None.
    """
    print(
        "#===========================================================================#\n"
        "# SabiM-AI-Tools  Copyright (C) 2024  Natan Moreira Regis                   #\n"
        "# This program comes with ABSOLUTELY NO WARRANTY; for details see LICENSE.  #\n"
        "# This is free software, and you are welcome to redistribute it             #\n"
        "# under certain conditions; see LICENSE file for details.                   #\n"
        "#===========================================================================#\n"
    )

    print("Reading the bibliographic file.")
    if file_path.endswith(".bib"):
        bibcontent = read_bibtex_to_dataframe(file_path)
    else:
        raise ValueError("Currently, the code only supports .bib files.")

    # Step 2: Ensure a JSON file for results exists
    json_file_name = "Articles_analysis.json"
    if not os.path.isfile(json_file_name):
        print("Creating a new JSON file for analysis results.")
        json_utilities(task="w", file=json_file_name, data=bibcontent)

    # Step 3: Load or process data based on the activity
    print("Loading or analyzing data.")
    task_map = {"a": "all", "r": "remain"}
    if activity not in task_map:
        raise ValueError("Invalid activity. Use 'a' for all or 'r' for remaining analysis.")

    task = task_map[activity]

    # Step 4: Perform LLM analysis
    print("Starting LLM analysis.")
    analyzer = LLMAnalysis(data=bibcontent, model=model, api_key=api_key)
    analyzer.llm_analysis(task=task, json_path="./", json_file=json_file_name)

    print("Analysis complete. Results saved to JSON file.")
