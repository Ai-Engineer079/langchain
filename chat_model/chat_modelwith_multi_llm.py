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
print("\nJust the Answer (OpenAI):\n", result.content) # clean answer only

# googlechat model
from langchain_google_genai import ChatGoogleGenerativeAI

googlechat_llm = ChatGoogleGenerativeAI(model= "gemini-2.5-flash" )

googlechat_result = googlechat_llm.invoke(message)

print("\nJust the Answer (Google Chat):\n", googlechat_result.content) # clean answer only

# anthropic model
# from langchain_anthropic import ChatAnthropic       
# anthropic_llm = ChatAnthropic(model="claude-2")

# anthropic_result = anthropic_llm.invoke(message)

# print("\nJust the Answer (Anthropic):\n", anthropic_result.content) # clean answer only
