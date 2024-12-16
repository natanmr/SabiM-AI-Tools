# Article Analyzer with LLMs

A Python-based project for analyzing and extracting insights from article metadata and content using Large Language Models (LLMs). This tool simplifies tasks like summarization, keyword extraction, and topic categorization for academic or professional articles.

---

## Features

- Extract and analyze article metadata (title, authors, publication date, etc.).
- Generate summaries and identify key points from the text.
- Perform keyword extraction for indexing and SEO purposes.
- Conduct sentiment analysis to evaluate the tone of the article.
- Categorize articles into predefined or dynamic topics.
- Export analyzed data into various formats (CSV, JSON, etc.).

---

## Requirements

- Python 3.7 or higher
- For local runing using llama model, its needed to install and setup ollama in your computer. It's highly recommended to use docker containers. For linux-based systems, you can follow these insructions: 
   - Install docker: [https://docs.docker.com/desktop/setup/install/linux/](https://docs.docker.com/desktop/setup/install/linux/).

   - Install ollama in docker: [https://hub.docker.com/r/ollama/ollama](https://hub.docker.com/r/ollama/ollama).
   - A list of other requeriments is given in requirements.txt file. 

---

## Installation

The instructions for install in Linux environments is as follow: 

1. Create a virtual environment and activate it:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```


2. Clone the repository:

   ```bash
   git clone https://github.com/natanmr/SabiM-AI-Tools.git
   cd SabiM-AI-Tools
   ```

3. Install the package:

   ```
   pip install .
   ```

---

## Usage

1. Prepare your articles as text files. Currenly the code only suport bibtex files. 

2. Run the program:

   ```bash
   python main.py
   ```

3. Choose the analysis type when prompted:

4. View the results in the terminal or exported files in the `output/` directory.

---

## Example

Here's a quick example of running a summarization task:

### Input:  
Article Title: *The Role of Quantum Computing in Material Science*  
Text: *Quantum computing offers new possibilities for simulating material properties...*  

### Output:  
- **Summary**: Quantum computing advances material science by enabling better simulations.
- **Keywords**: quantum computing, material science, simulations

---

## Customization

To modify the behavior of the program, edit the `config.json` file for settings like:
- Default output format (CSV, JSON)
- API parameters (e.g., temperature, max tokens)
- Analysis modules to enable/disable

---

## Limitations

- Requires an internet connection for API calls.
- Limited by the API token quota of the LLM provider.
- May require fine-tuning for domain-specific content.

---

## Contributing

Contributions are welcome! If you'd like to enhance this project:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact

For issues or suggestions, contact **[Your Name]** at [your-email@example.com].  

Explore the project and start analyzing articles more effectively with LLMs!
