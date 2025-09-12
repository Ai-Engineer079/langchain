from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")


message = [
    SystemMessage(content="You are a helpful assistant that translates English to Sindhi"),
    HumanMessage(content="Translate the following English text to Sindhi: 'Hello, how are you?'"),
]

result = llm.invoke(message)

#print(result)
print("\nJust the Answer:\n", result.content) # clean answer only
