from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo") # create a new instance of the ChatOpenAI class with the free GPT model and temperature set to 0

result = llm.invoke("What is the Square Root of 49?") # invoke is a method that takes a string as input and returns a string as output from llm model

print(result.content) 