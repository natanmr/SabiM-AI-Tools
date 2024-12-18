# sabim_ai_tools/rag.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sabim_ai_tools.models import Models

class RAG:
    """ 
    Class implementing Retrieval-Augmented Generation (RAG).
    
    RAG combines information retrieval and text generation. It retrieves relevant
    documents from a dataset and uses them as context for generating responses.
    This implementation uses the Ollama model for text generation.

    Attributes:
        data (list of dict): The dataset used for retrieval.
        column (str): The column of data to use for retrieval, defaults to 'abstract'.
        model (ollama.Ollama): The Ollama model instance for text generation.
        vectorizer (TfidfVectorizer): TF-IDF vectorizer for text retrieval.
    """

    def __init__(self, model, data, api_key = None, column="abstract"):
        """
        Initializes the RAG model with the given data and column.

        Args:
            data (list of dict): The data used for retrieval, expected to be a list of dictionaries.
            column (str, optional): The column to use for text retrieval, defaults to "abstract".
        """
        self.data = data
        self.column = column
        self.model = model 
        self.api_key = api_key

        # Initialize the Ollama model for text generation.
        self.llm_model = Models(model = self.model, api_key=self.api_key).model_call()  
        
        # Initialize the TF-IDF vectorizer for document retrieval.
        self.vectorizer = TfidfVectorizer()

    def _retrieve_documents(self, query, top_n=5):
        """
        Retrieves the most relevant documents based on the input query using cosine similarity.

        Args:
            query (str): The query for which relevant documents need to be retrieved.
            top_n (int, optional): The number of top documents to retrieve, defaults to 5.

        Returns:
            list of str: A list of the most relevant documents.
        """
        # Extract the text from the specified column in the dataset.
        documents = [item[self.column] for item in self.data]
        
        # Transform the documents into TF-IDF vectors.
        tfidf_matrix = self.vectorizer.fit_transform(documents + [query])
        
        # Compute the cosine similarity between the query and the documents.
        cosine_similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
        
        # Get the indices of the top_n most similar documents.
        top_indices = cosine_similarities.argsort()[0][-top_n:][::-1]
        
        # Return the top_n most similar documents.
        return [documents[i] for i in top_indices]

    def _generate_response(self, context, prompt):
        """
        Uses the Ollama model to generate a response based on the provided context.

        Args:
            context (str): The context to guide the generation process.
            prompt (str): The query or prompt to generate a response for.

        Returns:
            str: The generated response from the model.
        """
        # Combine the context with the prompt to form the full input for the model.
        input_text = f"Context: {context}\nPrompt: {prompt}"
        
        # Generate a response from the Ollama model using the combined input text.
        response = self.model.chat(input_text)
        
        return response['text']

    def generate(self, query, top_n=5):
        """
        Generates a response to the query by retrieving relevant documents and using them as context for the Ollama model.

        Args:
            query (str): The query to generate a response for.
            top_n (int, optional): The number of top documents to retrieve, defaults to 5.

        Returns:
            str: The generated response.
        """
        # Step 1: Retrieve the top N relevant documents based on the query.
        relevant_documents = self._retrieve_documents(query, top_n)
        
        # Step 2: Combine the retrieved documents into a single context.
        context = "\n".join(relevant_documents)
        
        # Step 3: Generate a response using the context and the query.
        response = self._generate_response(context, query)
        
        return response

