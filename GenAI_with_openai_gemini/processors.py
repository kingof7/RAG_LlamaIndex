from llama_index.core import PromptTemplate
from llama_index.core.output_parsers import PydanticOutputParser
from base import match_output
from llama_index.llms.openai import OpenAI

def get_matched_text(source_list, destination_list):

    # define llm endpoint
    llm = OpenAI(model = "gpt-4o-mini", temperature = 0)

    template = """
        You will be given a list of sentences. You need to find the sentence that matches the given sentence.
        Source: {source}
        Destination: {destination}
        Matched Text: {matched_text}

    """

    # 2:54