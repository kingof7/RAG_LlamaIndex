from llama_index.core.tools import FunctionTool
from llama_index.core.agent import ReActAgent
from llama_index.core import Settings
from llama_index.llms.ollama import Ollama
from weather import get_current_weather_C, get_current_weather_F

# 1. initialize llm
Settings.llm = Ollama(model = "llama3.1", request_timeout="300")

# 2. convert method to a tool
weather_tool_C = FunctionTool.from_defaults(fn = get_current_weather_C)
weather_tool_F = FunctionTool.from_defaults(fn = get_current_weather_F)

# 3. call agent with the given tool
agent = ReActAgent.from_tools([weather_tool_C, weather_tool_F], verbose=True)

response = agent.query("What's the temperature in Seoul in celsius degrees and fahrenheit degrees?")

print(response)