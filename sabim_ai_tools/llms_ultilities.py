from sabim_ai_tools.rw import json_utilities
import pandas as pd
import ollama
import json
import re


class LLMAnalysis:
    """
    Class for performing LLM (Large Language Model) analysis on article data.
    """

    def __init__(self, data, model="llama3.2:1b", api_key=None, prompt=None, template=None):
        """
        Initialize the llm_analysis class.

        Args:
            data (pd.DataFrame): DataFrame containing articles for analysis.
            model (str): Model to use for the analysis (default: llama3.2:1b).
            api_key (str): API key for non-local models (default: None).
            prompt (dict): Prompt configuration for the LLM (default: None).
            template (dict): Template for structuring AI responses (default: None).
        """
        self.data = data
        self.model = model
        self.api_key = api_key
        self.prompt = prompt or {
            'prompt_header': (
                "You are an expert text processor and analyzer. Your task is to extract and categorize "
                "information from an article into specific sections. The sections are as follows: \n"
                "'Systems' identify and list the systems discussed in the article (e.g., two-dimensional, "
                "compositions, structure, etc.). \n"
                "'Type' Determine if the article is experimental or theoretical. \n"
                "'Methods' Extract and list the methods used in the study. \n"
                "'Main Scope' Summarize the main scope or objective of the article. \n"
                "'Main Results' Summarize the key findings or main results of the article. \n"
                "Now, process the provided article content:"
            ),
            'prompt_instructions': (
                "Instructions: \n"
                "Systems: Look for any mention of systems, whether two-dimensional, three-dimensional, structure, space groups, etc., and list them. \n"
                "Type: identify if the study is experimental (involving practical tests, observations, experiments) or theoretical (involving mathematical models, theoretical analysis, simulations). \n"
                "Methods: Extract any mention of methods, techniques, or procedures used in the study. \n"
                "Main Scope: Provide a brief summary of the main goal or objective of the study. \n"
                "Main Results: Provide a concise summary of the main findings or results reported in the article. \n\n"
            )
        }
        self.template = template or {
            "Systems": [],
            "Type": [],
            "Methods": [],
            "Main Scope": [],
            "Main Results": [],
            "Keywords": []
        }

    def model_call(self):
        """
        Initializes and returns an instance of the LLM model.

        Returns:
            object: The Llama3 model instance.
        """
        if self.model.startswith("llama3"):
            return ollama
        else:
            raise ValueError("Unsupported model. Only Llama3 and Google GenAI are supported.")

    def chat_interaction(self, title=None, abstract=None):
        """
        Interacts with an LLM model to generate a response based on a provided structure.

        Args:
            title (str): The title of the article.
            abstract (str): The abstract of the article.

        Returns:
            str: The content generated by the AI model.
        """
        model = self.model_call()
        input_ai = (
            f"{self.prompt['prompt_header']} \n"
            f"Title: {title} \n"
            f"Abstract: {abstract} \n"
            f"{self.prompt['prompt_instructions']} \n"
            f"Use the following template: {json.dumps(self.template)}."
        )
        response = model.chat(model=self.model, messages=[{"role": "user", "content": input_ai}])
        return response["message"]["content"]

    def parse_ai_response_json(self, ai_response):
        """
        Parse the AI response, extracting JSON data.

        Args:
            ai_response (str): The AI-generated response.

        Returns:
            dict: Parsed data structured according to the template.
        """
        match = re.search(r'\{.*?\}', ai_response, re.DOTALL)
        if match:
            try:
                parsed_data = json.loads(match.group(0))
                return {key: parsed_data.get(key, []) if isinstance(parsed_data.get(key), list) else parsed_data.get(key, "") for key in self.template.keys()}
            except json.JSONDecodeError:
                print("Error decoding JSON from AI response.")
                return None
        print("No JSON found in AI response.")
        return None

    def llm_analysis(self, data = [], task="remain", json_path="./", json_file="Articles_llm.json"):
        """
        Perform LLM analysis and update results in a JSON file.

        Args:
            data (pd.DataFrame): Input DataFrame with 'id', 'Title', and 'Abstract'.
            task (str): Task to perform ("all" or "remain").
            json_path (str): Path to JSON directory.
            json_file (str): JSON file name.

        Returns:
            None
        """

        data = self.data

        try:
            data_llm = json_utilities(task="r", path=json_path, file=json_file)
        except FileNotFoundError:
            data_llm = pd.DataFrame(columns=['id', 'BibKey', 'AI-Result', 'AI-Systems', 'AI-Type', 
                                             'AI-Methods', 'AI-Main Scope', 'AI-Main Results', 'AI-Keywords'])

        for col in ['id', 'BibKey', 'AI-Result']:
            if col not in data_llm.columns:
                data_llm[col] = None

        for index, row in data.iterrows():
            print(f"Analysing article: {row['id']}")

            if task == "remain" and row["id"] in data_llm["id"].values and pd.notna(data_llm.loc[data_llm["id"] == row["id"], "AI-Result"].iloc[0]):
                continue

            ai_result = self.chat_interaction(title=row["title"], abstract=row["abstract"])
            print(ai_result)

            # ai_parsed = self.parse_ai_response_json(ai_result)

            new_entry = {**row.to_dict(), "AI-Result": ai_result}

            # for key, value in ai_parsed.items():
            #     new_entry[f"AI-{key}"] = value

            if row["id"] in data_llm["id"].values:
                data_llm.update(pd.DataFrame([new_entry]))
            else:
                data_llm = pd.concat([data_llm, pd.DataFrame([new_entry])], ignore_index=True)

        json_utilities(task="u", path=json_path, file=json_file, data=data_llm)
