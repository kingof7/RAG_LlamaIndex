from llama_index.core.tools import FunctionTool
from llama_index.core.agent import ReActAgent
from llama_index.core import Settings
from llama_index.llms.ollama import Ollama
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
import os

# MS OAuth2 설정
client_id = os.getenv("MS_CLIENT_ID")
client_secret = os.getenv("MS_CLIENT_SECRET")
token_url = "https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token"

def get_lme_prices():
    # OAuth2 인증
    client = BackendApplicationClient(client_id=client_id)
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url=token_url, client_id=client_id, client_secret=client_secret)

    # LME API 호출 (여기서는 예시 URL을 사용합니다. 실제 API URL과 파라미터를 사용하세요)
    api_url = "https://kzlme.koreazinc.co.kr/kzlme/daily.html"
    headers = {
        "Authorization": f"Bearer {token['access_token']}"
    }
    response = oauth.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch LME prices"}

# 1. initialize llm
Settings.llm = Ollama(model = "llama3.1", request_timeout="300")

# 2. convert method to a tool
lme_tool = FunctionTool.from_defaults(fn = get_lme_prices)

# 3. call agent with the given tool
agent = ReActAgent.from_tools([lme_tool], verbose=True)

response = agent.query("provide the latest LME prices.")

print(response)