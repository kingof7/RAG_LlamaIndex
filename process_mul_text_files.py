from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.llms.ollama import Ollama
# from llama_index.llms.openai import OpenAI

# Settings.llm = OpenAI(model="gpt-4o-mini")
Settings.llm = Ollama(model="llama3.1", request_timeout="300")

def query_over_text(query):

    # load multiple files
    documents = SimpleDirectoryReader("text").load_data()
    #print(documents)

    # create index and get query engine
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()

    # pass query and get a response
    response = query_engine.query(query)
    return response

# ask query
output = query_over_text("Who has recognized Mogwli as her lost son?")
print(output)