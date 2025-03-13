# filepath: d:\vscode\01_basic_agents.py
from llama_index.core.agent import ReActAgent
# from llama_index.llms.openai import OpenAI
from llama_index.core import Settings
from llama_index.llms.ollama import Ollama
from llama_index.core.tools import FunctionTool
from dotenv import load_dotenv
import os

load_dotenv()

# create basic tool on custom functions
# OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# define multiply function
# important : docstring helps LLM to understand what a specific function does
def multiply(a: float, b: float) -> float:
    """Multiply two numbers"""
    return a * b

# define multiply tool
multiply_tool = FunctionTool.from_defaults(fn = multiply)

# define add function
def add(a: int, b:int) -> int:
    """add two numbers and return a number"""
    return a + b

# define add tool
# add_tool = FunctionTool.from_defaults(fn = add)

# initialize llm
# llm = OpenAI(model = "gpt-3.0", temperature = 0, api_key=OPENAI_API_KEY)

# initialize agent
# agent = ReActAgent.from_tools([multiply_tool, add_tool], verbose=True)

# 1. initialize llm
Settings.llm = Ollama(model = "llama3.1", request_timeout="300")

# 2. convert method to a tool
f_multiply = FunctionTool.from_defaults(fn = multiply)
f_add = FunctionTool.from_defaults(fn = add)

# 3. call agent with the given tool
agent = ReActAgent.from_tools([f_multiply, f_add], verbose=True)

# ask question
response = agent.chat("What is 20+(2*4)? Use a tool to calculate every step.")

print(response)