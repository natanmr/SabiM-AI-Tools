# __main__.py

# Imports:
from sabim_ai_tools.sabim_ai_tools import run_analysis
import argparse

if __name__ == "__main__":

    """
    Main function to parse command-line arguments and initiate the analysis of articles using LLM.
    """
    # Initialize argument parser with program name and description
    parser = argparse.ArgumentParser(prog='ArticleAnalysisLLM',
                                     description='Analysis of articles abstracts and titles using LLM')
    
    # Add argument for specifying the LLM model type (optional, default is model_type_default)
    parser.add_argument('-m', '--model_type', 
                        help="LLM model (genai or llama3).",
                        default="llama3:8b",
                        type=str,
                        required=False)  # Large Language Model (Optional)

    # Add argument for specifying the API key (optional, default is an empty string)
    parser.add_argument('-k', '--key',
                        help="API Key",
                        default="",
                        type=str,  
                        required=False)  # API key
    
    # Add argument for specifying the activity to perform (optional, default is "write")
    parser.add_argument('-a', '--activity',
                        help="Activity to perform (run-llm or write).",
                        default="write",
                        type=str, 
                        required=False)  # Define what to do 

    # Add argument for specifying the file to process (optional, default is file_articles)
    parser.add_argument('-f', '--file',
                        help="File to process the data",
                        default="refs.bib",
                        required=False)  # File to process

    # Parse the command-line arguments
    args = parser.parse_args()

    run_analysis(activity = args.activity, file_path = args.file, model = args.model_type, api_key=args.key)
