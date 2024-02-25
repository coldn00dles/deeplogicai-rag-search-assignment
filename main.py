import os

from ragmodel.ingestor import getDocument
from ragmodel.indexer import getRetriever
from ragmodel.ragchain import getRAGChain


#Ingestion 

docs = getDocument("docs/")

#indexing / embedding

ret = getRetriever(docs)

#RAG Chain

rag_chain = getRAGChain(ret)

question = str(input("What would you like to know from your RAG model? "))

print(rag_chain.invoke(question))