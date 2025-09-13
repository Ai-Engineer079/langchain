from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()

llm = ChatOpenAI(model='gpt-4')

template = """write a {tone} email to {company}
expressing  in {position} position, mentioning {skill} as a key strength.
keep it {length} words long."""


prompt_template = ChatPromptTemplate.from_template(template)

prompt = prompt_template.invoke({
    "tone": "professional",
    "company" : "Google",
    "position": "AI Engineer",
    "skill": "Python programming",
    "length" :100
})
result = llm.invoke(prompt)
print(result.content) 