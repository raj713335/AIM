from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    ServiceContext,
    load_index_from_storage
)
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.llms.groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

print(GROQ_API_KEY)

# Data Ingestion

reader = SimpleDirectoryReader(input_files=["./Airbus-Commercial-Aircraft-AC-A320.pdf"])
documents = reader.load_data()

print(len(documents))
print(documents[4].metadata)

# Chunking

text_splitter = SentenceSplitter(chunk_size=1024, chunk_overlap=200)
nodes = text_splitter.get_nodes_from_documents(documents, show_progress=True)

print(len(nodes))
print(nodes[0].metadata)


# Embedding Model

embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")


# Define LLM Model

llm = Groq(model="llama3-70b-8192", api_key=GROQ_API_KEY)


# Configure Service Context

service_context = ServiceContext.from_defaults(embed_model=embed_model, llm=llm)


# Create Vector Store Index

vector_index = VectorStoreIndex.from_documents(documents, show_progress=True, service_context=service_context, node_parser=nodes)

# Persist/Save Index

vector_index.storage_context.persist(persist_dir="./storage_mini")

# Define Storage Context

storage_context = StorageContext.from_defaults(persist_dir="./storage_mini")


# Load Index

index = load_index_from_storage(storage_context, service_context=service_context)


# Define Query Engine

query_engine = index.as_query_engine(service_context=service_context)


# Feed in user query


query = "Explain Jacking of the Landing Gear?"
resp = query_engine.query(query)


print(resp.response)