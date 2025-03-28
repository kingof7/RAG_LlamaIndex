# weatherapi.com 회원가입 및 API_KEY 발급

- https://weatherapi.com 접속 및 회원가입
- https://weatherapi.com/my 접속 및 상단에 API_KEY 복사
- .env 파일 만들어서 키=값 입력

# Ollama 서버 설치 및 llama3.1 기동

- https://ollama.com/download
- Ollama 다운로드 및 설치
- 커맨드 열어서 ollama run llama3.1 입력

# python 가상환경 설치

- python --version
- python -m venv ollama_tools

# python 가상환경 진입(Windows/Mac)

- .\ollama_tools\Scripts\python.exe activate (Windows)
- source ollama_tools/bin/activate (Mac)

# 필수 pip install 설치

- .\ollama_tools\Scripts\python.exe -m pip install --upgrade pip
- .\ollama_tools\Scripts\pip.exe install llama_index llama-index-llms-ollama llama-index-embeddings-ollama
- .\ollama_tools\Scripts\pip.exe install llama-index-vector-stores-weaviate
- .\ollama_tools\Scripts\pip.exe requests load_dotenv os requests_oauthlib scikit-learn

# Gen AI Revolutionizes Text Analysis with OpenAI and Gemini 패키지

- .\ollama_tools\Scripts\pip.exe install fastapi uvicorn llama_index llama-index-llms-openai llama-index-llms-gemini

# Sementic Mapping : Gen AI Revolutionizes Text Anlaysis with llama-index-openai, gemini

- pip install fastapi uvicorn llama_index llama-index-llms-openai llama-index-llms-gemini
