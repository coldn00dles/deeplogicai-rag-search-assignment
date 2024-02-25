# RAG Search Tool Assignment

## Deliverables achieved : 

 - ~~RAG Model~~
 - Web Application : Not built

## Technologies Used : 
 - Python
 - Langchain
 - OpenAI
 - FAISS


## Instructions for execution

__IMPORTANT__ : An OpenAI key is required for this task. 
Kindly refer to the `.env-example` file to see how to put the key in the dotenv file.

For downloading dependencies, run `pip -r requirements.txt` in a virtual environment running on `Python 3.10.6`
## Documentation

The model's workings can be divided into 4 main parts :  <br>

1) `Ingestion` : The data from the PDF's is read by the `fitz` module and is then further pre-processed with regex. The PDF is splitted using filters and specific chunk limits (handled by fitz) and each paragraph/sentence hence obtained is stored in a `Document` object.

2) `Embedding` : The obtained paragraph documents are then embedded into vectors using `OpenAI's` text embedding models. 
A `RetrievalVectorStore` instance is returned from the embedded documents, which can be used to search documents for queries and define thresholds for results obtained from those searches.

3) `LLM Chain` : Using OpenAI's chat model `gpt-3.5-turbo`, we firstly perform prompt engineering to fit our use case by making a suitable prompt and a PromptTemplate out of it. Following this, we use Langchain's LCEL (Langchain Expression Langage) to compose a LLM Chain simply by piping different parts of the chain. We put together the retrieved context and the question to be asked by the user in the form of variables (defined in the prompt template as well), the llm/chat model and a output parser to ensure answers are in string (all defined in Langchain)

3) `User Interaction` : Documents in the `docs` folder are ingested and the user is prompted to ask a question pertaining to those documents. The RAG application then returns a suitable answer. 

The model can be __easily retrained__ by just adding the PDF's in the `docs` folder and rerunning `main.py`

