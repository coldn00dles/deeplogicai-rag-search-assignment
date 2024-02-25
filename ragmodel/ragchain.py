from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = api_key

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def getRAGChain(retriever):
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.2)
    template = """You are a Search tool assistant required to assist users with their queries on the basis of the context provided below:
    Context : {context} 
    The user has asked : {question}
    Answer : """

    prompt = PromptTemplate.from_template(template)

    lcel_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return lcel_chain