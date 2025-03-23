from llama_index.core.output_parsers import PydanticOutputParser
from llama_index.core import PromptTemplate
from base import match_output
from llama_index.llms.openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def get_matched_text(source_list, destination_list):
    llm = OpenAI(model = "gpt-4o-mini", temperature=0, api_key=OPENAI_API_KEY)

    template = """
    You will be provided a source and destination list containing strings.
    You need to take a string one by one from source list until its empty
    and try to match it with string in the destination list.

    Plese do note that you need to match the strings based on the sementic mapping
    and not just based on the string similarity. If you are not able to find any match
    for the given text in the source list, please do say "No match found" in the destination
    string only.

    Please also mention the matching score based on your conficence on the mapping.
    The match score should be a number between 0-100 where 0 means no match and
    100 means perfect match.

    Please remove ```json from the final response.

    source list questinons : 
    {source_list}

    destination list questions :
    {destination_list}

    Your response :
    """

    # output parser : helps in getting the structured output as per our pydantic class
    output_parser = PydanticOutputParser(output_cls = match_output)

    # generating prompt
    prompt = PromptTemplate(template, output_parser=output_parser)

    # formatting the message using the prompt template
    message = prompt.format_messages(source_list=source_list, destination_list=destination_list)

    # generate response from llm
    llm_response = llm.chat(message)

    return llm_response.message.content