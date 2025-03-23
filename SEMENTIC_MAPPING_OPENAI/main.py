from fastapi import FastAPI
from base import match_input
from processor import get_matched_text
import json

# creating fastapi instance
app = FastAPI()

# define post endpoint
@app.post("/match")
def sementic_match(item : match_input):

    output = get_matched_text(item.source_list, item.destination_list)

    return json.loads(output) # json to python object