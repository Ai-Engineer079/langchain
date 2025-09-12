from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

load_dotenv()

model =ChatOpenAI(model="gpt-4o")


chat_history = []

SystemMessage = SystemMessage(content="You are a helpful assistant for the learn python programming language.")
chat_history.append(SystemMessage)

while True:
    query = input("You: ")
    if query.lower() == 'exit':
        break
    chat_history.append(HumanMessage(content=query))
    
    response = model.invoke(chat_history)
    
    chat_history.append(AIMessage(content=response.content))
    
    print("AI:", response.content)
