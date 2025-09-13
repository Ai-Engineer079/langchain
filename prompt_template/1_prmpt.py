from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate


load_dotenv()

llm = ChatOpenAI(model='gpt-4')

template = """write a {tone} email to {company}
expressing  in {position} position, mentioning {skill} as a key strength.
keep it {length} words long."""