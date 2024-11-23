# sabim_ai_tools/models.py

def model_call(model_type = "llama", api_key = None):
        """
        Calls the appropriate LLM model based on the model type specified in the instance.

        Args:
            - model_type (str): type of model to use. Defaults to 'llama'
            - api_key (str): API key for external resources as genain and oneai/ChatGPT. Defaults to None

        Returns:
            - model_LLM: The language model instance based on the model type.

        Raises:
        - ImportError: If there is an issue with importing the required modules.
        """
        # Using Google Germini model
        if model_type == 'genai':
            import google.generativeai as genai  # Import Google Generative AI module
        
            # Configure the API key for the Google Generative AI model
            genai.configure(api_key=api_key)
        
            # Initialize and return the Google GenerativeModel instance
            model_LLM = genai.GenerativeModel('gemini-pro')
            return model_LLM
    
        # Using Llama3 model
        if model_type == "llama":
            import ollama  # Import Ollama module
        
            # Initialize and return the Llama3 model instance
            model_LLM = ollama
            return model_LLM



