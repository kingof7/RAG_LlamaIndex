from llama_index.core.agent import ReActAgent
from llama_index.core import Settings
from llama_index.llms.ollama import Ollama
from llama_index.core.tools import FunctionTool
from llama_index.core import VectorStoreIndex
from llama_index.embeddings.ollama import OllamaEmbedding
from dotenv import load_dotenv
import pandas as pd
from sklearn.metrics import accuracy_score

load_dotenv()

# 샘플 데이터 생성
data = {
    "column1": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "column2": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    "label": ["label1", "label2", "label3", "label4", "label5", "label6", "label7", "label8", "label9", "label10"]
}

# 데이터프레임 생성
df = pd.DataFrame(data)

# CSV 파일로 저장
df.to_csv('data.csv', index=False)

# 2. 데이터 변환
# 예제: 데이터 정제 및 변환
def transform_data(data):
    # 필요한 데이터만 선택
    transformed_data = data[['column1', 'column2']]
    # 데이터 변환 로직 추가
    return transformed_data

transformed_data = transform_data(df)

# 3. 데이터 벡터화 및 인덱싱
embed_model = OllamaEmbedding(
    model_name="llama3",
    base_url="http://localhost:11434",
    ollama_additional_kwargs={"mirostat": 0}
)

vector_index = VectorStoreIndex(embedding_model=embed_model)

# 데이터 벡터화 및 인덱싱
for index, row in transformed_data.iterrows():
    vector_index.add_document(row.to_dict())

# 4. top_k 검색 함수 정의
def search_top_k(query, k=5):
    results = vector_index.search(query, top_k=k)
    return results

# define a tool for the search_top_k function
search_top_k_tool = FunctionTool.from_defaults(fn=search_top_k)

# 5. initialize llm
Settings.llm = Ollama(model="llama3.1", request_timeout="300")


# 7. call agent with the given tool
agent = ReActAgent.from_tools([search_top_k_tool], verbose=True)

# 8. 평가 함수 정의
def evaluate_k_values(query, true_labels, k_values):
    best_k = None
    best_accuracy = 0
    for k in k_values:
        results = search_top_k(query, k=k)
        predicted_labels = [result['label'] for result in results]
        accuracy = accuracy_score(true_labels, predicted_labels)
        print(f"k={k}, accuracy={accuracy}")
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_k = k
    return best_k, best_accuracy

# 예제 쿼리와 실제 레이블
query = "example query"
true_labels = ["label1", "label2", "label3", "label4", "label5"]

# 평가할 k 값들
k_values = [1, 3, 5, 10]

# 최적의 k 값 찾기
best_k, best_accuracy = evaluate_k_values(query, true_labels, k_values)
print(f"Best k: {best_k}, Best accuracy: {best_accuracy}")

# 9. 최적의 k 값을 사용하여 에이전트 호출
response = agent.chat(f"Search for the top {best_k} relevant documents for the query '{query}'.")

print(response)

# 단계별 설명
# Raw Data 로드: pandas 라이브러리를 사용하여 CSV 파일에서 데이터를 로드합니다.
# 데이터 변환: transform_data 함수를 정의하여 데이터를 필요한 형식으로 변환합니다. 이 예제에서는 특정 열만 선택하고, 추가적인 변환 로직을 적용합니다.
# 데이터 벡터화 및 인덱싱: OpenAIEmbedding 모델을 사용하여 데이터를 벡터화하고, VectorIndexStore를 사용하여 인덱싱합니다. 이를 통해 효율적으로 데이터를 검색할 수 있습니다.
# top_k 검색 함수 정의: search_top_k 함수를 정의하여 주어진 쿼리에 대해 top_k 검색을 수행합니다.
# 평가 함수 정의: evaluate_k_values 함수를 정의하여 다양한 k 값에 대해 검색 결과의 정확도를 평가합니다. 최적의 k 값을 찾기 위해 accuracy_score를 사용합니다.
# 최적의 k 값 찾기: evaluate_k_values 함수를 호출하여 최적의 k 값을 찾습니다.
# 최적의 k 값을 사용하여 에이전트 호출: 최적의 k 값을 사용하여 에이전트를 호출하고, 검색 결과를 출력합니다.
# 이 예제는 llama_index와 Ollama를 사용하여 raw data를 로드하고 변환한 후, 데이터를 벡터화하여 인덱싱하고, top_k 검색을 수행하여 최적의 k 값을 찾는 전체적인 과정을 보여줍니다. 실제 사용 사례에 맞게 데이터를 로드하고 변환하는 로직을 수정해야 합니다.