**Title**: **Chat with Website Using RAG Pipeline**

## Overview
The goal of this project is to implement a **Retrieval-Augmented Generation (RAG) pipeline** that enables users to interact with both structured and unstructured data extracted from websites. The system crawls, scrapes, and stores website content, converts it into vector embeddings, and retrieves context-rich responses using a selected **Large Language Model (LLM)**.

---

## Functional Requirements

### 1. Data Ingestion
- **Input**: URLs or a list of websites to crawl/scrape.
- **Process**:
   - Crawl and scrape content from target websites.
   - Extract key data fields, metadata, and textual content.
   - Segment content into chunks for better granularity.
   - Convert chunks into vector embeddings using a pre-trained embedding model.
   - Store embeddings in a vector database with associated metadata for efficient retrieval.

### 2. Query Handling
- **Input**: User's natural language question.
- **Process**:
   - Convert the user's query into vector embeddings using the same embedding model.
   - Perform a similarity search in the vector database to retrieve the most relevant content chunks.
   - Pass the retrieved chunks to the LLM along with agentic context to generate a detailed response.

### 3. Response Generation
- **Input**: Relevant information retrieved from the vector database and the user query.
- **Process**:
   - Use the LLM with retrieval-augmented prompts to produce accurate, context-aware responses.
   - Ensure factuality by incorporating retrieved data directly into the response.

---

## Features
- **Web Crawling & Scraping**: Crawl target websites and extract relevant textual and metadata information.
- **Vector Database**: Store website data in vector format for efficient similarity-based retrieval.
- **LLM Integration**: Use an advanced Large Language Model to provide meaningful and context-rich answers.
- **Retrieval-Augmented Generation**: Enhance LLM responses using factual data retrieved from the website.
- **Embedding Generation**: Convert text into high-dimensional vector embeddings for semantic similarity.

---

**Brief explanation of how RAG works**
A RAG bot is short for Retrieval-Augmented Generation. This means that we are going to "augment" the knowledge of our LLM with new information that we are going to pass in our prompt. We first vectorize all the text that we want to use as "augmented knowledge" and then look through the vectorized text to find the most similar text to our prompt. We then pass this text to our LLM as a prefix.
![image](https://github.com/user-attachments/assets/735eabdd-3fe3-452b-94ec-51b174ee9d29)

## Installation
Follow these steps to set up and run the project:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Bhanuprakash-cse16/ragg-pipeline.git
   cd ragg-pipeline
   ```

2. **Set Up the Environment**:
   - Install the required dependencies:
     ```bash
     pip install -r requirements.txt
     ```

3. **Configure API Keys**:
   - Ensure your OpenAI API key is stored securely as an environment variable:
     ```bash
     export OPENAI_API_KEY=your_api_key
     ```

---

## Usage
### Run the Pipeline
To run the RAG pipeline, execute the following command:
```bash
python main.py
```

### Workflow
1. Provide the list of target website URLs.
2. Enter a natural language query.
3. The system will:
   - Crawl and process the website content.
   - Retrieve relevant information using similarity search.
   - Generate a detailed, accurate response using the LLM.

---

## Technologies Used
- **Python**: Programming language.
- **OpenAI API**: For LLM-based response generation.
- **BeautifulSoup**: Web scraping tool for extracting website data.
- **FAISS**: Vector database for storing and retrieving content embeddings.
- **Pre-trained Embedding Model**: Converts text into vector representations.

---

## File Structure
```plaintext
ragg-pipeline/
|-- crawl_scrape.py      # Web crawling and scraping logic
|-- embeddings.py        # Embedding generation logic
|-- llm_response.py      # LLM response generation
|-- vector_store.py      # Vector database storage and retrieval
|-- main.py              # Pipeline orchestration
|-- requirements.txt     # Project dependencies
|-- README.md            # Project documentation
```

---

## Example Output
- **Input Query**: "What are the contact details of the target website?"
- **System Response**:
   "The contact details are: Phone - 1234567890, Email - info@example.com."

---

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request.

---

## License
This project is licensed under the MIT License.
