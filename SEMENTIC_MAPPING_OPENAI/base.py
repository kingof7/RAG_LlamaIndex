from pydantic import BaseModel
from typing import List

# define pydantic class for structured output
class match_output (BaseModel):
    source_string: str
    destination_string : str
    match_scroe : int

# define pydantic class for input
class match_input (BaseModel):
    source_list: List[str]
    destination_list: List[str]